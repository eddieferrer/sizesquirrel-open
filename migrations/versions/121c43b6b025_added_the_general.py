"""added the general

Revision ID: 121c43b6b025
Revises: 59ed83f9b533
Create Date: 2018-03-18 08:35:29.353785

"""

# revision identifiers, used by Alembic.
revision = '121c43b6b025'
down_revision = '59ed83f9b533'

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

    # La Sportiva
    op.bulk_insert(item_table,
        [
            {'model':'the general', 'brand_id':'1', 'gender_id':'3', 'type':'rock'}
        ]
    )


def downgrade():
    pass
