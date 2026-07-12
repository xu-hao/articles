# Stop Scrolling Up to Remember What You Asked Claude to Do.

## worknote is a live, two-level "what am I working on" note pinned under Claude Code, refreshed by a cheap model only when the conversation moves.

It's 3 PM and you have three Claude Code sessions open in three terminal tabs. One is migrating a schema. One is chasing a flaky test. The third has been running tools for five minutes, and you have honestly forgotten what you asked it to do. So you tab over and scroll: file reads, greps, a test run, more greps. Somewhere up in the scrollback is the message where you stated the task. You are now spending your attention reconstructing your own intent.

Scrollback is a log. It was fine when you wrote the code and the tool just displayed it. Agentic coding flips the ratio: the assistant works for minutes at a time, you supervise several of these at once, and every glance at a session starts with the same question. What is this one doing? The agent always knows. You are the one who forgets.

Discipline won't fix this, and neither will a bigger monitor. **A session's state should be readable in one glance, and a model that costs a fraction of a cent can keep that glance current.** That is the whole idea behind [worknote](https://github.com/xu-hao/worknote), a status line for Claude Code that pins this to the bottom of every session:

```
🎯 Build a per-session status-line summarizer for Claude Code
📌 Adding the worktree segment to the metadata row and refreshing the README
🌿 feat/worktree-seg  ·  🌳 worktree-seg  ·  21% ctx
```

*(Disclosure: I wrote worknote, so read the design opinions below with that bias in mind. It's MIT-licensed, free, and small enough to read in one sitting: two bash scripts and an installer.)*

Three lines, three questions:

- **🎯 Big picture** is why you're here. The session's overarching goal, the thing that stays true across many turns.
- **📌 Detail** is what's happening right now. It rewrites itself as the conversation moves.
- **🌿 Metadata** is where you are: branch, worktree if you're in one, and how full the context window is.

The rest of this article covers how those three lines are kept accurate and cheap. That is where the actual design decisions are.

## One stable line and one live line

When you come back to a session, you need the goal and the current step, and they move at completely different speeds. The goal should survive fifty turns. The step changes every turn. Collapse them into one summary and you get the worst of both: a line that churns so much you stop trusting it, or a line so general it tells you nothing.

So worknote holds them apart, and it enforces the stability of the goal line mechanically. On every refresh, the generator feeds the model the current goal back and asks for a verdict:

```
CHANGED: <yes or no. Say yes when the focus has moved to a different
  feature or objective, not merely the next small step within it.>
BIG: <the overarching goal as one terse phrase, at most 8 words>
NOW: <the specific thing being worked on right now, one sentence>
```

Unless the model answers yes, the goal line is reproduced character for character. Why so strict? Because a summarizer left to its own devices will happily rephrase the same goal a different way every call, and a status line that keeps rewording itself reads like noise. The yes/no question turns "rewrite the summary" into "judge whether the work changed", which is a much easier call for a small model to get right.

## Refresh only when a new message arrives

Status lines redraw constantly. The obvious implementation, summarize on every redraw, would bill you for staring at your own terminal. The other obvious implementation, summarize every N seconds, still burns tokens while you're at lunch.

worknote refreshes on exactly one event: the transcript gained a new user or assistant message. The script counts text messages in the session transcript and compares against the count it saw last time. No new message, no model call. An idle session costs zero. A long tool-running turn costs zero too: tool calls and tool results don't count as messages. You pay once per actual conversational step, which is the only time the note could have changed anyway.

The call itself runs detached in the background, so the status line renders instantly from the previous note and the refresh lands a few seconds later. The render path never waits on a model.

## Let the model ask for more context

How much transcript does the summarizer need? Usually very little. The last 14 messages almost always name the task. But sometimes the recent window is all confirmations: "yes", "ok", "do it". The real task is forty messages back, and a summary of "the developer agreed to something" helps nobody.

The tempting fix is to always send a big window. That costs more on every call and, worse, it drags the detail line backward: a model reading 120 messages summarizes the session instead of the moment. worknote does the opposite: it sends the small window first and tells the model to reply with the single word NEED_MORE if it can't tell what's being worked on. On that reply, the generator re-runs with 40 messages, then 120:

```bash
TIERS=("14:4000" "40:14000" "120:40000")
```

Escalation is the rare path, so the common path stays cheap and stays recent. The model decides when it needs history, which beats you guessing a window size that fits every conversation.

## One note per session

The note is keyed by session id, one file per session under `~/.claude/worknote/notes/`. Run five Claude Code sessions side by side and each tab shows its own goal, its own current step, its own branch. That was the point of the whole exercise: the times you most need the note are exactly the times you're running enough sessions to forget one.

## What it costs

One short Haiku call per message: a few thousand input tokens, a handful of output tokens. A fraction of a cent per refresh, nothing while idle, nothing while tools run. If you can afford the agent, the note that tells you what the agent is doing is a rounding error.

## Install

```sh
git clone https://github.com/xu-hao/worknote.git
cd worknote
./install.sh
```

The installer copies the scripts to `~/.claude/worknote/` and merges a `statusLine` entry into your Claude Code settings. It needs the `claude` CLI on your PATH plus `jq` and standard Unix tools, and it works on Linux and macOS. Uninstalling is `./uninstall.sh`, which removes only what was installed.

Next time you tab into that third session, the one you abandoned twenty minutes ago, don't scroll. The answer to "what was I doing here" is the bottom three lines of the terminal.
