"""added climbing shoes Jan2019

Revision ID: 3fb215a4e51e
Revises: 9a98673423a
Create Date: 2019-01-12 18:05:13.670858

"""

# revision identifiers, used by Alembic.
revision = '3fb215a4e51e'
down_revision = '9a98673423a'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # brand 28 unparallel
    brand_table = table('brand',
                        column('name', String)
                        )
    op.bulk_insert(brand_table,
                   [
                       {'name': 'unparallel'},
                   ]
                   )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
                       column('model', String),
                       column('brand_id', Integer),
                       column('gender_id', Integer),
                       column('small_image_url', String),
                       column('medium_image_url', String),
                       column('type', String)
                       )

    # 5|Scarpa|UK
    op.bulk_insert(
        item_table, [
            {'model': 'arpia', 'brand_id': '5',
                'gender_id': '1', 'type': 'rock'},
        ])

    # 2|five ten|US
    op.bulk_insert(
        item_table, [
            {'model': 'grandstone', 'brand_id': '2',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'aleon', 'brand_id': '2',
                'gender_id': '1', 'type': 'rock'},
        ])

    # 28|unparallel|US
    op.bulk_insert(
        item_table, [
            {'model': 'engage vcs', 'brand_id': '28',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'up rise vcs', 'brand_id': '28',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'up rise zero', 'brand_id': '28',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'up lace', 'brand_id': '28',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'sirius lace', 'brand_id': '28',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'vega', 'brand_id': '28', 'gender_id': '1', 'type': 'rock'},
            {'model': 'regulus', 'brand_id': '28',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'leopard', 'brand_id': '28',
                'gender_id': '1', 'type': 'rock'},

            {'model': 'up mocc', 'brand_id': '28',
                'gender_id': '3', 'type': 'rock'},
            {'model': 'vega', 'brand_id': '28', 'gender_id': '3', 'type': 'rock'},


            {'model': 'engage vcs lv', 'brand_id': '28',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'up lace lv', 'brand_id': '28',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'regulus lv', 'brand_id': '28',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'up rise vcs lv', 'brand_id': '28',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'up rise zero lv', 'brand_id': '28',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'sirius lace lv', 'brand_id': '28',
                'gender_id': '2', 'type': 'rock'},
        ])


def downgrade():
    pass
