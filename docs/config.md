# 配置文件说明

## treasureBoxs

配置所有源码蛋。

### `id`

- 源码蛋ID。

### `treasureBoxId`

- 源码蛋奖励提示。

- `treasure_box_id == 1` 时奖励提示为 "·包含一只1星或2星源码精灵\n·金币 X 100\n·源码立方 X 5"。

- `treasure_box_id == 2` 时奖励提示为 "·包含一只3星源码精灵\n·金币 X 100\n·源码立方 X 5"。

- `treasure_box_id == 3` 时奖励提示为 "·包含一只4星或5星源码精灵\n·金币 X 300\n·源码立方 X 5"。

- `treasure_box_id`不满足上述条件时奖励提示为 "奖品未知"。

### `boxImageUrl`

- 源码蛋图片链接。

### `enName`和`boxName`

- 源码蛋的英文名称和中文名称。

### `videoType`

- 源码蛋样式。

- `videoType == 1` 时源码蛋样式为蓝色。

- `videoType == 2` 时源码蛋样式为灰色。

- `videoType == 3` 时源码蛋样式为金色。

- `videoType == 4` 时源码蛋样式为紫色。

### `unlockNeedTime`

- 源码蛋解锁总计时间，单位为秒。

### `status`

- 源码蛋状态。

- `status == 1` 时源码蛋解锁需要时间，需要手动点击解锁按钮。

- `status == 2` 时源码蛋解锁需要时间，获得后自动进入解锁。

- `status == 3` 时源码蛋解锁不需要时间，需要手动点击解锁按钮。

### `remainingTime`

- 源码蛋解锁剩余时间，单位为秒。

- 一般情况下建议和`unlock_need_time`保持一致。

### `addMoney`

- 源码蛋解锁后奖励金币数量，在第一和第二个值之间取随机值。

### `addBall`

- 源码蛋解锁后奖励源码立方数量，在第一和第二个值之间取随机值。

### `spriteIcon`

- 源码蛋解锁后奖励精灵图片链接。

### `spriteName`

- 源码蛋解锁后奖励精灵名称。

## newUser

配置新注册用户行为。

### `printUserCookie`

- 新注册用户是否打印Cookie。

### `gold`

- 新注册用户赠送金币数量。

### `gold`

- 新注册用户赠送金币数量。

### `masonry`

- 新注册用户赠送红宝石数量。

### `masonry`

- 新注册用户赠送红宝石数量。

### `spriteBallCount`

- 新注册用户赠送源码立方数量。

### `treasurebox`

- 新注册用户赠送源码蛋信息。

- 参考 [`treasureBoxs`](#treasureboxs)。

## showSprite

- 配置召唤页面新精灵信息。

### `spriteUrl`

- 新精灵图片链接。

### `name`

- 新精灵名称。

## arStore

配置商店物品。

### `enDescription`和`description`

- `type == 0` 时为商店物品的英文名称和中文名称。

### `enName`和`name`

- 商店物品的英文名称和中文名称。

### `star`

- `type == 0` 时为商店物品的星数。

### `preview`

- `type == 0` 时为商店物品的预览图片。

### `boxImageUrl`

- `type == 2` 时为商店物品的显示图片。

### `id`

- `type == 2` 且 `id == 1` 时商店物品简介为 "·包含一只1星或2星源码精灵\n·金币 X 100\n·源码立方 X 5"，商店物品显示解锁时间为4小时。

- `type == 2` 且 `id == 2` 时商店物品简介为 "·包含一只3星源码精灵\n·金币 X 100\n·源码立方 X 5"，商店物品显示解锁时间为4小时。

- `type == 2` 且 `id == 3` 时商店物品简介为 "·包含一只4星或5星源码精灵\n·金币 X 300\n·源码立方 X 5"，商店物品显示解锁时间为12小时。

### `type`

- 商店物品类型。

### `needGold`

- `type == 0` 时为商品购买显示所需金币。

### `gold`

- `type == 1` 时为商品购买显示所需金币。

### `num`

- `type == 1` 时为商品购买显示所得数量。

### `needMasonry`

- `type == 2` 时为商品购买显示所需红宝石。
