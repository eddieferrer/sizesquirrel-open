"""approach shoes

Revision ID: 49f59716a36a
Revises: 492e42f91c6f
Create Date: 2016-04-27 16:15:44.881970

"""

# revision identifiers, used by Alembic.
revision = '49f59716a36a'
down_revision = '492e42f91c6f'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Data migration for approach shoes.

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('type', String)
    )

    # Brands
    # 1|evolv|US
    # 2|five ten|US
    # 3|la sportiva|EUR
    # 4|mad rock|US
    # 5|scarpa|EUR
    # 6|boreal|US
    # 7|tenaya|US
    # 8|climb x|US
    # 9|red chili|US
    # 10|eb|EUR
    # 11|simond|EUR
    # 12|butora|US
    # 13|cypher|US

    # Evolv Approach Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'cruzer psyche', 'brand_id':'1', 'gender_id':'1', 'type':'approach'},
            {'model':'cruzer', 'brand_id':'1', 'gender_id':'1', 'type':'approach'},
            {'model':'cruzer slip-on', 'brand_id':'1', 'gender_id':'1', 'type':'approach'},
            {'model':'cruzer slip-on', 'brand_id':'1', 'gender_id':'2', 'type':'approach'},
            {'model':'cruzer purple', 'brand_id':'1', 'gender_id':'2', 'type':'approach'},
            {'model':'cruzer psyche', 'brand_id':'1', 'gender_id':'2', 'type':'approach'},
            {'model':'cruzer turquoise', 'brand_id':'1', 'gender_id':'2', 'type':'approach'},
        ]
    )

    # Five Ten Approach Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'guide tennie leather', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'guide tennie', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'guide tennie mid', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'guide tennie mid gtx', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'guide tennie', 'brand_id':'2', 'gender_id':'2', 'type':'approach'},
            {'model':'aescent', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'camp four', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
        ]
    )

    # La Sportiva Approach Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'boulder x', 'brand_id':'3', 'gender_id':'1', 'type':'approach'},
            {'model':'boulder x', 'brand_id':'3', 'gender_id':'2', 'type':'approach'},
            {'model':'mix', 'brand_id':'3', 'gender_id':'1', 'type':'approach'},
            {'model':'mix', 'brand_id':'3', 'gender_id':'2', 'type':'approach'},
            {'model':'tx2', 'brand_id':'3', 'gender_id':'2', 'type':'approach'},
            {'model':'tx2', 'brand_id':'3', 'gender_id':'1', 'type':'approach'},
            {'model':'tx3', 'brand_id':'3', 'gender_id':'2', 'type':'approach'},
            {'model':'tx3', 'brand_id':'3', 'gender_id':'1', 'type':'approach'},
            {'model':'tx4', 'brand_id':'3', 'gender_id':'2', 'type':'approach'},
            {'model':'tx4', 'brand_id':'3', 'gender_id':'1', 'type':'approach'},
            {'model':'ganda', 'brand_id':'3', 'gender_id':'1', 'type':'approach'},
            {'model':'xplorer', 'brand_id':'3', 'gender_id':'2', 'type':'approach'},
        ]
    )

    # Scarpa Approach Shoes
    op.bulk_insert(item_table,
        [
            {'model':'gecko', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
            {'model':'gecko', 'brand_id':'5', 'gender_id':'2', 'type':'approach'},
            {'model':'gecko lite', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
            {'model':'gecko lite', 'brand_id':'5', 'gender_id':'2', 'type':'approach'},
            {'model':'iguana', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
            {'model':'iguana', 'brand_id':'5', 'gender_id':'2', 'type':'approach'},
            {'model':'crux', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
            {'model':'crux', 'brand_id':'5', 'gender_id':'2', 'type':'approach'},
            {'model':'crux canvas', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
            {'model':'crux canvas', 'brand_id':'5', 'gender_id':'2', 'type':'approach'},
            {'model':'tech ascent', 'brand_id':'5', 'gender_id':'3', 'type':'approach'},
            {'model':'vitamin', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
            {'model':'zen', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
            {'model':'mojito', 'brand_id':'5', 'gender_id':'1', 'type':'approach'},
        ]
    )

    # Boreal Approach Shoes
    op.bulk_insert(item_table,
        [
            {'model':'flyers', 'brand_id':'6', 'gender_id':'1', 'type':'approach'},
            {'model':'flyers mid', 'brand_id':'6', 'gender_id':'1', 'type':'approach'},
            {'model':'flyers', 'brand_id':'6', 'gender_id':'2', 'type':'approach'},
            {'model':'flyers mid', 'brand_id':'6', 'gender_id':'2', 'type':'approach'},
            {'model':'sendai', 'brand_id':'6', 'gender_id':'1', 'type':'approach'},
            {'model':'drom', 'brand_id':'6', 'gender_id':'1', 'type':'approach'},
            {'model':'drom', 'brand_id':'6', 'gender_id':'2', 'type':'approach'},
        ]
    )

def downgrade():
    pass
