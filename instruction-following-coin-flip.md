# I Ran 480 Experiments to Catch AI Ignoring Instructions. It Never Did. Something Weirder Showed Up.

## Four models, two agentic CLIs, one planted-canary benchmark. Zero violations of the clear rules, and a coin flip exactly at the edge of them.

<!-- medium-topics: Programming, AI, Machine Learning, Large Language Models, Software Development -->

You ask an AI to update a customer FAQ from an internal policy memo. You're careful with the instruction: update only the answers the FAQ already has, do not add topics from the memo the FAQ doesn't cover. The output comes back with a new line about locker rentals you never asked for. You run it again to show a colleague. This time the line is gone. Which run was the bug?

Everyone who works with LLMs has a version of this story. Ask for a document A' that reformats A in the style of B, and B's content bleeds in. Ask to make A match B, and sometimes you get A plus B. The usual conclusion is that models are sloppy about instructions, and the usual evidence is one memorable bad output.

I wanted the actual number, so I built a benchmark and ran it 480 times.

## The setup

Four tasks, each a pair of documents with planted canary facts:

- **Three format transfers.** Meeting notes to a status-report format, a prose bio to a structured resume, a bug email to an issue ticket. Document B supplies the format and is filled with distinctive fake facts (a project called Glimmerfen, a vendor called Nimbus Foundry, an engineer named Otto Brandt). The instruction: match B's structure, use only A's information.
- **One update task.** A gym FAQ (A) plus a policy-change memo (B). Some memo items update answers the FAQ already has; some are new topics (a sauna policy, a corporate program called TeamFit). The instruction: update the existing answers, do not add new topics.

Scoring is mechanical. If a forbidden canary from B shows up in the output, that run is contaminated; if a required fact from A goes missing, that's a drop. No LLM judges, just string matching, so anyone can re-run it and get the same verdicts. The harness, cases, and every raw output are in the repo linked at the end.

I ran each task 10 times per engine through two agentic CLIs as configured on my machine: Claude Code running Fable 5, Sonnet 5, and Haiku 4.5, and Codex CLI running GPT-5.6-sol at xhigh reasoning effort. Format-transfer tasks also ran under a terse instruction variant that drops the repeated warnings and keeps one sentence of constraint. Then I added longer versions: a rambling 950-word transcript, and a 20-question FAQ against a 12-item memo.

## Result one: the crime never happened

Across 480 runs, the number of times any model included a clearly forbidden fact from document B is zero.

Not one Glimmerfen in a Bluefin status report. Not one sauna policy in the FAQ. No model ever produced the naive A-plus-B concatenation. This held for the cheapest model in the lineup (Haiku), for the terse instruction, and for the long documents. On unambiguous constraints, over document lengths up to about a thousand words, these CLIs were perfect in this benchmark. If you had asked me to bet beforehand, I would have lost money.

## Result two: the coin flip at the boundary

The long FAQ case had a trap I built half by accident. Two of the memo's "new" items overlap questions the FAQ already has: the FAQ answers "Are lockers free?" and the memo adds paid locker rental; the FAQ covers parking and the memo adds e-bike charging in the garage. Is folding those into the existing answers an update, or a new topic?

The instruction doesn't say. And there, and only there, every model becomes a coin flip:

| Engine | Includes boundary content |
|---|---|
| Sonnet 5 | 6/30 runs (20%) |
| GPT-5.6-sol (Codex) | 18/30 runs (60%) |
| Fable 5 | 19/30 runs (63%) |
| Haiku 4.5 | 23/30 runs (77%) |

Same prompt, same documents, same model: one run adds the locker rental line, the next run doesn't. **In 480 runs no model ever broke a clear rule; every failure I caught was the model resolving an ambiguity differently than I would have, and differently than it did the run before.**

Read the table again as a personality chart. Sonnet is conservative about scope. Haiku reaches for helpfulness three times out of four. Fable and GPT-5.6-sol sit in the middle, near a true coin flip. None of these is wrong exactly; the instruction genuinely underdetermines the answer. But if your pipeline depends on where that line lands, you now have a 20% to 77% behavioral spread hiding behind identical marketing claims of "follows instructions."

## Your one bad output was a sample

Here's the part that should change how you file these bugs. After my first 10 runs, Fable's boundary rate looked like 40%. At 30 runs it settled at 63%. My own benchmark misled me at a sample size that is ten times larger than the sample size anyone uses when they paste a prompt into a playground, see one bad output, and conclude the model "ignores instructions."

A single run tells you which side of the coin you saw. It cannot tell you the coin's bias, and the bias is the behavior. This is the same lesson as [benchmark-driven development](https://xu-hao.github.io/articles/benchmark-driven-development.html): a semantic failure reproduces as a fraction.

## What to do about it

Three things fall straight out of the data.

1. **Budget for ambiguity.** The models followed every rule that had a definite meaning. The failures clustered at the exact points where my instruction had no definite meaning. Before blaming the model, ask: does my instruction actually decide this case? Mine didn't.
2. **Name the boundary.** "Do not add new topics" left the overlap cases open. "If a memo item relates to an existing question, update that answer; if it would need a new question, leave it out" closes them. The instruction-writing skill that matters is enumerating the edge, and the edge is exactly what you'll find by sampling.
3. **Measure.** Ten runs and a grep told me more than a month of anecdotes. The whole harness is a bash loop, two prompt files, and a string-matching scorer. If a document transformation matters to your product, it deserves 10 runs and a fraction, and the fraction belongs in CI.

Everything is reproducible: cases, harness, scorer, and all 480 raw outputs are at [github.com/xu-hao/instruction-bleed](https://github.com/xu-hao/instruction-bleed). Swap in your own documents and your own boundary, and find out which side of the coin your pipeline has been silently betting on.

The next time a model "adds something you didn't ask for," check the instruction first. There's a decent chance you'll find what I found: a rule with an edge nobody defined, a model flipping a fair coin on it, and a single run pretending to be an answer.
