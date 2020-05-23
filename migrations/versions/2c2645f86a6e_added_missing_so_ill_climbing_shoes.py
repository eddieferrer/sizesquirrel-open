"""added missing so ill climbing shoes

Revision ID: 2c2645f86a6e
Revises: 3fb215a4e51e
Create Date: 2019-02-18 19:55:47.884219

"""

# revision identifiers, used by Alembic.
revision = '2c2645f86a6e'
down_revision = '3fb215a4e51e'

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
                       column('small_image_url', String),
                       column('medium_image_url', String),
                       column('type', String)
                       )

    # 25|so ill|US
    op.bulk_insert(
        item_table, [
            {'model': 'one', 'brand_id': '25',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'tokyo streets', 'brand_id': '25',
                'gender_id': '1', 'type': 'rock'},
            {'model': '2020 gold', 'brand_id': '25',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'free range lv', 'brand_id': '25',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'new zero', 'brand_id': '25',
             'gender_id': '1', 'type': 'rock'},
            {'model': 'camo new zero', 'brand_id': '25',
             'gender_id': '1', 'type': 'rock'},
            {'model': 'approach', 'brand_id': '25',
                'gender_id': '1', 'type': 'approach'},
        ])

    op.execute(
        item_table.update().
        where(item_table.c.model == 'free range').
        values({'gender_id': '1'})
    )
