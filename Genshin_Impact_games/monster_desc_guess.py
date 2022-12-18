import asyncio
import os
import random

from hoshino import Service
from hoshino.modules.Genshin_Impact_games import chara
from hoshino.typing import CQEvent, MessageSegment as Seg

from . import _Genshin_Impact_data
from . import GameMaster

desc_DEBUG = False
PREPARE_TIME = 4
ONE_TURN_TIME = 6.5
TURN_NUMBER = 4
DB_PATH = os.path.expanduser("~/.hoshino/Genshin_monster_desc_guess.db")
NOT_USE = []
gm = GameMaster(DB_PATH)
sv = Service("猜原魔", bundle="原神娱乐", help_="""
[原神猜角色] 猜猜bot在描述哪位角色
[原神猜角色排行] 显示小游戏的群排行榜(只显示前十)
""".strip()
             )


@sv.on_fullmatch(("猜原魔排行", "猜原魔排名", "猜原魔排行榜", "猜原魔群排行"))
async def description_guess_group_ranking(bot, ev: CQEvent):
    ranking = gm.db.get_ranking(ev.group_id)
    msg = ["【猜原魔小游戏排行榜】"]
    for i, item in enumerate(ranking):
        uid, count = item
        m = await bot.get_group_member_info(self_id=ev.self_id, group_id=ev.group_id, user_id=uid)
        name = m["card"] or m["nickname"] or str(uid)
        msg.append(f"第{i + 1}名：{name} 猜对{count}次")
    await bot.send(ev, "\n".join(msg))


@sv.on_fullmatch(("猜原魔", "原魔猜角色"))
async def description_guess(bot, ev: CQEvent):
    global desc_DEBUG
    if desc_DEBUG:
        await bot.send(ev, f"此小游戏暂不开放呢\n")
    else:
        if gm.is_playing(ev.group_id):
            await bot.finish(ev, "游戏仍在进行中…")
        with gm.start_game(ev.group_id) as game:
            game.answer = random.choice(list(_Genshin_Impact_data.MONSTER_PROFILE.keys()))
            while game.answer in NOT_USE:
                game.answer = random.choice(list(_Genshin_Impact_data.MONSTER_PROFILE.keys()))
            profile = _Genshin_Impact_data.MONSTER_PROFILE[game.answer]
            kws = list(profile.keys())
            kws.remove('名字')
            random.shuffle(kws)
            await bot.send(ev, f"{PREPARE_TIME}秒后每隔{ONE_TURN_TIME}秒我会给出某位原魔的一个描述，根据这些描述猜猜TA是谁~")
            await asyncio.sleep(PREPARE_TIME)
            for i, k in enumerate(kws):
                await bot.send(ev, f"提示{i + 1}/{len(kws)}:\nTA的{k}是 {profile[k]}")
                await asyncio.sleep(ONE_TURN_TIME)
                if game.winner:
                    return
            c = chara.fromid(game.answer)
        await bot.send(ev, f"正确答案是：{c.name} {c.icon.cqcode}\n")


@sv.on_message()
async def on_input_chara_name(bot, ev: CQEvent):
    game = gm.get_game(ev.group_id)
    if not game or game.winner:
        return
    c = chara.fromname(ev.message.extract_plain_text())
    if c.id != chara.UNKNOWN and c.id == game.answer:
        game.winner = ev.user_id
        n = game.record()
        msg = f"正确答案是：{c.name}{c.icon.cqcode}\n{Seg.at(ev.user_id)}猜对了，不愧来自深渊教团！\n(此轮游戏将在几秒后自动结束，请耐心等待)"
        await bot.send(ev, msg)
