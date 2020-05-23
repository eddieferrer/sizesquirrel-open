"""empty message

Revision ID: 464bb7df9f1d
Revises: 4abc81dfeed6
Create Date: 2016-04-07 20:34:18.525390

"""

# revision identifiers, used by Alembic.
revision = '464bb7df9f1d'
down_revision = '4abc81dfeed6'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 10 EB
    brand_table = table('brand',
        column('name', String),
        column('sizing', String),
    )
    op.bulk_insert(brand_table,
        [
            {'name':'eb', 'sizing':'EUR'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )
    # EB List
    op.bulk_insert(item_table,
        [
            {'model':'captain', 'brand_id':'10', 'gender_id':'1'},
            {'model':'hulk', 'brand_id':'10', 'gender_id':'1'},
            {'model':'guardian', 'brand_id':'10', 'gender_id':'1'},
            {'model':'avatar', 'brand_id':'10', 'gender_id':'1'},
            {'model':'django', 'brand_id':'10', 'gender_id':'1'},
            {'model':'django', 'brand_id':'10', 'gender_id':'2'},
        ]
    )

def downgrade():
    pass
