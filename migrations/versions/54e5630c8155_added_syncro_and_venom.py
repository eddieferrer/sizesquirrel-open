"""added syncro and venom

Revision ID: 54e5630c8155
Revises: 23458c482852
Create Date: 2017-05-22 18:25:05.500183

"""

# revision identifiers, used by Alembic.
revision = '54e5630c8155'
down_revision = '23458c482852'

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
            {'model':'venom', 'brand_id':'3', 'gender_id':'1', 'type':'rock'},
            {'model':'syncro', 'brand_id':'3', 'gender_id':'1', 'type':'rock'}
        ]
    )


def downgrade():
    pass
