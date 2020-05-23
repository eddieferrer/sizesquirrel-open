"""brand-butora

Revision ID: 1fb7eb6375c8
Revises: 78ef3eca892
Create Date: 2016-04-09 13:14:57.408568

"""

# revision identifiers, used by Alembic.
revision = '1fb7eb6375c8'
down_revision = '78ef3eca892'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 12 butora
    brand_table = table('brand',
        column('name', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'butora'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )
    # Red Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'blue acro', 'brand_id':'12', 'gender_id':'3'},
            {'model':'orange acro', 'brand_id':'12', 'gender_id':'3'},
            {'model':'endeavor moss', 'brand_id':'12', 'gender_id':'1'},
            {'model':'endeavor sierra gold', 'brand_id':'12', 'gender_id':'1'},
            {'model':'altura green', 'brand_id':'12', 'gender_id':'3'},
            {'model':'altura orange', 'brand_id':'12', 'gender_id':'3'},
            {'model':'mantra green', 'brand_id':'12', 'gender_id':'3'},
            {'model':'mantra orange', 'brand_id':'12', 'gender_id':'3'},
            {'model':'endeavor crimson', 'brand_id':'12', 'gender_id':'2'},
            {'model':'endeavor lavender', 'brand_id':'12', 'gender_id':'2'},
            {'model':'libra fancy', 'brand_id':'12', 'gender_id':'2'},
            {'model':'habara blue', 'brand_id':'12', 'gender_id':'3'},
            {'model':'habara picante', 'brand_id':'12', 'gender_id':'3'},
            {'model':'brava blue', 'brand_id':'12', 'gender_id':'4'},
            {'model':'brava pink', 'brand_id':'12', 'gender_id':'4'},
            {'model':'brava violet', 'brand_id':'12', 'gender_id':'4'},
        ]
    )


def downgrade():
    pass
