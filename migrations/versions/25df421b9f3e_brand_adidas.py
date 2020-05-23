"""brand_adidas

Revision ID: 25df421b9f3e
Revises: 4c2a40f8ed4f
Create Date: 2016-06-02 08:24:15.415159

"""

# revision identifiers, used by Alembic.
revision = '25df421b9f3e'
down_revision = '4c2a40f8ed4f'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 16 Adidas
    brand_table = table('brand',
        column('name', String),
        column('sizing', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'adidas', 'sizing': 'US'}
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('type', String)
    )

    # Adidas List
    op.bulk_insert(item_table,
        [
            {'model':'terrex solo', 'brand_id':'16', 'gender_id':'1', 'type':'approach'},
            {'model':'terrex swift r gtx', 'brand_id':'16', 'gender_id':'2', 'type':'approach'},
            {'model':'terrex swift r gtx', 'brand_id':'16', 'gender_id':'1', 'type':'approach'},
            {'model':'terrex swift r mid gtx', 'brand_id':'16', 'gender_id':'1', 'type':'approach'},
        ]
    )

def downgrade():
    pass
