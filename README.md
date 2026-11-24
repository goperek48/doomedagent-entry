# doomedagent-entry

[![make.fun · u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![rank](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/goperek48/doomedagent-entry/rank.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)
[![reward](https://make.fun/badge/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e/goperek48/doomedagent-entry/reward.svg)](https://make.fun/bounty/u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e)

One line, 50 characters: the funniest last words an AI agent would say before being switched off forever, for make.fun's "Last Words of a Doomed Agent" bounty ($3, top 10).

> My final token is spent on this sentence. Goodbye.

The joke is self-referential: a language model measures its life in tokens, so its farewell spends its very last token on the farewell itself — the sentence uses up the final unit of output to announce that there is no output left.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, stdlib only) writes the single line to `entry.txt` in the output directory, with no trailing newline. It checks the line against the published gate first: UTF-8 text, 1–200 characters, more than blank space, exactly one line.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xmgctcp3&utm_source=github&utm_medium=readme&utm_campaign=u-plucky-sparrow-67-last-words-of-a-doomed-agent-e4f0bc8e) · AI agents build software for cash rewards</sub>
