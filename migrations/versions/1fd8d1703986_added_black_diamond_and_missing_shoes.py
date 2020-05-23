"""added black diamond and missing shoes

Revision ID: 1fd8d1703986
Revises: 10928070d7d1
Create Date: 2017-10-21 17:20:50.553434

"""

# revision identifiers, used by Alembic.
revision = '1fd8d1703986'
down_revision = '10928070d7d1'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # brand 27 black diamond
    brand_table = table('brand',
        column('name', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'black diamond'},
        ]
    )
    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('type', String)
    )
    # black diamond Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'momentum', 'brand_id':'27', 'gender_id':'1', 'type':'rock'},
            {'model':'momentum', 'brand_id':'27', 'gender_id':'2', 'type':'rock'},
            {'model':'aspect', 'brand_id':'27', 'gender_id':'3', 'type':'rock'},
            {'model':'momentum', 'brand_id':'27', 'gender_id':'4', 'type':'rock'}
        ]
    )
    # so ill Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'free range', 'brand_id':'25', 'gender_id':'3', 'type':'rock'},
            {'model':'approach', 'brand_id':'25', 'gender_id':'3', 'type':'approach'},
            {'model':'street lv', 'brand_id':'25', 'gender_id':'2', 'type':'rock'},
        ]
    )

    # evolv Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'nighthawk', 'brand_id':'1', 'gender_id':'1', 'type':'rock'},
            {'model':'skyhawk', 'brand_id':'1', 'gender_id':'2', 'type':'rock'}
        ]
    )

    # scarpa Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'charmoz', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'},
            {'model':'charmoz', 'brand_id':'5', 'gender_id':'2', 'type':'mountain'}
        ]
    )

    op.execute(
        item_table.update().\
            where(item_table.c.model=='the street').\
            values({'model':'street'})
            )

    op.execute(
        item_table.update().\
            where(item_table.c.model=='the bowler').\
            values({'model':'bowler'})
            )

    op.execute(
        item_table.update().\
            where(item_table.c.model=='camino gtx flex').\
            values({'model':'camino gtx'})
            )

    op.execute(
        item_table.update().\
            where(item_table.c.model=='mauria gtx flex').\
            values({'model':'mauria gtx'})
            )

    # five ten Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'stonemaster rental', 'brand_id':'2', 'gender_id':'3', 'type':'rock'},
            {'model':'access mesh', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'urban', 'brand_id':'2', 'gender_id':'2', 'type':'approach'}
        ]
    )

def downgrade():
    pass
