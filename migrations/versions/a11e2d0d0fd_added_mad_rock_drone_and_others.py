"""added mad rock drone and others

Revision ID: a11e2d0d0fd
Revises: 2ccabbd7f6e3
Create Date: 2018-07-09 11:50:51.634450

"""

# revision identifiers, used by Alembic.
revision = 'a11e2d0d0fd'
down_revision = '2ccabbd7f6e3'

from alembic import op
import sqlalchemy as sa

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

    # mad rock drones and others
    op.bulk_insert(item_table,
        [
            {'model':'drone HV', 'brand_id':'4', 'gender_id':'3', 'type':'rock'},
            {'model':'drone LV', 'brand_id':'4', 'gender_id':'3', 'type':'rock'},
            {'model':'haywire', 'brand_id':'4', 'gender_id':'3', 'type':'rock'},
            {'model':'weaver', 'brand_id':'4', 'gender_id':'3', 'type':'rock'},
            {'model':'pulse negative', 'brand_id':'4', 'gender_id':'3', 'type':'rock'}
        ]
    )

    # lowa rocket
    op.bulk_insert(item_table,
        [
            {'model':'rocket', 'brand_id':'19', 'gender_id':'3', 'type':'rock'}
        ]
    )


    # five ten access
    op.bulk_insert(item_table,
        [
            {'model':'access', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'access', 'brand_id':'2', 'gender_id':'2', 'type':'approach'}
        ]
    )

    # evolv access
    op.bulk_insert(item_table,
        [
            {'model':'maximus', 'brand_id':'1', 'gender_id':'1', 'type':'approach'},
            {'model':'capitan', 'brand_id':'1', 'gender_id':'1', 'type':'approach'},
            {'model':'valor', 'brand_id':'1', 'gender_id':'1', 'type':'rock'}
        ]
    )

    # BD focus
    op.bulk_insert(item_table,
        [
            {'model':'focus', 'brand_id':'27', 'gender_id':'2', 'type':'rock'},
            {'model':'focus', 'brand_id':'27', 'gender_id':'1', 'type':'rock'}
        ]
    )

    # 18|asolo|EUR
    op.bulk_insert(item_table,
        [
            {'model':'ascender GV', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'}
        ]
    )

    # red chili spirit speed
    op.bulk_insert(item_table,
        [
            {'model':'spirit speed', 'brand_id':'9', 'gender_id':'3', 'type':'rock'}
        ]
    )

    # change pulse to 'pulse positive'
    op.execute(
        item_table.update().\
            where(item_table.c.model=='pulse').\
            values({'model':'pulse positive', 'gender_id':'3'})
            )

def downgrade():
    pass
