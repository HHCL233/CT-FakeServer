from fastapi import FastAPI, Request, Cookie
from typing import TypedDict, Annotated, cast
from pydantic import BaseModel, Field
import random
from contextlib import asynccontextmanager
import json


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


# 宝箱对象的类型
class ConfigTreasureBox(TypedDict):
    id: int
    treasureBoxId: int
    boxImageUrl: str
    enName: str
    boxName: str
    videoType: int
    unlockNeedTime: int
    status: int
    remainingTime: int
    addMoney: list[int]
    addBall: list[int]
    spriteIcon: str
    spriteName: str


# 新用户对象的类型
class NewUser(TypedDict):
    printUserCookie: bool
    gold: int
    masonry: int
    spriteBallCount: int
    treasurebox: list[ConfigTreasureBox]


# 精灵展示对象的类型
class ShowSprite(TypedDict):
    spriteUrl: str
    name: str


# 商店商品对象的类型
class ArStoreItem(TypedDict):
    enDescription: str
    description: str
    star: int
    preview: str
    boxImageUrl: str
    id: int
    type: int
    name: str
    enName: str
    needGold: int
    gold: int
    num: int
    needMasonry: int


# 最外层数据类型
class RootData(TypedDict):
    treasureBoxs: list[ConfigTreasureBox]
    newUser: NewUser
    showSprite: ShowSprite
    arStore: list[ArStoreItem]


users_data: dict[str, UserData] = {}
config_data: RootData = cast(RootData, {})


@asynccontextmanager
async def lifespan(app: FastAPI):
    global config_data
    # 初始化
    print("[日志] 开始加载config")

    with open("config.json", "r", encoding="utf-8") as f:
        config_data = json.load(f)

    print("[日志] 加载完成")

    yield
    # 关闭程序

    print("[日志] 正在保存数据")
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4, ensure_ascii=False)

    del config_data

    print("[日志] 保存完成")


app = FastAPI(lifespan=lifespan)


def new_treasure(
    length: int,
    name: str,
    en_name: str,
    image_url: str,
    treasure_box_id: int,
    unlock_need_time: int,
    authorization: str,
    id: int = 64,
    video_type: int = 4,
    remainingTime: int = -1,
    status: int = 1,
):
    # 添加源码蛋
    temp_treasurebox: list[TreasureBox] = []
    for _index in range(length):
        temp_treasurebox.append(
            {
                "id": id,
                "treasure_box_id": treasure_box_id,
                "box_image_url": image_url,
                "en_name": en_name,
                "box_name": name,
                "video_type": video_type,
                "unlock_need_time": unlock_need_time,
                "status": status,
                "remainingTime": unlock_need_time
                if remainingTime == -1
                else remainingTime,
            }
        )
    users_data[authorization]["treasurebox"] += temp_treasurebox
    return temp_treasurebox


@app.get("/")
async def root():
    return {}


@app.post("/user/get_gold_and_ballCount")
async def get_gold_and_ballCount(
    request: Request, authorization: Annotated[str, Cookie()]
):
    # 获取用户基础信息

    if authorization not in users_data.keys():
        print(
            f"[日志] 新用户注册 {authorization if config_data['newUser']['printUserCookie'] else ''}"
        )
        users_data[authorization] = {
            "gold": config_data["newUser"]["gold"],
            "masonry": config_data["newUser"]["masonry"],
            "my_sprite": None,
            "treasurebox": [
                {
                    "id": item["id"],
                    "treasure_box_id": item["treasureBoxId"],
                    "box_image_url": item["boxImageUrl"],
                    "en_name": item["enName"],
                    "box_name": item["boxName"],
                    "video_type": item["videoType"],
                    "unlock_need_time": item["unlockNeedTime"],
                    "status": item["status"],
                    "remainingTime": item["remainingTime"],
                }
                for item in config_data["newUser"].get("treasurebox", [])
            ],
            "sprite_ball_count": config_data["newUser"]["spriteBallCount"],
        }

    return {
        "code": "200",
        "data": {
            "gold": users_data[authorization]["gold"],
            "treasure_num": users_data[authorization]["sprite_ball_count"],
            "masonry": users_data[authorization]["masonry"],
        },
    }


@app.post("/store/ar_store")
async def ar_store(request: Request):
    # 获取商店所有内容信息

    return {
        "code": "200",
        "message": "success",
        "data": {
            "sprite": [
                {
                    # 英文简介(type == 0)
                    "en_description": item["enDescription"],
                    # 简介(type == 0)
                    "description": item["description"],
                    # 星数(type == 0)
                    "star": item["star"],
                    # 预览图片(type == 0)
                    "preview": item["preview"],
                    # 显示图片(type == 2)
                    "box_image_url": item["boxImageUrl"],
                    # id(1-3)(type == 2时使用)
                    "id": item["id"],
                    # 类型
                    "type": item["type"],
                    # 名称
                    "name": item["name"],
                    # 英文名称
                    "en_name": item["enName"],
                    # 需要金币(type == 0)
                    "need_gold": item["needGold"],
                    # 需要金币(type == 1)
                    "gold": item["gold"],
                    # 数量(type == 1)
                    "num": item["num"],
                    # 需要红宝石(type == 2)
                    "need_masonry": item["needMasonry"],
                }
                for item in config_data["arStore"]
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
                    "id": 64,
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
                    "id": 64,
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
                    "id": 64,
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
    # 转换为实际ID
    data_id: str = _data_string.split("=")[1]

    def filter_true_box(treasureBox: ConfigTreasureBox):
        return str(treasureBox["id"]) == data_id

    open_box_list = list(filter(filter_true_box, config_data["treasureBoxs"]))

    if len(open_box_list) != 1:
        return {"code": "400"}

    open_box = open_box_list[0]

    # 添加钱币和精灵球数量
    add_money = random.randint(open_box["addMoney"][0], open_box["addMoney"][1])
    add_ball = random.randint(open_box["addBall"][0], open_box["addBall"][1])
    users_data[authorization]["gold"] += add_money
    users_data[authorization]["sprite_ball_count"] += add_ball

    # 没有实际加入

    return {
        "code": "200",
        "data": {
            "money": add_money,
            "spriteBallCount": add_ball,
            "spriteIcon": open_box["spriteIcon"],
            "spriteName": open_box["spriteName"],
        },
    }


@app.get("/sprite/team/my")
async def get_my_team():
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
async def get_showsprite(request: Request, authorization: Annotated[str, Cookie()]):
    # 获取本次捕捉精灵信息

    return {
        "code": "200",
        "data": {
            "isCatch": random.randint(0, 1),
            "treasure_num": users_data[authorization]["sprite_ball_count"],
            "spriteUrl": config_data["showSprite"]["spriteUrl"],
            "name": config_data["showSprite"]["name"],
        },
    }


@app.post("/sprite/catchsprite")
async def give_catchsprite(authorization: Annotated[str, Cookie()]):
    # 捕捉精灵

    users_data[authorization]["sprite_ball_count"] -= 1
    random_treasure = random.choice(config_data["treasureBoxs"])
    new_treasure(
        1,
        random_treasure["boxName"],
        random_treasure["enName"],
        random_treasure["boxImageUrl"],
        random_treasure["treasureBoxId"],
        random_treasure["unlockNeedTime"],
        authorization,
        random_treasure["id"],
        random_treasure["videoType"],
        random_treasure["remainingTime"],
        random_treasure["status"],
    )
    print(11)

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
