from fastapi import FastAPI, Request, Cookie
from typing import TypedDict, Annotated
import random


class UserInfo(TypedDict):
    avatar: str
    nickname: str


class RankList(TypedDict):
    user_id: int
    sort: int
    total_fight: int
    self: int
    user: UserInfo


class TreasureBox(TypedDict):
    id: int
    treasure_box_id: int
    box_image_url: str
    en_name: str
    box_name: str
    video_type: int
    unlock_need_time: int
    status: int
    remainingTime: int


class UserData(TypedDict):
    gold: int
    masonry: int
    # 精灵存储结构暂未明确
    my_sprite: None
    treasurebox: list[TreasureBox]
    sprite_ball_count: int


users_data: dict[str, UserData] = {}

app = FastAPI()


def new_treasure(
    length: int,
    name: str,
    en_name: str,
    image_url: str,
    treasure_box_id: int,
    unlock_need_time: int,
    authorization: str,
    video_type: int = 1,
):
    treasurebox: list[TreasureBox] = []
    for _index in range(length):
        treasurebox.append(
            {
                "id": 0,
                "treasure_box_id": treasure_box_id,
                "box_image_url": image_url,
                "en_name": en_name,
                "box_name": name,
                "video_type": video_type,
                "unlock_need_time": unlock_need_time,
                "status": 0,
                "remainingTime": unlock_need_time,
            }
        )
    users_data[authorization]["treasurebox"] += treasurebox
    return treasurebox


@app.get("/")
async def root():
    return {}


@app.post("/user/get_gold_and_ballCount")
async def get_gold_and_ballCount(authorization: Annotated[str, Cookie()]):
    # 获取用户基础信息

    if authorization not in users_data.keys():
        print("[日志] 新用户注册")
        users_data[authorization] = {
            "gold": 0,
            "masonry": 0,
            "my_sprite": None,
            "treasurebox": [],
            "sprite_ball_count": 999,
        }

    # 未实现
    return {
        "code": "200",
        "data": {
            "gold": users_data[authorization]["gold"],
            "treasure_num": users_data[authorization]["sprite_ball_count"],
            "masonry": users_data[authorization]["masonry"],
        },
    }


@app.post("/store/ar_store")
async def ar_store():
    # 获取商店所有内容信息

    # 未实现
    return {
        "code": "200",
        "message": "success",
        "data": {
            "sprite": [
                {
                    # 英文简介(type == 0)
                    "en_description": "ltc!",
                    # 简介(type == 0)
                    "description": "占位符!",
                    # 星数(type == 0)
                    "star": 1,
                    # 预览图片(type == 0)
                    "preview": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # 显示图片(type == 2)
                    "box_image_url": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # id(1-3)
                    "id": 3,
                    # 类型(type = 1时使用)
                    "type": 1,
                    # 名称
                    "name": "占位符",
                    # 英文名称
                    "en_name": "ltc",
                    # 需要金币(type == 0)
                    "need_gold": 2015,
                    # 需要金币(type == 1)
                    "gold": 12,
                    # 数量(type == 1)
                    "num": 2,
                    # 需要红宝石(type == 2)
                    "need_masonry": 8,
                }
            ],
            "spriteBall": [],
            "treasureBox": [],
        },
    }


@app.get("/check-version")
async def check_version(local_version: str = "2.0.2"):
    # 检查客户端版本

    return {
        "code": "200",
        "data": {"is_last": True, "must_update": False},
    }


@app.get("/rank")
async def get_rank():
    # 获取排行榜信息和挑战券数量

    # 未实现
    rank_list: list[RankList] = []
    for index in range(100):
        rank_list.append(
            {
                "user_id": 157090347,
                "sort": index + 1,
                "total_fight": random.randint(0, 10000),
                "self": 0,
                "user": {
                    "avatar": "https://cdn-community.bcmcdn.com/47/community/d2ViXzEwMDFfMTU3MDkwMzQ3XzE1NzA5MDM0N18xNzYwMTgzMTQxOTgwXzg1N2MxZjEw.jpeg",
                    "nickname": "Argon_awa",
                },
            },
        )
    rank_list.append(
        {
            "user_id": 0,
            "sort": 101,
            "total_fight": random.randint(0, 10000),
            "self": 1,
            "user": {
                "avatar": "",
                "nickname": "自己",
            },
        },
    )

    return {
        "code": "200",
        "data": {
            "rank_list": rank_list,
            "ticket": 99,
        },
    }


@app.post("/sprite/getsprite")
async def get_sprite():
    # 获取所有精灵信息

    # 未实现
    return {
        "code": "200",
        "data": {
            "mySprite": [
                {
                    # 等级
                    "spriteLevel": 1,
                    # 战斗力
                    "fight": 0,
                    # 血量
                    "hp": 0,
                    # 普攻伤害
                    "atk": 0,
                    # 特攻伤害
                    "sp_atk": 0,
                    # 类别
                    "faction_name": "地",
                    # 用户ID
                    "user_id": 1,
                    # 英文名
                    "en_name": "ltc",
                    # 中文名
                    "name": "占位符",
                    # 英文简介
                    "en_description": "Dog",
                    # 中文简介
                    "description": "大狗大狗叫叫叫",
                    # 英文技能1介绍
                    "en_skill_1": "prosperous",
                    # 中文技能1介绍
                    "skill_1": "狗叫",
                    # 英文技能2介绍
                    "en_skill_2": "prosperous",
                    # 中文技能2介绍
                    "skill_2": "狗叫",
                    # 星数
                    "star": 1,
                    # 卡片预览图片(在id对应图片时使用本体内图片,否则使用preview)
                    "preview": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # id(在id对应图片时使用本体内图片,否则使用preview)
                    "id": 1,
                    # 当前升级素材数量
                    "num": 0,
                    # 升级等级所需升级素材数量
                    "upgradeCount": 100,
                    # 卡片图片
                    "image": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # 速度
                    "speed": 0,
                    # 防御
                    "def": 0,
                    # 特防
                    "sp_def": 0,
                    # 血量一次升级提升
                    "hp_up": 0,
                    # 普攻一次升级提升
                    "atk_up": 0,
                    # 特攻一次升级提升
                    "sp_atk_up": 0,
                    # 编号
                    "NO": 64,
                    # 能否攻击(?)
                    "can_atk": 1,
                },
                {
                    # 等级
                    "spriteLevel": 1,
                    # 战斗力
                    "fight": 67,
                    # 血量
                    "hp": 0,
                    # 普攻伤害
                    "atk": 0,
                    # 特攻伤害
                    "sp_atk": 0,
                    # 类别
                    "faction_name": "普通",
                    # 用户ID
                    "user_id": 1,
                    # 英文名
                    "en_name": "ltc",
                    # 中文名
                    "name": "占位符1",
                    # 英文简介
                    "en_description": "Dog",
                    # 中文简介
                    "description": "大狗大狗叫叫叫",
                    # 英文技能1介绍
                    "en_skill_1": "prosperous",
                    # 中文技能1介绍
                    "skill_1": "狗叫",
                    # 英文技能2介绍
                    "en_skill_2": "prosperous",
                    # 中文技能2介绍
                    "skill_2": "狗叫",
                    # 星数
                    "star": 1,
                    # 卡片预览图片(在id对应图片时使用本体内图片,否则使用preview)
                    "preview": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # id(在id对应图片时使用本体内图片,否则使用preview)
                    "id": 3,
                    # 当前升级素材数量
                    "num": 0,
                    # 升级等级所需升级素材数量
                    "upgradeCount": 0,
                    # 卡片图片
                    "image": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # 速度
                    "speed": 0,
                    # 防御
                    "def": 0,
                    # 特防
                    "sp_def": 0,
                    # 血量一次升级提升
                    "hp_up": 0,
                    # 普攻一次升级提升
                    "atk_up": 0,
                    # 特攻一次升级提升
                    "sp_atk_up": 0,
                    # 编号
                    "NO": 65,
                    # 能否攻击(?)
                    "can_atk": 1,
                },
                {
                    # 等级
                    "spriteLevel": 1,
                    # 战斗力
                    "fight": 0,
                    # 血量
                    "hp": 0,
                    # 普攻伤害
                    "atk": 0,
                    # 特攻伤害
                    "sp_atk": 0,
                    # 类别
                    "faction_name": "水",
                    # 用户ID
                    "user_id": 1,
                    # 英文名
                    "en_name": "ltc",
                    # 中文名
                    "name": "占位符2",
                    # 英文简介
                    "en_description": "Dog",
                    # 中文简介
                    "description": "大狗大狗叫叫叫",
                    # 英文技能1介绍
                    "en_skill_1": "prosperous",
                    # 中文技能1介绍
                    "skill_1": "狗叫",
                    # 英文技能2介绍
                    "en_skill_2": "prosperous",
                    # 中文技能2介绍
                    "skill_2": "狗叫",
                    # 星数
                    "star": 1,
                    # 卡片预览图片(在id对应图片时使用本体内图片,否则使用preview)
                    "preview": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # id(在id对应图片时使用本体内图片,否则使用preview)
                    "id": 2,
                    # 当前升级素材数量
                    "num": 0,
                    # 升级等级所需升级素材数量
                    "upgradeCount": 0,
                    # 卡片图片
                    "image": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    # 速度
                    "speed": 0,
                    # 防御
                    "def": 0,
                    # 特防
                    "sp_def": 0,
                    # 血量一次升级提升
                    "hp_up": 0,
                    # 普攻一次升级提升
                    "atk_up": 0,
                    # 特攻一次升级提升
                    "sp_atk_up": 0,
                    # 编号
                    "NO": 66,
                    # 能否攻击(若设置为0则无法在编队页面显示)
                    "can_atk": 1,
                },
            ]
        },
    }


@app.post("/treasure-box/get")
async def get_treasurebox(authorization: Annotated[str, Cookie()]):
    # 获取所有源码蛋信息

    # 未实现
    return {
        "code": "200",
        "content": {"treasureBox": users_data[authorization]["treasurebox"]},
    }


@app.post("/treasure-box/unlock")
async def unlock_treasurebox(request: Request):
    # 解锁源码蛋

    # 未实现

    # 获取请求内容
    body = await request.body()
    # 转换为字符串
    _data_string = body.decode("utf-8")

    return {
        "code": "200",
    }


@app.post("/treasure-box/open")
async def open_treasurebox(request: Request, authorization: Annotated[str, Cookie()]):
    # 打开源码蛋

    # 获取请求内容
    body = await request.body()
    # 转换为字符串
    _data_string = body.decode("utf-8")

    # 添加钱币和精灵球数量
    add_money = random.randint(10, 25)
    add_ball = random.randint(10, 25)
    users_data[authorization]["gold"] += add_money
    users_data[authorization]["sprite_ball_count"] += add_ball

    return {
        "code": "200",
        "data": {
            "money": add_money,
            "spriteBallCount": add_ball,
            "spriteIcon": "",
            "spriteName": "暂不支持",
        },
    }


@app.get("/sprite/team/my")
async def get_my_tem():
    # 获取战队信息

    # 未实现

    return {
        "code": "200",
        "data": {
            "sprite_list": [],
            "total_fight": 9421,
        },
    }


@app.post("/sprite/showsprite")
async def get_showsprite(authorization: Annotated[str, Cookie()]):
    # 获取本次捕捉精灵信息

    return {
        "code": "200",
        "data": {
            "isCatch": 1,
            "treasure_num": users_data[authorization]["sprite_ball_count"],
            "spriteUrl": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
            "name": "占位符",
        },
    }


@app.post("/sprite/catchsprite")
async def give_catchsprite(authorization: Annotated[str, Cookie()]):
    # 捕捉精灵

    users_data[authorization]["sprite_ball_count"] -= 1
    new_treasure(
        1,
        "占位符",
        "ltc",
        "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
        3,
        0,
        authorization,
    )

    return {
        "code": "200",
    }


@app.get("/rank/enemy/info/{id}")
async def get_rank_enemy_info(authorization: Annotated[str, Cookie()], id: int = 0):
    # 获取对应用户精灵

    # 暂未实现

    return {
        "code": "200",
        "message": "success",
        "data": {
            "fight_sign": "dda",
            "enemy_sprites": [
                {
                    "level": 1,
                    "sprite_id": 64,
                    "fight": 67,
                    "hp": 999,
                    "atk": 183,
                    "sp_atk": 291,
                    "faction_name": "地",
                    "user_id": id,
                    "en_name": "ltc",
                    "name": "占位符",
                },
                {
                    "level": 1,
                    "sprite_id": "64",
                    "fight": 67,
                    "hp": 999,
                    "atk": 183,
                    "sp_atk": 291,
                    "faction_name": "地",
                    "user_id": id,
                    "en_name": "ltc",
                    "name": "占位符",
                },
                {
                    "level": 1,
                    "sprite_id": "64",
                    "fight": 67,
                    "hp": 999,
                    "atk": 183,
                    "sp_atk": 291,
                    "faction_name": "地",
                    "user_id": id,
                    "en_name": "ltc",
                    "name": "占位符",
                },
            ],
        },
    }


@app.post("/rank/fight/challenge")
async def get_fight_challenge(request: Request):
    # 比赛完成后请求确认

    # 未实现
    # 获取请求内容
    body = await request.body()
    # 转换为字符串
    _data_string = body.decode("utf-8")

    return {"code": 200}
