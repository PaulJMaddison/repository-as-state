# Validation audit — hostile-review candidate

Validated manuscript tree before publication to the audit branch:

- canonical paper base: `758e771b5e983873a48f4ef6a277846bcbeeccfb`
- hostile-audit manuscript candidate tree: `bae45e49cc770384931aedb18d4c367d05bf7034`
- P0 executed: **false**

## Repository state and diff

GitHub tree/diff audit found:

- 21 manuscript section inputs;
- all section/table/figure input paths present;
- no unmatched LaTeX environments in the audited manuscript/figure/table sources;
- no duplicate labels found in the source-level label audit;
- approximate manuscript word count: **10.3k** excluding bibliography/supporting Markdown;
- 24 bibliography entries after literature expansion;
- every bibliography entry is used by the manuscript;
- no KynticAI, Fortress or Very Group material in the audit diff;
- no credential/private-key pattern in the audit diff;
- no positive empirical-result phrasing detected by the audit scan;
- P0 remains explicitly unexecuted.

The literal string `TODO` found in the diff is the legitimate methodological phrase `changelogs/TODOs` in the task-leakage checklist, not unfinished manuscript work.

The old KL-divergence equation appears only on deleted diff lines; it is absent from the revised repository-sufficiency formulation.

## Repository tests

The research metric source and tests were fetched by exact Git blob SHA from the audited repository state and materialised in an isolated local validation directory.

Command:

    cd /mnt/data/ras-audit-tests && PYTHONPATH=src pytest -q

Outcome:

    ...............                                                          [100%]
    15 passed in 0.03s

The audit did not modify research metric source or tests.

## LaTeX environment

Commands and outcomes:

    command -v pdflatex
    /usr/bin/pdflatex

    command -v latexmk
    /usr/bin/latexmk

The `bibtex` command name is broken in this environment:

    /usr/bin/bibtex -> /etc/alternatives/bibtex

with the alternative target missing. The actual binary remains available as:

    /usr/bin/bibtex.original --version

Outcome begins:

    BibTeX 0.99d (TeX Live 2025/dev/Debian)

## Full PDF compilation status

A complete PDF build was **not executed successfully in this environment** because the GitHub repository cannot be materialised into the shell runtime.

Attempted command:

    git clone --no-checkout https://github.com/PaulJMaddison/repository-as-state.git /mnt/data/ras-audit-check

Outcome:

    fatal: unable to access 'https://github.com/PaulJMaddison/repository-as-state.git/':
    Could not resolve host: github.com

The GitHub connector can read/write repository content but does not expose a repository archive into the shell filesystem. Therefore claiming a successful `pdflatex/bibtex` build here would be false.

Source-level LaTeX validation was completed through the exact Git tree/objects. A full compilation should be rerun in a normal clone with:

    cd paper
    pdflatex main.tex
    /usr/bin/bibtex.original main
    pdflatex main.tex
    pdflatex main.tex

or with a functioning `bibtex` alternative:

    latexmk -pdf main.tex

## Literature verification

Primary/first-party sources checked during the audit include:

- SWE-agent;
- OpenHands / OpenHands SDK;
- SWE-STEPS;
- Handoff Debt;
- Why Git Is the Memory Solution for the Agentic Development Lifecycle;
- Improving Code Localization with Repository Memory;
- Learning to Commit;
- Evaluating AGENTS.md;
- Do Context Files Help Coding Agents?;
- Cost-Effective Repository Exploration for Agentic Issue Localization;
- Durable Functions;
- BEGIN AI TRANSACTION;
- RouteLLM;
- PagedAttention/vLLM;
- DistServe;
- Mooncake;
- Cursor Continuity / Git at any scale;
- current agent-memory/context-engineering sources already in the bibliography.

## Validation conclusion

Source integrity and repository tests are suitable for publishing the hostile-audit branch.

**Compilation caveat remains open solely because the validation shell cannot materialise the GitHub repository. It is not recorded as a successful PDF build.**
