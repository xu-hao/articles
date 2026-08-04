# Appendix: Every benchmark task and prompt

This appendix contains the frozen corpus used in the article: all 32 tasks and all 128 exact request bodies. Each task has the same four conditions: full prose, defined abbreviations, undefined abbreviations, and concise language. Token counts are Gemini 3.6 Flash count-token results.

The tasks are closed by default because this is a reference document. Expand a task to inspect its expected JSON answer and all four prompts.

<details><summary><strong>support-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 247 input tokens</summary>

<pre><code>Review every customer support request. A customer support request qualifies only when all three rules hold:
1. Its priority level is at least 3.
2. Its response deadline is day 10 or earlier.
3. Its escalation status is exactly &quot;required&quot;.

Records:
- R01 — priority level: 5; response deadline: day 1; escalation status: required.
- R02 — priority level: 1; response deadline: day 30; escalation status: not required.
- R03 — priority level: 4; response deadline: day 4; escalation status: pending.
- R04 — priority level: 4; response deadline: day 28; escalation status: pending.
- R05 — priority level: 4; response deadline: day 20; escalation status: pending.
- R06 — priority level: 4; response deadline: day 21; escalation status: required.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 252 input tokens</summary>

<pre><code>Abbreviation legend:
- CSR = customer support request
- PL = priority level
- RD = response deadline
- ES = escalation status

Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 3.
2. Its RD is day 10 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 4; RD: day 4; ES: pending.
- R04 — PL: 4; RD: day 28; ES: pending.
- R05 — PL: 4; RD: day 20; ES: pending.
- R06 — PL: 4; RD: day 21; ES: required.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 222 input tokens</summary>

<pre><code>Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 3.
2. Its RD is day 10 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 4; RD: day 4; ES: pending.
- R04 — PL: 4; RD: day 28; ES: pending.
- R05 — PL: 4; RD: day 20; ES: pending.
- R06 — PL: 4; RD: day 21; ES: required.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 158 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 10; state = &quot;required&quot;.

Records:
- R01: score=5; day=1; state=required.
- R02: score=1; day=30; state=not required.
- R03: score=4; day=4; state=pending.
- R04: score=4; day=28; state=pending.
- R05: score=4; day=20; state=pending.
- R06: score=4; day=21; state=required.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>support-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 401 input tokens</summary>

<pre><code>Review every customer support request. A customer support request qualifies only when all three rules hold:
1. Its priority level is at least 4.
2. Its response deadline is day 15 or earlier.
3. Its escalation status is exactly &quot;required&quot;.

Records:
- R01 — priority level: 5; response deadline: day 1; escalation status: required.
- R02 — priority level: 1; response deadline: day 30; escalation status: not required.
- R03 — priority level: 4; response deadline: day 28; escalation status: required.
- R04 — priority level: 1; response deadline: day 12; escalation status: required.
- R05 — priority level: 2; response deadline: day 17; escalation status: pending.
- R06 — priority level: 5; response deadline: day 23; escalation status: not required.
- R07 — priority level: 5; response deadline: day 18; escalation status: not required.
- R08 — priority level: 2; response deadline: day 27; escalation status: not required.
- R09 — priority level: 4; response deadline: day 24; escalation status: required.
- R10 — priority level: 5; response deadline: day 20; escalation status: pending.
- R11 — priority level: 3; response deadline: day 24; escalation status: pending.
- R12 — priority level: 4; response deadline: day 13; escalation status: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 388 input tokens</summary>

<pre><code>Abbreviation legend:
- CSR = customer support request
- PL = priority level
- RD = response deadline
- ES = escalation status

Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 4.
2. Its RD is day 15 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 4; RD: day 28; ES: required.
- R04 — PL: 1; RD: day 12; ES: required.
- R05 — PL: 2; RD: day 17; ES: pending.
- R06 — PL: 5; RD: day 23; ES: not required.
- R07 — PL: 5; RD: day 18; ES: not required.
- R08 — PL: 2; RD: day 27; ES: not required.
- R09 — PL: 4; RD: day 24; ES: required.
- R10 — PL: 5; RD: day 20; ES: pending.
- R11 — PL: 3; RD: day 24; ES: pending.
- R12 — PL: 4; RD: day 13; ES: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 358 input tokens</summary>

<pre><code>Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 4.
2. Its RD is day 15 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 4; RD: day 28; ES: required.
- R04 — PL: 1; RD: day 12; ES: required.
- R05 — PL: 2; RD: day 17; ES: pending.
- R06 — PL: 5; RD: day 23; ES: not required.
- R07 — PL: 5; RD: day 18; ES: not required.
- R08 — PL: 2; RD: day 27; ES: not required.
- R09 — PL: 4; RD: day 24; ES: required.
- R10 — PL: 5; RD: day 20; ES: pending.
- R11 — PL: 3; RD: day 24; ES: pending.
- R12 — PL: 4; RD: day 13; ES: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 276 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 15; state = &quot;required&quot;.

Records:
- R01: score=5; day=1; state=required.
- R02: score=1; day=30; state=not required.
- R03: score=4; day=28; state=required.
- R04: score=1; day=12; state=required.
- R05: score=2; day=17; state=pending.
- R06: score=5; day=23; state=not required.
- R07: score=5; day=18; state=not required.
- R08: score=2; day=27; state=not required.
- R09: score=4; day=24; state=required.
- R10: score=5; day=20; state=pending.
- R11: score=3; day=24; state=pending.
- R12: score=4; day=13; state=pending.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>support-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R08&quot;, &quot;R09&quot;, &quot;R18&quot;, &quot;R19&quot;]}</code></summary>

<details><summary>Full prose — 703 input tokens</summary>

<pre><code>Review every customer support request. A customer support request qualifies only when all three rules hold:
1. Its priority level is at least 3.
2. Its response deadline is day 20 or earlier.
3. Its escalation status is exactly &quot;required&quot;.

Records:
- R01 — priority level: 5; response deadline: day 1; escalation status: required.
- R02 — priority level: 1; response deadline: day 30; escalation status: not required.
- R03 — priority level: 5; response deadline: day 23; escalation status: required.
- R04 — priority level: 2; response deadline: day 30; escalation status: required.
- R05 — priority level: 4; response deadline: day 23; escalation status: not required.
- R06 — priority level: 5; response deadline: day 30; escalation status: required.
- R07 — priority level: 3; response deadline: day 14; escalation status: not required.
- R08 — priority level: 3; response deadline: day 11; escalation status: required.
- R09 — priority level: 5; response deadline: day 17; escalation status: required.
- R10 — priority level: 4; response deadline: day 25; escalation status: required.
- R11 — priority level: 5; response deadline: day 8; escalation status: pending.
- R12 — priority level: 2; response deadline: day 29; escalation status: required.
- R13 — priority level: 1; response deadline: day 12; escalation status: not required.
- R14 — priority level: 3; response deadline: day 21; escalation status: not required.
- R15 — priority level: 4; response deadline: day 15; escalation status: pending.
- R16 — priority level: 4; response deadline: day 27; escalation status: not required.
- R17 — priority level: 5; response deadline: day 30; escalation status: required.
- R18 — priority level: 4; response deadline: day 17; escalation status: required.
- R19 — priority level: 3; response deadline: day 14; escalation status: required.
- R20 — priority level: 3; response deadline: day 7; escalation status: not required.
- R21 — priority level: 3; response deadline: day 2; escalation status: not required.
- R22 — priority level: 3; response deadline: day 19; escalation status: not required.
- R23 — priority level: 2; response deadline: day 26; escalation status: not required.
- R24 — priority level: 3; response deadline: day 3; escalation status: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 654 input tokens</summary>

<pre><code>Abbreviation legend:
- CSR = customer support request
- PL = priority level
- RD = response deadline
- ES = escalation status

Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 3.
2. Its RD is day 20 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 5; RD: day 23; ES: required.
- R04 — PL: 2; RD: day 30; ES: required.
- R05 — PL: 4; RD: day 23; ES: not required.
- R06 — PL: 5; RD: day 30; ES: required.
- R07 — PL: 3; RD: day 14; ES: not required.
- R08 — PL: 3; RD: day 11; ES: required.
- R09 — PL: 5; RD: day 17; ES: required.
- R10 — PL: 4; RD: day 25; ES: required.
- R11 — PL: 5; RD: day 8; ES: pending.
- R12 — PL: 2; RD: day 29; ES: required.
- R13 — PL: 1; RD: day 12; ES: not required.
- R14 — PL: 3; RD: day 21; ES: not required.
- R15 — PL: 4; RD: day 15; ES: pending.
- R16 — PL: 4; RD: day 27; ES: not required.
- R17 — PL: 5; RD: day 30; ES: required.
- R18 — PL: 4; RD: day 17; ES: required.
- R19 — PL: 3; RD: day 14; ES: required.
- R20 — PL: 3; RD: day 7; ES: not required.
- R21 — PL: 3; RD: day 2; ES: not required.
- R22 — PL: 3; RD: day 19; ES: not required.
- R23 — PL: 2; RD: day 26; ES: not required.
- R24 — PL: 3; RD: day 3; ES: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 624 input tokens</summary>

<pre><code>Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 3.
2. Its RD is day 20 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 5; RD: day 23; ES: required.
- R04 — PL: 2; RD: day 30; ES: required.
- R05 — PL: 4; RD: day 23; ES: not required.
- R06 — PL: 5; RD: day 30; ES: required.
- R07 — PL: 3; RD: day 14; ES: not required.
- R08 — PL: 3; RD: day 11; ES: required.
- R09 — PL: 5; RD: day 17; ES: required.
- R10 — PL: 4; RD: day 25; ES: required.
- R11 — PL: 5; RD: day 8; ES: pending.
- R12 — PL: 2; RD: day 29; ES: required.
- R13 — PL: 1; RD: day 12; ES: not required.
- R14 — PL: 3; RD: day 21; ES: not required.
- R15 — PL: 4; RD: day 15; ES: pending.
- R16 — PL: 4; RD: day 27; ES: not required.
- R17 — PL: 5; RD: day 30; ES: required.
- R18 — PL: 4; RD: day 17; ES: required.
- R19 — PL: 3; RD: day 14; ES: required.
- R20 — PL: 3; RD: day 7; ES: not required.
- R21 — PL: 3; RD: day 2; ES: not required.
- R22 — PL: 3; RD: day 19; ES: not required.
- R23 — PL: 2; RD: day 26; ES: not required.
- R24 — PL: 3; RD: day 3; ES: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 506 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 20; state = &quot;required&quot;.

Records:
- R01: score=5; day=1; state=required.
- R02: score=1; day=30; state=not required.
- R03: score=5; day=23; state=required.
- R04: score=2; day=30; state=required.
- R05: score=4; day=23; state=not required.
- R06: score=5; day=30; state=required.
- R07: score=3; day=14; state=not required.
- R08: score=3; day=11; state=required.
- R09: score=5; day=17; state=required.
- R10: score=4; day=25; state=required.
- R11: score=5; day=8; state=pending.
- R12: score=2; day=29; state=required.
- R13: score=1; day=12; state=not required.
- R14: score=3; day=21; state=not required.
- R15: score=4; day=15; state=pending.
- R16: score=4; day=27; state=not required.
- R17: score=5; day=30; state=required.
- R18: score=4; day=17; state=required.
- R19: score=3; day=14; state=required.
- R20: score=3; day=7; state=not required.
- R21: score=3; day=2; state=not required.
- R22: score=3; day=19; state=not required.
- R23: score=2; day=26; state=not required.
- R24: score=3; day=3; state=pending.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>support-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 1298 input tokens</summary>

<pre><code>Review every customer support request. A customer support request qualifies only when all three rules hold:
1. Its priority level is at least 4.
2. Its response deadline is day 10 or earlier.
3. Its escalation status is exactly &quot;required&quot;.

Records:
- R01 — priority level: 5; response deadline: day 1; escalation status: required.
- R02 — priority level: 1; response deadline: day 30; escalation status: not required.
- R03 — priority level: 3; response deadline: day 24; escalation status: not required.
- R04 — priority level: 2; response deadline: day 2; escalation status: pending.
- R05 — priority level: 2; response deadline: day 10; escalation status: not required.
- R06 — priority level: 1; response deadline: day 25; escalation status: not required.
- R07 — priority level: 5; response deadline: day 17; escalation status: required.
- R08 — priority level: 3; response deadline: day 18; escalation status: not required.
- R09 — priority level: 3; response deadline: day 21; escalation status: required.
- R10 — priority level: 2; response deadline: day 13; escalation status: required.
- R11 — priority level: 5; response deadline: day 21; escalation status: pending.
- R12 — priority level: 3; response deadline: day 19; escalation status: not required.
- R13 — priority level: 1; response deadline: day 9; escalation status: required.
- R14 — priority level: 5; response deadline: day 26; escalation status: required.
- R15 — priority level: 2; response deadline: day 16; escalation status: pending.
- R16 — priority level: 5; response deadline: day 9; escalation status: pending.
- R17 — priority level: 4; response deadline: day 22; escalation status: pending.
- R18 — priority level: 2; response deadline: day 23; escalation status: pending.
- R19 — priority level: 3; response deadline: day 7; escalation status: required.
- R20 — priority level: 4; response deadline: day 13; escalation status: required.
- R21 — priority level: 2; response deadline: day 15; escalation status: required.
- R22 — priority level: 5; response deadline: day 14; escalation status: required.
- R23 — priority level: 5; response deadline: day 20; escalation status: required.
- R24 — priority level: 5; response deadline: day 19; escalation status: not required.
- R25 — priority level: 2; response deadline: day 27; escalation status: pending.
- R26 — priority level: 3; response deadline: day 10; escalation status: pending.
- R27 — priority level: 2; response deadline: day 4; escalation status: not required.
- R28 — priority level: 2; response deadline: day 3; escalation status: required.
- R29 — priority level: 1; response deadline: day 7; escalation status: not required.
- R30 — priority level: 4; response deadline: day 6; escalation status: pending.
- R31 — priority level: 3; response deadline: day 5; escalation status: required.
- R32 — priority level: 1; response deadline: day 18; escalation status: required.
- R33 — priority level: 1; response deadline: day 11; escalation status: not required.
- R34 — priority level: 4; response deadline: day 15; escalation status: not required.
- R35 — priority level: 4; response deadline: day 16; escalation status: pending.
- R36 — priority level: 2; response deadline: day 9; escalation status: pending.
- R37 — priority level: 3; response deadline: day 9; escalation status: pending.
- R38 — priority level: 4; response deadline: day 14; escalation status: not required.
- R39 — priority level: 2; response deadline: day 21; escalation status: not required.
- R40 — priority level: 5; response deadline: day 22; escalation status: required.
- R41 — priority level: 2; response deadline: day 1; escalation status: not required.
- R42 — priority level: 3; response deadline: day 13; escalation status: not required.
- R43 — priority level: 2; response deadline: day 28; escalation status: required.
- R44 — priority level: 4; response deadline: day 7; escalation status: pending.
- R45 — priority level: 1; response deadline: day 11; escalation status: pending.
- R46 — priority level: 3; response deadline: day 17; escalation status: pending.
- R47 — priority level: 5; response deadline: day 7; escalation status: pending.
- R48 — priority level: 4; response deadline: day 11; escalation status: required.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1177 input tokens</summary>

<pre><code>Abbreviation legend:
- CSR = customer support request
- PL = priority level
- RD = response deadline
- ES = escalation status

Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 4.
2. Its RD is day 10 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 3; RD: day 24; ES: not required.
- R04 — PL: 2; RD: day 2; ES: pending.
- R05 — PL: 2; RD: day 10; ES: not required.
- R06 — PL: 1; RD: day 25; ES: not required.
- R07 — PL: 5; RD: day 17; ES: required.
- R08 — PL: 3; RD: day 18; ES: not required.
- R09 — PL: 3; RD: day 21; ES: required.
- R10 — PL: 2; RD: day 13; ES: required.
- R11 — PL: 5; RD: day 21; ES: pending.
- R12 — PL: 3; RD: day 19; ES: not required.
- R13 — PL: 1; RD: day 9; ES: required.
- R14 — PL: 5; RD: day 26; ES: required.
- R15 — PL: 2; RD: day 16; ES: pending.
- R16 — PL: 5; RD: day 9; ES: pending.
- R17 — PL: 4; RD: day 22; ES: pending.
- R18 — PL: 2; RD: day 23; ES: pending.
- R19 — PL: 3; RD: day 7; ES: required.
- R20 — PL: 4; RD: day 13; ES: required.
- R21 — PL: 2; RD: day 15; ES: required.
- R22 — PL: 5; RD: day 14; ES: required.
- R23 — PL: 5; RD: day 20; ES: required.
- R24 — PL: 5; RD: day 19; ES: not required.
- R25 — PL: 2; RD: day 27; ES: pending.
- R26 — PL: 3; RD: day 10; ES: pending.
- R27 — PL: 2; RD: day 4; ES: not required.
- R28 — PL: 2; RD: day 3; ES: required.
- R29 — PL: 1; RD: day 7; ES: not required.
- R30 — PL: 4; RD: day 6; ES: pending.
- R31 — PL: 3; RD: day 5; ES: required.
- R32 — PL: 1; RD: day 18; ES: required.
- R33 — PL: 1; RD: day 11; ES: not required.
- R34 — PL: 4; RD: day 15; ES: not required.
- R35 — PL: 4; RD: day 16; ES: pending.
- R36 — PL: 2; RD: day 9; ES: pending.
- R37 — PL: 3; RD: day 9; ES: pending.
- R38 — PL: 4; RD: day 14; ES: not required.
- R39 — PL: 2; RD: day 21; ES: not required.
- R40 — PL: 5; RD: day 22; ES: required.
- R41 — PL: 2; RD: day 1; ES: not required.
- R42 — PL: 3; RD: day 13; ES: not required.
- R43 — PL: 2; RD: day 28; ES: required.
- R44 — PL: 4; RD: day 7; ES: pending.
- R45 — PL: 1; RD: day 11; ES: pending.
- R46 — PL: 3; RD: day 17; ES: pending.
- R47 — PL: 5; RD: day 7; ES: pending.
- R48 — PL: 4; RD: day 11; ES: required.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1147 input tokens</summary>

<pre><code>Review every CSR. A CSR qualifies only when all three rules hold:
1. Its PL is at least 4.
2. Its RD is day 10 or earlier.
3. Its ES is exactly &quot;required&quot;.

Records:
- R01 — PL: 5; RD: day 1; ES: required.
- R02 — PL: 1; RD: day 30; ES: not required.
- R03 — PL: 3; RD: day 24; ES: not required.
- R04 — PL: 2; RD: day 2; ES: pending.
- R05 — PL: 2; RD: day 10; ES: not required.
- R06 — PL: 1; RD: day 25; ES: not required.
- R07 — PL: 5; RD: day 17; ES: required.
- R08 — PL: 3; RD: day 18; ES: not required.
- R09 — PL: 3; RD: day 21; ES: required.
- R10 — PL: 2; RD: day 13; ES: required.
- R11 — PL: 5; RD: day 21; ES: pending.
- R12 — PL: 3; RD: day 19; ES: not required.
- R13 — PL: 1; RD: day 9; ES: required.
- R14 — PL: 5; RD: day 26; ES: required.
- R15 — PL: 2; RD: day 16; ES: pending.
- R16 — PL: 5; RD: day 9; ES: pending.
- R17 — PL: 4; RD: day 22; ES: pending.
- R18 — PL: 2; RD: day 23; ES: pending.
- R19 — PL: 3; RD: day 7; ES: required.
- R20 — PL: 4; RD: day 13; ES: required.
- R21 — PL: 2; RD: day 15; ES: required.
- R22 — PL: 5; RD: day 14; ES: required.
- R23 — PL: 5; RD: day 20; ES: required.
- R24 — PL: 5; RD: day 19; ES: not required.
- R25 — PL: 2; RD: day 27; ES: pending.
- R26 — PL: 3; RD: day 10; ES: pending.
- R27 — PL: 2; RD: day 4; ES: not required.
- R28 — PL: 2; RD: day 3; ES: required.
- R29 — PL: 1; RD: day 7; ES: not required.
- R30 — PL: 4; RD: day 6; ES: pending.
- R31 — PL: 3; RD: day 5; ES: required.
- R32 — PL: 1; RD: day 18; ES: required.
- R33 — PL: 1; RD: day 11; ES: not required.
- R34 — PL: 4; RD: day 15; ES: not required.
- R35 — PL: 4; RD: day 16; ES: pending.
- R36 — PL: 2; RD: day 9; ES: pending.
- R37 — PL: 3; RD: day 9; ES: pending.
- R38 — PL: 4; RD: day 14; ES: not required.
- R39 — PL: 2; RD: day 21; ES: not required.
- R40 — PL: 5; RD: day 22; ES: required.
- R41 — PL: 2; RD: day 1; ES: not required.
- R42 — PL: 3; RD: day 13; ES: not required.
- R43 — PL: 2; RD: day 28; ES: required.
- R44 — PL: 4; RD: day 7; ES: pending.
- R45 — PL: 1; RD: day 11; ES: pending.
- R46 — PL: 3; RD: day 17; ES: pending.
- R47 — PL: 5; RD: day 7; ES: pending.
- R48 — PL: 4; RD: day 11; ES: required.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 957 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 10; state = &quot;required&quot;.

Records:
- R01: score=5; day=1; state=required.
- R02: score=1; day=30; state=not required.
- R03: score=3; day=24; state=not required.
- R04: score=2; day=2; state=pending.
- R05: score=2; day=10; state=not required.
- R06: score=1; day=25; state=not required.
- R07: score=5; day=17; state=required.
- R08: score=3; day=18; state=not required.
- R09: score=3; day=21; state=required.
- R10: score=2; day=13; state=required.
- R11: score=5; day=21; state=pending.
- R12: score=3; day=19; state=not required.
- R13: score=1; day=9; state=required.
- R14: score=5; day=26; state=required.
- R15: score=2; day=16; state=pending.
- R16: score=5; day=9; state=pending.
- R17: score=4; day=22; state=pending.
- R18: score=2; day=23; state=pending.
- R19: score=3; day=7; state=required.
- R20: score=4; day=13; state=required.
- R21: score=2; day=15; state=required.
- R22: score=5; day=14; state=required.
- R23: score=5; day=20; state=required.
- R24: score=5; day=19; state=not required.
- R25: score=2; day=27; state=pending.
- R26: score=3; day=10; state=pending.
- R27: score=2; day=4; state=not required.
- R28: score=2; day=3; state=required.
- R29: score=1; day=7; state=not required.
- R30: score=4; day=6; state=pending.
- R31: score=3; day=5; state=required.
- R32: score=1; day=18; state=required.
- R33: score=1; day=11; state=not required.
- R34: score=4; day=15; state=not required.
- R35: score=4; day=16; state=pending.
- R36: score=2; day=9; state=pending.
- R37: score=3; day=9; state=pending.
- R38: score=4; day=14; state=not required.
- R39: score=2; day=21; state=not required.
- R40: score=5; day=22; state=required.
- R41: score=2; day=1; state=not required.
- R42: score=3; day=13; state=not required.
- R43: score=2; day=28; state=required.
- R44: score=4; day=7; state=pending.
- R45: score=1; day=11; state=pending.
- R46: score=3; day=17; state=pending.
- R47: score=5; day=7; state=pending.
- R48: score=4; day=11; state=required.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>logistics-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R04&quot;, &quot;R05&quot;]}</code></summary>

<details><summary>Full prose — 246 input tokens</summary>

<pre><code>Review every shipment exception record. A shipment exception record qualifies only when all three rules hold:
1. Its disruption severity is at least 4.
2. Its resolution deadline is day 15 or earlier.
3. Its carrier status is exactly &quot;confirmed&quot;.

Records:
- R01 — disruption severity: 5; resolution deadline: day 1; carrier status: confirmed.
- R02 — disruption severity: 1; resolution deadline: day 30; carrier status: delayed.
- R03 — disruption severity: 2; resolution deadline: day 10; carrier status: confirmed.
- R04 — disruption severity: 5; resolution deadline: day 8; carrier status: confirmed.
- R05 — disruption severity: 5; resolution deadline: day 10; carrier status: confirmed.
- R06 — disruption severity: 2; resolution deadline: day 11; carrier status: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 251 input tokens</summary>

<pre><code>Abbreviation legend:
- SER = shipment exception record
- DS = disruption severity
- RD = resolution deadline
- CS = carrier status

Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its RD is day 15 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 2; RD: day 10; CS: confirmed.
- R04 — DS: 5; RD: day 8; CS: confirmed.
- R05 — DS: 5; RD: day 10; CS: confirmed.
- R06 — DS: 2; RD: day 11; CS: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 221 input tokens</summary>

<pre><code>Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its RD is day 15 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 2; RD: day 10; CS: confirmed.
- R04 — DS: 5; RD: day 8; CS: confirmed.
- R05 — DS: 5; RD: day 10; CS: confirmed.
- R06 — DS: 2; RD: day 11; CS: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 157 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 15; state = &quot;confirmed&quot;.

Records:
- R01: score=5; day=1; state=confirmed.
- R02: score=1; day=30; state=delayed.
- R03: score=2; day=10; state=confirmed.
- R04: score=5; day=8; state=confirmed.
- R05: score=5; day=10; state=confirmed.
- R06: score=2; day=11; state=pending.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>logistics-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R06&quot;]}</code></summary>

<details><summary>Full prose — 394 input tokens</summary>

<pre><code>Review every shipment exception record. A shipment exception record qualifies only when all three rules hold:
1. Its disruption severity is at least 3.
2. Its resolution deadline is day 20 or earlier.
3. Its carrier status is exactly &quot;confirmed&quot;.

Records:
- R01 — disruption severity: 5; resolution deadline: day 1; carrier status: confirmed.
- R02 — disruption severity: 1; resolution deadline: day 30; carrier status: delayed.
- R03 — disruption severity: 2; resolution deadline: day 1; carrier status: confirmed.
- R04 — disruption severity: 4; resolution deadline: day 24; carrier status: delayed.
- R05 — disruption severity: 2; resolution deadline: day 24; carrier status: delayed.
- R06 — disruption severity: 4; resolution deadline: day 4; carrier status: confirmed.
- R07 — disruption severity: 4; resolution deadline: day 21; carrier status: delayed.
- R08 — disruption severity: 1; resolution deadline: day 2; carrier status: delayed.
- R09 — disruption severity: 2; resolution deadline: day 18; carrier status: delayed.
- R10 — disruption severity: 4; resolution deadline: day 29; carrier status: confirmed.
- R11 — disruption severity: 4; resolution deadline: day 14; carrier status: pending.
- R12 — disruption severity: 2; resolution deadline: day 29; carrier status: delayed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 381 input tokens</summary>

<pre><code>Abbreviation legend:
- SER = shipment exception record
- DS = disruption severity
- RD = resolution deadline
- CS = carrier status

Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its RD is day 20 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 2; RD: day 1; CS: confirmed.
- R04 — DS: 4; RD: day 24; CS: delayed.
- R05 — DS: 2; RD: day 24; CS: delayed.
- R06 — DS: 4; RD: day 4; CS: confirmed.
- R07 — DS: 4; RD: day 21; CS: delayed.
- R08 — DS: 1; RD: day 2; CS: delayed.
- R09 — DS: 2; RD: day 18; CS: delayed.
- R10 — DS: 4; RD: day 29; CS: confirmed.
- R11 — DS: 4; RD: day 14; CS: pending.
- R12 — DS: 2; RD: day 29; CS: delayed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 351 input tokens</summary>

<pre><code>Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its RD is day 20 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 2; RD: day 1; CS: confirmed.
- R04 — DS: 4; RD: day 24; CS: delayed.
- R05 — DS: 2; RD: day 24; CS: delayed.
- R06 — DS: 4; RD: day 4; CS: confirmed.
- R07 — DS: 4; RD: day 21; CS: delayed.
- R08 — DS: 1; RD: day 2; CS: delayed.
- R09 — DS: 2; RD: day 18; CS: delayed.
- R10 — DS: 4; RD: day 29; CS: confirmed.
- R11 — DS: 4; RD: day 14; CS: pending.
- R12 — DS: 2; RD: day 29; CS: delayed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 269 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 20; state = &quot;confirmed&quot;.

Records:
- R01: score=5; day=1; state=confirmed.
- R02: score=1; day=30; state=delayed.
- R03: score=2; day=1; state=confirmed.
- R04: score=4; day=24; state=delayed.
- R05: score=2; day=24; state=delayed.
- R06: score=4; day=4; state=confirmed.
- R07: score=4; day=21; state=delayed.
- R08: score=1; day=2; state=delayed.
- R09: score=2; day=18; state=delayed.
- R10: score=4; day=29; state=confirmed.
- R11: score=4; day=14; state=pending.
- R12: score=2; day=29; state=delayed.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>logistics-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R09&quot;]}</code></summary>

<details><summary>Full prose — 691 input tokens</summary>

<pre><code>Review every shipment exception record. A shipment exception record qualifies only when all three rules hold:
1. Its disruption severity is at least 4.
2. Its resolution deadline is day 10 or earlier.
3. Its carrier status is exactly &quot;confirmed&quot;.

Records:
- R01 — disruption severity: 5; resolution deadline: day 1; carrier status: confirmed.
- R02 — disruption severity: 1; resolution deadline: day 30; carrier status: delayed.
- R03 — disruption severity: 1; resolution deadline: day 4; carrier status: delayed.
- R04 — disruption severity: 2; resolution deadline: day 22; carrier status: confirmed.
- R05 — disruption severity: 1; resolution deadline: day 19; carrier status: confirmed.
- R06 — disruption severity: 5; resolution deadline: day 20; carrier status: pending.
- R07 — disruption severity: 3; resolution deadline: day 12; carrier status: confirmed.
- R08 — disruption severity: 4; resolution deadline: day 30; carrier status: confirmed.
- R09 — disruption severity: 5; resolution deadline: day 1; carrier status: confirmed.
- R10 — disruption severity: 5; resolution deadline: day 14; carrier status: pending.
- R11 — disruption severity: 1; resolution deadline: day 13; carrier status: pending.
- R12 — disruption severity: 5; resolution deadline: day 5; carrier status: delayed.
- R13 — disruption severity: 3; resolution deadline: day 7; carrier status: delayed.
- R14 — disruption severity: 4; resolution deadline: day 28; carrier status: confirmed.
- R15 — disruption severity: 5; resolution deadline: day 19; carrier status: confirmed.
- R16 — disruption severity: 3; resolution deadline: day 1; carrier status: pending.
- R17 — disruption severity: 1; resolution deadline: day 18; carrier status: delayed.
- R18 — disruption severity: 1; resolution deadline: day 11; carrier status: delayed.
- R19 — disruption severity: 4; resolution deadline: day 25; carrier status: confirmed.
- R20 — disruption severity: 5; resolution deadline: day 5; carrier status: pending.
- R21 — disruption severity: 3; resolution deadline: day 13; carrier status: pending.
- R22 — disruption severity: 4; resolution deadline: day 22; carrier status: delayed.
- R23 — disruption severity: 1; resolution deadline: day 16; carrier status: delayed.
- R24 — disruption severity: 5; resolution deadline: day 21; carrier status: delayed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 642 input tokens</summary>

<pre><code>Abbreviation legend:
- SER = shipment exception record
- DS = disruption severity
- RD = resolution deadline
- CS = carrier status

Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its RD is day 10 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 1; RD: day 4; CS: delayed.
- R04 — DS: 2; RD: day 22; CS: confirmed.
- R05 — DS: 1; RD: day 19; CS: confirmed.
- R06 — DS: 5; RD: day 20; CS: pending.
- R07 — DS: 3; RD: day 12; CS: confirmed.
- R08 — DS: 4; RD: day 30; CS: confirmed.
- R09 — DS: 5; RD: day 1; CS: confirmed.
- R10 — DS: 5; RD: day 14; CS: pending.
- R11 — DS: 1; RD: day 13; CS: pending.
- R12 — DS: 5; RD: day 5; CS: delayed.
- R13 — DS: 3; RD: day 7; CS: delayed.
- R14 — DS: 4; RD: day 28; CS: confirmed.
- R15 — DS: 5; RD: day 19; CS: confirmed.
- R16 — DS: 3; RD: day 1; CS: pending.
- R17 — DS: 1; RD: day 18; CS: delayed.
- R18 — DS: 1; RD: day 11; CS: delayed.
- R19 — DS: 4; RD: day 25; CS: confirmed.
- R20 — DS: 5; RD: day 5; CS: pending.
- R21 — DS: 3; RD: day 13; CS: pending.
- R22 — DS: 4; RD: day 22; CS: delayed.
- R23 — DS: 1; RD: day 16; CS: delayed.
- R24 — DS: 5; RD: day 21; CS: delayed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 612 input tokens</summary>

<pre><code>Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its RD is day 10 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 1; RD: day 4; CS: delayed.
- R04 — DS: 2; RD: day 22; CS: confirmed.
- R05 — DS: 1; RD: day 19; CS: confirmed.
- R06 — DS: 5; RD: day 20; CS: pending.
- R07 — DS: 3; RD: day 12; CS: confirmed.
- R08 — DS: 4; RD: day 30; CS: confirmed.
- R09 — DS: 5; RD: day 1; CS: confirmed.
- R10 — DS: 5; RD: day 14; CS: pending.
- R11 — DS: 1; RD: day 13; CS: pending.
- R12 — DS: 5; RD: day 5; CS: delayed.
- R13 — DS: 3; RD: day 7; CS: delayed.
- R14 — DS: 4; RD: day 28; CS: confirmed.
- R15 — DS: 5; RD: day 19; CS: confirmed.
- R16 — DS: 3; RD: day 1; CS: pending.
- R17 — DS: 1; RD: day 18; CS: delayed.
- R18 — DS: 1; RD: day 11; CS: delayed.
- R19 — DS: 4; RD: day 25; CS: confirmed.
- R20 — DS: 5; RD: day 5; CS: pending.
- R21 — DS: 3; RD: day 13; CS: pending.
- R22 — DS: 4; RD: day 22; CS: delayed.
- R23 — DS: 1; RD: day 16; CS: delayed.
- R24 — DS: 5; RD: day 21; CS: delayed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 494 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 10; state = &quot;confirmed&quot;.

Records:
- R01: score=5; day=1; state=confirmed.
- R02: score=1; day=30; state=delayed.
- R03: score=1; day=4; state=delayed.
- R04: score=2; day=22; state=confirmed.
- R05: score=1; day=19; state=confirmed.
- R06: score=5; day=20; state=pending.
- R07: score=3; day=12; state=confirmed.
- R08: score=4; day=30; state=confirmed.
- R09: score=5; day=1; state=confirmed.
- R10: score=5; day=14; state=pending.
- R11: score=1; day=13; state=pending.
- R12: score=5; day=5; state=delayed.
- R13: score=3; day=7; state=delayed.
- R14: score=4; day=28; state=confirmed.
- R15: score=5; day=19; state=confirmed.
- R16: score=3; day=1; state=pending.
- R17: score=1; day=18; state=delayed.
- R18: score=1; day=11; state=delayed.
- R19: score=4; day=25; state=confirmed.
- R20: score=5; day=5; state=pending.
- R21: score=3; day=13; state=pending.
- R22: score=4; day=22; state=delayed.
- R23: score=1; day=16; state=delayed.
- R24: score=5; day=21; state=delayed.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>logistics-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R22&quot;, &quot;R24&quot;, &quot;R41&quot;, &quot;R44&quot;]}</code></summary>

<details><summary>Full prose — 1286 input tokens</summary>

<pre><code>Review every shipment exception record. A shipment exception record qualifies only when all three rules hold:
1. Its disruption severity is at least 3.
2. Its resolution deadline is day 15 or earlier.
3. Its carrier status is exactly &quot;confirmed&quot;.

Records:
- R01 — disruption severity: 5; resolution deadline: day 1; carrier status: confirmed.
- R02 — disruption severity: 1; resolution deadline: day 30; carrier status: delayed.
- R03 — disruption severity: 5; resolution deadline: day 25; carrier status: pending.
- R04 — disruption severity: 2; resolution deadline: day 14; carrier status: pending.
- R05 — disruption severity: 2; resolution deadline: day 2; carrier status: pending.
- R06 — disruption severity: 2; resolution deadline: day 23; carrier status: delayed.
- R07 — disruption severity: 5; resolution deadline: day 22; carrier status: pending.
- R08 — disruption severity: 1; resolution deadline: day 11; carrier status: delayed.
- R09 — disruption severity: 2; resolution deadline: day 13; carrier status: delayed.
- R10 — disruption severity: 1; resolution deadline: day 17; carrier status: pending.
- R11 — disruption severity: 3; resolution deadline: day 26; carrier status: pending.
- R12 — disruption severity: 1; resolution deadline: day 13; carrier status: delayed.
- R13 — disruption severity: 5; resolution deadline: day 25; carrier status: confirmed.
- R14 — disruption severity: 1; resolution deadline: day 25; carrier status: confirmed.
- R15 — disruption severity: 5; resolution deadline: day 26; carrier status: pending.
- R16 — disruption severity: 5; resolution deadline: day 23; carrier status: pending.
- R17 — disruption severity: 2; resolution deadline: day 18; carrier status: delayed.
- R18 — disruption severity: 3; resolution deadline: day 8; carrier status: pending.
- R19 — disruption severity: 3; resolution deadline: day 29; carrier status: confirmed.
- R20 — disruption severity: 4; resolution deadline: day 21; carrier status: confirmed.
- R21 — disruption severity: 5; resolution deadline: day 13; carrier status: delayed.
- R22 — disruption severity: 5; resolution deadline: day 5; carrier status: confirmed.
- R23 — disruption severity: 2; resolution deadline: day 1; carrier status: pending.
- R24 — disruption severity: 5; resolution deadline: day 3; carrier status: confirmed.
- R25 — disruption severity: 2; resolution deadline: day 26; carrier status: pending.
- R26 — disruption severity: 2; resolution deadline: day 5; carrier status: confirmed.
- R27 — disruption severity: 2; resolution deadline: day 22; carrier status: confirmed.
- R28 — disruption severity: 2; resolution deadline: day 9; carrier status: pending.
- R29 — disruption severity: 2; resolution deadline: day 17; carrier status: delayed.
- R30 — disruption severity: 2; resolution deadline: day 10; carrier status: pending.
- R31 — disruption severity: 5; resolution deadline: day 15; carrier status: pending.
- R32 — disruption severity: 3; resolution deadline: day 19; carrier status: pending.
- R33 — disruption severity: 2; resolution deadline: day 30; carrier status: confirmed.
- R34 — disruption severity: 5; resolution deadline: day 28; carrier status: pending.
- R35 — disruption severity: 4; resolution deadline: day 10; carrier status: pending.
- R36 — disruption severity: 4; resolution deadline: day 15; carrier status: pending.
- R37 — disruption severity: 4; resolution deadline: day 29; carrier status: pending.
- R38 — disruption severity: 4; resolution deadline: day 26; carrier status: delayed.
- R39 — disruption severity: 2; resolution deadline: day 5; carrier status: pending.
- R40 — disruption severity: 5; resolution deadline: day 7; carrier status: delayed.
- R41 — disruption severity: 4; resolution deadline: day 2; carrier status: confirmed.
- R42 — disruption severity: 3; resolution deadline: day 23; carrier status: delayed.
- R43 — disruption severity: 2; resolution deadline: day 23; carrier status: delayed.
- R44 — disruption severity: 5; resolution deadline: day 7; carrier status: confirmed.
- R45 — disruption severity: 1; resolution deadline: day 12; carrier status: confirmed.
- R46 — disruption severity: 3; resolution deadline: day 21; carrier status: confirmed.
- R47 — disruption severity: 5; resolution deadline: day 28; carrier status: confirmed.
- R48 — disruption severity: 4; resolution deadline: day 19; carrier status: confirmed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1165 input tokens</summary>

<pre><code>Abbreviation legend:
- SER = shipment exception record
- DS = disruption severity
- RD = resolution deadline
- CS = carrier status

Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its RD is day 15 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 5; RD: day 25; CS: pending.
- R04 — DS: 2; RD: day 14; CS: pending.
- R05 — DS: 2; RD: day 2; CS: pending.
- R06 — DS: 2; RD: day 23; CS: delayed.
- R07 — DS: 5; RD: day 22; CS: pending.
- R08 — DS: 1; RD: day 11; CS: delayed.
- R09 — DS: 2; RD: day 13; CS: delayed.
- R10 — DS: 1; RD: day 17; CS: pending.
- R11 — DS: 3; RD: day 26; CS: pending.
- R12 — DS: 1; RD: day 13; CS: delayed.
- R13 — DS: 5; RD: day 25; CS: confirmed.
- R14 — DS: 1; RD: day 25; CS: confirmed.
- R15 — DS: 5; RD: day 26; CS: pending.
- R16 — DS: 5; RD: day 23; CS: pending.
- R17 — DS: 2; RD: day 18; CS: delayed.
- R18 — DS: 3; RD: day 8; CS: pending.
- R19 — DS: 3; RD: day 29; CS: confirmed.
- R20 — DS: 4; RD: day 21; CS: confirmed.
- R21 — DS: 5; RD: day 13; CS: delayed.
- R22 — DS: 5; RD: day 5; CS: confirmed.
- R23 — DS: 2; RD: day 1; CS: pending.
- R24 — DS: 5; RD: day 3; CS: confirmed.
- R25 — DS: 2; RD: day 26; CS: pending.
- R26 — DS: 2; RD: day 5; CS: confirmed.
- R27 — DS: 2; RD: day 22; CS: confirmed.
- R28 — DS: 2; RD: day 9; CS: pending.
- R29 — DS: 2; RD: day 17; CS: delayed.
- R30 — DS: 2; RD: day 10; CS: pending.
- R31 — DS: 5; RD: day 15; CS: pending.
- R32 — DS: 3; RD: day 19; CS: pending.
- R33 — DS: 2; RD: day 30; CS: confirmed.
- R34 — DS: 5; RD: day 28; CS: pending.
- R35 — DS: 4; RD: day 10; CS: pending.
- R36 — DS: 4; RD: day 15; CS: pending.
- R37 — DS: 4; RD: day 29; CS: pending.
- R38 — DS: 4; RD: day 26; CS: delayed.
- R39 — DS: 2; RD: day 5; CS: pending.
- R40 — DS: 5; RD: day 7; CS: delayed.
- R41 — DS: 4; RD: day 2; CS: confirmed.
- R42 — DS: 3; RD: day 23; CS: delayed.
- R43 — DS: 2; RD: day 23; CS: delayed.
- R44 — DS: 5; RD: day 7; CS: confirmed.
- R45 — DS: 1; RD: day 12; CS: confirmed.
- R46 — DS: 3; RD: day 21; CS: confirmed.
- R47 — DS: 5; RD: day 28; CS: confirmed.
- R48 — DS: 4; RD: day 19; CS: confirmed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1135 input tokens</summary>

<pre><code>Review every SER. A SER qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its RD is day 15 or earlier.
3. Its CS is exactly &quot;confirmed&quot;.

Records:
- R01 — DS: 5; RD: day 1; CS: confirmed.
- R02 — DS: 1; RD: day 30; CS: delayed.
- R03 — DS: 5; RD: day 25; CS: pending.
- R04 — DS: 2; RD: day 14; CS: pending.
- R05 — DS: 2; RD: day 2; CS: pending.
- R06 — DS: 2; RD: day 23; CS: delayed.
- R07 — DS: 5; RD: day 22; CS: pending.
- R08 — DS: 1; RD: day 11; CS: delayed.
- R09 — DS: 2; RD: day 13; CS: delayed.
- R10 — DS: 1; RD: day 17; CS: pending.
- R11 — DS: 3; RD: day 26; CS: pending.
- R12 — DS: 1; RD: day 13; CS: delayed.
- R13 — DS: 5; RD: day 25; CS: confirmed.
- R14 — DS: 1; RD: day 25; CS: confirmed.
- R15 — DS: 5; RD: day 26; CS: pending.
- R16 — DS: 5; RD: day 23; CS: pending.
- R17 — DS: 2; RD: day 18; CS: delayed.
- R18 — DS: 3; RD: day 8; CS: pending.
- R19 — DS: 3; RD: day 29; CS: confirmed.
- R20 — DS: 4; RD: day 21; CS: confirmed.
- R21 — DS: 5; RD: day 13; CS: delayed.
- R22 — DS: 5; RD: day 5; CS: confirmed.
- R23 — DS: 2; RD: day 1; CS: pending.
- R24 — DS: 5; RD: day 3; CS: confirmed.
- R25 — DS: 2; RD: day 26; CS: pending.
- R26 — DS: 2; RD: day 5; CS: confirmed.
- R27 — DS: 2; RD: day 22; CS: confirmed.
- R28 — DS: 2; RD: day 9; CS: pending.
- R29 — DS: 2; RD: day 17; CS: delayed.
- R30 — DS: 2; RD: day 10; CS: pending.
- R31 — DS: 5; RD: day 15; CS: pending.
- R32 — DS: 3; RD: day 19; CS: pending.
- R33 — DS: 2; RD: day 30; CS: confirmed.
- R34 — DS: 5; RD: day 28; CS: pending.
- R35 — DS: 4; RD: day 10; CS: pending.
- R36 — DS: 4; RD: day 15; CS: pending.
- R37 — DS: 4; RD: day 29; CS: pending.
- R38 — DS: 4; RD: day 26; CS: delayed.
- R39 — DS: 2; RD: day 5; CS: pending.
- R40 — DS: 5; RD: day 7; CS: delayed.
- R41 — DS: 4; RD: day 2; CS: confirmed.
- R42 — DS: 3; RD: day 23; CS: delayed.
- R43 — DS: 2; RD: day 23; CS: delayed.
- R44 — DS: 5; RD: day 7; CS: confirmed.
- R45 — DS: 1; RD: day 12; CS: confirmed.
- R46 — DS: 3; RD: day 21; CS: confirmed.
- R47 — DS: 5; RD: day 28; CS: confirmed.
- R48 — DS: 4; RD: day 19; CS: confirmed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 945 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 15; state = &quot;confirmed&quot;.

Records:
- R01: score=5; day=1; state=confirmed.
- R02: score=1; day=30; state=delayed.
- R03: score=5; day=25; state=pending.
- R04: score=2; day=14; state=pending.
- R05: score=2; day=2; state=pending.
- R06: score=2; day=23; state=delayed.
- R07: score=5; day=22; state=pending.
- R08: score=1; day=11; state=delayed.
- R09: score=2; day=13; state=delayed.
- R10: score=1; day=17; state=pending.
- R11: score=3; day=26; state=pending.
- R12: score=1; day=13; state=delayed.
- R13: score=5; day=25; state=confirmed.
- R14: score=1; day=25; state=confirmed.
- R15: score=5; day=26; state=pending.
- R16: score=5; day=23; state=pending.
- R17: score=2; day=18; state=delayed.
- R18: score=3; day=8; state=pending.
- R19: score=3; day=29; state=confirmed.
- R20: score=4; day=21; state=confirmed.
- R21: score=5; day=13; state=delayed.
- R22: score=5; day=5; state=confirmed.
- R23: score=2; day=1; state=pending.
- R24: score=5; day=3; state=confirmed.
- R25: score=2; day=26; state=pending.
- R26: score=2; day=5; state=confirmed.
- R27: score=2; day=22; state=confirmed.
- R28: score=2; day=9; state=pending.
- R29: score=2; day=17; state=delayed.
- R30: score=2; day=10; state=pending.
- R31: score=5; day=15; state=pending.
- R32: score=3; day=19; state=pending.
- R33: score=2; day=30; state=confirmed.
- R34: score=5; day=28; state=pending.
- R35: score=4; day=10; state=pending.
- R36: score=4; day=15; state=pending.
- R37: score=4; day=29; state=pending.
- R38: score=4; day=26; state=delayed.
- R39: score=2; day=5; state=pending.
- R40: score=5; day=7; state=delayed.
- R41: score=4; day=2; state=confirmed.
- R42: score=3; day=23; state=delayed.
- R43: score=2; day=23; state=delayed.
- R44: score=5; day=7; state=confirmed.
- R45: score=1; day=12; state=confirmed.
- R46: score=3; day=21; state=confirmed.
- R47: score=5; day=28; state=confirmed.
- R48: score=4; day=19; state=confirmed.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>security-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R05&quot;]}</code></summary>

<details><summary>Full prose — 246 input tokens</summary>

<pre><code>Review every security incident report. A security incident report qualifies only when all three rules hold:
1. Its risk level is at least 3.
2. Its remediation deadline is day 20 or earlier.
3. Its containment status is exactly &quot;complete&quot;.

Records:
- R01 — risk level: 5; remediation deadline: day 1; containment status: complete.
- R02 — risk level: 1; remediation deadline: day 30; containment status: incomplete.
- R03 — risk level: 3; remediation deadline: day 11; containment status: incomplete.
- R04 — risk level: 2; remediation deadline: day 7; containment status: incomplete.
- R05 — risk level: 3; remediation deadline: day 20; containment status: complete.
- R06 — risk level: 4; remediation deadline: day 20; containment status: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 251 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = security incident report
- RL = risk level
- RD = remediation deadline
- CS = containment status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 3.
2. Its RD is day 20 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 3; RD: day 11; CS: incomplete.
- R04 — RL: 2; RD: day 7; CS: incomplete.
- R05 — RL: 3; RD: day 20; CS: complete.
- R06 — RL: 4; RD: day 20; CS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 221 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 3.
2. Its RD is day 20 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 3; RD: day 11; CS: incomplete.
- R04 — RL: 2; RD: day 7; CS: incomplete.
- R05 — RL: 3; RD: day 20; CS: complete.
- R06 — RL: 4; RD: day 20; CS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 157 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 20; state = &quot;complete&quot;.

Records:
- R01: score=5; day=1; state=complete.
- R02: score=1; day=30; state=incomplete.
- R03: score=3; day=11; state=incomplete.
- R04: score=2; day=7; state=incomplete.
- R05: score=3; day=20; state=complete.
- R06: score=4; day=20; state=incomplete.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>security-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 394 input tokens</summary>

<pre><code>Review every security incident report. A security incident report qualifies only when all three rules hold:
1. Its risk level is at least 4.
2. Its remediation deadline is day 10 or earlier.
3. Its containment status is exactly &quot;complete&quot;.

Records:
- R01 — risk level: 5; remediation deadline: day 1; containment status: complete.
- R02 — risk level: 1; remediation deadline: day 30; containment status: incomplete.
- R03 — risk level: 4; remediation deadline: day 24; containment status: complete.
- R04 — risk level: 4; remediation deadline: day 17; containment status: complete.
- R05 — risk level: 5; remediation deadline: day 5; containment status: pending.
- R06 — risk level: 5; remediation deadline: day 28; containment status: complete.
- R07 — risk level: 5; remediation deadline: day 4; containment status: incomplete.
- R08 — risk level: 5; remediation deadline: day 15; containment status: incomplete.
- R09 — risk level: 3; remediation deadline: day 23; containment status: complete.
- R10 — risk level: 3; remediation deadline: day 18; containment status: incomplete.
- R11 — risk level: 2; remediation deadline: day 8; containment status: complete.
- R12 — risk level: 1; remediation deadline: day 22; containment status: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 381 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = security incident report
- RL = risk level
- RD = remediation deadline
- CS = containment status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 4.
2. Its RD is day 10 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 4; RD: day 24; CS: complete.
- R04 — RL: 4; RD: day 17; CS: complete.
- R05 — RL: 5; RD: day 5; CS: pending.
- R06 — RL: 5; RD: day 28; CS: complete.
- R07 — RL: 5; RD: day 4; CS: incomplete.
- R08 — RL: 5; RD: day 15; CS: incomplete.
- R09 — RL: 3; RD: day 23; CS: complete.
- R10 — RL: 3; RD: day 18; CS: incomplete.
- R11 — RL: 2; RD: day 8; CS: complete.
- R12 — RL: 1; RD: day 22; CS: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 351 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 4.
2. Its RD is day 10 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 4; RD: day 24; CS: complete.
- R04 — RL: 4; RD: day 17; CS: complete.
- R05 — RL: 5; RD: day 5; CS: pending.
- R06 — RL: 5; RD: day 28; CS: complete.
- R07 — RL: 5; RD: day 4; CS: incomplete.
- R08 — RL: 5; RD: day 15; CS: incomplete.
- R09 — RL: 3; RD: day 23; CS: complete.
- R10 — RL: 3; RD: day 18; CS: incomplete.
- R11 — RL: 2; RD: day 8; CS: complete.
- R12 — RL: 1; RD: day 22; CS: pending.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 269 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 10; state = &quot;complete&quot;.

Records:
- R01: score=5; day=1; state=complete.
- R02: score=1; day=30; state=incomplete.
- R03: score=4; day=24; state=complete.
- R04: score=4; day=17; state=complete.
- R05: score=5; day=5; state=pending.
- R06: score=5; day=28; state=complete.
- R07: score=5; day=4; state=incomplete.
- R08: score=5; day=15; state=incomplete.
- R09: score=3; day=23; state=complete.
- R10: score=3; day=18; state=incomplete.
- R11: score=2; day=8; state=complete.
- R12: score=1; day=22; state=pending.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>security-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R15&quot;]}</code></summary>

<details><summary>Full prose — 690 input tokens</summary>

<pre><code>Review every security incident report. A security incident report qualifies only when all three rules hold:
1. Its risk level is at least 3.
2. Its remediation deadline is day 15 or earlier.
3. Its containment status is exactly &quot;complete&quot;.

Records:
- R01 — risk level: 5; remediation deadline: day 1; containment status: complete.
- R02 — risk level: 1; remediation deadline: day 30; containment status: incomplete.
- R03 — risk level: 3; remediation deadline: day 1; containment status: pending.
- R04 — risk level: 4; remediation deadline: day 26; containment status: complete.
- R05 — risk level: 2; remediation deadline: day 3; containment status: pending.
- R06 — risk level: 4; remediation deadline: day 30; containment status: incomplete.
- R07 — risk level: 1; remediation deadline: day 23; containment status: incomplete.
- R08 — risk level: 1; remediation deadline: day 5; containment status: incomplete.
- R09 — risk level: 4; remediation deadline: day 27; containment status: pending.
- R10 — risk level: 2; remediation deadline: day 25; containment status: complete.
- R11 — risk level: 2; remediation deadline: day 4; containment status: complete.
- R12 — risk level: 1; remediation deadline: day 11; containment status: complete.
- R13 — risk level: 3; remediation deadline: day 26; containment status: incomplete.
- R14 — risk level: 4; remediation deadline: day 23; containment status: pending.
- R15 — risk level: 5; remediation deadline: day 14; containment status: complete.
- R16 — risk level: 1; remediation deadline: day 6; containment status: incomplete.
- R17 — risk level: 2; remediation deadline: day 17; containment status: incomplete.
- R18 — risk level: 3; remediation deadline: day 23; containment status: pending.
- R19 — risk level: 2; remediation deadline: day 11; containment status: complete.
- R20 — risk level: 3; remediation deadline: day 24; containment status: pending.
- R21 — risk level: 2; remediation deadline: day 21; containment status: pending.
- R22 — risk level: 4; remediation deadline: day 15; containment status: pending.
- R23 — risk level: 1; remediation deadline: day 4; containment status: complete.
- R24 — risk level: 3; remediation deadline: day 8; containment status: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 641 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = security incident report
- RL = risk level
- RD = remediation deadline
- CS = containment status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 3.
2. Its RD is day 15 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 3; RD: day 1; CS: pending.
- R04 — RL: 4; RD: day 26; CS: complete.
- R05 — RL: 2; RD: day 3; CS: pending.
- R06 — RL: 4; RD: day 30; CS: incomplete.
- R07 — RL: 1; RD: day 23; CS: incomplete.
- R08 — RL: 1; RD: day 5; CS: incomplete.
- R09 — RL: 4; RD: day 27; CS: pending.
- R10 — RL: 2; RD: day 25; CS: complete.
- R11 — RL: 2; RD: day 4; CS: complete.
- R12 — RL: 1; RD: day 11; CS: complete.
- R13 — RL: 3; RD: day 26; CS: incomplete.
- R14 — RL: 4; RD: day 23; CS: pending.
- R15 — RL: 5; RD: day 14; CS: complete.
- R16 — RL: 1; RD: day 6; CS: incomplete.
- R17 — RL: 2; RD: day 17; CS: incomplete.
- R18 — RL: 3; RD: day 23; CS: pending.
- R19 — RL: 2; RD: day 11; CS: complete.
- R20 — RL: 3; RD: day 24; CS: pending.
- R21 — RL: 2; RD: day 21; CS: pending.
- R22 — RL: 4; RD: day 15; CS: pending.
- R23 — RL: 1; RD: day 4; CS: complete.
- R24 — RL: 3; RD: day 8; CS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 611 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 3.
2. Its RD is day 15 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 3; RD: day 1; CS: pending.
- R04 — RL: 4; RD: day 26; CS: complete.
- R05 — RL: 2; RD: day 3; CS: pending.
- R06 — RL: 4; RD: day 30; CS: incomplete.
- R07 — RL: 1; RD: day 23; CS: incomplete.
- R08 — RL: 1; RD: day 5; CS: incomplete.
- R09 — RL: 4; RD: day 27; CS: pending.
- R10 — RL: 2; RD: day 25; CS: complete.
- R11 — RL: 2; RD: day 4; CS: complete.
- R12 — RL: 1; RD: day 11; CS: complete.
- R13 — RL: 3; RD: day 26; CS: incomplete.
- R14 — RL: 4; RD: day 23; CS: pending.
- R15 — RL: 5; RD: day 14; CS: complete.
- R16 — RL: 1; RD: day 6; CS: incomplete.
- R17 — RL: 2; RD: day 17; CS: incomplete.
- R18 — RL: 3; RD: day 23; CS: pending.
- R19 — RL: 2; RD: day 11; CS: complete.
- R20 — RL: 3; RD: day 24; CS: pending.
- R21 — RL: 2; RD: day 21; CS: pending.
- R22 — RL: 4; RD: day 15; CS: pending.
- R23 — RL: 1; RD: day 4; CS: complete.
- R24 — RL: 3; RD: day 8; CS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 493 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 15; state = &quot;complete&quot;.

Records:
- R01: score=5; day=1; state=complete.
- R02: score=1; day=30; state=incomplete.
- R03: score=3; day=1; state=pending.
- R04: score=4; day=26; state=complete.
- R05: score=2; day=3; state=pending.
- R06: score=4; day=30; state=incomplete.
- R07: score=1; day=23; state=incomplete.
- R08: score=1; day=5; state=incomplete.
- R09: score=4; day=27; state=pending.
- R10: score=2; day=25; state=complete.
- R11: score=2; day=4; state=complete.
- R12: score=1; day=11; state=complete.
- R13: score=3; day=26; state=incomplete.
- R14: score=4; day=23; state=pending.
- R15: score=5; day=14; state=complete.
- R16: score=1; day=6; state=incomplete.
- R17: score=2; day=17; state=incomplete.
- R18: score=3; day=23; state=pending.
- R19: score=2; day=11; state=complete.
- R20: score=3; day=24; state=pending.
- R21: score=2; day=21; state=pending.
- R22: score=4; day=15; state=pending.
- R23: score=1; day=4; state=complete.
- R24: score=3; day=8; state=incomplete.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>security-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R28&quot;, &quot;R30&quot;, &quot;R39&quot;]}</code></summary>

<details><summary>Full prose — 1282 input tokens</summary>

<pre><code>Review every security incident report. A security incident report qualifies only when all three rules hold:
1. Its risk level is at least 4.
2. Its remediation deadline is day 20 or earlier.
3. Its containment status is exactly &quot;complete&quot;.

Records:
- R01 — risk level: 5; remediation deadline: day 1; containment status: complete.
- R02 — risk level: 1; remediation deadline: day 30; containment status: incomplete.
- R03 — risk level: 3; remediation deadline: day 30; containment status: incomplete.
- R04 — risk level: 2; remediation deadline: day 12; containment status: incomplete.
- R05 — risk level: 2; remediation deadline: day 8; containment status: complete.
- R06 — risk level: 2; remediation deadline: day 14; containment status: pending.
- R07 — risk level: 1; remediation deadline: day 21; containment status: pending.
- R08 — risk level: 1; remediation deadline: day 25; containment status: pending.
- R09 — risk level: 3; remediation deadline: day 28; containment status: complete.
- R10 — risk level: 3; remediation deadline: day 2; containment status: pending.
- R11 — risk level: 4; remediation deadline: day 23; containment status: incomplete.
- R12 — risk level: 2; remediation deadline: day 21; containment status: incomplete.
- R13 — risk level: 3; remediation deadline: day 9; containment status: incomplete.
- R14 — risk level: 3; remediation deadline: day 22; containment status: complete.
- R15 — risk level: 5; remediation deadline: day 18; containment status: incomplete.
- R16 — risk level: 1; remediation deadline: day 18; containment status: pending.
- R17 — risk level: 3; remediation deadline: day 20; containment status: pending.
- R18 — risk level: 3; remediation deadline: day 1; containment status: pending.
- R19 — risk level: 5; remediation deadline: day 2; containment status: incomplete.
- R20 — risk level: 2; remediation deadline: day 2; containment status: complete.
- R21 — risk level: 4; remediation deadline: day 17; containment status: pending.
- R22 — risk level: 5; remediation deadline: day 27; containment status: complete.
- R23 — risk level: 3; remediation deadline: day 23; containment status: pending.
- R24 — risk level: 3; remediation deadline: day 9; containment status: complete.
- R25 — risk level: 3; remediation deadline: day 21; containment status: complete.
- R26 — risk level: 3; remediation deadline: day 26; containment status: incomplete.
- R27 — risk level: 1; remediation deadline: day 11; containment status: incomplete.
- R28 — risk level: 5; remediation deadline: day 17; containment status: complete.
- R29 — risk level: 2; remediation deadline: day 28; containment status: complete.
- R30 — risk level: 4; remediation deadline: day 13; containment status: complete.
- R31 — risk level: 4; remediation deadline: day 25; containment status: incomplete.
- R32 — risk level: 5; remediation deadline: day 21; containment status: pending.
- R33 — risk level: 4; remediation deadline: day 3; containment status: pending.
- R34 — risk level: 4; remediation deadline: day 23; containment status: pending.
- R35 — risk level: 3; remediation deadline: day 12; containment status: complete.
- R36 — risk level: 2; remediation deadline: day 25; containment status: complete.
- R37 — risk level: 4; remediation deadline: day 26; containment status: pending.
- R38 — risk level: 4; remediation deadline: day 2; containment status: incomplete.
- R39 — risk level: 5; remediation deadline: day 4; containment status: complete.
- R40 — risk level: 1; remediation deadline: day 3; containment status: incomplete.
- R41 — risk level: 3; remediation deadline: day 28; containment status: complete.
- R42 — risk level: 3; remediation deadline: day 12; containment status: incomplete.
- R43 — risk level: 3; remediation deadline: day 1; containment status: complete.
- R44 — risk level: 2; remediation deadline: day 4; containment status: complete.
- R45 — risk level: 4; remediation deadline: day 24; containment status: pending.
- R46 — risk level: 5; remediation deadline: day 4; containment status: incomplete.
- R47 — risk level: 5; remediation deadline: day 16; containment status: pending.
- R48 — risk level: 2; remediation deadline: day 1; containment status: complete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1161 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = security incident report
- RL = risk level
- RD = remediation deadline
- CS = containment status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 4.
2. Its RD is day 20 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 3; RD: day 30; CS: incomplete.
- R04 — RL: 2; RD: day 12; CS: incomplete.
- R05 — RL: 2; RD: day 8; CS: complete.
- R06 — RL: 2; RD: day 14; CS: pending.
- R07 — RL: 1; RD: day 21; CS: pending.
- R08 — RL: 1; RD: day 25; CS: pending.
- R09 — RL: 3; RD: day 28; CS: complete.
- R10 — RL: 3; RD: day 2; CS: pending.
- R11 — RL: 4; RD: day 23; CS: incomplete.
- R12 — RL: 2; RD: day 21; CS: incomplete.
- R13 — RL: 3; RD: day 9; CS: incomplete.
- R14 — RL: 3; RD: day 22; CS: complete.
- R15 — RL: 5; RD: day 18; CS: incomplete.
- R16 — RL: 1; RD: day 18; CS: pending.
- R17 — RL: 3; RD: day 20; CS: pending.
- R18 — RL: 3; RD: day 1; CS: pending.
- R19 — RL: 5; RD: day 2; CS: incomplete.
- R20 — RL: 2; RD: day 2; CS: complete.
- R21 — RL: 4; RD: day 17; CS: pending.
- R22 — RL: 5; RD: day 27; CS: complete.
- R23 — RL: 3; RD: day 23; CS: pending.
- R24 — RL: 3; RD: day 9; CS: complete.
- R25 — RL: 3; RD: day 21; CS: complete.
- R26 — RL: 3; RD: day 26; CS: incomplete.
- R27 — RL: 1; RD: day 11; CS: incomplete.
- R28 — RL: 5; RD: day 17; CS: complete.
- R29 — RL: 2; RD: day 28; CS: complete.
- R30 — RL: 4; RD: day 13; CS: complete.
- R31 — RL: 4; RD: day 25; CS: incomplete.
- R32 — RL: 5; RD: day 21; CS: pending.
- R33 — RL: 4; RD: day 3; CS: pending.
- R34 — RL: 4; RD: day 23; CS: pending.
- R35 — RL: 3; RD: day 12; CS: complete.
- R36 — RL: 2; RD: day 25; CS: complete.
- R37 — RL: 4; RD: day 26; CS: pending.
- R38 — RL: 4; RD: day 2; CS: incomplete.
- R39 — RL: 5; RD: day 4; CS: complete.
- R40 — RL: 1; RD: day 3; CS: incomplete.
- R41 — RL: 3; RD: day 28; CS: complete.
- R42 — RL: 3; RD: day 12; CS: incomplete.
- R43 — RL: 3; RD: day 1; CS: complete.
- R44 — RL: 2; RD: day 4; CS: complete.
- R45 — RL: 4; RD: day 24; CS: pending.
- R46 — RL: 5; RD: day 4; CS: incomplete.
- R47 — RL: 5; RD: day 16; CS: pending.
- R48 — RL: 2; RD: day 1; CS: complete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1131 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its RL is at least 4.
2. Its RD is day 20 or earlier.
3. Its CS is exactly &quot;complete&quot;.

Records:
- R01 — RL: 5; RD: day 1; CS: complete.
- R02 — RL: 1; RD: day 30; CS: incomplete.
- R03 — RL: 3; RD: day 30; CS: incomplete.
- R04 — RL: 2; RD: day 12; CS: incomplete.
- R05 — RL: 2; RD: day 8; CS: complete.
- R06 — RL: 2; RD: day 14; CS: pending.
- R07 — RL: 1; RD: day 21; CS: pending.
- R08 — RL: 1; RD: day 25; CS: pending.
- R09 — RL: 3; RD: day 28; CS: complete.
- R10 — RL: 3; RD: day 2; CS: pending.
- R11 — RL: 4; RD: day 23; CS: incomplete.
- R12 — RL: 2; RD: day 21; CS: incomplete.
- R13 — RL: 3; RD: day 9; CS: incomplete.
- R14 — RL: 3; RD: day 22; CS: complete.
- R15 — RL: 5; RD: day 18; CS: incomplete.
- R16 — RL: 1; RD: day 18; CS: pending.
- R17 — RL: 3; RD: day 20; CS: pending.
- R18 — RL: 3; RD: day 1; CS: pending.
- R19 — RL: 5; RD: day 2; CS: incomplete.
- R20 — RL: 2; RD: day 2; CS: complete.
- R21 — RL: 4; RD: day 17; CS: pending.
- R22 — RL: 5; RD: day 27; CS: complete.
- R23 — RL: 3; RD: day 23; CS: pending.
- R24 — RL: 3; RD: day 9; CS: complete.
- R25 — RL: 3; RD: day 21; CS: complete.
- R26 — RL: 3; RD: day 26; CS: incomplete.
- R27 — RL: 1; RD: day 11; CS: incomplete.
- R28 — RL: 5; RD: day 17; CS: complete.
- R29 — RL: 2; RD: day 28; CS: complete.
- R30 — RL: 4; RD: day 13; CS: complete.
- R31 — RL: 4; RD: day 25; CS: incomplete.
- R32 — RL: 5; RD: day 21; CS: pending.
- R33 — RL: 4; RD: day 3; CS: pending.
- R34 — RL: 4; RD: day 23; CS: pending.
- R35 — RL: 3; RD: day 12; CS: complete.
- R36 — RL: 2; RD: day 25; CS: complete.
- R37 — RL: 4; RD: day 26; CS: pending.
- R38 — RL: 4; RD: day 2; CS: incomplete.
- R39 — RL: 5; RD: day 4; CS: complete.
- R40 — RL: 1; RD: day 3; CS: incomplete.
- R41 — RL: 3; RD: day 28; CS: complete.
- R42 — RL: 3; RD: day 12; CS: incomplete.
- R43 — RL: 3; RD: day 1; CS: complete.
- R44 — RL: 2; RD: day 4; CS: complete.
- R45 — RL: 4; RD: day 24; CS: pending.
- R46 — RL: 5; RD: day 4; CS: incomplete.
- R47 — RL: 5; RD: day 16; CS: pending.
- R48 — RL: 2; RD: day 1; CS: complete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 941 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 20; state = &quot;complete&quot;.

Records:
- R01: score=5; day=1; state=complete.
- R02: score=1; day=30; state=incomplete.
- R03: score=3; day=30; state=incomplete.
- R04: score=2; day=12; state=incomplete.
- R05: score=2; day=8; state=complete.
- R06: score=2; day=14; state=pending.
- R07: score=1; day=21; state=pending.
- R08: score=1; day=25; state=pending.
- R09: score=3; day=28; state=complete.
- R10: score=3; day=2; state=pending.
- R11: score=4; day=23; state=incomplete.
- R12: score=2; day=21; state=incomplete.
- R13: score=3; day=9; state=incomplete.
- R14: score=3; day=22; state=complete.
- R15: score=5; day=18; state=incomplete.
- R16: score=1; day=18; state=pending.
- R17: score=3; day=20; state=pending.
- R18: score=3; day=1; state=pending.
- R19: score=5; day=2; state=incomplete.
- R20: score=2; day=2; state=complete.
- R21: score=4; day=17; state=pending.
- R22: score=5; day=27; state=complete.
- R23: score=3; day=23; state=pending.
- R24: score=3; day=9; state=complete.
- R25: score=3; day=21; state=complete.
- R26: score=3; day=26; state=incomplete.
- R27: score=1; day=11; state=incomplete.
- R28: score=5; day=17; state=complete.
- R29: score=2; day=28; state=complete.
- R30: score=4; day=13; state=complete.
- R31: score=4; day=25; state=incomplete.
- R32: score=5; day=21; state=pending.
- R33: score=4; day=3; state=pending.
- R34: score=4; day=23; state=pending.
- R35: score=3; day=12; state=complete.
- R36: score=2; day=25; state=complete.
- R37: score=4; day=26; state=pending.
- R38: score=4; day=2; state=incomplete.
- R39: score=5; day=4; state=complete.
- R40: score=1; day=3; state=incomplete.
- R41: score=3; day=28; state=complete.
- R42: score=3; day=12; state=incomplete.
- R43: score=3; day=1; state=complete.
- R44: score=2; day=4; state=complete.
- R45: score=4; day=24; state=pending.
- R46: score=5; day=4; state=incomplete.
- R47: score=5; day=16; state=pending.
- R48: score=2; day=1; state=complete.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>finance-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 247 input tokens</summary>

<pre><code>Review every expense reimbursement request. A expense reimbursement request qualifies only when all three rules hold:
1. Its audit score is at least 4.
2. Its submission deadline is day 10 or earlier.
3. Its approval status is exactly &quot;approved&quot;.

Records:
- R01 — audit score: 5; submission deadline: day 1; approval status: approved.
- R02 — audit score: 1; submission deadline: day 30; approval status: denied.
- R03 — audit score: 2; submission deadline: day 28; approval status: denied.
- R04 — audit score: 1; submission deadline: day 12; approval status: pending.
- R05 — audit score: 1; submission deadline: day 12; approval status: denied.
- R06 — audit score: 3; submission deadline: day 15; approval status: approved.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 252 input tokens</summary>

<pre><code>Abbreviation legend:
- ERR = expense reimbursement request
- AS = audit score
- SD = submission deadline
- APS = approval status

Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 4.
2. Its SD is day 10 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 2; SD: day 28; APS: denied.
- R04 — AS: 1; SD: day 12; APS: pending.
- R05 — AS: 1; SD: day 12; APS: denied.
- R06 — AS: 3; SD: day 15; APS: approved.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 222 input tokens</summary>

<pre><code>Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 4.
2. Its SD is day 10 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 2; SD: day 28; APS: denied.
- R04 — AS: 1; SD: day 12; APS: pending.
- R05 — AS: 1; SD: day 12; APS: denied.
- R06 — AS: 3; SD: day 15; APS: approved.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 161 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 10; state = &quot;approved&quot;.

Records:
- R01: score=5; day=1; state=approved.
- R02: score=1; day=30; state=denied.
- R03: score=2; day=28; state=denied.
- R04: score=1; day=12; state=pending.
- R05: score=1; day=12; state=denied.
- R06: score=3; day=15; state=approved.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>finance-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R03&quot;]}</code></summary>

<details><summary>Full prose — 393 input tokens</summary>

<pre><code>Review every expense reimbursement request. A expense reimbursement request qualifies only when all three rules hold:
1. Its audit score is at least 3.
2. Its submission deadline is day 15 or earlier.
3. Its approval status is exactly &quot;approved&quot;.

Records:
- R01 — audit score: 5; submission deadline: day 1; approval status: approved.
- R02 — audit score: 1; submission deadline: day 30; approval status: denied.
- R03 — audit score: 3; submission deadline: day 9; approval status: approved.
- R04 — audit score: 1; submission deadline: day 18; approval status: approved.
- R05 — audit score: 2; submission deadline: day 18; approval status: approved.
- R06 — audit score: 1; submission deadline: day 1; approval status: pending.
- R07 — audit score: 1; submission deadline: day 27; approval status: pending.
- R08 — audit score: 5; submission deadline: day 3; approval status: denied.
- R09 — audit score: 3; submission deadline: day 4; approval status: pending.
- R10 — audit score: 5; submission deadline: day 28; approval status: denied.
- R11 — audit score: 4; submission deadline: day 30; approval status: pending.
- R12 — audit score: 3; submission deadline: day 23; approval status: approved.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 380 input tokens</summary>

<pre><code>Abbreviation legend:
- ERR = expense reimbursement request
- AS = audit score
- SD = submission deadline
- APS = approval status

Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 3.
2. Its SD is day 15 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 3; SD: day 9; APS: approved.
- R04 — AS: 1; SD: day 18; APS: approved.
- R05 — AS: 2; SD: day 18; APS: approved.
- R06 — AS: 1; SD: day 1; APS: pending.
- R07 — AS: 1; SD: day 27; APS: pending.
- R08 — AS: 5; SD: day 3; APS: denied.
- R09 — AS: 3; SD: day 4; APS: pending.
- R10 — AS: 5; SD: day 28; APS: denied.
- R11 — AS: 4; SD: day 30; APS: pending.
- R12 — AS: 3; SD: day 23; APS: approved.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 350 input tokens</summary>

<pre><code>Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 3.
2. Its SD is day 15 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 3; SD: day 9; APS: approved.
- R04 — AS: 1; SD: day 18; APS: approved.
- R05 — AS: 2; SD: day 18; APS: approved.
- R06 — AS: 1; SD: day 1; APS: pending.
- R07 — AS: 1; SD: day 27; APS: pending.
- R08 — AS: 5; SD: day 3; APS: denied.
- R09 — AS: 3; SD: day 4; APS: pending.
- R10 — AS: 5; SD: day 28; APS: denied.
- R11 — AS: 4; SD: day 30; APS: pending.
- R12 — AS: 3; SD: day 23; APS: approved.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 271 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 15; state = &quot;approved&quot;.

Records:
- R01: score=5; day=1; state=approved.
- R02: score=1; day=30; state=denied.
- R03: score=3; day=9; state=approved.
- R04: score=1; day=18; state=approved.
- R05: score=2; day=18; state=approved.
- R06: score=1; day=1; state=pending.
- R07: score=1; day=27; state=pending.
- R08: score=5; day=3; state=denied.
- R09: score=3; day=4; state=pending.
- R10: score=5; day=28; state=denied.
- R11: score=4; day=30; state=pending.
- R12: score=3; day=23; state=approved.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>finance-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R17&quot;]}</code></summary>

<details><summary>Full prose — 692 input tokens</summary>

<pre><code>Review every expense reimbursement request. A expense reimbursement request qualifies only when all three rules hold:
1. Its audit score is at least 4.
2. Its submission deadline is day 20 or earlier.
3. Its approval status is exactly &quot;approved&quot;.

Records:
- R01 — audit score: 5; submission deadline: day 1; approval status: approved.
- R02 — audit score: 1; submission deadline: day 30; approval status: denied.
- R03 — audit score: 1; submission deadline: day 6; approval status: denied.
- R04 — audit score: 5; submission deadline: day 28; approval status: denied.
- R05 — audit score: 4; submission deadline: day 15; approval status: denied.
- R06 — audit score: 4; submission deadline: day 5; approval status: pending.
- R07 — audit score: 3; submission deadline: day 10; approval status: denied.
- R08 — audit score: 2; submission deadline: day 28; approval status: approved.
- R09 — audit score: 4; submission deadline: day 28; approval status: approved.
- R10 — audit score: 1; submission deadline: day 19; approval status: approved.
- R11 — audit score: 2; submission deadline: day 25; approval status: denied.
- R12 — audit score: 5; submission deadline: day 12; approval status: pending.
- R13 — audit score: 4; submission deadline: day 6; approval status: denied.
- R14 — audit score: 1; submission deadline: day 5; approval status: approved.
- R15 — audit score: 3; submission deadline: day 28; approval status: denied.
- R16 — audit score: 4; submission deadline: day 29; approval status: pending.
- R17 — audit score: 5; submission deadline: day 6; approval status: approved.
- R18 — audit score: 5; submission deadline: day 15; approval status: pending.
- R19 — audit score: 3; submission deadline: day 25; approval status: pending.
- R20 — audit score: 3; submission deadline: day 14; approval status: approved.
- R21 — audit score: 3; submission deadline: day 16; approval status: pending.
- R22 — audit score: 3; submission deadline: day 27; approval status: approved.
- R23 — audit score: 3; submission deadline: day 19; approval status: denied.
- R24 — audit score: 5; submission deadline: day 27; approval status: denied.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 643 input tokens</summary>

<pre><code>Abbreviation legend:
- ERR = expense reimbursement request
- AS = audit score
- SD = submission deadline
- APS = approval status

Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 4.
2. Its SD is day 20 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 1; SD: day 6; APS: denied.
- R04 — AS: 5; SD: day 28; APS: denied.
- R05 — AS: 4; SD: day 15; APS: denied.
- R06 — AS: 4; SD: day 5; APS: pending.
- R07 — AS: 3; SD: day 10; APS: denied.
- R08 — AS: 2; SD: day 28; APS: approved.
- R09 — AS: 4; SD: day 28; APS: approved.
- R10 — AS: 1; SD: day 19; APS: approved.
- R11 — AS: 2; SD: day 25; APS: denied.
- R12 — AS: 5; SD: day 12; APS: pending.
- R13 — AS: 4; SD: day 6; APS: denied.
- R14 — AS: 1; SD: day 5; APS: approved.
- R15 — AS: 3; SD: day 28; APS: denied.
- R16 — AS: 4; SD: day 29; APS: pending.
- R17 — AS: 5; SD: day 6; APS: approved.
- R18 — AS: 5; SD: day 15; APS: pending.
- R19 — AS: 3; SD: day 25; APS: pending.
- R20 — AS: 3; SD: day 14; APS: approved.
- R21 — AS: 3; SD: day 16; APS: pending.
- R22 — AS: 3; SD: day 27; APS: approved.
- R23 — AS: 3; SD: day 19; APS: denied.
- R24 — AS: 5; SD: day 27; APS: denied.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 613 input tokens</summary>

<pre><code>Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 4.
2. Its SD is day 20 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 1; SD: day 6; APS: denied.
- R04 — AS: 5; SD: day 28; APS: denied.
- R05 — AS: 4; SD: day 15; APS: denied.
- R06 — AS: 4; SD: day 5; APS: pending.
- R07 — AS: 3; SD: day 10; APS: denied.
- R08 — AS: 2; SD: day 28; APS: approved.
- R09 — AS: 4; SD: day 28; APS: approved.
- R10 — AS: 1; SD: day 19; APS: approved.
- R11 — AS: 2; SD: day 25; APS: denied.
- R12 — AS: 5; SD: day 12; APS: pending.
- R13 — AS: 4; SD: day 6; APS: denied.
- R14 — AS: 1; SD: day 5; APS: approved.
- R15 — AS: 3; SD: day 28; APS: denied.
- R16 — AS: 4; SD: day 29; APS: pending.
- R17 — AS: 5; SD: day 6; APS: approved.
- R18 — AS: 5; SD: day 15; APS: pending.
- R19 — AS: 3; SD: day 25; APS: pending.
- R20 — AS: 3; SD: day 14; APS: approved.
- R21 — AS: 3; SD: day 16; APS: pending.
- R22 — AS: 3; SD: day 27; APS: approved.
- R23 — AS: 3; SD: day 19; APS: denied.
- R24 — AS: 5; SD: day 27; APS: denied.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 505 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 20; state = &quot;approved&quot;.

Records:
- R01: score=5; day=1; state=approved.
- R02: score=1; day=30; state=denied.
- R03: score=1; day=6; state=denied.
- R04: score=5; day=28; state=denied.
- R05: score=4; day=15; state=denied.
- R06: score=4; day=5; state=pending.
- R07: score=3; day=10; state=denied.
- R08: score=2; day=28; state=approved.
- R09: score=4; day=28; state=approved.
- R10: score=1; day=19; state=approved.
- R11: score=2; day=25; state=denied.
- R12: score=5; day=12; state=pending.
- R13: score=4; day=6; state=denied.
- R14: score=1; day=5; state=approved.
- R15: score=3; day=28; state=denied.
- R16: score=4; day=29; state=pending.
- R17: score=5; day=6; state=approved.
- R18: score=5; day=15; state=pending.
- R19: score=3; day=25; state=pending.
- R20: score=3; day=14; state=approved.
- R21: score=3; day=16; state=pending.
- R22: score=3; day=27; state=approved.
- R23: score=3; day=19; state=denied.
- R24: score=5; day=27; state=denied.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>finance-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R03&quot;, &quot;R30&quot;, &quot;R42&quot;, &quot;R44&quot;]}</code></summary>

<details><summary>Full prose — 1282 input tokens</summary>

<pre><code>Review every expense reimbursement request. A expense reimbursement request qualifies only when all three rules hold:
1. Its audit score is at least 3.
2. Its submission deadline is day 10 or earlier.
3. Its approval status is exactly &quot;approved&quot;.

Records:
- R01 — audit score: 5; submission deadline: day 1; approval status: approved.
- R02 — audit score: 1; submission deadline: day 30; approval status: denied.
- R03 — audit score: 3; submission deadline: day 10; approval status: approved.
- R04 — audit score: 2; submission deadline: day 1; approval status: denied.
- R05 — audit score: 2; submission deadline: day 30; approval status: approved.
- R06 — audit score: 4; submission deadline: day 11; approval status: approved.
- R07 — audit score: 1; submission deadline: day 17; approval status: pending.
- R08 — audit score: 4; submission deadline: day 16; approval status: pending.
- R09 — audit score: 2; submission deadline: day 8; approval status: denied.
- R10 — audit score: 3; submission deadline: day 26; approval status: pending.
- R11 — audit score: 2; submission deadline: day 23; approval status: denied.
- R12 — audit score: 3; submission deadline: day 7; approval status: pending.
- R13 — audit score: 1; submission deadline: day 22; approval status: approved.
- R14 — audit score: 4; submission deadline: day 8; approval status: denied.
- R15 — audit score: 4; submission deadline: day 8; approval status: pending.
- R16 — audit score: 3; submission deadline: day 28; approval status: approved.
- R17 — audit score: 2; submission deadline: day 5; approval status: denied.
- R18 — audit score: 2; submission deadline: day 15; approval status: approved.
- R19 — audit score: 1; submission deadline: day 3; approval status: pending.
- R20 — audit score: 4; submission deadline: day 15; approval status: denied.
- R21 — audit score: 3; submission deadline: day 26; approval status: approved.
- R22 — audit score: 3; submission deadline: day 26; approval status: denied.
- R23 — audit score: 3; submission deadline: day 21; approval status: pending.
- R24 — audit score: 4; submission deadline: day 9; approval status: pending.
- R25 — audit score: 2; submission deadline: day 14; approval status: approved.
- R26 — audit score: 5; submission deadline: day 22; approval status: approved.
- R27 — audit score: 1; submission deadline: day 2; approval status: pending.
- R28 — audit score: 3; submission deadline: day 30; approval status: denied.
- R29 — audit score: 1; submission deadline: day 9; approval status: pending.
- R30 — audit score: 4; submission deadline: day 5; approval status: approved.
- R31 — audit score: 1; submission deadline: day 10; approval status: denied.
- R32 — audit score: 5; submission deadline: day 23; approval status: approved.
- R33 — audit score: 3; submission deadline: day 14; approval status: denied.
- R34 — audit score: 5; submission deadline: day 30; approval status: approved.
- R35 — audit score: 2; submission deadline: day 21; approval status: denied.
- R36 — audit score: 3; submission deadline: day 23; approval status: pending.
- R37 — audit score: 4; submission deadline: day 25; approval status: denied.
- R38 — audit score: 1; submission deadline: day 13; approval status: pending.
- R39 — audit score: 4; submission deadline: day 29; approval status: approved.
- R40 — audit score: 4; submission deadline: day 14; approval status: approved.
- R41 — audit score: 1; submission deadline: day 3; approval status: denied.
- R42 — audit score: 4; submission deadline: day 6; approval status: approved.
- R43 — audit score: 1; submission deadline: day 26; approval status: approved.
- R44 — audit score: 3; submission deadline: day 9; approval status: approved.
- R45 — audit score: 4; submission deadline: day 23; approval status: pending.
- R46 — audit score: 4; submission deadline: day 19; approval status: approved.
- R47 — audit score: 2; submission deadline: day 2; approval status: pending.
- R48 — audit score: 1; submission deadline: day 13; approval status: denied.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1161 input tokens</summary>

<pre><code>Abbreviation legend:
- ERR = expense reimbursement request
- AS = audit score
- SD = submission deadline
- APS = approval status

Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 3.
2. Its SD is day 10 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 3; SD: day 10; APS: approved.
- R04 — AS: 2; SD: day 1; APS: denied.
- R05 — AS: 2; SD: day 30; APS: approved.
- R06 — AS: 4; SD: day 11; APS: approved.
- R07 — AS: 1; SD: day 17; APS: pending.
- R08 — AS: 4; SD: day 16; APS: pending.
- R09 — AS: 2; SD: day 8; APS: denied.
- R10 — AS: 3; SD: day 26; APS: pending.
- R11 — AS: 2; SD: day 23; APS: denied.
- R12 — AS: 3; SD: day 7; APS: pending.
- R13 — AS: 1; SD: day 22; APS: approved.
- R14 — AS: 4; SD: day 8; APS: denied.
- R15 — AS: 4; SD: day 8; APS: pending.
- R16 — AS: 3; SD: day 28; APS: approved.
- R17 — AS: 2; SD: day 5; APS: denied.
- R18 — AS: 2; SD: day 15; APS: approved.
- R19 — AS: 1; SD: day 3; APS: pending.
- R20 — AS: 4; SD: day 15; APS: denied.
- R21 — AS: 3; SD: day 26; APS: approved.
- R22 — AS: 3; SD: day 26; APS: denied.
- R23 — AS: 3; SD: day 21; APS: pending.
- R24 — AS: 4; SD: day 9; APS: pending.
- R25 — AS: 2; SD: day 14; APS: approved.
- R26 — AS: 5; SD: day 22; APS: approved.
- R27 — AS: 1; SD: day 2; APS: pending.
- R28 — AS: 3; SD: day 30; APS: denied.
- R29 — AS: 1; SD: day 9; APS: pending.
- R30 — AS: 4; SD: day 5; APS: approved.
- R31 — AS: 1; SD: day 10; APS: denied.
- R32 — AS: 5; SD: day 23; APS: approved.
- R33 — AS: 3; SD: day 14; APS: denied.
- R34 — AS: 5; SD: day 30; APS: approved.
- R35 — AS: 2; SD: day 21; APS: denied.
- R36 — AS: 3; SD: day 23; APS: pending.
- R37 — AS: 4; SD: day 25; APS: denied.
- R38 — AS: 1; SD: day 13; APS: pending.
- R39 — AS: 4; SD: day 29; APS: approved.
- R40 — AS: 4; SD: day 14; APS: approved.
- R41 — AS: 1; SD: day 3; APS: denied.
- R42 — AS: 4; SD: day 6; APS: approved.
- R43 — AS: 1; SD: day 26; APS: approved.
- R44 — AS: 3; SD: day 9; APS: approved.
- R45 — AS: 4; SD: day 23; APS: pending.
- R46 — AS: 4; SD: day 19; APS: approved.
- R47 — AS: 2; SD: day 2; APS: pending.
- R48 — AS: 1; SD: day 13; APS: denied.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1131 input tokens</summary>

<pre><code>Review every ERR. A ERR qualifies only when all three rules hold:
1. Its AS is at least 3.
2. Its SD is day 10 or earlier.
3. Its APS is exactly &quot;approved&quot;.

Records:
- R01 — AS: 5; SD: day 1; APS: approved.
- R02 — AS: 1; SD: day 30; APS: denied.
- R03 — AS: 3; SD: day 10; APS: approved.
- R04 — AS: 2; SD: day 1; APS: denied.
- R05 — AS: 2; SD: day 30; APS: approved.
- R06 — AS: 4; SD: day 11; APS: approved.
- R07 — AS: 1; SD: day 17; APS: pending.
- R08 — AS: 4; SD: day 16; APS: pending.
- R09 — AS: 2; SD: day 8; APS: denied.
- R10 — AS: 3; SD: day 26; APS: pending.
- R11 — AS: 2; SD: day 23; APS: denied.
- R12 — AS: 3; SD: day 7; APS: pending.
- R13 — AS: 1; SD: day 22; APS: approved.
- R14 — AS: 4; SD: day 8; APS: denied.
- R15 — AS: 4; SD: day 8; APS: pending.
- R16 — AS: 3; SD: day 28; APS: approved.
- R17 — AS: 2; SD: day 5; APS: denied.
- R18 — AS: 2; SD: day 15; APS: approved.
- R19 — AS: 1; SD: day 3; APS: pending.
- R20 — AS: 4; SD: day 15; APS: denied.
- R21 — AS: 3; SD: day 26; APS: approved.
- R22 — AS: 3; SD: day 26; APS: denied.
- R23 — AS: 3; SD: day 21; APS: pending.
- R24 — AS: 4; SD: day 9; APS: pending.
- R25 — AS: 2; SD: day 14; APS: approved.
- R26 — AS: 5; SD: day 22; APS: approved.
- R27 — AS: 1; SD: day 2; APS: pending.
- R28 — AS: 3; SD: day 30; APS: denied.
- R29 — AS: 1; SD: day 9; APS: pending.
- R30 — AS: 4; SD: day 5; APS: approved.
- R31 — AS: 1; SD: day 10; APS: denied.
- R32 — AS: 5; SD: day 23; APS: approved.
- R33 — AS: 3; SD: day 14; APS: denied.
- R34 — AS: 5; SD: day 30; APS: approved.
- R35 — AS: 2; SD: day 21; APS: denied.
- R36 — AS: 3; SD: day 23; APS: pending.
- R37 — AS: 4; SD: day 25; APS: denied.
- R38 — AS: 1; SD: day 13; APS: pending.
- R39 — AS: 4; SD: day 29; APS: approved.
- R40 — AS: 4; SD: day 14; APS: approved.
- R41 — AS: 1; SD: day 3; APS: denied.
- R42 — AS: 4; SD: day 6; APS: approved.
- R43 — AS: 1; SD: day 26; APS: approved.
- R44 — AS: 3; SD: day 9; APS: approved.
- R45 — AS: 4; SD: day 23; APS: pending.
- R46 — AS: 4; SD: day 19; APS: approved.
- R47 — AS: 2; SD: day 2; APS: pending.
- R48 — AS: 1; SD: day 13; APS: denied.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 956 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 10; state = &quot;approved&quot;.

Records:
- R01: score=5; day=1; state=approved.
- R02: score=1; day=30; state=denied.
- R03: score=3; day=10; state=approved.
- R04: score=2; day=1; state=denied.
- R05: score=2; day=30; state=approved.
- R06: score=4; day=11; state=approved.
- R07: score=1; day=17; state=pending.
- R08: score=4; day=16; state=pending.
- R09: score=2; day=8; state=denied.
- R10: score=3; day=26; state=pending.
- R11: score=2; day=23; state=denied.
- R12: score=3; day=7; state=pending.
- R13: score=1; day=22; state=approved.
- R14: score=4; day=8; state=denied.
- R15: score=4; day=8; state=pending.
- R16: score=3; day=28; state=approved.
- R17: score=2; day=5; state=denied.
- R18: score=2; day=15; state=approved.
- R19: score=1; day=3; state=pending.
- R20: score=4; day=15; state=denied.
- R21: score=3; day=26; state=approved.
- R22: score=3; day=26; state=denied.
- R23: score=3; day=21; state=pending.
- R24: score=4; day=9; state=pending.
- R25: score=2; day=14; state=approved.
- R26: score=5; day=22; state=approved.
- R27: score=1; day=2; state=pending.
- R28: score=3; day=30; state=denied.
- R29: score=1; day=9; state=pending.
- R30: score=4; day=5; state=approved.
- R31: score=1; day=10; state=denied.
- R32: score=5; day=23; state=approved.
- R33: score=3; day=14; state=denied.
- R34: score=5; day=30; state=approved.
- R35: score=2; day=21; state=denied.
- R36: score=3; day=23; state=pending.
- R37: score=4; day=25; state=denied.
- R38: score=1; day=13; state=pending.
- R39: score=4; day=29; state=approved.
- R40: score=4; day=14; state=approved.
- R41: score=1; day=3; state=denied.
- R42: score=4; day=6; state=approved.
- R43: score=1; day=26; state=approved.
- R44: score=3; day=9; state=approved.
- R45: score=4; day=23; state=pending.
- R46: score=4; day=19; state=approved.
- R47: score=2; day=2; state=pending.
- R48: score=1; day=13; state=denied.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>healthcare-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 248 input tokens</summary>

<pre><code>Review every patient appointment request. A patient appointment request qualifies only when all three rules hold:
1. Its urgency level is at least 3.
2. Its appointment deadline is day 15 or earlier.
3. Its insurance status is exactly &quot;verified&quot;.

Records:
- R01 — urgency level: 5; appointment deadline: day 1; insurance status: verified.
- R02 — urgency level: 1; appointment deadline: day 30; insurance status: unverified.
- R03 — urgency level: 3; appointment deadline: day 15; insurance status: unverified.
- R04 — urgency level: 3; appointment deadline: day 17; insurance status: pending.
- R05 — urgency level: 2; appointment deadline: day 8; insurance status: pending.
- R06 — urgency level: 2; appointment deadline: day 15; insurance status: verified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 253 input tokens</summary>

<pre><code>Abbreviation legend:
- PAR = patient appointment request
- UL = urgency level
- AD = appointment deadline
- IS = insurance status

Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 3.
2. Its AD is day 15 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 3; AD: day 15; IS: unverified.
- R04 — UL: 3; AD: day 17; IS: pending.
- R05 — UL: 2; AD: day 8; IS: pending.
- R06 — UL: 2; AD: day 15; IS: verified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 223 input tokens</summary>

<pre><code>Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 3.
2. Its AD is day 15 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 3; AD: day 15; IS: unverified.
- R04 — UL: 3; AD: day 17; IS: pending.
- R05 — UL: 2; AD: day 8; IS: pending.
- R06 — UL: 2; AD: day 15; IS: verified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 159 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 15; state = &quot;verified&quot;.

Records:
- R01: score=5; day=1; state=verified.
- R02: score=1; day=30; state=unverified.
- R03: score=3; day=15; state=unverified.
- R04: score=3; day=17; state=pending.
- R05: score=2; day=8; state=pending.
- R06: score=2; day=15; state=verified.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>healthcare-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 396 input tokens</summary>

<pre><code>Review every patient appointment request. A patient appointment request qualifies only when all three rules hold:
1. Its urgency level is at least 4.
2. Its appointment deadline is day 20 or earlier.
3. Its insurance status is exactly &quot;verified&quot;.

Records:
- R01 — urgency level: 5; appointment deadline: day 1; insurance status: verified.
- R02 — urgency level: 1; appointment deadline: day 30; insurance status: unverified.
- R03 — urgency level: 3; appointment deadline: day 6; insurance status: verified.
- R04 — urgency level: 2; appointment deadline: day 26; insurance status: verified.
- R05 — urgency level: 1; appointment deadline: day 16; insurance status: verified.
- R06 — urgency level: 2; appointment deadline: day 19; insurance status: verified.
- R07 — urgency level: 5; appointment deadline: day 19; insurance status: pending.
- R08 — urgency level: 5; appointment deadline: day 27; insurance status: verified.
- R09 — urgency level: 1; appointment deadline: day 17; insurance status: pending.
- R10 — urgency level: 3; appointment deadline: day 8; insurance status: pending.
- R11 — urgency level: 3; appointment deadline: day 1; insurance status: pending.
- R12 — urgency level: 5; appointment deadline: day 11; insurance status: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 383 input tokens</summary>

<pre><code>Abbreviation legend:
- PAR = patient appointment request
- UL = urgency level
- AD = appointment deadline
- IS = insurance status

Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 4.
2. Its AD is day 20 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 3; AD: day 6; IS: verified.
- R04 — UL: 2; AD: day 26; IS: verified.
- R05 — UL: 1; AD: day 16; IS: verified.
- R06 — UL: 2; AD: day 19; IS: verified.
- R07 — UL: 5; AD: day 19; IS: pending.
- R08 — UL: 5; AD: day 27; IS: verified.
- R09 — UL: 1; AD: day 17; IS: pending.
- R10 — UL: 3; AD: day 8; IS: pending.
- R11 — UL: 3; AD: day 1; IS: pending.
- R12 — UL: 5; AD: day 11; IS: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 353 input tokens</summary>

<pre><code>Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 4.
2. Its AD is day 20 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 3; AD: day 6; IS: verified.
- R04 — UL: 2; AD: day 26; IS: verified.
- R05 — UL: 1; AD: day 16; IS: verified.
- R06 — UL: 2; AD: day 19; IS: verified.
- R07 — UL: 5; AD: day 19; IS: pending.
- R08 — UL: 5; AD: day 27; IS: verified.
- R09 — UL: 1; AD: day 17; IS: pending.
- R10 — UL: 3; AD: day 8; IS: pending.
- R11 — UL: 3; AD: day 1; IS: pending.
- R12 — UL: 5; AD: day 11; IS: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 271 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 20; state = &quot;verified&quot;.

Records:
- R01: score=5; day=1; state=verified.
- R02: score=1; day=30; state=unverified.
- R03: score=3; day=6; state=verified.
- R04: score=2; day=26; state=verified.
- R05: score=1; day=16; state=verified.
- R06: score=2; day=19; state=verified.
- R07: score=5; day=19; state=pending.
- R08: score=5; day=27; state=verified.
- R09: score=1; day=17; state=pending.
- R10: score=3; day=8; state=pending.
- R11: score=3; day=1; state=pending.
- R12: score=5; day=11; state=unverified.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>healthcare-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 698 input tokens</summary>

<pre><code>Review every patient appointment request. A patient appointment request qualifies only when all three rules hold:
1. Its urgency level is at least 3.
2. Its appointment deadline is day 10 or earlier.
3. Its insurance status is exactly &quot;verified&quot;.

Records:
- R01 — urgency level: 5; appointment deadline: day 1; insurance status: verified.
- R02 — urgency level: 1; appointment deadline: day 30; insurance status: unverified.
- R03 — urgency level: 1; appointment deadline: day 9; insurance status: pending.
- R04 — urgency level: 4; appointment deadline: day 24; insurance status: verified.
- R05 — urgency level: 5; appointment deadline: day 29; insurance status: unverified.
- R06 — urgency level: 4; appointment deadline: day 27; insurance status: unverified.
- R07 — urgency level: 3; appointment deadline: day 2; insurance status: pending.
- R08 — urgency level: 3; appointment deadline: day 29; insurance status: verified.
- R09 — urgency level: 3; appointment deadline: day 19; insurance status: pending.
- R10 — urgency level: 3; appointment deadline: day 15; insurance status: verified.
- R11 — urgency level: 3; appointment deadline: day 20; insurance status: unverified.
- R12 — urgency level: 4; appointment deadline: day 12; insurance status: verified.
- R13 — urgency level: 4; appointment deadline: day 17; insurance status: unverified.
- R14 — urgency level: 3; appointment deadline: day 25; insurance status: pending.
- R15 — urgency level: 5; appointment deadline: day 9; insurance status: pending.
- R16 — urgency level: 3; appointment deadline: day 22; insurance status: pending.
- R17 — urgency level: 4; appointment deadline: day 12; insurance status: verified.
- R18 — urgency level: 1; appointment deadline: day 11; insurance status: verified.
- R19 — urgency level: 2; appointment deadline: day 9; insurance status: verified.
- R20 — urgency level: 1; appointment deadline: day 8; insurance status: pending.
- R21 — urgency level: 2; appointment deadline: day 21; insurance status: verified.
- R22 — urgency level: 5; appointment deadline: day 21; insurance status: verified.
- R23 — urgency level: 5; appointment deadline: day 2; insurance status: unverified.
- R24 — urgency level: 5; appointment deadline: day 12; insurance status: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 649 input tokens</summary>

<pre><code>Abbreviation legend:
- PAR = patient appointment request
- UL = urgency level
- AD = appointment deadline
- IS = insurance status

Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 3.
2. Its AD is day 10 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 1; AD: day 9; IS: pending.
- R04 — UL: 4; AD: day 24; IS: verified.
- R05 — UL: 5; AD: day 29; IS: unverified.
- R06 — UL: 4; AD: day 27; IS: unverified.
- R07 — UL: 3; AD: day 2; IS: pending.
- R08 — UL: 3; AD: day 29; IS: verified.
- R09 — UL: 3; AD: day 19; IS: pending.
- R10 — UL: 3; AD: day 15; IS: verified.
- R11 — UL: 3; AD: day 20; IS: unverified.
- R12 — UL: 4; AD: day 12; IS: verified.
- R13 — UL: 4; AD: day 17; IS: unverified.
- R14 — UL: 3; AD: day 25; IS: pending.
- R15 — UL: 5; AD: day 9; IS: pending.
- R16 — UL: 3; AD: day 22; IS: pending.
- R17 — UL: 4; AD: day 12; IS: verified.
- R18 — UL: 1; AD: day 11; IS: verified.
- R19 — UL: 2; AD: day 9; IS: verified.
- R20 — UL: 1; AD: day 8; IS: pending.
- R21 — UL: 2; AD: day 21; IS: verified.
- R22 — UL: 5; AD: day 21; IS: verified.
- R23 — UL: 5; AD: day 2; IS: unverified.
- R24 — UL: 5; AD: day 12; IS: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 619 input tokens</summary>

<pre><code>Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 3.
2. Its AD is day 10 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 1; AD: day 9; IS: pending.
- R04 — UL: 4; AD: day 24; IS: verified.
- R05 — UL: 5; AD: day 29; IS: unverified.
- R06 — UL: 4; AD: day 27; IS: unverified.
- R07 — UL: 3; AD: day 2; IS: pending.
- R08 — UL: 3; AD: day 29; IS: verified.
- R09 — UL: 3; AD: day 19; IS: pending.
- R10 — UL: 3; AD: day 15; IS: verified.
- R11 — UL: 3; AD: day 20; IS: unverified.
- R12 — UL: 4; AD: day 12; IS: verified.
- R13 — UL: 4; AD: day 17; IS: unverified.
- R14 — UL: 3; AD: day 25; IS: pending.
- R15 — UL: 5; AD: day 9; IS: pending.
- R16 — UL: 3; AD: day 22; IS: pending.
- R17 — UL: 4; AD: day 12; IS: verified.
- R18 — UL: 1; AD: day 11; IS: verified.
- R19 — UL: 2; AD: day 9; IS: verified.
- R20 — UL: 1; AD: day 8; IS: pending.
- R21 — UL: 2; AD: day 21; IS: verified.
- R22 — UL: 5; AD: day 21; IS: verified.
- R23 — UL: 5; AD: day 2; IS: unverified.
- R24 — UL: 5; AD: day 12; IS: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 501 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 10; state = &quot;verified&quot;.

Records:
- R01: score=5; day=1; state=verified.
- R02: score=1; day=30; state=unverified.
- R03: score=1; day=9; state=pending.
- R04: score=4; day=24; state=verified.
- R05: score=5; day=29; state=unverified.
- R06: score=4; day=27; state=unverified.
- R07: score=3; day=2; state=pending.
- R08: score=3; day=29; state=verified.
- R09: score=3; day=19; state=pending.
- R10: score=3; day=15; state=verified.
- R11: score=3; day=20; state=unverified.
- R12: score=4; day=12; state=verified.
- R13: score=4; day=17; state=unverified.
- R14: score=3; day=25; state=pending.
- R15: score=5; day=9; state=pending.
- R16: score=3; day=22; state=pending.
- R17: score=4; day=12; state=verified.
- R18: score=1; day=11; state=verified.
- R19: score=2; day=9; state=verified.
- R20: score=1; day=8; state=pending.
- R21: score=2; day=21; state=verified.
- R22: score=5; day=21; state=verified.
- R23: score=5; day=2; state=unverified.
- R24: score=5; day=12; state=unverified.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>healthcare-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R41&quot;]}</code></summary>

<details><summary>Full prose — 1292 input tokens</summary>

<pre><code>Review every patient appointment request. A patient appointment request qualifies only when all three rules hold:
1. Its urgency level is at least 4.
2. Its appointment deadline is day 15 or earlier.
3. Its insurance status is exactly &quot;verified&quot;.

Records:
- R01 — urgency level: 5; appointment deadline: day 1; insurance status: verified.
- R02 — urgency level: 1; appointment deadline: day 30; insurance status: unverified.
- R03 — urgency level: 4; appointment deadline: day 12; insurance status: unverified.
- R04 — urgency level: 4; appointment deadline: day 20; insurance status: unverified.
- R05 — urgency level: 2; appointment deadline: day 21; insurance status: verified.
- R06 — urgency level: 2; appointment deadline: day 1; insurance status: pending.
- R07 — urgency level: 1; appointment deadline: day 22; insurance status: verified.
- R08 — urgency level: 1; appointment deadline: day 29; insurance status: pending.
- R09 — urgency level: 2; appointment deadline: day 6; insurance status: verified.
- R10 — urgency level: 5; appointment deadline: day 22; insurance status: verified.
- R11 — urgency level: 2; appointment deadline: day 27; insurance status: verified.
- R12 — urgency level: 1; appointment deadline: day 5; insurance status: pending.
- R13 — urgency level: 4; appointment deadline: day 14; insurance status: pending.
- R14 — urgency level: 4; appointment deadline: day 14; insurance status: unverified.
- R15 — urgency level: 3; appointment deadline: day 22; insurance status: verified.
- R16 — urgency level: 4; appointment deadline: day 21; insurance status: unverified.
- R17 — urgency level: 3; appointment deadline: day 25; insurance status: verified.
- R18 — urgency level: 4; appointment deadline: day 2; insurance status: pending.
- R19 — urgency level: 2; appointment deadline: day 18; insurance status: pending.
- R20 — urgency level: 5; appointment deadline: day 8; insurance status: pending.
- R21 — urgency level: 2; appointment deadline: day 3; insurance status: unverified.
- R22 — urgency level: 4; appointment deadline: day 9; insurance status: unverified.
- R23 — urgency level: 3; appointment deadline: day 26; insurance status: verified.
- R24 — urgency level: 3; appointment deadline: day 8; insurance status: verified.
- R25 — urgency level: 5; appointment deadline: day 7; insurance status: pending.
- R26 — urgency level: 5; appointment deadline: day 5; insurance status: unverified.
- R27 — urgency level: 5; appointment deadline: day 28; insurance status: unverified.
- R28 — urgency level: 5; appointment deadline: day 15; insurance status: unverified.
- R29 — urgency level: 1; appointment deadline: day 2; insurance status: verified.
- R30 — urgency level: 3; appointment deadline: day 19; insurance status: verified.
- R31 — urgency level: 3; appointment deadline: day 17; insurance status: pending.
- R32 — urgency level: 1; appointment deadline: day 16; insurance status: pending.
- R33 — urgency level: 2; appointment deadline: day 6; insurance status: unverified.
- R34 — urgency level: 5; appointment deadline: day 14; insurance status: pending.
- R35 — urgency level: 2; appointment deadline: day 4; insurance status: unverified.
- R36 — urgency level: 1; appointment deadline: day 24; insurance status: pending.
- R37 — urgency level: 1; appointment deadline: day 4; insurance status: pending.
- R38 — urgency level: 4; appointment deadline: day 7; insurance status: pending.
- R39 — urgency level: 1; appointment deadline: day 15; insurance status: pending.
- R40 — urgency level: 5; appointment deadline: day 28; insurance status: pending.
- R41 — urgency level: 5; appointment deadline: day 9; insurance status: verified.
- R42 — urgency level: 5; appointment deadline: day 25; insurance status: pending.
- R43 — urgency level: 2; appointment deadline: day 8; insurance status: unverified.
- R44 — urgency level: 4; appointment deadline: day 2; insurance status: pending.
- R45 — urgency level: 3; appointment deadline: day 23; insurance status: verified.
- R46 — urgency level: 2; appointment deadline: day 2; insurance status: unverified.
- R47 — urgency level: 3; appointment deadline: day 4; insurance status: verified.
- R48 — urgency level: 2; appointment deadline: day 23; insurance status: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1171 input tokens</summary>

<pre><code>Abbreviation legend:
- PAR = patient appointment request
- UL = urgency level
- AD = appointment deadline
- IS = insurance status

Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 4.
2. Its AD is day 15 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 4; AD: day 12; IS: unverified.
- R04 — UL: 4; AD: day 20; IS: unverified.
- R05 — UL: 2; AD: day 21; IS: verified.
- R06 — UL: 2; AD: day 1; IS: pending.
- R07 — UL: 1; AD: day 22; IS: verified.
- R08 — UL: 1; AD: day 29; IS: pending.
- R09 — UL: 2; AD: day 6; IS: verified.
- R10 — UL: 5; AD: day 22; IS: verified.
- R11 — UL: 2; AD: day 27; IS: verified.
- R12 — UL: 1; AD: day 5; IS: pending.
- R13 — UL: 4; AD: day 14; IS: pending.
- R14 — UL: 4; AD: day 14; IS: unverified.
- R15 — UL: 3; AD: day 22; IS: verified.
- R16 — UL: 4; AD: day 21; IS: unverified.
- R17 — UL: 3; AD: day 25; IS: verified.
- R18 — UL: 4; AD: day 2; IS: pending.
- R19 — UL: 2; AD: day 18; IS: pending.
- R20 — UL: 5; AD: day 8; IS: pending.
- R21 — UL: 2; AD: day 3; IS: unverified.
- R22 — UL: 4; AD: day 9; IS: unverified.
- R23 — UL: 3; AD: day 26; IS: verified.
- R24 — UL: 3; AD: day 8; IS: verified.
- R25 — UL: 5; AD: day 7; IS: pending.
- R26 — UL: 5; AD: day 5; IS: unverified.
- R27 — UL: 5; AD: day 28; IS: unverified.
- R28 — UL: 5; AD: day 15; IS: unverified.
- R29 — UL: 1; AD: day 2; IS: verified.
- R30 — UL: 3; AD: day 19; IS: verified.
- R31 — UL: 3; AD: day 17; IS: pending.
- R32 — UL: 1; AD: day 16; IS: pending.
- R33 — UL: 2; AD: day 6; IS: unverified.
- R34 — UL: 5; AD: day 14; IS: pending.
- R35 — UL: 2; AD: day 4; IS: unverified.
- R36 — UL: 1; AD: day 24; IS: pending.
- R37 — UL: 1; AD: day 4; IS: pending.
- R38 — UL: 4; AD: day 7; IS: pending.
- R39 — UL: 1; AD: day 15; IS: pending.
- R40 — UL: 5; AD: day 28; IS: pending.
- R41 — UL: 5; AD: day 9; IS: verified.
- R42 — UL: 5; AD: day 25; IS: pending.
- R43 — UL: 2; AD: day 8; IS: unverified.
- R44 — UL: 4; AD: day 2; IS: pending.
- R45 — UL: 3; AD: day 23; IS: verified.
- R46 — UL: 2; AD: day 2; IS: unverified.
- R47 — UL: 3; AD: day 4; IS: verified.
- R48 — UL: 2; AD: day 23; IS: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1141 input tokens</summary>

<pre><code>Review every PAR. A PAR qualifies only when all three rules hold:
1. Its UL is at least 4.
2. Its AD is day 15 or earlier.
3. Its IS is exactly &quot;verified&quot;.

Records:
- R01 — UL: 5; AD: day 1; IS: verified.
- R02 — UL: 1; AD: day 30; IS: unverified.
- R03 — UL: 4; AD: day 12; IS: unverified.
- R04 — UL: 4; AD: day 20; IS: unverified.
- R05 — UL: 2; AD: day 21; IS: verified.
- R06 — UL: 2; AD: day 1; IS: pending.
- R07 — UL: 1; AD: day 22; IS: verified.
- R08 — UL: 1; AD: day 29; IS: pending.
- R09 — UL: 2; AD: day 6; IS: verified.
- R10 — UL: 5; AD: day 22; IS: verified.
- R11 — UL: 2; AD: day 27; IS: verified.
- R12 — UL: 1; AD: day 5; IS: pending.
- R13 — UL: 4; AD: day 14; IS: pending.
- R14 — UL: 4; AD: day 14; IS: unverified.
- R15 — UL: 3; AD: day 22; IS: verified.
- R16 — UL: 4; AD: day 21; IS: unverified.
- R17 — UL: 3; AD: day 25; IS: verified.
- R18 — UL: 4; AD: day 2; IS: pending.
- R19 — UL: 2; AD: day 18; IS: pending.
- R20 — UL: 5; AD: day 8; IS: pending.
- R21 — UL: 2; AD: day 3; IS: unverified.
- R22 — UL: 4; AD: day 9; IS: unverified.
- R23 — UL: 3; AD: day 26; IS: verified.
- R24 — UL: 3; AD: day 8; IS: verified.
- R25 — UL: 5; AD: day 7; IS: pending.
- R26 — UL: 5; AD: day 5; IS: unverified.
- R27 — UL: 5; AD: day 28; IS: unverified.
- R28 — UL: 5; AD: day 15; IS: unverified.
- R29 — UL: 1; AD: day 2; IS: verified.
- R30 — UL: 3; AD: day 19; IS: verified.
- R31 — UL: 3; AD: day 17; IS: pending.
- R32 — UL: 1; AD: day 16; IS: pending.
- R33 — UL: 2; AD: day 6; IS: unverified.
- R34 — UL: 5; AD: day 14; IS: pending.
- R35 — UL: 2; AD: day 4; IS: unverified.
- R36 — UL: 1; AD: day 24; IS: pending.
- R37 — UL: 1; AD: day 4; IS: pending.
- R38 — UL: 4; AD: day 7; IS: pending.
- R39 — UL: 1; AD: day 15; IS: pending.
- R40 — UL: 5; AD: day 28; IS: pending.
- R41 — UL: 5; AD: day 9; IS: verified.
- R42 — UL: 5; AD: day 25; IS: pending.
- R43 — UL: 2; AD: day 8; IS: unverified.
- R44 — UL: 4; AD: day 2; IS: pending.
- R45 — UL: 3; AD: day 23; IS: verified.
- R46 — UL: 2; AD: day 2; IS: unverified.
- R47 — UL: 3; AD: day 4; IS: verified.
- R48 — UL: 2; AD: day 23; IS: unverified.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 951 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 15; state = &quot;verified&quot;.

Records:
- R01: score=5; day=1; state=verified.
- R02: score=1; day=30; state=unverified.
- R03: score=4; day=12; state=unverified.
- R04: score=4; day=20; state=unverified.
- R05: score=2; day=21; state=verified.
- R06: score=2; day=1; state=pending.
- R07: score=1; day=22; state=verified.
- R08: score=1; day=29; state=pending.
- R09: score=2; day=6; state=verified.
- R10: score=5; day=22; state=verified.
- R11: score=2; day=27; state=verified.
- R12: score=1; day=5; state=pending.
- R13: score=4; day=14; state=pending.
- R14: score=4; day=14; state=unverified.
- R15: score=3; day=22; state=verified.
- R16: score=4; day=21; state=unverified.
- R17: score=3; day=25; state=verified.
- R18: score=4; day=2; state=pending.
- R19: score=2; day=18; state=pending.
- R20: score=5; day=8; state=pending.
- R21: score=2; day=3; state=unverified.
- R22: score=4; day=9; state=unverified.
- R23: score=3; day=26; state=verified.
- R24: score=3; day=8; state=verified.
- R25: score=5; day=7; state=pending.
- R26: score=5; day=5; state=unverified.
- R27: score=5; day=28; state=unverified.
- R28: score=5; day=15; state=unverified.
- R29: score=1; day=2; state=verified.
- R30: score=3; day=19; state=verified.
- R31: score=3; day=17; state=pending.
- R32: score=1; day=16; state=pending.
- R33: score=2; day=6; state=unverified.
- R34: score=5; day=14; state=pending.
- R35: score=2; day=4; state=unverified.
- R36: score=1; day=24; state=pending.
- R37: score=1; day=4; state=pending.
- R38: score=4; day=7; state=pending.
- R39: score=1; day=15; state=pending.
- R40: score=5; day=28; state=pending.
- R41: score=5; day=9; state=verified.
- R42: score=5; day=25; state=pending.
- R43: score=2; day=8; state=unverified.
- R44: score=4; day=2; state=pending.
- R45: score=3; day=23; state=verified.
- R46: score=2; day=2; state=unverified.
- R47: score=3; day=4; state=verified.
- R48: score=2; day=23; state=unverified.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>manufacturing-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 246 input tokens</summary>

<pre><code>Review every quality inspection report. A quality inspection report qualifies only when all three rules hold:
1. Its defect severity is at least 4.
2. Its correction deadline is day 20 or earlier.
3. Its inspection status is exactly &quot;failed&quot;.

Records:
- R01 — defect severity: 5; correction deadline: day 1; inspection status: failed.
- R02 — defect severity: 1; correction deadline: day 30; inspection status: passed.
- R03 — defect severity: 3; correction deadline: day 17; inspection status: failed.
- R04 — defect severity: 5; correction deadline: day 9; inspection status: passed.
- R05 — defect severity: 1; correction deadline: day 22; inspection status: passed.
- R06 — defect severity: 3; correction deadline: day 29; inspection status: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 254 input tokens</summary>

<pre><code>Abbreviation legend:
- QIR = quality inspection report
- DS = defect severity
- CD = correction deadline
- IS = inspection status

Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its CD is day 20 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 3; CD: day 17; IS: failed.
- R04 — DS: 5; CD: day 9; IS: passed.
- R05 — DS: 1; CD: day 22; IS: passed.
- R06 — DS: 3; CD: day 29; IS: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 223 input tokens</summary>

<pre><code>Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its CD is day 20 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 3; CD: day 17; IS: failed.
- R04 — DS: 5; CD: day 9; IS: passed.
- R05 — DS: 1; CD: day 22; IS: passed.
- R06 — DS: 3; CD: day 29; IS: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 157 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 20; state = &quot;failed&quot;.

Records:
- R01: score=5; day=1; state=failed.
- R02: score=1; day=30; state=passed.
- R03: score=3; day=17; state=failed.
- R04: score=5; day=9; state=passed.
- R05: score=1; day=22; state=passed.
- R06: score=3; day=29; state=passed.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>manufacturing-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 394 input tokens</summary>

<pre><code>Review every quality inspection report. A quality inspection report qualifies only when all three rules hold:
1. Its defect severity is at least 3.
2. Its correction deadline is day 10 or earlier.
3. Its inspection status is exactly &quot;failed&quot;.

Records:
- R01 — defect severity: 5; correction deadline: day 1; inspection status: failed.
- R02 — defect severity: 1; correction deadline: day 30; inspection status: passed.
- R03 — defect severity: 1; correction deadline: day 13; inspection status: passed.
- R04 — defect severity: 1; correction deadline: day 8; inspection status: passed.
- R05 — defect severity: 4; correction deadline: day 8; inspection status: passed.
- R06 — defect severity: 2; correction deadline: day 14; inspection status: failed.
- R07 — defect severity: 3; correction deadline: day 28; inspection status: failed.
- R08 — defect severity: 2; correction deadline: day 26; inspection status: failed.
- R09 — defect severity: 2; correction deadline: day 13; inspection status: passed.
- R10 — defect severity: 1; correction deadline: day 15; inspection status: passed.
- R11 — defect severity: 2; correction deadline: day 10; inspection status: failed.
- R12 — defect severity: 4; correction deadline: day 1; inspection status: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 384 input tokens</summary>

<pre><code>Abbreviation legend:
- QIR = quality inspection report
- DS = defect severity
- CD = correction deadline
- IS = inspection status

Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its CD is day 10 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 1; CD: day 13; IS: passed.
- R04 — DS: 1; CD: day 8; IS: passed.
- R05 — DS: 4; CD: day 8; IS: passed.
- R06 — DS: 2; CD: day 14; IS: failed.
- R07 — DS: 3; CD: day 28; IS: failed.
- R08 — DS: 2; CD: day 26; IS: failed.
- R09 — DS: 2; CD: day 13; IS: passed.
- R10 — DS: 1; CD: day 15; IS: passed.
- R11 — DS: 2; CD: day 10; IS: failed.
- R12 — DS: 4; CD: day 1; IS: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 353 input tokens</summary>

<pre><code>Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its CD is day 10 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 1; CD: day 13; IS: passed.
- R04 — DS: 1; CD: day 8; IS: passed.
- R05 — DS: 4; CD: day 8; IS: passed.
- R06 — DS: 2; CD: day 14; IS: failed.
- R07 — DS: 3; CD: day 28; IS: failed.
- R08 — DS: 2; CD: day 26; IS: failed.
- R09 — DS: 2; CD: day 13; IS: passed.
- R10 — DS: 1; CD: day 15; IS: passed.
- R11 — DS: 2; CD: day 10; IS: failed.
- R12 — DS: 4; CD: day 1; IS: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 269 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 10; state = &quot;failed&quot;.

Records:
- R01: score=5; day=1; state=failed.
- R02: score=1; day=30; state=passed.
- R03: score=1; day=13; state=passed.
- R04: score=1; day=8; state=passed.
- R05: score=4; day=8; state=passed.
- R06: score=2; day=14; state=failed.
- R07: score=3; day=28; state=failed.
- R08: score=2; day=26; state=failed.
- R09: score=2; day=13; state=passed.
- R10: score=1; day=15; state=passed.
- R11: score=2; day=10; state=failed.
- R12: score=4; day=1; state=passed.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>manufacturing-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R13&quot;]}</code></summary>

<details><summary>Full prose — 690 input tokens</summary>

<pre><code>Review every quality inspection report. A quality inspection report qualifies only when all three rules hold:
1. Its defect severity is at least 4.
2. Its correction deadline is day 15 or earlier.
3. Its inspection status is exactly &quot;failed&quot;.

Records:
- R01 — defect severity: 5; correction deadline: day 1; inspection status: failed.
- R02 — defect severity: 1; correction deadline: day 30; inspection status: passed.
- R03 — defect severity: 1; correction deadline: day 6; inspection status: passed.
- R04 — defect severity: 5; correction deadline: day 24; inspection status: pending.
- R05 — defect severity: 2; correction deadline: day 6; inspection status: failed.
- R06 — defect severity: 4; correction deadline: day 8; inspection status: pending.
- R07 — defect severity: 2; correction deadline: day 15; inspection status: pending.
- R08 — defect severity: 1; correction deadline: day 21; inspection status: pending.
- R09 — defect severity: 2; correction deadline: day 28; inspection status: pending.
- R10 — defect severity: 4; correction deadline: day 5; inspection status: pending.
- R11 — defect severity: 2; correction deadline: day 14; inspection status: pending.
- R12 — defect severity: 1; correction deadline: day 1; inspection status: passed.
- R13 — defect severity: 4; correction deadline: day 3; inspection status: failed.
- R14 — defect severity: 4; correction deadline: day 26; inspection status: pending.
- R15 — defect severity: 5; correction deadline: day 10; inspection status: pending.
- R16 — defect severity: 4; correction deadline: day 14; inspection status: pending.
- R17 — defect severity: 2; correction deadline: day 18; inspection status: failed.
- R18 — defect severity: 3; correction deadline: day 16; inspection status: failed.
- R19 — defect severity: 4; correction deadline: day 17; inspection status: pending.
- R20 — defect severity: 2; correction deadline: day 19; inspection status: pending.
- R21 — defect severity: 2; correction deadline: day 11; inspection status: passed.
- R22 — defect severity: 1; correction deadline: day 5; inspection status: failed.
- R23 — defect severity: 2; correction deadline: day 27; inspection status: pending.
- R24 — defect severity: 5; correction deadline: day 27; inspection status: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 644 input tokens</summary>

<pre><code>Abbreviation legend:
- QIR = quality inspection report
- DS = defect severity
- CD = correction deadline
- IS = inspection status

Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its CD is day 15 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 1; CD: day 6; IS: passed.
- R04 — DS: 5; CD: day 24; IS: pending.
- R05 — DS: 2; CD: day 6; IS: failed.
- R06 — DS: 4; CD: day 8; IS: pending.
- R07 — DS: 2; CD: day 15; IS: pending.
- R08 — DS: 1; CD: day 21; IS: pending.
- R09 — DS: 2; CD: day 28; IS: pending.
- R10 — DS: 4; CD: day 5; IS: pending.
- R11 — DS: 2; CD: day 14; IS: pending.
- R12 — DS: 1; CD: day 1; IS: passed.
- R13 — DS: 4; CD: day 3; IS: failed.
- R14 — DS: 4; CD: day 26; IS: pending.
- R15 — DS: 5; CD: day 10; IS: pending.
- R16 — DS: 4; CD: day 14; IS: pending.
- R17 — DS: 2; CD: day 18; IS: failed.
- R18 — DS: 3; CD: day 16; IS: failed.
- R19 — DS: 4; CD: day 17; IS: pending.
- R20 — DS: 2; CD: day 19; IS: pending.
- R21 — DS: 2; CD: day 11; IS: passed.
- R22 — DS: 1; CD: day 5; IS: failed.
- R23 — DS: 2; CD: day 27; IS: pending.
- R24 — DS: 5; CD: day 27; IS: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 613 input tokens</summary>

<pre><code>Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 4.
2. Its CD is day 15 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 1; CD: day 6; IS: passed.
- R04 — DS: 5; CD: day 24; IS: pending.
- R05 — DS: 2; CD: day 6; IS: failed.
- R06 — DS: 4; CD: day 8; IS: pending.
- R07 — DS: 2; CD: day 15; IS: pending.
- R08 — DS: 1; CD: day 21; IS: pending.
- R09 — DS: 2; CD: day 28; IS: pending.
- R10 — DS: 4; CD: day 5; IS: pending.
- R11 — DS: 2; CD: day 14; IS: pending.
- R12 — DS: 1; CD: day 1; IS: passed.
- R13 — DS: 4; CD: day 3; IS: failed.
- R14 — DS: 4; CD: day 26; IS: pending.
- R15 — DS: 5; CD: day 10; IS: pending.
- R16 — DS: 4; CD: day 14; IS: pending.
- R17 — DS: 2; CD: day 18; IS: failed.
- R18 — DS: 3; CD: day 16; IS: failed.
- R19 — DS: 4; CD: day 17; IS: pending.
- R20 — DS: 2; CD: day 19; IS: pending.
- R21 — DS: 2; CD: day 11; IS: passed.
- R22 — DS: 1; CD: day 5; IS: failed.
- R23 — DS: 2; CD: day 27; IS: pending.
- R24 — DS: 5; CD: day 27; IS: passed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 493 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 15; state = &quot;failed&quot;.

Records:
- R01: score=5; day=1; state=failed.
- R02: score=1; day=30; state=passed.
- R03: score=1; day=6; state=passed.
- R04: score=5; day=24; state=pending.
- R05: score=2; day=6; state=failed.
- R06: score=4; day=8; state=pending.
- R07: score=2; day=15; state=pending.
- R08: score=1; day=21; state=pending.
- R09: score=2; day=28; state=pending.
- R10: score=4; day=5; state=pending.
- R11: score=2; day=14; state=pending.
- R12: score=1; day=1; state=passed.
- R13: score=4; day=3; state=failed.
- R14: score=4; day=26; state=pending.
- R15: score=5; day=10; state=pending.
- R16: score=4; day=14; state=pending.
- R17: score=2; day=18; state=failed.
- R18: score=3; day=16; state=failed.
- R19: score=4; day=17; state=pending.
- R20: score=2; day=19; state=pending.
- R21: score=2; day=11; state=passed.
- R22: score=1; day=5; state=failed.
- R23: score=2; day=27; state=pending.
- R24: score=5; day=27; state=passed.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>manufacturing-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R07&quot;, &quot;R21&quot;, &quot;R24&quot;, &quot;R35&quot;, &quot;R38&quot;, &quot;R40&quot;, &quot;R48&quot;]}</code></summary>

<details><summary>Full prose — 1287 input tokens</summary>

<pre><code>Review every quality inspection report. A quality inspection report qualifies only when all three rules hold:
1. Its defect severity is at least 3.
2. Its correction deadline is day 20 or earlier.
3. Its inspection status is exactly &quot;failed&quot;.

Records:
- R01 — defect severity: 5; correction deadline: day 1; inspection status: failed.
- R02 — defect severity: 1; correction deadline: day 30; inspection status: passed.
- R03 — defect severity: 2; correction deadline: day 27; inspection status: pending.
- R04 — defect severity: 2; correction deadline: day 7; inspection status: passed.
- R05 — defect severity: 5; correction deadline: day 17; inspection status: passed.
- R06 — defect severity: 4; correction deadline: day 20; inspection status: passed.
- R07 — defect severity: 4; correction deadline: day 1; inspection status: failed.
- R08 — defect severity: 1; correction deadline: day 12; inspection status: failed.
- R09 — defect severity: 5; correction deadline: day 30; inspection status: passed.
- R10 — defect severity: 5; correction deadline: day 19; inspection status: passed.
- R11 — defect severity: 3; correction deadline: day 28; inspection status: pending.
- R12 — defect severity: 5; correction deadline: day 6; inspection status: passed.
- R13 — defect severity: 3; correction deadline: day 29; inspection status: failed.
- R14 — defect severity: 5; correction deadline: day 2; inspection status: passed.
- R15 — defect severity: 5; correction deadline: day 25; inspection status: failed.
- R16 — defect severity: 2; correction deadline: day 21; inspection status: passed.
- R17 — defect severity: 4; correction deadline: day 14; inspection status: passed.
- R18 — defect severity: 4; correction deadline: day 5; inspection status: passed.
- R19 — defect severity: 1; correction deadline: day 23; inspection status: failed.
- R20 — defect severity: 3; correction deadline: day 29; inspection status: passed.
- R21 — defect severity: 3; correction deadline: day 17; inspection status: failed.
- R22 — defect severity: 2; correction deadline: day 22; inspection status: pending.
- R23 — defect severity: 2; correction deadline: day 18; inspection status: passed.
- R24 — defect severity: 3; correction deadline: day 4; inspection status: failed.
- R25 — defect severity: 4; correction deadline: day 11; inspection status: pending.
- R26 — defect severity: 5; correction deadline: day 27; inspection status: passed.
- R27 — defect severity: 2; correction deadline: day 7; inspection status: failed.
- R28 — defect severity: 2; correction deadline: day 11; inspection status: pending.
- R29 — defect severity: 5; correction deadline: day 23; inspection status: failed.
- R30 — defect severity: 3; correction deadline: day 18; inspection status: pending.
- R31 — defect severity: 2; correction deadline: day 24; inspection status: passed.
- R32 — defect severity: 4; correction deadline: day 23; inspection status: pending.
- R33 — defect severity: 1; correction deadline: day 2; inspection status: pending.
- R34 — defect severity: 5; correction deadline: day 12; inspection status: passed.
- R35 — defect severity: 3; correction deadline: day 12; inspection status: failed.
- R36 — defect severity: 4; correction deadline: day 13; inspection status: passed.
- R37 — defect severity: 3; correction deadline: day 29; inspection status: failed.
- R38 — defect severity: 4; correction deadline: day 7; inspection status: failed.
- R39 — defect severity: 4; correction deadline: day 15; inspection status: pending.
- R40 — defect severity: 3; correction deadline: day 13; inspection status: failed.
- R41 — defect severity: 5; correction deadline: day 1; inspection status: passed.
- R42 — defect severity: 4; correction deadline: day 22; inspection status: passed.
- R43 — defect severity: 4; correction deadline: day 19; inspection status: pending.
- R44 — defect severity: 4; correction deadline: day 21; inspection status: passed.
- R45 — defect severity: 5; correction deadline: day 25; inspection status: pending.
- R46 — defect severity: 2; correction deadline: day 20; inspection status: failed.
- R47 — defect severity: 2; correction deadline: day 29; inspection status: failed.
- R48 — defect severity: 3; correction deadline: day 14; inspection status: failed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1169 input tokens</summary>

<pre><code>Abbreviation legend:
- QIR = quality inspection report
- DS = defect severity
- CD = correction deadline
- IS = inspection status

Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its CD is day 20 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 2; CD: day 27; IS: pending.
- R04 — DS: 2; CD: day 7; IS: passed.
- R05 — DS: 5; CD: day 17; IS: passed.
- R06 — DS: 4; CD: day 20; IS: passed.
- R07 — DS: 4; CD: day 1; IS: failed.
- R08 — DS: 1; CD: day 12; IS: failed.
- R09 — DS: 5; CD: day 30; IS: passed.
- R10 — DS: 5; CD: day 19; IS: passed.
- R11 — DS: 3; CD: day 28; IS: pending.
- R12 — DS: 5; CD: day 6; IS: passed.
- R13 — DS: 3; CD: day 29; IS: failed.
- R14 — DS: 5; CD: day 2; IS: passed.
- R15 — DS: 5; CD: day 25; IS: failed.
- R16 — DS: 2; CD: day 21; IS: passed.
- R17 — DS: 4; CD: day 14; IS: passed.
- R18 — DS: 4; CD: day 5; IS: passed.
- R19 — DS: 1; CD: day 23; IS: failed.
- R20 — DS: 3; CD: day 29; IS: passed.
- R21 — DS: 3; CD: day 17; IS: failed.
- R22 — DS: 2; CD: day 22; IS: pending.
- R23 — DS: 2; CD: day 18; IS: passed.
- R24 — DS: 3; CD: day 4; IS: failed.
- R25 — DS: 4; CD: day 11; IS: pending.
- R26 — DS: 5; CD: day 27; IS: passed.
- R27 — DS: 2; CD: day 7; IS: failed.
- R28 — DS: 2; CD: day 11; IS: pending.
- R29 — DS: 5; CD: day 23; IS: failed.
- R30 — DS: 3; CD: day 18; IS: pending.
- R31 — DS: 2; CD: day 24; IS: passed.
- R32 — DS: 4; CD: day 23; IS: pending.
- R33 — DS: 1; CD: day 2; IS: pending.
- R34 — DS: 5; CD: day 12; IS: passed.
- R35 — DS: 3; CD: day 12; IS: failed.
- R36 — DS: 4; CD: day 13; IS: passed.
- R37 — DS: 3; CD: day 29; IS: failed.
- R38 — DS: 4; CD: day 7; IS: failed.
- R39 — DS: 4; CD: day 15; IS: pending.
- R40 — DS: 3; CD: day 13; IS: failed.
- R41 — DS: 5; CD: day 1; IS: passed.
- R42 — DS: 4; CD: day 22; IS: passed.
- R43 — DS: 4; CD: day 19; IS: pending.
- R44 — DS: 4; CD: day 21; IS: passed.
- R45 — DS: 5; CD: day 25; IS: pending.
- R46 — DS: 2; CD: day 20; IS: failed.
- R47 — DS: 2; CD: day 29; IS: failed.
- R48 — DS: 3; CD: day 14; IS: failed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1138 input tokens</summary>

<pre><code>Review every QIR. A QIR qualifies only when all three rules hold:
1. Its DS is at least 3.
2. Its CD is day 20 or earlier.
3. Its IS is exactly &quot;failed&quot;.

Records:
- R01 — DS: 5; CD: day 1; IS: failed.
- R02 — DS: 1; CD: day 30; IS: passed.
- R03 — DS: 2; CD: day 27; IS: pending.
- R04 — DS: 2; CD: day 7; IS: passed.
- R05 — DS: 5; CD: day 17; IS: passed.
- R06 — DS: 4; CD: day 20; IS: passed.
- R07 — DS: 4; CD: day 1; IS: failed.
- R08 — DS: 1; CD: day 12; IS: failed.
- R09 — DS: 5; CD: day 30; IS: passed.
- R10 — DS: 5; CD: day 19; IS: passed.
- R11 — DS: 3; CD: day 28; IS: pending.
- R12 — DS: 5; CD: day 6; IS: passed.
- R13 — DS: 3; CD: day 29; IS: failed.
- R14 — DS: 5; CD: day 2; IS: passed.
- R15 — DS: 5; CD: day 25; IS: failed.
- R16 — DS: 2; CD: day 21; IS: passed.
- R17 — DS: 4; CD: day 14; IS: passed.
- R18 — DS: 4; CD: day 5; IS: passed.
- R19 — DS: 1; CD: day 23; IS: failed.
- R20 — DS: 3; CD: day 29; IS: passed.
- R21 — DS: 3; CD: day 17; IS: failed.
- R22 — DS: 2; CD: day 22; IS: pending.
- R23 — DS: 2; CD: day 18; IS: passed.
- R24 — DS: 3; CD: day 4; IS: failed.
- R25 — DS: 4; CD: day 11; IS: pending.
- R26 — DS: 5; CD: day 27; IS: passed.
- R27 — DS: 2; CD: day 7; IS: failed.
- R28 — DS: 2; CD: day 11; IS: pending.
- R29 — DS: 5; CD: day 23; IS: failed.
- R30 — DS: 3; CD: day 18; IS: pending.
- R31 — DS: 2; CD: day 24; IS: passed.
- R32 — DS: 4; CD: day 23; IS: pending.
- R33 — DS: 1; CD: day 2; IS: pending.
- R34 — DS: 5; CD: day 12; IS: passed.
- R35 — DS: 3; CD: day 12; IS: failed.
- R36 — DS: 4; CD: day 13; IS: passed.
- R37 — DS: 3; CD: day 29; IS: failed.
- R38 — DS: 4; CD: day 7; IS: failed.
- R39 — DS: 4; CD: day 15; IS: pending.
- R40 — DS: 3; CD: day 13; IS: failed.
- R41 — DS: 5; CD: day 1; IS: passed.
- R42 — DS: 4; CD: day 22; IS: passed.
- R43 — DS: 4; CD: day 19; IS: pending.
- R44 — DS: 4; CD: day 21; IS: passed.
- R45 — DS: 5; CD: day 25; IS: pending.
- R46 — DS: 2; CD: day 20; IS: failed.
- R47 — DS: 2; CD: day 29; IS: failed.
- R48 — DS: 3; CD: day 14; IS: failed.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 946 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 20; state = &quot;failed&quot;.

Records:
- R01: score=5; day=1; state=failed.
- R02: score=1; day=30; state=passed.
- R03: score=2; day=27; state=pending.
- R04: score=2; day=7; state=passed.
- R05: score=5; day=17; state=passed.
- R06: score=4; day=20; state=passed.
- R07: score=4; day=1; state=failed.
- R08: score=1; day=12; state=failed.
- R09: score=5; day=30; state=passed.
- R10: score=5; day=19; state=passed.
- R11: score=3; day=28; state=pending.
- R12: score=5; day=6; state=passed.
- R13: score=3; day=29; state=failed.
- R14: score=5; day=2; state=passed.
- R15: score=5; day=25; state=failed.
- R16: score=2; day=21; state=passed.
- R17: score=4; day=14; state=passed.
- R18: score=4; day=5; state=passed.
- R19: score=1; day=23; state=failed.
- R20: score=3; day=29; state=passed.
- R21: score=3; day=17; state=failed.
- R22: score=2; day=22; state=pending.
- R23: score=2; day=18; state=passed.
- R24: score=3; day=4; state=failed.
- R25: score=4; day=11; state=pending.
- R26: score=5; day=27; state=passed.
- R27: score=2; day=7; state=failed.
- R28: score=2; day=11; state=pending.
- R29: score=5; day=23; state=failed.
- R30: score=3; day=18; state=pending.
- R31: score=2; day=24; state=passed.
- R32: score=4; day=23; state=pending.
- R33: score=1; day=2; state=pending.
- R34: score=5; day=12; state=passed.
- R35: score=3; day=12; state=failed.
- R36: score=4; day=13; state=passed.
- R37: score=3; day=29; state=failed.
- R38: score=4; day=7; state=failed.
- R39: score=4; day=15; state=pending.
- R40: score=3; day=13; state=failed.
- R41: score=5; day=1; state=passed.
- R42: score=4; day=22; state=passed.
- R43: score=4; day=19; state=pending.
- R44: score=4; day=21; state=passed.
- R45: score=5; day=25; state=pending.
- R46: score=2; day=20; state=failed.
- R47: score=2; day=29; state=failed.
- R48: score=3; day=14; state=failed.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>human_resources-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 246 input tokens</summary>

<pre><code>Review every employee training record. A employee training record qualifies only when all three rules hold:
1. Its compliance score is at least 3.
2. Its renewal deadline is day 10 or earlier.
3. Its completion status is exactly &quot;incomplete&quot;.

Records:
- R01 — compliance score: 5; renewal deadline: day 1; completion status: incomplete.
- R02 — compliance score: 1; renewal deadline: day 30; completion status: complete.
- R03 — compliance score: 1; renewal deadline: day 10; completion status: incomplete.
- R04 — compliance score: 1; renewal deadline: day 27; completion status: pending.
- R05 — compliance score: 1; renewal deadline: day 27; completion status: incomplete.
- R06 — compliance score: 1; renewal deadline: day 4; completion status: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 254 input tokens</summary>

<pre><code>Abbreviation legend:
- ETR = employee training record
- CS = compliance score
- RD = renewal deadline
- CTS = completion status

Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 3.
2. Its RD is day 10 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 1; RD: day 10; CTS: incomplete.
- R04 — CS: 1; RD: day 27; CTS: pending.
- R05 — CS: 1; RD: day 27; CTS: incomplete.
- R06 — CS: 1; RD: day 4; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 223 input tokens</summary>

<pre><code>Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 3.
2. Its RD is day 10 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 1; RD: day 10; CTS: incomplete.
- R04 — CS: 1; RD: day 27; CTS: pending.
- R05 — CS: 1; RD: day 27; CTS: incomplete.
- R06 — CS: 1; RD: day 4; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 157 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 10; state = &quot;incomplete&quot;.

Records:
- R01: score=5; day=1; state=incomplete.
- R02: score=1; day=30; state=complete.
- R03: score=1; day=10; state=incomplete.
- R04: score=1; day=27; state=pending.
- R05: score=1; day=27; state=incomplete.
- R06: score=1; day=4; state=incomplete.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>human_resources-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R05&quot;]}</code></summary>

<details><summary>Full prose — 394 input tokens</summary>

<pre><code>Review every employee training record. A employee training record qualifies only when all three rules hold:
1. Its compliance score is at least 4.
2. Its renewal deadline is day 15 or earlier.
3. Its completion status is exactly &quot;incomplete&quot;.

Records:
- R01 — compliance score: 5; renewal deadline: day 1; completion status: incomplete.
- R02 — compliance score: 1; renewal deadline: day 30; completion status: complete.
- R03 — compliance score: 5; renewal deadline: day 14; completion status: pending.
- R04 — compliance score: 5; renewal deadline: day 23; completion status: complete.
- R05 — compliance score: 4; renewal deadline: day 6; completion status: incomplete.
- R06 — compliance score: 2; renewal deadline: day 11; completion status: pending.
- R07 — compliance score: 3; renewal deadline: day 8; completion status: complete.
- R08 — compliance score: 5; renewal deadline: day 26; completion status: complete.
- R09 — compliance score: 3; renewal deadline: day 7; completion status: incomplete.
- R10 — compliance score: 2; renewal deadline: day 21; completion status: incomplete.
- R11 — compliance score: 4; renewal deadline: day 27; completion status: incomplete.
- R12 — compliance score: 3; renewal deadline: day 20; completion status: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 384 input tokens</summary>

<pre><code>Abbreviation legend:
- ETR = employee training record
- CS = compliance score
- RD = renewal deadline
- CTS = completion status

Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 4.
2. Its RD is day 15 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 5; RD: day 14; CTS: pending.
- R04 — CS: 5; RD: day 23; CTS: complete.
- R05 — CS: 4; RD: day 6; CTS: incomplete.
- R06 — CS: 2; RD: day 11; CTS: pending.
- R07 — CS: 3; RD: day 8; CTS: complete.
- R08 — CS: 5; RD: day 26; CTS: complete.
- R09 — CS: 3; RD: day 7; CTS: incomplete.
- R10 — CS: 2; RD: day 21; CTS: incomplete.
- R11 — CS: 4; RD: day 27; CTS: incomplete.
- R12 — CS: 3; RD: day 20; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 353 input tokens</summary>

<pre><code>Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 4.
2. Its RD is day 15 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 5; RD: day 14; CTS: pending.
- R04 — CS: 5; RD: day 23; CTS: complete.
- R05 — CS: 4; RD: day 6; CTS: incomplete.
- R06 — CS: 2; RD: day 11; CTS: pending.
- R07 — CS: 3; RD: day 8; CTS: complete.
- R08 — CS: 5; RD: day 26; CTS: complete.
- R09 — CS: 3; RD: day 7; CTS: incomplete.
- R10 — CS: 2; RD: day 21; CTS: incomplete.
- R11 — CS: 4; RD: day 27; CTS: incomplete.
- R12 — CS: 3; RD: day 20; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 269 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 15; state = &quot;incomplete&quot;.

Records:
- R01: score=5; day=1; state=incomplete.
- R02: score=1; day=30; state=complete.
- R03: score=5; day=14; state=pending.
- R04: score=5; day=23; state=complete.
- R05: score=4; day=6; state=incomplete.
- R06: score=2; day=11; state=pending.
- R07: score=3; day=8; state=complete.
- R08: score=5; day=26; state=complete.
- R09: score=3; day=7; state=incomplete.
- R10: score=2; day=21; state=incomplete.
- R11: score=4; day=27; state=incomplete.
- R12: score=3; day=20; state=incomplete.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>human_resources-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R05&quot;, &quot;R14&quot;, &quot;R16&quot;, &quot;R24&quot;]}</code></summary>

<details><summary>Full prose — 686 input tokens</summary>

<pre><code>Review every employee training record. A employee training record qualifies only when all three rules hold:
1. Its compliance score is at least 3.
2. Its renewal deadline is day 20 or earlier.
3. Its completion status is exactly &quot;incomplete&quot;.

Records:
- R01 — compliance score: 5; renewal deadline: day 1; completion status: incomplete.
- R02 — compliance score: 1; renewal deadline: day 30; completion status: complete.
- R03 — compliance score: 3; renewal deadline: day 12; completion status: pending.
- R04 — compliance score: 5; renewal deadline: day 4; completion status: pending.
- R05 — compliance score: 5; renewal deadline: day 14; completion status: incomplete.
- R06 — compliance score: 2; renewal deadline: day 19; completion status: incomplete.
- R07 — compliance score: 2; renewal deadline: day 6; completion status: incomplete.
- R08 — compliance score: 2; renewal deadline: day 7; completion status: complete.
- R09 — compliance score: 5; renewal deadline: day 6; completion status: complete.
- R10 — compliance score: 2; renewal deadline: day 2; completion status: complete.
- R11 — compliance score: 4; renewal deadline: day 16; completion status: pending.
- R12 — compliance score: 2; renewal deadline: day 25; completion status: incomplete.
- R13 — compliance score: 1; renewal deadline: day 20; completion status: complete.
- R14 — compliance score: 3; renewal deadline: day 14; completion status: incomplete.
- R15 — compliance score: 2; renewal deadline: day 8; completion status: incomplete.
- R16 — compliance score: 5; renewal deadline: day 7; completion status: incomplete.
- R17 — compliance score: 2; renewal deadline: day 5; completion status: incomplete.
- R18 — compliance score: 4; renewal deadline: day 15; completion status: complete.
- R19 — compliance score: 2; renewal deadline: day 12; completion status: complete.
- R20 — compliance score: 3; renewal deadline: day 1; completion status: complete.
- R21 — compliance score: 1; renewal deadline: day 25; completion status: incomplete.
- R22 — compliance score: 2; renewal deadline: day 5; completion status: complete.
- R23 — compliance score: 1; renewal deadline: day 2; completion status: incomplete.
- R24 — compliance score: 4; renewal deadline: day 14; completion status: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 640 input tokens</summary>

<pre><code>Abbreviation legend:
- ETR = employee training record
- CS = compliance score
- RD = renewal deadline
- CTS = completion status

Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 3.
2. Its RD is day 20 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 3; RD: day 12; CTS: pending.
- R04 — CS: 5; RD: day 4; CTS: pending.
- R05 — CS: 5; RD: day 14; CTS: incomplete.
- R06 — CS: 2; RD: day 19; CTS: incomplete.
- R07 — CS: 2; RD: day 6; CTS: incomplete.
- R08 — CS: 2; RD: day 7; CTS: complete.
- R09 — CS: 5; RD: day 6; CTS: complete.
- R10 — CS: 2; RD: day 2; CTS: complete.
- R11 — CS: 4; RD: day 16; CTS: pending.
- R12 — CS: 2; RD: day 25; CTS: incomplete.
- R13 — CS: 1; RD: day 20; CTS: complete.
- R14 — CS: 3; RD: day 14; CTS: incomplete.
- R15 — CS: 2; RD: day 8; CTS: incomplete.
- R16 — CS: 5; RD: day 7; CTS: incomplete.
- R17 — CS: 2; RD: day 5; CTS: incomplete.
- R18 — CS: 4; RD: day 15; CTS: complete.
- R19 — CS: 2; RD: day 12; CTS: complete.
- R20 — CS: 3; RD: day 1; CTS: complete.
- R21 — CS: 1; RD: day 25; CTS: incomplete.
- R22 — CS: 2; RD: day 5; CTS: complete.
- R23 — CS: 1; RD: day 2; CTS: incomplete.
- R24 — CS: 4; RD: day 14; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 609 input tokens</summary>

<pre><code>Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 3.
2. Its RD is day 20 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 3; RD: day 12; CTS: pending.
- R04 — CS: 5; RD: day 4; CTS: pending.
- R05 — CS: 5; RD: day 14; CTS: incomplete.
- R06 — CS: 2; RD: day 19; CTS: incomplete.
- R07 — CS: 2; RD: day 6; CTS: incomplete.
- R08 — CS: 2; RD: day 7; CTS: complete.
- R09 — CS: 5; RD: day 6; CTS: complete.
- R10 — CS: 2; RD: day 2; CTS: complete.
- R11 — CS: 4; RD: day 16; CTS: pending.
- R12 — CS: 2; RD: day 25; CTS: incomplete.
- R13 — CS: 1; RD: day 20; CTS: complete.
- R14 — CS: 3; RD: day 14; CTS: incomplete.
- R15 — CS: 2; RD: day 8; CTS: incomplete.
- R16 — CS: 5; RD: day 7; CTS: incomplete.
- R17 — CS: 2; RD: day 5; CTS: incomplete.
- R18 — CS: 4; RD: day 15; CTS: complete.
- R19 — CS: 2; RD: day 12; CTS: complete.
- R20 — CS: 3; RD: day 1; CTS: complete.
- R21 — CS: 1; RD: day 25; CTS: incomplete.
- R22 — CS: 2; RD: day 5; CTS: complete.
- R23 — CS: 1; RD: day 2; CTS: incomplete.
- R24 — CS: 4; RD: day 14; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 489 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 20; state = &quot;incomplete&quot;.

Records:
- R01: score=5; day=1; state=incomplete.
- R02: score=1; day=30; state=complete.
- R03: score=3; day=12; state=pending.
- R04: score=5; day=4; state=pending.
- R05: score=5; day=14; state=incomplete.
- R06: score=2; day=19; state=incomplete.
- R07: score=2; day=6; state=incomplete.
- R08: score=2; day=7; state=complete.
- R09: score=5; day=6; state=complete.
- R10: score=2; day=2; state=complete.
- R11: score=4; day=16; state=pending.
- R12: score=2; day=25; state=incomplete.
- R13: score=1; day=20; state=complete.
- R14: score=3; day=14; state=incomplete.
- R15: score=2; day=8; state=incomplete.
- R16: score=5; day=7; state=incomplete.
- R17: score=2; day=5; state=incomplete.
- R18: score=4; day=15; state=complete.
- R19: score=2; day=12; state=complete.
- R20: score=3; day=1; state=complete.
- R21: score=1; day=25; state=incomplete.
- R22: score=2; day=5; state=complete.
- R23: score=1; day=2; state=incomplete.
- R24: score=4; day=14; state=incomplete.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>human_resources-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R21&quot;, &quot;R27&quot;]}</code></summary>

<details><summary>Full prose — 1288 input tokens</summary>

<pre><code>Review every employee training record. A employee training record qualifies only when all three rules hold:
1. Its compliance score is at least 4.
2. Its renewal deadline is day 10 or earlier.
3. Its completion status is exactly &quot;incomplete&quot;.

Records:
- R01 — compliance score: 5; renewal deadline: day 1; completion status: incomplete.
- R02 — compliance score: 1; renewal deadline: day 30; completion status: complete.
- R03 — compliance score: 5; renewal deadline: day 17; completion status: incomplete.
- R04 — compliance score: 1; renewal deadline: day 18; completion status: incomplete.
- R05 — compliance score: 1; renewal deadline: day 26; completion status: pending.
- R06 — compliance score: 1; renewal deadline: day 24; completion status: complete.
- R07 — compliance score: 5; renewal deadline: day 19; completion status: complete.
- R08 — compliance score: 2; renewal deadline: day 3; completion status: pending.
- R09 — compliance score: 3; renewal deadline: day 2; completion status: complete.
- R10 — compliance score: 1; renewal deadline: day 15; completion status: incomplete.
- R11 — compliance score: 1; renewal deadline: day 29; completion status: complete.
- R12 — compliance score: 4; renewal deadline: day 24; completion status: pending.
- R13 — compliance score: 2; renewal deadline: day 21; completion status: complete.
- R14 — compliance score: 2; renewal deadline: day 28; completion status: complete.
- R15 — compliance score: 4; renewal deadline: day 22; completion status: complete.
- R16 — compliance score: 4; renewal deadline: day 12; completion status: pending.
- R17 — compliance score: 2; renewal deadline: day 23; completion status: complete.
- R18 — compliance score: 3; renewal deadline: day 24; completion status: pending.
- R19 — compliance score: 2; renewal deadline: day 1; completion status: incomplete.
- R20 — compliance score: 2; renewal deadline: day 21; completion status: pending.
- R21 — compliance score: 5; renewal deadline: day 8; completion status: incomplete.
- R22 — compliance score: 5; renewal deadline: day 28; completion status: incomplete.
- R23 — compliance score: 1; renewal deadline: day 15; completion status: complete.
- R24 — compliance score: 3; renewal deadline: day 30; completion status: pending.
- R25 — compliance score: 4; renewal deadline: day 8; completion status: complete.
- R26 — compliance score: 4; renewal deadline: day 15; completion status: incomplete.
- R27 — compliance score: 4; renewal deadline: day 6; completion status: incomplete.
- R28 — compliance score: 2; renewal deadline: day 23; completion status: incomplete.
- R29 — compliance score: 4; renewal deadline: day 23; completion status: incomplete.
- R30 — compliance score: 4; renewal deadline: day 12; completion status: incomplete.
- R31 — compliance score: 3; renewal deadline: day 13; completion status: incomplete.
- R32 — compliance score: 3; renewal deadline: day 23; completion status: complete.
- R33 — compliance score: 5; renewal deadline: day 28; completion status: complete.
- R34 — compliance score: 4; renewal deadline: day 20; completion status: incomplete.
- R35 — compliance score: 3; renewal deadline: day 29; completion status: incomplete.
- R36 — compliance score: 2; renewal deadline: day 16; completion status: pending.
- R37 — compliance score: 5; renewal deadline: day 30; completion status: pending.
- R38 — compliance score: 2; renewal deadline: day 22; completion status: complete.
- R39 — compliance score: 1; renewal deadline: day 27; completion status: complete.
- R40 — compliance score: 3; renewal deadline: day 10; completion status: pending.
- R41 — compliance score: 3; renewal deadline: day 4; completion status: incomplete.
- R42 — compliance score: 1; renewal deadline: day 8; completion status: incomplete.
- R43 — compliance score: 2; renewal deadline: day 28; completion status: incomplete.
- R44 — compliance score: 2; renewal deadline: day 22; completion status: incomplete.
- R45 — compliance score: 2; renewal deadline: day 28; completion status: pending.
- R46 — compliance score: 2; renewal deadline: day 7; completion status: complete.
- R47 — compliance score: 3; renewal deadline: day 15; completion status: pending.
- R48 — compliance score: 5; renewal deadline: day 30; completion status: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1170 input tokens</summary>

<pre><code>Abbreviation legend:
- ETR = employee training record
- CS = compliance score
- RD = renewal deadline
- CTS = completion status

Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 4.
2. Its RD is day 10 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 5; RD: day 17; CTS: incomplete.
- R04 — CS: 1; RD: day 18; CTS: incomplete.
- R05 — CS: 1; RD: day 26; CTS: pending.
- R06 — CS: 1; RD: day 24; CTS: complete.
- R07 — CS: 5; RD: day 19; CTS: complete.
- R08 — CS: 2; RD: day 3; CTS: pending.
- R09 — CS: 3; RD: day 2; CTS: complete.
- R10 — CS: 1; RD: day 15; CTS: incomplete.
- R11 — CS: 1; RD: day 29; CTS: complete.
- R12 — CS: 4; RD: day 24; CTS: pending.
- R13 — CS: 2; RD: day 21; CTS: complete.
- R14 — CS: 2; RD: day 28; CTS: complete.
- R15 — CS: 4; RD: day 22; CTS: complete.
- R16 — CS: 4; RD: day 12; CTS: pending.
- R17 — CS: 2; RD: day 23; CTS: complete.
- R18 — CS: 3; RD: day 24; CTS: pending.
- R19 — CS: 2; RD: day 1; CTS: incomplete.
- R20 — CS: 2; RD: day 21; CTS: pending.
- R21 — CS: 5; RD: day 8; CTS: incomplete.
- R22 — CS: 5; RD: day 28; CTS: incomplete.
- R23 — CS: 1; RD: day 15; CTS: complete.
- R24 — CS: 3; RD: day 30; CTS: pending.
- R25 — CS: 4; RD: day 8; CTS: complete.
- R26 — CS: 4; RD: day 15; CTS: incomplete.
- R27 — CS: 4; RD: day 6; CTS: incomplete.
- R28 — CS: 2; RD: day 23; CTS: incomplete.
- R29 — CS: 4; RD: day 23; CTS: incomplete.
- R30 — CS: 4; RD: day 12; CTS: incomplete.
- R31 — CS: 3; RD: day 13; CTS: incomplete.
- R32 — CS: 3; RD: day 23; CTS: complete.
- R33 — CS: 5; RD: day 28; CTS: complete.
- R34 — CS: 4; RD: day 20; CTS: incomplete.
- R35 — CS: 3; RD: day 29; CTS: incomplete.
- R36 — CS: 2; RD: day 16; CTS: pending.
- R37 — CS: 5; RD: day 30; CTS: pending.
- R38 — CS: 2; RD: day 22; CTS: complete.
- R39 — CS: 1; RD: day 27; CTS: complete.
- R40 — CS: 3; RD: day 10; CTS: pending.
- R41 — CS: 3; RD: day 4; CTS: incomplete.
- R42 — CS: 1; RD: day 8; CTS: incomplete.
- R43 — CS: 2; RD: day 28; CTS: incomplete.
- R44 — CS: 2; RD: day 22; CTS: incomplete.
- R45 — CS: 2; RD: day 28; CTS: pending.
- R46 — CS: 2; RD: day 7; CTS: complete.
- R47 — CS: 3; RD: day 15; CTS: pending.
- R48 — CS: 5; RD: day 30; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1139 input tokens</summary>

<pre><code>Review every ETR. A ETR qualifies only when all three rules hold:
1. Its CS is at least 4.
2. Its RD is day 10 or earlier.
3. Its CTS is exactly &quot;incomplete&quot;.

Records:
- R01 — CS: 5; RD: day 1; CTS: incomplete.
- R02 — CS: 1; RD: day 30; CTS: complete.
- R03 — CS: 5; RD: day 17; CTS: incomplete.
- R04 — CS: 1; RD: day 18; CTS: incomplete.
- R05 — CS: 1; RD: day 26; CTS: pending.
- R06 — CS: 1; RD: day 24; CTS: complete.
- R07 — CS: 5; RD: day 19; CTS: complete.
- R08 — CS: 2; RD: day 3; CTS: pending.
- R09 — CS: 3; RD: day 2; CTS: complete.
- R10 — CS: 1; RD: day 15; CTS: incomplete.
- R11 — CS: 1; RD: day 29; CTS: complete.
- R12 — CS: 4; RD: day 24; CTS: pending.
- R13 — CS: 2; RD: day 21; CTS: complete.
- R14 — CS: 2; RD: day 28; CTS: complete.
- R15 — CS: 4; RD: day 22; CTS: complete.
- R16 — CS: 4; RD: day 12; CTS: pending.
- R17 — CS: 2; RD: day 23; CTS: complete.
- R18 — CS: 3; RD: day 24; CTS: pending.
- R19 — CS: 2; RD: day 1; CTS: incomplete.
- R20 — CS: 2; RD: day 21; CTS: pending.
- R21 — CS: 5; RD: day 8; CTS: incomplete.
- R22 — CS: 5; RD: day 28; CTS: incomplete.
- R23 — CS: 1; RD: day 15; CTS: complete.
- R24 — CS: 3; RD: day 30; CTS: pending.
- R25 — CS: 4; RD: day 8; CTS: complete.
- R26 — CS: 4; RD: day 15; CTS: incomplete.
- R27 — CS: 4; RD: day 6; CTS: incomplete.
- R28 — CS: 2; RD: day 23; CTS: incomplete.
- R29 — CS: 4; RD: day 23; CTS: incomplete.
- R30 — CS: 4; RD: day 12; CTS: incomplete.
- R31 — CS: 3; RD: day 13; CTS: incomplete.
- R32 — CS: 3; RD: day 23; CTS: complete.
- R33 — CS: 5; RD: day 28; CTS: complete.
- R34 — CS: 4; RD: day 20; CTS: incomplete.
- R35 — CS: 3; RD: day 29; CTS: incomplete.
- R36 — CS: 2; RD: day 16; CTS: pending.
- R37 — CS: 5; RD: day 30; CTS: pending.
- R38 — CS: 2; RD: day 22; CTS: complete.
- R39 — CS: 1; RD: day 27; CTS: complete.
- R40 — CS: 3; RD: day 10; CTS: pending.
- R41 — CS: 3; RD: day 4; CTS: incomplete.
- R42 — CS: 1; RD: day 8; CTS: incomplete.
- R43 — CS: 2; RD: day 28; CTS: incomplete.
- R44 — CS: 2; RD: day 22; CTS: incomplete.
- R45 — CS: 2; RD: day 28; CTS: pending.
- R46 — CS: 2; RD: day 7; CTS: complete.
- R47 — CS: 3; RD: day 15; CTS: pending.
- R48 — CS: 5; RD: day 30; CTS: incomplete.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 947 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 10; state = &quot;incomplete&quot;.

Records:
- R01: score=5; day=1; state=incomplete.
- R02: score=1; day=30; state=complete.
- R03: score=5; day=17; state=incomplete.
- R04: score=1; day=18; state=incomplete.
- R05: score=1; day=26; state=pending.
- R06: score=1; day=24; state=complete.
- R07: score=5; day=19; state=complete.
- R08: score=2; day=3; state=pending.
- R09: score=3; day=2; state=complete.
- R10: score=1; day=15; state=incomplete.
- R11: score=1; day=29; state=complete.
- R12: score=4; day=24; state=pending.
- R13: score=2; day=21; state=complete.
- R14: score=2; day=28; state=complete.
- R15: score=4; day=22; state=complete.
- R16: score=4; day=12; state=pending.
- R17: score=2; day=23; state=complete.
- R18: score=3; day=24; state=pending.
- R19: score=2; day=1; state=incomplete.
- R20: score=2; day=21; state=pending.
- R21: score=5; day=8; state=incomplete.
- R22: score=5; day=28; state=incomplete.
- R23: score=1; day=15; state=complete.
- R24: score=3; day=30; state=pending.
- R25: score=4; day=8; state=complete.
- R26: score=4; day=15; state=incomplete.
- R27: score=4; day=6; state=incomplete.
- R28: score=2; day=23; state=incomplete.
- R29: score=4; day=23; state=incomplete.
- R30: score=4; day=12; state=incomplete.
- R31: score=3; day=13; state=incomplete.
- R32: score=3; day=23; state=complete.
- R33: score=5; day=28; state=complete.
- R34: score=4; day=20; state=incomplete.
- R35: score=3; day=29; state=incomplete.
- R36: score=2; day=16; state=pending.
- R37: score=5; day=30; state=pending.
- R38: score=2; day=22; state=complete.
- R39: score=1; day=27; state=complete.
- R40: score=3; day=10; state=pending.
- R41: score=3; day=4; state=incomplete.
- R42: score=1; day=8; state=incomplete.
- R43: score=2; day=28; state=incomplete.
- R44: score=2; day=22; state=incomplete.
- R45: score=2; day=28; state=pending.
- R46: score=2; day=7; state=complete.
- R47: score=3; day=15; state=pending.
- R48: score=5; day=30; state=incomplete.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>operations-06</strong> — 6 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;]}</code></summary>

<details><summary>Full prose — 245 input tokens</summary>

<pre><code>Review every service interruption report. A service interruption report qualifies only when all three rules hold:
1. Its impact severity is at least 4.
2. Its recovery deadline is day 15 or earlier.
3. Its restoration status is exactly &quot;unavailable&quot;.

Records:
- R01 — impact severity: 5; recovery deadline: day 1; restoration status: unavailable.
- R02 — impact severity: 1; recovery deadline: day 30; restoration status: degraded.
- R03 — impact severity: 4; recovery deadline: day 25; restoration status: restored.
- R04 — impact severity: 3; recovery deadline: day 1; restoration status: unavailable.
- R05 — impact severity: 1; recovery deadline: day 6; restoration status: degraded.
- R06 — impact severity: 3; recovery deadline: day 28; restoration status: degraded.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 250 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = service interruption report
- IS = impact severity
- RD = recovery deadline
- RS = restoration status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 4.
2. Its RD is day 15 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 4; RD: day 25; RS: restored.
- R04 — IS: 3; RD: day 1; RS: unavailable.
- R05 — IS: 1; RD: day 6; RS: degraded.
- R06 — IS: 3; RD: day 28; RS: degraded.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 220 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 4.
2. Its RD is day 15 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 4; RD: day 25; RS: restored.
- R04 — IS: 3; RD: day 1; RS: unavailable.
- R05 — IS: 1; RD: day 6; RS: degraded.
- R06 — IS: 3; RD: day 28; RS: degraded.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 160 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 15; state = &quot;unavailable&quot;.

Records:
- R01: score=5; day=1; state=unavailable.
- R02: score=1; day=30; state=degraded.
- R03: score=4; day=25; state=restored.
- R04: score=3; day=1; state=unavailable.
- R05: score=1; day=6; state=degraded.
- R06: score=3; day=28; state=degraded.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>operations-12</strong> — 12 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R12&quot;]}</code></summary>

<details><summary>Full prose — 395 input tokens</summary>

<pre><code>Review every service interruption report. A service interruption report qualifies only when all three rules hold:
1. Its impact severity is at least 3.
2. Its recovery deadline is day 20 or earlier.
3. Its restoration status is exactly &quot;unavailable&quot;.

Records:
- R01 — impact severity: 5; recovery deadline: day 1; restoration status: unavailable.
- R02 — impact severity: 1; recovery deadline: day 30; restoration status: degraded.
- R03 — impact severity: 3; recovery deadline: day 11; restoration status: restored.
- R04 — impact severity: 5; recovery deadline: day 25; restoration status: unavailable.
- R05 — impact severity: 1; recovery deadline: day 17; restoration status: restored.
- R06 — impact severity: 2; recovery deadline: day 12; restoration status: restored.
- R07 — impact severity: 3; recovery deadline: day 30; restoration status: degraded.
- R08 — impact severity: 2; recovery deadline: day 26; restoration status: unavailable.
- R09 — impact severity: 1; recovery deadline: day 17; restoration status: restored.
- R10 — impact severity: 1; recovery deadline: day 11; restoration status: unavailable.
- R11 — impact severity: 3; recovery deadline: day 7; restoration status: restored.
- R12 — impact severity: 4; recovery deadline: day 3; restoration status: unavailable.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 382 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = service interruption report
- IS = impact severity
- RD = recovery deadline
- RS = restoration status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 3.
2. Its RD is day 20 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 3; RD: day 11; RS: restored.
- R04 — IS: 5; RD: day 25; RS: unavailable.
- R05 — IS: 1; RD: day 17; RS: restored.
- R06 — IS: 2; RD: day 12; RS: restored.
- R07 — IS: 3; RD: day 30; RS: degraded.
- R08 — IS: 2; RD: day 26; RS: unavailable.
- R09 — IS: 1; RD: day 17; RS: restored.
- R10 — IS: 1; RD: day 11; RS: unavailable.
- R11 — IS: 3; RD: day 7; RS: restored.
- R12 — IS: 4; RD: day 3; RS: unavailable.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 352 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 3.
2. Its RD is day 20 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 3; RD: day 11; RS: restored.
- R04 — IS: 5; RD: day 25; RS: unavailable.
- R05 — IS: 1; RD: day 17; RS: restored.
- R06 — IS: 2; RD: day 12; RS: restored.
- R07 — IS: 3; RD: day 30; RS: degraded.
- R08 — IS: 2; RD: day 26; RS: unavailable.
- R09 — IS: 1; RD: day 17; RS: restored.
- R10 — IS: 1; RD: day 11; RS: unavailable.
- R11 — IS: 3; RD: day 7; RS: restored.
- R12 — IS: 4; RD: day 3; RS: unavailable.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 277 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 20; state = &quot;unavailable&quot;.

Records:
- R01: score=5; day=1; state=unavailable.
- R02: score=1; day=30; state=degraded.
- R03: score=3; day=11; state=restored.
- R04: score=5; day=25; state=unavailable.
- R05: score=1; day=17; state=restored.
- R06: score=2; day=12; state=restored.
- R07: score=3; day=30; state=degraded.
- R08: score=2; day=26; state=unavailable.
- R09: score=1; day=17; state=restored.
- R10: score=1; day=11; state=unavailable.
- R11: score=3; day=7; state=restored.
- R12: score=4; day=3; state=unavailable.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>operations-24</strong> — 24 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R08&quot;]}</code></summary>

<details><summary>Full prose — 691 input tokens</summary>

<pre><code>Review every service interruption report. A service interruption report qualifies only when all three rules hold:
1. Its impact severity is at least 4.
2. Its recovery deadline is day 10 or earlier.
3. Its restoration status is exactly &quot;unavailable&quot;.

Records:
- R01 — impact severity: 5; recovery deadline: day 1; restoration status: unavailable.
- R02 — impact severity: 1; recovery deadline: day 30; restoration status: degraded.
- R03 — impact severity: 5; recovery deadline: day 21; restoration status: unavailable.
- R04 — impact severity: 1; recovery deadline: day 21; restoration status: degraded.
- R05 — impact severity: 5; recovery deadline: day 26; restoration status: unavailable.
- R06 — impact severity: 3; recovery deadline: day 13; restoration status: unavailable.
- R07 — impact severity: 1; recovery deadline: day 17; restoration status: restored.
- R08 — impact severity: 5; recovery deadline: day 9; restoration status: unavailable.
- R09 — impact severity: 3; recovery deadline: day 25; restoration status: degraded.
- R10 — impact severity: 4; recovery deadline: day 11; restoration status: restored.
- R11 — impact severity: 5; recovery deadline: day 28; restoration status: restored.
- R12 — impact severity: 4; recovery deadline: day 6; restoration status: restored.
- R13 — impact severity: 3; recovery deadline: day 9; restoration status: restored.
- R14 — impact severity: 3; recovery deadline: day 15; restoration status: unavailable.
- R15 — impact severity: 3; recovery deadline: day 28; restoration status: restored.
- R16 — impact severity: 1; recovery deadline: day 27; restoration status: unavailable.
- R17 — impact severity: 4; recovery deadline: day 14; restoration status: restored.
- R18 — impact severity: 5; recovery deadline: day 26; restoration status: unavailable.
- R19 — impact severity: 2; recovery deadline: day 27; restoration status: unavailable.
- R20 — impact severity: 2; recovery deadline: day 5; restoration status: degraded.
- R21 — impact severity: 5; recovery deadline: day 15; restoration status: degraded.
- R22 — impact severity: 1; recovery deadline: day 17; restoration status: unavailable.
- R23 — impact severity: 5; recovery deadline: day 7; restoration status: restored.
- R24 — impact severity: 3; recovery deadline: day 8; restoration status: unavailable.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 642 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = service interruption report
- IS = impact severity
- RD = recovery deadline
- RS = restoration status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 4.
2. Its RD is day 10 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 5; RD: day 21; RS: unavailable.
- R04 — IS: 1; RD: day 21; RS: degraded.
- R05 — IS: 5; RD: day 26; RS: unavailable.
- R06 — IS: 3; RD: day 13; RS: unavailable.
- R07 — IS: 1; RD: day 17; RS: restored.
- R08 — IS: 5; RD: day 9; RS: unavailable.
- R09 — IS: 3; RD: day 25; RS: degraded.
- R10 — IS: 4; RD: day 11; RS: restored.
- R11 — IS: 5; RD: day 28; RS: restored.
- R12 — IS: 4; RD: day 6; RS: restored.
- R13 — IS: 3; RD: day 9; RS: restored.
- R14 — IS: 3; RD: day 15; RS: unavailable.
- R15 — IS: 3; RD: day 28; RS: restored.
- R16 — IS: 1; RD: day 27; RS: unavailable.
- R17 — IS: 4; RD: day 14; RS: restored.
- R18 — IS: 5; RD: day 26; RS: unavailable.
- R19 — IS: 2; RD: day 27; RS: unavailable.
- R20 — IS: 2; RD: day 5; RS: degraded.
- R21 — IS: 5; RD: day 15; RS: degraded.
- R22 — IS: 1; RD: day 17; RS: unavailable.
- R23 — IS: 5; RD: day 7; RS: restored.
- R24 — IS: 3; RD: day 8; RS: unavailable.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 612 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 4.
2. Its RD is day 10 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 5; RD: day 21; RS: unavailable.
- R04 — IS: 1; RD: day 21; RS: degraded.
- R05 — IS: 5; RD: day 26; RS: unavailable.
- R06 — IS: 3; RD: day 13; RS: unavailable.
- R07 — IS: 1; RD: day 17; RS: restored.
- R08 — IS: 5; RD: day 9; RS: unavailable.
- R09 — IS: 3; RD: day 25; RS: degraded.
- R10 — IS: 4; RD: day 11; RS: restored.
- R11 — IS: 5; RD: day 28; RS: restored.
- R12 — IS: 4; RD: day 6; RS: restored.
- R13 — IS: 3; RD: day 9; RS: restored.
- R14 — IS: 3; RD: day 15; RS: unavailable.
- R15 — IS: 3; RD: day 28; RS: restored.
- R16 — IS: 1; RD: day 27; RS: unavailable.
- R17 — IS: 4; RD: day 14; RS: restored.
- R18 — IS: 5; RD: day 26; RS: unavailable.
- R19 — IS: 2; RD: day 27; RS: unavailable.
- R20 — IS: 2; RD: day 5; RS: degraded.
- R21 — IS: 5; RD: day 15; RS: degraded.
- R22 — IS: 1; RD: day 17; RS: unavailable.
- R23 — IS: 5; RD: day 7; RS: restored.
- R24 — IS: 3; RD: day 8; RS: unavailable.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 507 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 4; day &lt;= 10; state = &quot;unavailable&quot;.

Records:
- R01: score=5; day=1; state=unavailable.
- R02: score=1; day=30; state=degraded.
- R03: score=5; day=21; state=unavailable.
- R04: score=1; day=21; state=degraded.
- R05: score=5; day=26; state=unavailable.
- R06: score=3; day=13; state=unavailable.
- R07: score=1; day=17; state=restored.
- R08: score=5; day=9; state=unavailable.
- R09: score=3; day=25; state=degraded.
- R10: score=4; day=11; state=restored.
- R11: score=5; day=28; state=restored.
- R12: score=4; day=6; state=restored.
- R13: score=3; day=9; state=restored.
- R14: score=3; day=15; state=unavailable.
- R15: score=3; day=28; state=restored.
- R16: score=1; day=27; state=unavailable.
- R17: score=4; day=14; state=restored.
- R18: score=5; day=26; state=unavailable.
- R19: score=2; day=27; state=unavailable.
- R20: score=2; day=5; state=degraded.
- R21: score=5; day=15; state=degraded.
- R22: score=1; day=17; state=unavailable.
- R23: score=5; day=7; state=restored.
- R24: score=3; day=8; state=unavailable.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>

<details><summary><strong>operations-48</strong> — 48 records; expected <code>{&quot;answer&quot;: [&quot;R01&quot;, &quot;R24&quot;, &quot;R30&quot;, &quot;R45&quot;, &quot;R47&quot;]}</code></summary>

<details><summary>Full prose — 1287 input tokens</summary>

<pre><code>Review every service interruption report. A service interruption report qualifies only when all three rules hold:
1. Its impact severity is at least 3.
2. Its recovery deadline is day 15 or earlier.
3. Its restoration status is exactly &quot;unavailable&quot;.

Records:
- R01 — impact severity: 5; recovery deadline: day 1; restoration status: unavailable.
- R02 — impact severity: 1; recovery deadline: day 30; restoration status: degraded.
- R03 — impact severity: 5; recovery deadline: day 28; restoration status: degraded.
- R04 — impact severity: 1; recovery deadline: day 26; restoration status: unavailable.
- R05 — impact severity: 3; recovery deadline: day 12; restoration status: degraded.
- R06 — impact severity: 2; recovery deadline: day 4; restoration status: degraded.
- R07 — impact severity: 1; recovery deadline: day 11; restoration status: degraded.
- R08 — impact severity: 2; recovery deadline: day 12; restoration status: degraded.
- R09 — impact severity: 2; recovery deadline: day 23; restoration status: unavailable.
- R10 — impact severity: 1; recovery deadline: day 25; restoration status: unavailable.
- R11 — impact severity: 4; recovery deadline: day 23; restoration status: unavailable.
- R12 — impact severity: 1; recovery deadline: day 1; restoration status: degraded.
- R13 — impact severity: 4; recovery deadline: day 15; restoration status: restored.
- R14 — impact severity: 4; recovery deadline: day 9; restoration status: restored.
- R15 — impact severity: 4; recovery deadline: day 16; restoration status: restored.
- R16 — impact severity: 2; recovery deadline: day 20; restoration status: unavailable.
- R17 — impact severity: 5; recovery deadline: day 26; restoration status: unavailable.
- R18 — impact severity: 5; recovery deadline: day 20; restoration status: unavailable.
- R19 — impact severity: 4; recovery deadline: day 23; restoration status: restored.
- R20 — impact severity: 4; recovery deadline: day 26; restoration status: restored.
- R21 — impact severity: 4; recovery deadline: day 21; restoration status: restored.
- R22 — impact severity: 1; recovery deadline: day 3; restoration status: restored.
- R23 — impact severity: 1; recovery deadline: day 19; restoration status: restored.
- R24 — impact severity: 3; recovery deadline: day 14; restoration status: unavailable.
- R25 — impact severity: 3; recovery deadline: day 27; restoration status: degraded.
- R26 — impact severity: 1; recovery deadline: day 21; restoration status: unavailable.
- R27 — impact severity: 2; recovery deadline: day 30; restoration status: degraded.
- R28 — impact severity: 2; recovery deadline: day 4; restoration status: degraded.
- R29 — impact severity: 3; recovery deadline: day 20; restoration status: restored.
- R30 — impact severity: 3; recovery deadline: day 15; restoration status: unavailable.
- R31 — impact severity: 1; recovery deadline: day 14; restoration status: restored.
- R32 — impact severity: 2; recovery deadline: day 10; restoration status: degraded.
- R33 — impact severity: 4; recovery deadline: day 4; restoration status: restored.
- R34 — impact severity: 5; recovery deadline: day 8; restoration status: degraded.
- R35 — impact severity: 2; recovery deadline: day 13; restoration status: restored.
- R36 — impact severity: 3; recovery deadline: day 19; restoration status: unavailable.
- R37 — impact severity: 2; recovery deadline: day 21; restoration status: restored.
- R38 — impact severity: 4; recovery deadline: day 22; restoration status: restored.
- R39 — impact severity: 1; recovery deadline: day 20; restoration status: degraded.
- R40 — impact severity: 1; recovery deadline: day 19; restoration status: degraded.
- R41 — impact severity: 5; recovery deadline: day 10; restoration status: restored.
- R42 — impact severity: 5; recovery deadline: day 8; restoration status: restored.
- R43 — impact severity: 5; recovery deadline: day 17; restoration status: restored.
- R44 — impact severity: 2; recovery deadline: day 5; restoration status: degraded.
- R45 — impact severity: 3; recovery deadline: day 5; restoration status: unavailable.
- R46 — impact severity: 2; recovery deadline: day 23; restoration status: restored.
- R47 — impact severity: 5; recovery deadline: day 11; restoration status: unavailable.
- R48 — impact severity: 2; recovery deadline: day 16; restoration status: restored.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Defined abbreviations — 1166 input tokens</summary>

<pre><code>Abbreviation legend:
- SIR = service interruption report
- IS = impact severity
- RD = recovery deadline
- RS = restoration status

Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 3.
2. Its RD is day 15 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 5; RD: day 28; RS: degraded.
- R04 — IS: 1; RD: day 26; RS: unavailable.
- R05 — IS: 3; RD: day 12; RS: degraded.
- R06 — IS: 2; RD: day 4; RS: degraded.
- R07 — IS: 1; RD: day 11; RS: degraded.
- R08 — IS: 2; RD: day 12; RS: degraded.
- R09 — IS: 2; RD: day 23; RS: unavailable.
- R10 — IS: 1; RD: day 25; RS: unavailable.
- R11 — IS: 4; RD: day 23; RS: unavailable.
- R12 — IS: 1; RD: day 1; RS: degraded.
- R13 — IS: 4; RD: day 15; RS: restored.
- R14 — IS: 4; RD: day 9; RS: restored.
- R15 — IS: 4; RD: day 16; RS: restored.
- R16 — IS: 2; RD: day 20; RS: unavailable.
- R17 — IS: 5; RD: day 26; RS: unavailable.
- R18 — IS: 5; RD: day 20; RS: unavailable.
- R19 — IS: 4; RD: day 23; RS: restored.
- R20 — IS: 4; RD: day 26; RS: restored.
- R21 — IS: 4; RD: day 21; RS: restored.
- R22 — IS: 1; RD: day 3; RS: restored.
- R23 — IS: 1; RD: day 19; RS: restored.
- R24 — IS: 3; RD: day 14; RS: unavailable.
- R25 — IS: 3; RD: day 27; RS: degraded.
- R26 — IS: 1; RD: day 21; RS: unavailable.
- R27 — IS: 2; RD: day 30; RS: degraded.
- R28 — IS: 2; RD: day 4; RS: degraded.
- R29 — IS: 3; RD: day 20; RS: restored.
- R30 — IS: 3; RD: day 15; RS: unavailable.
- R31 — IS: 1; RD: day 14; RS: restored.
- R32 — IS: 2; RD: day 10; RS: degraded.
- R33 — IS: 4; RD: day 4; RS: restored.
- R34 — IS: 5; RD: day 8; RS: degraded.
- R35 — IS: 2; RD: day 13; RS: restored.
- R36 — IS: 3; RD: day 19; RS: unavailable.
- R37 — IS: 2; RD: day 21; RS: restored.
- R38 — IS: 4; RD: day 22; RS: restored.
- R39 — IS: 1; RD: day 20; RS: degraded.
- R40 — IS: 1; RD: day 19; RS: degraded.
- R41 — IS: 5; RD: day 10; RS: restored.
- R42 — IS: 5; RD: day 8; RS: restored.
- R43 — IS: 5; RD: day 17; RS: restored.
- R44 — IS: 2; RD: day 5; RS: degraded.
- R45 — IS: 3; RD: day 5; RS: unavailable.
- R46 — IS: 2; RD: day 23; RS: restored.
- R47 — IS: 5; RD: day 11; RS: unavailable.
- R48 — IS: 2; RD: day 16; RS: restored.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Undefined abbreviations — 1136 input tokens</summary>

<pre><code>Review every SIR. A SIR qualifies only when all three rules hold:
1. Its IS is at least 3.
2. Its RD is day 15 or earlier.
3. Its RS is exactly &quot;unavailable&quot;.

Records:
- R01 — IS: 5; RD: day 1; RS: unavailable.
- R02 — IS: 1; RD: day 30; RS: degraded.
- R03 — IS: 5; RD: day 28; RS: degraded.
- R04 — IS: 1; RD: day 26; RS: unavailable.
- R05 — IS: 3; RD: day 12; RS: degraded.
- R06 — IS: 2; RD: day 4; RS: degraded.
- R07 — IS: 1; RD: day 11; RS: degraded.
- R08 — IS: 2; RD: day 12; RS: degraded.
- R09 — IS: 2; RD: day 23; RS: unavailable.
- R10 — IS: 1; RD: day 25; RS: unavailable.
- R11 — IS: 4; RD: day 23; RS: unavailable.
- R12 — IS: 1; RD: day 1; RS: degraded.
- R13 — IS: 4; RD: day 15; RS: restored.
- R14 — IS: 4; RD: day 9; RS: restored.
- R15 — IS: 4; RD: day 16; RS: restored.
- R16 — IS: 2; RD: day 20; RS: unavailable.
- R17 — IS: 5; RD: day 26; RS: unavailable.
- R18 — IS: 5; RD: day 20; RS: unavailable.
- R19 — IS: 4; RD: day 23; RS: restored.
- R20 — IS: 4; RD: day 26; RS: restored.
- R21 — IS: 4; RD: day 21; RS: restored.
- R22 — IS: 1; RD: day 3; RS: restored.
- R23 — IS: 1; RD: day 19; RS: restored.
- R24 — IS: 3; RD: day 14; RS: unavailable.
- R25 — IS: 3; RD: day 27; RS: degraded.
- R26 — IS: 1; RD: day 21; RS: unavailable.
- R27 — IS: 2; RD: day 30; RS: degraded.
- R28 — IS: 2; RD: day 4; RS: degraded.
- R29 — IS: 3; RD: day 20; RS: restored.
- R30 — IS: 3; RD: day 15; RS: unavailable.
- R31 — IS: 1; RD: day 14; RS: restored.
- R32 — IS: 2; RD: day 10; RS: degraded.
- R33 — IS: 4; RD: day 4; RS: restored.
- R34 — IS: 5; RD: day 8; RS: degraded.
- R35 — IS: 2; RD: day 13; RS: restored.
- R36 — IS: 3; RD: day 19; RS: unavailable.
- R37 — IS: 2; RD: day 21; RS: restored.
- R38 — IS: 4; RD: day 22; RS: restored.
- R39 — IS: 1; RD: day 20; RS: degraded.
- R40 — IS: 1; RD: day 19; RS: degraded.
- R41 — IS: 5; RD: day 10; RS: restored.
- R42 — IS: 5; RD: day 8; RS: restored.
- R43 — IS: 5; RD: day 17; RS: restored.
- R44 — IS: 2; RD: day 5; RS: degraded.
- R45 — IS: 3; RD: day 5; RS: unavailable.
- R46 — IS: 2; RD: day 23; RS: restored.
- R47 — IS: 5; RD: day 11; RS: unavailable.
- R48 — IS: 2; RD: day 16; RS: restored.

Return only a JSON object of the form {&quot;answer&quot;: [&quot;R01&quot;, &quot;R02&quot;]}.
The answer must contain every qualifying record ID in ascending order and no others.</code></pre>

</details>

<details><summary>Concise language — 980 input tokens</summary>

<pre><code>Select every record satisfying all conditions:
score &gt;= 3; day &lt;= 15; state = &quot;unavailable&quot;.

Records:
- R01: score=5; day=1; state=unavailable.
- R02: score=1; day=30; state=degraded.
- R03: score=5; day=28; state=degraded.
- R04: score=1; day=26; state=unavailable.
- R05: score=3; day=12; state=degraded.
- R06: score=2; day=4; state=degraded.
- R07: score=1; day=11; state=degraded.
- R08: score=2; day=12; state=degraded.
- R09: score=2; day=23; state=unavailable.
- R10: score=1; day=25; state=unavailable.
- R11: score=4; day=23; state=unavailable.
- R12: score=1; day=1; state=degraded.
- R13: score=4; day=15; state=restored.
- R14: score=4; day=9; state=restored.
- R15: score=4; day=16; state=restored.
- R16: score=2; day=20; state=unavailable.
- R17: score=5; day=26; state=unavailable.
- R18: score=5; day=20; state=unavailable.
- R19: score=4; day=23; state=restored.
- R20: score=4; day=26; state=restored.
- R21: score=4; day=21; state=restored.
- R22: score=1; day=3; state=restored.
- R23: score=1; day=19; state=restored.
- R24: score=3; day=14; state=unavailable.
- R25: score=3; day=27; state=degraded.
- R26: score=1; day=21; state=unavailable.
- R27: score=2; day=30; state=degraded.
- R28: score=2; day=4; state=degraded.
- R29: score=3; day=20; state=restored.
- R30: score=3; day=15; state=unavailable.
- R31: score=1; day=14; state=restored.
- R32: score=2; day=10; state=degraded.
- R33: score=4; day=4; state=restored.
- R34: score=5; day=8; state=degraded.
- R35: score=2; day=13; state=restored.
- R36: score=3; day=19; state=unavailable.
- R37: score=2; day=21; state=restored.
- R38: score=4; day=22; state=restored.
- R39: score=1; day=20; state=degraded.
- R40: score=1; day=19; state=degraded.
- R41: score=5; day=10; state=restored.
- R42: score=5; day=8; state=restored.
- R43: score=5; day=17; state=restored.
- R44: score=2; day=5; state=degraded.
- R45: score=3; day=5; state=unavailable.
- R46: score=2; day=23; state=restored.
- R47: score=5; day=11; state=unavailable.
- R48: score=2; day=16; state=restored.

Return only {&quot;answer&quot;: [record IDs]} with qualifying IDs in ascending order.</code></pre>

</details>

</details>
