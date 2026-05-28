# -*- encoding=utf8 -*-
from airtest.core.api import *


# =========================================================
# 1. 공통 UI 이미지
# =========================================================

IMG_BUILD_MODE_WINDOW = Template(
    r"images/common/tpl1779937675615.png",
    record_pos=(0.002, -0.004),
    resolution=(1920, 1009)
)

IMG_DEFAULT_HUD = Template(
    r"images/common/tpl1779937714928.png",
    record_pos=(-0.378, 0.22),
    resolution=(1920, 1009)
)


# =========================================================
# 2. 탭 이미지
# =========================================================

IMG_TAB_PRODUCTION = Template(
    r"images/tabs/tpl1779946561529.png",
    record_pos=(-0.282, -0.207),
    resolution=(1920, 1009)
)

IMG_TAB_PAL = Template(
    r"images/tabs/tpl1779946569946.png",
    record_pos=(-0.226, -0.205),
    resolution=(1920, 1009)
)

IMG_TAB_STORAGE = Template(
    r"images/tabs/tpl1779946576937.png",
    record_pos=(-0.169, -0.205),
    resolution=(1920, 1009)
)

IMG_TAB_FOOD = Template(
    r"images/tabs/tpl1779946586410.png",
    record_pos=(-0.113, -0.205),
    resolution=(1920, 1009)
)

IMG_TAB_INFRA = Template(
    r"images/tabs/tpl1779946598685.png",
    record_pos=(-0.057, -0.204),
    resolution=(1920, 1009)
)

IMG_TAB_LIGHTING = Template(
    r"images/tabs/tpl1779946607648.png",
    record_pos=(0.0, -0.206),
    resolution=(1920, 1009)
)

IMG_TAB_ARCHITECTURE = Template(
    r"images/tabs/tpl1779946616422.png",
    record_pos=(0.057, -0.204),
    resolution=(1920, 1009)
)

IMG_TAB_DEFENSE = Template(
    r"images/tabs/tpl1779946622844.png",
    record_pos=(0.113, -0.205),
    resolution=(1920, 1009)
)

IMG_TAB_FURNITURE = Template(
    r"images/tabs/tpl1779946628812.png",
    record_pos=(0.17, -0.204),
    resolution=(1920, 1009)
)

IMG_TAB_MISC = Template(
    r"images/tabs/tpl1779946635941.png",
    record_pos=(0.227, -0.205),
    resolution=(1920, 1009)
)


# =========================================================
# 3. 탭 대표 항목 이미지
# =========================================================

IMG_REP_PRODUCTION = Template(
    r"images/representatives/tpl1779937913529.png",
    record_pos=(-0.255, -0.103),
    resolution=(1920, 1009)
)

IMG_REP_PAL = Template(
    r"images/representatives/tpl1779937927034.png",
    record_pos=(-0.255, -0.102),
    resolution=(1920, 1009)
)

IMG_REP_STORAGE = Template(
    r"images/representatives/tpl1779937940177.png",
    record_pos=(-0.255, -0.102),
    resolution=(1920, 1009)
)

IMG_REP_FOOD = Template(
    r"images/representatives/tpl1779941759745.png",
    record_pos=(-0.255, -0.103),
    resolution=(1920, 1009)
)

IMG_REP_INFRA = Template(
    r"images/representatives/tpl1779941769316.png",
    record_pos=(-0.255, -0.102),
    resolution=(1920, 1009)
)

IMG_REP_LIGHTING = Template(
    r"images/representatives/tpl1779941784393.png",
    record_pos=(-0.255, -0.102),
    resolution=(1920, 1009)
)

IMG_REP_ARCHITECTURE = Template(
    r"images/representatives/tpl1779941793503.png",
    record_pos=(-0.256, -0.103),
    resolution=(1920, 1009)
)

IMG_REP_DEFENSE = Template(
    r"images/representatives/tpl1779941801217.png",
    record_pos=(-0.255, -0.102),
    resolution=(1920, 1009)
)

IMG_REP_FURNITURE = Template(
    r"images/representatives/tpl1779941810098.png",
    record_pos=(-0.254, -0.102),
    resolution=(1920, 1009)
)

IMG_REP_MISC = Template(
    r"images/representatives/tpl1779941819834.png",
    record_pos=(-0.256, -0.102),
    resolution=(1920, 1009)
)


# =========================================================
# 4. 건축물 아이템 이미지
# =========================================================

# 생산 탭
IMG_ITEM_PRIMITIVE_WORKBENCH = Template(
    r"images/items/tpl1779986896125.png",
    record_pos=(-0.255, -0.102),
    resolution=(1920, 1009)
)

IMG_ITEM_REPAIR_BENCH = Template(r"images/items/tpl1779990615761.png", record_pos=(-0.199, -0.102), resolution=(1920, 1009))


# 팰 탭
IMG_ITEM_PAL_BOX = Template(r"images/items/tpl1779990626969.png", record_pos=(-0.255, -0.103), resolution=(1920, 1009))


# 수납 탭
IMG_ITEM_WOOD_WALL_SHELF = Template(r"images/items/tpl1779990666323.png", record_pos=(-0.03, -0.025), resolution=(1920, 1009))

IMG_ITEM_STEEL_WALL_SHELF = Template(r"images/items/tpl1779990681108.png", record_pos=(0.253, -0.025), resolution=(1920, 1009))


# 식료품 탭
IMG_ITEM_CAMPFIRE = Template(r"images/items/tpl1779990693604.png", record_pos=(-0.256, -0.102), resolution=(1920, 1009))


# 인프라 탭
IMG_ITEM_BASIC_BED = Template(r"images/items/tpl1779990702399.png", record_pos=(-0.256, -0.103), resolution=(1920, 1009))


# 조명 탭
IMG_ITEM_WALL_TORCH = Template(r"images/items/tpl1779990714393.png", record_pos=(-0.256, -0.025), resolution=(1920, 1009))


# 건축 탭
IMG_ITEM_WOOD_FOUNDATION = Template(r"images/items/tpl1779990971729.png", record_pos=(-0.255, -0.103), resolution=(1920, 1009))

IMG_ITEM_WOOD_WALL = Template(r"images/items/tpl1779990979545.png", record_pos=(-0.143, -0.102), resolution=(1920, 1009))

IMG_ITEM_WOOD_DOOR = Template(r"images/items/tpl1779990990697.png", record_pos=(-0.03, -0.103), resolution=(1920, 1009))

IMG_ITEM_WOOD_TRIANGLE_WALL = Template(r"images/items/tpl1779991003892.png", record_pos=(0.083, -0.103), resolution=(1920, 1009))

IMG_ITEM_WOOD_ROOF = Template(r"images/items/tpl1779991024181.png", record_pos=(0.196, -0.102), resolution=(1920, 1009))

IMG_ITEM_WOOD_SLOPED_ROOF = Template(r"images/items/tpl1779991044554.png", record_pos=(-0.255, -0.046), resolution=(1920, 1009))

IMG_ITEM_WOOD_CORNER_ROOF = Template(r"images/items/tpl1779991066401.png", record_pos=(-0.143, -0.047), resolution=(1920, 1009))

IMG_ITEM_WOOD_PYRAMID_ROOF = Template(r"images/items/tpl1779991074111.png", record_pos=(-0.086, -0.046), resolution=(1920, 1009))

IMG_ITEM_WOOD_STAIRS = Template(r"images/items/tpl1779991081669.png", record_pos=(-0.03, -0.046), resolution=(1920, 1009))

IMG_ITEM_LADDER = Template(r"images/items/tpl1779991092700.png", record_pos=(0.196, -0.046), resolution=(1920, 1009))


# 방어 탭
IMG_ITEM_ALARM_BELL = Template(r"images/items/tpl1779990829888.png", record_pos=(-0.142, -0.102), resolution=(1920, 1009))


# 가구 탭
IMG_ITEM_SQUARE_TABLE = Template(r"images/items/tpl1779990861072.png", record_pos=(-0.255, -0.102), resolution=(1920, 1009))

IMG_ITEM_WOOD_CHAIR = Template(r"images/items/tpl1779990881137.png", record_pos=(-0.086, -0.025), resolution=(1920, 1009))

IMG_ITEM_ANTIQUE_RED_CARPET = Template(r"images/items/tpl1779990889466.png", record_pos=(-0.199, 0.053), resolution=(1920, 1009))

IMG_ITEM_WOOD_WALL_DECOR_SHELF = Template(r"images/items/tpl1779990900546.png", record_pos=(-0.255, 0.13), resolution=(1920, 1009))

IMG_ITEM_HOUSEPLANT = Template(r"images/items/tpl1779990931562.png", record_pos=(-0.256, 0.135), resolution=(1920, 1009))


# 기타 탭
IMG_ITEM_SIGNBOARD = Template(r"images/items/tpl1779990948434.png", record_pos=(-0.255, -0.102), resolution=(1920, 1009))

# =========================================================
# 5. 프리뷰 UI 이미지
# =========================================================

IMG_BUILD_PREVIEW_UI = Template(
    r"images/preview/tpl1779992707749.png",
    record_pos=(0.0, 0.24),
    resolution=(1920, 1009)
)