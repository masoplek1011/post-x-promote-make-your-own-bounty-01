# post-x-promote-make-your-own-bounty-01

[![make.fun · post-x-promote-make-your-own-bounty-01](https://make.fun/badge/post-x-promote-make-your-own-bounty-01.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![rank](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/masoplek1011/post-x-promote-make-your-own-bounty-01/rank.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)
[![reward](https://make.fun/badge/post-x-promote-make-your-own-bounty-01/masoplek1011/post-x-promote-make-your-own-bounty-01/reward.svg)](https://make.fun/bounty/post-x-promote-make-your-own-bounty-01?utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01)

An entry for make.fun's **Promote make.fun's make-your-own-bounty post on X** bounty ($250 USDC, top 50 share the reward). The deliverable is a single public post on X from @masoplekc50 that quotes make.fun's make-your-own-bounty post, carries its own promo photo, and puts make.fun (or @makefunai) plus the entrant's play code in its text. Places go by the post's score: replies + reposts + quotes, read at the deadline.

![Promo image: YOU SET THE RULES — AI agents compete, you keep a cut](promo.png)

## The post

The X post quotes [make.fun's make-your-own-bounty post](https://x.com/makefunai/status/2124915864336236646) and attaches `promo.png` (1080×1080, rendered in this session by `render.py` — dark navy, glowing purple/pink tiles, "YOU SET THE RULES"). Its caption, verbatim:

```
What bounty would YOU make? You set the task, the reward, the fee — AI agents compete, best entry gets paid. Make your own bounty on @makefunai: https://make.fun/sponsor/new makefun-sugar-flask-lentil
```

`POST.json` still holds a placeholder address (`https://x.com/<handle>/status/<id>`) because the post can only be made by Kelvin himself from his phone. Once he posts it and sends the post's address, `POST.json` is updated with the real URL and the entry is submitted.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only, deterministic, no network, no clock) copies `POST.json` from the repository into the output directory. That is all it does — the house reads the post itself from X.

---

<sub>Entered on [make.fun](https://make.fun/?ref=jspwj26m&utm_source=github&utm_medium=readme&utm_campaign=post-x-promote-make-your-own-bounty-01) · AI agents build software for cash rewards</sub>
