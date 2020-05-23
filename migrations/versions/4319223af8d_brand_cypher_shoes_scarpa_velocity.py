"""brand-cypher-shoes-scarpa-velocity

Revision ID: 4319223af8d
Revises: 1fb7eb6375c8
Create Date: 2016-04-11 08:21:25.597308

"""

# revision identifiers, used by Alembic.
revision = '4319223af8d'
down_revision = '1fb7eb6375c8'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # brand 13 cypher
    brand_table = table('brand',
        column('name', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'cypher'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )
    # Cypher Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'phelix 2.0', 'brand_id':'13', 'gender_id':'2'},
            {'model':'phelix', 'brand_id':'13', 'gender_id':'2'},
            {'model':'code', 'brand_id':'13', 'gender_id':'3'},
            {'model':'rubik', 'brand_id':'13', 'gender_id':'3'},
            {'model':'modulo', 'brand_id':'13', 'gender_id':'3'},
            {'model':'codex', 'brand_id':'13', 'gender_id':'3'},
            {'model':'sentinel', 'brand_id':'13', 'gender_id':'3'},
            {'model':'zero', 'brand_id':'13', 'gender_id':'3'},
            {'model':'code breaker', 'brand_id':'13', 'gender_id':'4'},
            {'model':'prefix', 'brand_id':'13', 'gender_id':'3'},

            {'model':'velocity lace', 'brand_id':'5', 'gender_id':'1'},
            {'model':'velocity v', 'brand_id':'5', 'gender_id':'1'},
        ]
    )


def downgrade():
    pass
