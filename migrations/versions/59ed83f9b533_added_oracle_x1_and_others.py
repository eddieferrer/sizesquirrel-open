"""added oracle, x1 and others

Revision ID: 59ed83f9b533
Revises: 58de193e09cc
Create Date: 2018-03-15 19:41:24.063059

"""

# revision identifiers, used by Alembic.
revision = '59ed83f9b533'
down_revision = '58de193e09cc'

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

    # Evolv
    op.bulk_insert(item_table,
        [
            {'model':'oracle', 'brand_id':'1', 'gender_id':'1', 'type':'rock'},
            {'model':'kai shaman', 'brand_id':'1', 'gender_id':'1', 'type':'rock'},
            {'model':'x1', 'brand_id':'1', 'gender_id':'1', 'type':'rock'}
        ]
    )
    # Scarpa
    op.bulk_insert(item_table,
        [
            {'model':'maestro', 'brand_id':'5', 'gender_id':'1', 'type':'rock'},
            {'model':'maestro', 'brand_id':'5', 'gender_id':'2', 'type':'rock'},
            {'model':'maestro mid', 'brand_id':'5', 'gender_id':'3', 'type':'rock'}
        ]
    )
    # Tenaya
    op.bulk_insert(item_table,
        [
            {'model':'mundaka', 'brand_id':'7', 'gender_id':'3', 'type':'rock'}
        ]
    )
    # FiveTen
    op.bulk_insert(item_table,
        [
            {'model':'anasazi pro', 'brand_id':'2', 'gender_id':'1', 'type':'rock'},
            {'model':'anasazi pro', 'brand_id':'2', 'gender_id':'2', 'type':'rock'},
            {'model':'gym master', 'brand_id':'2', 'gender_id':'3', 'type':'rock'}
        ]
    )
    # BD
    op.bulk_insert(item_table,
        [
            {'model':'shadow', 'brand_id':'27', 'gender_id':'3', 'type':'rock'}
        ]
    )


def downgrade():
    pass
