"""mountaineering_boots

Revision ID: 47c82daef901
Revises: 54970e52b86b
Create Date: 2016-06-15 16:12:02.909837

"""

# revision identifiers, used by Alembic.
revision = '47c82daef901'
down_revision = '54970e52b86b'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('type', String)
    )

    brand_table = table('brand',
        column('name', String),
        column('sizing', String)
    )

    # Brands:

    # 1|evolv|US
    op.bulk_insert(item_table,
        [
            {'model':'prime', 'brand_id':'1', 'gender_id':'3', 'type':'rock'}
        ]
    )

    # 2|five ten|US
    # None

    # 3|la sportiva|eur
    op.bulk_insert(item_table,
        [
            {'model':'olympus mons evo', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'g2 sm', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'spantik', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'baruntse', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'batura 2.0 gtx', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'nepal cube gtx', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'nepal cube gtx', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'},
            {'model':'trango ice cube gtx', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'trango cube gtx', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'trango cube gtx', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'},
            {'model':'trango s evo gtx', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'trango s evo gtx', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'},
            {'model':'trango alp evo gtx', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'trango alp evo gtx', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'},
            {'model':'makalu', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'karakorum', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'},
            {'model':'glacier wlf', 'brand_id':'3', 'gender_id':'3', 'type':'mountain'}
        ]
    )

    # 4|mad rock|US
    op.bulk_insert(item_table,
        [
            {'model':'alpinist', 'brand_id':'4', 'gender_id':'3', 'type':'mountain'},
            {'model':'mountain', 'brand_id':'4', 'gender_id':'3', 'type':'mountain'},
            {'model':'topo charcoal', 'brand_id':'4', 'gender_id':'3', 'type':'approach'},
            {'model':'topo teal', 'brand_id':'4', 'gender_id':'3', 'type':'approach'},
            {'model':'switchback', 'brand_id':'4', 'gender_id':'3', 'type':'approach'}
        ]
    )
    # 5|scarpa|EUR
    op.bulk_insert(item_table,
        [
            {'model':'inverno', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'phantom 6000', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'phantom 8000', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'phantom tech', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'phantom guide', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'rebel pro gtx', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'rebel ice', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'mont blanc pro gtx', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'},
            {'model':'mont blanc pro gtx', 'brand_id':'5', 'gender_id':'2', 'type':'mountain'},
            {'model':'mont blanc gtx', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'},
            {'model':'mont blanc gtx', 'brand_id':'5', 'gender_id':'2', 'type':'mountain'},
            {'model':'triolet pro gtx', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'tech ascent gtx', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'charmoz pro gtx', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'},
            {'model':'charmoz pro gtx', 'brand_id':'5', 'gender_id':'2', 'type':'mountain'},
            {'model':'wrangell gtx', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'fuego', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'},
            {'model':'grand dru gtx', 'brand_id':'5', 'gender_id':'3', 'type':'mountain'}
        ]
    )

    # 6|boreal|US
    op.bulk_insert(item_table,
        [
            {'model':'g1 expe', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'siula', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'g1 lite', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'stetind', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'kangri', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'arwa', 'brand_id':'6', 'gender_id':'1', 'type':'mountain'},
            {'model':'arwa', 'brand_id':'6', 'gender_id':'2', 'type':'mountain'},
            {'model':'nelion', 'brand_id':'6', 'gender_id':'1', 'type':'mountain'},
            {'model':'nelion', 'brand_id':'6', 'gender_id':'2', 'type':'mountain'},
            {'model':'triglav', 'brand_id':'6', 'gender_id':'1', 'type':'mountain'},
            {'model':'triglav', 'brand_id':'6', 'gender_id':'2', 'type':'mountain'},
            {'model':'brenta', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'maipo', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'mali', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'bulnes', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'fuji', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'asan', 'brand_id':'6', 'gender_id':'3', 'type':'mountain'},
            {'model':'super latok', 'brand_id':'6', 'gender_id':'1', 'type':'mountain'},
            {'model':'super latok', 'brand_id':'6', 'gender_id':'2', 'type':'mountain'}
        ]
    )

    # 7|tenaya|US
    # None

    # 8|climb x|US
    # None

    # 9|red chili|US
    # None

    # 10|eb|EUR
    # None

    # 11|simond|EUR
    # None

    # 12|butora|US
    # None

    # 13|cypher|US
    op.bulk_insert(item_table,
        [
            {'model':'logic', 'brand_id':'13', 'gender_id':'3', 'type':'approach'}
        ]
    )

    # 14|ocun|EUR
    # None

    # 15|salewa|US
    op.bulk_insert(item_table,
        [
            {'model':'raven 2 gtx', 'brand_id':'15', 'gender_id':'1', 'type':'mountain'},
            {'model':'crow gtx', 'brand_id':'15', 'gender_id':'1', 'type':'mountain'},
            {'model':'rapace gtx', 'brand_id':'15', 'gender_id':'1', 'type':'mountain'},
            {'model':'raven combi gore-tex', 'brand_id':'15', 'gender_id':'1', 'type':'mountain'},
            {'model':'raven 2 gtx', 'brand_id':'15', 'gender_id':'2', 'type':'mountain'},
            {'model':'crow gtx', 'brand_id':'15', 'gender_id':'2', 'type':'mountain'},
            {'model':'rapace gtx', 'brand_id':'15', 'gender_id':'2', 'type':'mountain'},
            {'model':'condor evo gtx', 'brand_id':'15', 'gender_id':'2', 'type':'mountain'}
        ]
    )

    # 16|adidas|US
    # None

    # 17|andrea boldrini|EUR
    # None

    # brand 18 asolo
    op.bulk_insert(brand_table,
        [
            {'name':'asolo', 'sizing': 'EUR'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'manaslu gv', 'brand_id':'18', 'gender_id':'3', 'type':'mountain'},
            {'model':'afs 8000', 'brand_id':'18', 'gender_id':'3', 'type':'mountain'},
            {'model':'afs evoluzione', 'brand_id':'18', 'gender_id':'3', 'type':'mountain'},
            {'model':'eiger gv', 'brand_id':'18', 'gender_id':'3', 'type':'mountain'},
            {'model':'comp xt petzl', 'brand_id':'18', 'gender_id':'3', 'type':'mountain'},
            {'model':'freney xt gv', 'brand_id':'18', 'gender_id':'3', 'type':'mountain'},
            {'model':'aconcagua gv', 'brand_id':'18', 'gender_id':'3', 'type':'mountain'},
            {'model':'alta via gv', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'6b+ gv', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'parete nord gv', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'piolet gv', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'elbrus gv', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'alta via gv', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'6b+ gv', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'parete nord gv', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'piolet gv', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'elbrus gv', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'jumla gv', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'jumla gv', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'salyan', 'brand_id':'18', 'gender_id':'1', 'type':'approach'},
            {'model':'salyan', 'brand_id':'18', 'gender_id':'2', 'type':'approach'},
            {'model':'magix', 'brand_id':'18', 'gender_id':'1', 'type':'approach'},
            {'model':'magix', 'brand_id':'18', 'gender_id':'2', 'type':'approach'},
            {'model':'runout gv', 'brand_id':'18', 'gender_id':'1', 'type':'approach'},
            {'model':'runout gv', 'brand_id':'18', 'gender_id':'2', 'type':'approach'},
            {'model':'path gv', 'brand_id':'18', 'gender_id':'1', 'type':'approach'},
            {'model':'path gv', 'brand_id':'18', 'gender_id':'2', 'type':'approach'}
        ]
    )

    # brand 19 lowa
    op.bulk_insert(brand_table,
        [
            {'name':'lowa', 'sizing': 'US'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'x-boulder', 'brand_id':'19', 'gender_id':'3', 'type':'rock'},
            {'model':'red eagle lace', 'brand_id':'19', 'gender_id':'3', 'type':'rock'},
            {'model':'red eagle VCR', 'brand_id':'19', 'gender_id':'3', 'type':'rock'},
            {'model':'falco lace', 'brand_id':'19', 'gender_id':'3', 'type':'rock'},
            {'model':'falco vcr', 'brand_id':'19', 'gender_id':'3', 'type':'rock'},
            {'model':'laurin gtx lo', 'brand_id':'19', 'gender_id':'3', 'type':'approach'},
            {'model':'expedition 8000 evo rd', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'},
            {'model':'expedition 6000 evo rd', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'},
            {'model':'latok xt', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'},
            {'model':'ice comp ip gtx', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'},
            {'model':'ice comp gtx', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'},
            {'model':'weisshorn gtx', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'},
            {'model':'mountain expert gtx evo', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'},
            {'model':'cevedale pro gtx', 'brand_id':'19', 'gender_id':'3', 'type':'mountain'}
        ]
    )

    # brand 20 zamberlan
    op.bulk_insert(brand_table,
        [
            {'name':'zamberlan', 'sizing': 'EUR'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'fitz roy gtx rr', 'brand_id':'20', 'gender_id':'3', 'type':'mountain'},
            {'model':'pamir gtx rr', 'brand_id':'20', 'gender_id':'3', 'type':'mountain'},
            {'model':'eiger gtx rr', 'brand_id':'20', 'gender_id':'3', 'type':'mountain'},
            {'model':'expert ibex gtx rr', 'brand_id':'20', 'gender_id':'3', 'type':'mountain'},
            {'model':'karka rr', 'brand_id':'20', 'gender_id':'3', 'type':'mountain'}
        ]
    )

    # brand 21 mammut
    op.bulk_insert(brand_table,
        [
            {'name':'mammut', 'sizing': 'UK'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'eisfeld high gtx', 'brand_id':'21', 'gender_id':'1', 'type':'mountain'},
            {'model':'magic gtx', 'brand_id':'21', 'gender_id':'1', 'type':'mountain'},
            {'model':'magic peak high gtx', 'brand_id':'21', 'gender_id':'1', 'type':'mountain'},
            {'model':'magic advanced high gtx', 'brand_id':'21', 'gender_id':'1', 'type':'mountain'},
            {'model':'magic gtx', 'brand_id':'21', 'gender_id':'2', 'type':'mountain'},
            {'model':'magic advanced high gtx', 'brand_id':'21', 'gender_id':'2', 'type':'mountain'},
            {'model':'nordwand 2.1 high', 'brand_id':'21', 'gender_id':'3', 'type':'mountain'},
            {'model':'wall guide low', 'brand_id':'21', 'gender_id':'2', 'type':'approach'},
            {'model':'sloper low lth', 'brand_id':'21', 'gender_id':'2', 'type':'approach'},
            {'model':'sloper low canvas', 'brand_id':'21', 'gender_id':'2', 'type':'approach'},
            {'model':'wall low', 'brand_id':'21', 'gender_id':'2', 'type':'approach'},
            {'model':'wall guide low gtx', 'brand_id':'21', 'gender_id':'2', 'type':'approach'},
            {'model':'super low denim', 'brand_id':'21', 'gender_id':'2', 'type':'approach'},
            {'model':'wall guide low', 'brand_id':'21', 'gender_id':'1', 'type':'approach'},
            {'model':'sloper low lth', 'brand_id':'21', 'gender_id':'1', 'type':'approach'},
            {'model':'wall guide low gtx', 'brand_id':'21', 'gender_id':'1', 'type':'approach'},
            {'model':'sloper low canvas', 'brand_id':'21', 'gender_id':'1', 'type':'approach'},
            {'model':'wall low', 'brand_id':'21', 'gender_id':'1', 'type':'approach'}
        ]
    )

    # brand 22 mammut
    op.bulk_insert(brand_table,
        [
            {'name':'garmont', 'sizing': 'UK'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'dragontail lt gtx', 'brand_id':'22', 'gender_id':'1', 'type':'approach'},
            {'model':'dragontail lt gtx', 'brand_id':'22', 'gender_id':'2', 'type':'approach'},
            {'model':'dragontail mnt gtx', 'brand_id':'22', 'gender_id':'3', 'type':'approach'},
            {'model':'pumori lx', 'brand_id':'22', 'gender_id':'3', 'type':'mountain'},
            {'model':'ferrata gtx', 'brand_id':'22', 'gender_id':'3', 'type':'mountain'},
            {'model':'vetta mnt gtx', 'brand_id':'22', 'gender_id':'3', 'type':'mountain'},
            {'model':'mountain guide pro gtx', 'brand_id':'22', 'gender_id':'3', 'type':'mountain'},
            {'model':'icon plus gtx', 'brand_id':'22', 'gender_id':'3', 'type':'mountain'},
            {'model':'pinnacle gtx', 'brand_id':'22', 'gender_id':'3', 'type':'mountain'},
            {'model':'tower extreme lx gtx', 'brand_id':'22', 'gender_id':'3', 'type':'mountain'},
            {'model':'tower plus lx gtx', 'brand_id':'22', 'gender_id':'1', 'type':'mountain'},
            {'model':'tower plus lx gtx', 'brand_id':'22', 'gender_id':'2', 'type':'mountain'},
            {'model':'tower lx gtx', 'brand_id':'22', 'gender_id':'1', 'type':'mountain'},
            {'model':'tower lx gtx', 'brand_id':'22', 'gender_id':'2', 'type':'mountain'}
        ]
    )

    # brand 23 the north face
    op.bulk_insert(brand_table,
        [
            {'name':'the north face', 'sizing': 'US'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'verto s8k', 'brand_id':'23', 'gender_id':'1', 'type':'mountain'},
            {'model':'verto s6k extreme', 'brand_id':'23', 'gender_id':'1', 'type':'mountain'},
            {'model':'verto s6k glacier gtx', 'brand_id':'23', 'gender_id':'1', 'type':'mountain'},
            {'model':'verto s4k ice gtx', 'brand_id':'23', 'gender_id':'1', 'type':'mountain'},
            {'model':'verto s4k gtx', 'brand_id':'23', 'gender_id':'1', 'type':'mountain'},
            {'model':'verto s4k gtx', 'brand_id':'23', 'gender_id':'2', 'type':'mountain'},
        ]
    )

    # brand 24 millet
    op.bulk_insert(brand_table,
        [
            {'name':'millet', 'sizing': 'UK'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'yalla', 'brand_id':'24', 'gender_id':'3', 'type':'rock'},
            {'model':'rock up', 'brand_id':'24', 'gender_id':'3', 'type':'rock'},
            {'model':'hybrid lace', 'brand_id':'24', 'gender_id':'3', 'type':'rock'},
            {'model':'hybrid', 'brand_id':'24', 'gender_id':'1', 'type':'rock'},
            {'model':'hybrid', 'brand_id':'24', 'gender_id':'2', 'type':'rock'},
            {'model':'myo sulfure', 'brand_id':'24', 'gender_id':'3', 'type':'rock'},
            {'model':'kalymnos', 'brand_id':'24', 'gender_id':'2', 'type':'rock'},
            {'model':'kalymnos', 'brand_id':'24', 'gender_id':'1', 'type':'rock'},
            {'model':'cliffhanger', 'brand_id':'24', 'gender_id':'1', 'type':'rock'},
            {'model':'cliffhanger', 'brand_id':'24', 'gender_id':'2', 'type':'rock'},
            {'model':'easy up', 'brand_id':'24', 'gender_id':'3', 'type':'rock'},
            {'model':'easy up', 'brand_id':'24', 'gender_id':'4', 'type':'rock'},
            {'model':'trident guide', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'trident', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'trident gtx', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'trident guide gtx', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'super trident gtx', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'friction', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'friction gtx', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'friction gtx', 'brand_id':'24', 'gender_id':'2', 'type':'approach'},
            {'model':'rockrise', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'rockrise', 'brand_id':'24', 'gender_id':'2', 'type':'approach'},
            {'model':'sandstone', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'sandstone', 'brand_id':'24', 'gender_id':'2', 'type':'approach'},
            {'model':'hike up', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'rockway', 'brand_id':'24', 'gender_id':'1', 'type':'approach'},
            {'model':'trident winter', 'brand_id':'24', 'gender_id':'1', 'type':'mountain'},
            {'model':'everest summer gtx', 'brand_id':'24', 'gender_id':'1', 'type':'mountain'},
            {'model':'davai', 'brand_id':'24', 'gender_id':'1', 'type':'mountain'}
        ]
    )


def downgrade():
    pass
