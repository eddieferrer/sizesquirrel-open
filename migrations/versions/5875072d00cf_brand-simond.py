"""empty message

Revision ID: 5875072d00cf
Revises: 464bb7df9f1d
Create Date: 2016-04-07 20:39:20.835681

"""

# revision identifiers, used by Alembic.
revision = '5875072d00cf'
down_revision = '464bb7df9f1d'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 11 Simond
    brand_table = table('brand',
        column('name', String),
        column('sizing', String),
    )
    op.bulk_insert(brand_table,
        [
            {'name':'simond', 'sizing':'EUR'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )
    # Simond List
    op.bulk_insert(item_table,
        [
            {'model':'rock junior', 'brand_id':'11', 'gender_id':'4'},
            {'model':'rock blue', 'brand_id':'11', 'gender_id':'1'},
            {'model':'rock', 'brand_id':'11', 'gender_id':'1'},
            {'model':'cliff slipper', 'brand_id':'11', 'gender_id':'1'},
            {'model':'edge', 'brand_id':'11', 'gender_id':'1'},
        ]
    )


def downgrade():
    pass
