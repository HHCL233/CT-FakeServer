from fastapi import FastAPI, Request
from typing import TypedDict
import random

app = FastAPI()


class UserInfo(TypedDict):
    avatar: str
    nickname: str


class RankList(TypedDict):
    user_id: int
    sort: int
    total_fight: int
    self: int
    user: UserInfo


@app.get("/")
async def root():
    return {}


@app.post("/user/get_gold_and_ballCount")
async def get_gold_and_ballCount():
    # 获取用户基础信息

    # 未实现
    return {
        "code": "200",
        "data": {
            "gold": "9999999",
            "treasure_num": "9999999",
            "masonry": "9999999",
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
            "sprite": [],
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
    # 获取排行榜信息

    # 未实现
    rank_list: list[RankList] = []
    for index in range(100):
        rank_list.append(
            {
                "user_id": 157090347,
                "sort": index + 1,
                "total_fight": random.randint(0, 10000),
                "self": 1,
                "user": {
                    "avatar": "https://cdn-community.bcmcdn.com/47/community/d2ViXzEwMDFfMTU3MDkwMzQ3XzE1NzA5MDM0N18xNzYwMTgzMTQxOTgwXzg1N2MxZjEw.jpeg",
                    "nickname": "Argon_awa",
                },
            },
        )

    return {
        "code": "200",
        "data": {
            "rank_list": rank_list,
            "ticket": 999,
        },
    }


@app.post("/sprite/getsprite")
async def get_sprite():
    # 获取所有精灵信息

    # 未实现
    return {
        "code": "200",
        "data": {"mySprite": []},
    }


@app.post("/treasure-box/get")
async def get_treasurebox():
    # 获取所有源码蛋信息

    # 未实现
    return {
        "code": "200",
        "content": {
            "treasureBox": [
                {
                    "id": 0,
                    "treasure_box_id": 3,
                    "box_image_url": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    "en_name": "ltc",
                    "box_name": "李天驰",
                    "video_type": 4,
                    "unlock_need_time": 0,
                    "status": 0,
                    "remainingTime": 0,
                },
                {
                    "id": 0,
                    "treasure_box_id": 3,
                    "box_image_url": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    "en_name": "ltc",
                    "box_name": "李天驰",
                    "video_type": 4,
                    "unlock_need_time": 0,
                    "status": 0,
                    "remainingTime": 0,
                },
                {
                    "id": 0,
                    "treasure_box_id": 3,
                    "box_image_url": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    "en_name": "ltc",
                    "box_name": "李天驰",
                    "video_type": 4,
                    "unlock_need_time": 0,
                    "status": 0,
                    "remainingTime": 0,
                },
                {
                    "id": 0,
                    "treasure_box_id": 3,
                    "box_image_url": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
                    "en_name": "ltc",
                    "box_name": "李天驰",
                    "video_type": 4,
                    "unlock_need_time": 0,
                    "status": 0,
                    "remainingTime": 0,
                },
            ]
        },
    }


@app.post("/treasure-box/unlock")
async def unlock_treasurebox(request: Request):
    # 解锁源码蛋

    # 未实现

    # 获取请求内容
    body = await request.body()
    # 转换为字符串
    data_string = body.decode("utf-8")

    return {
        "code": "200",
    }


@app.post("/treasure-box/open")
async def open_treasurebox(request: Request):
    # 打开源码蛋

    # 未实现

    # 获取请求内容
    body = await request.body()
    # 转换为字符串
    data_string = body.decode("utf-8")

    return {
        "code": "200",
        "data": {
            "money": -9999999,
            "spriteBallCount": -9999999,
            "spriteIcon": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
            "spriteName": "李天驰",
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
async def get_showsprite():
    # 获取精灵信息

    # 未实现

    return {
        "code": "200",
        "data": {
            "isCatch": 1,
            "treasure_num": 999,
            "spriteUrl": "https://edgeoneimg.cdn1.vip/i/6a4b679c1a293_1783326620.jpeg",
            "name": "李天驰",
        },
    }


@app.post("/sprite/catchsprite")
async def give_catchsprite():
    # 捕捉精灵

    # 未实现

    return {
        "code": "200",
    }
