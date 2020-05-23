"""add scarpa shoes

Revision ID: 549a4db82c99
Revises: 25df421b9f3e
Create Date: 2016-06-07 12:47:35.539531

"""

# revision identifiers, used by Alembic.
revision = '549a4db82c99'
down_revision = '25df421b9f3e'

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
    # Scarpa
    op.bulk_insert(item_table,
        [
            {'model':'hyper mid gtx', 'brand_id':'3', 'gender_id':'3', 'type': 'approach'},
            {'model':'boulder x mid gtx', 'brand_id':'3', 'gender_id':'3', 'type': 'approach'},
            {'model':'skwama', 'brand_id':'3', 'gender_id':'3', 'type': 'rock'},
            {'model':'finale', 'brand_id':'3', 'gender_id':'1', 'type': 'rock'},
            {'model':'finale', 'brand_id':'3', 'gender_id':'2', 'type': 'rock'}
        ]
    )

def downgrade():
    pass
