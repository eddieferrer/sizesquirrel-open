"""added synth moccs and evolv supra

Revision ID: 4a34a7b1d044
Revises: 54e5630c8155
Create Date: 2017-07-03 09:12:42.403930

"""

# revision identifiers, used by Alembic.
revision = '4a34a7b1d044'
down_revision = '54e5630c8155'

from alembic import op
import sqlalchemy as sa

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

    # 
    op.bulk_insert(item_table,
        [
            {'model':'supra', 'brand_id':'1', 'gender_id':'1', 'type':'rock'},
            {'model':'moccasym synthetic', 'brand_id':'2', 'gender_id':'1', 'type':'rock'}
        ]
    )


def downgrade():
    pass
