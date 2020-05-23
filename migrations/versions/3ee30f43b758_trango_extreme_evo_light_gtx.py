"""trango extreme evo light gtx

Revision ID: 3ee30f43b758
Revises: 48cea04e8a87
Create Date: 2017-01-15 10:36:38.603674

"""

# revision identifiers, used by Alembic.
revision = '3ee30f43b758'
down_revision = '48cea04e8a87'

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

    # Trango Extreme Evo Light GTX
    op.bulk_insert(item_table,
        [
            {'model':'trango extreme evo light gtx', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'}
        ]
    )


def downgrade():
    pass
