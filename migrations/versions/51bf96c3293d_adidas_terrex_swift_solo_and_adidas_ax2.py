"""adidas terrex swift solo and adidas ax2

Revision ID: 51bf96c3293d
Revises: 4a34a7b1d044
Create Date: 2017-07-26 20:10:40.599482

"""

# revision identifiers, used by Alembic.
revision = '51bf96c3293d'
down_revision = '4a34a7b1d044'

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
            {'model':'terrex swift solo', 'brand_id':'16', 'gender_id':'1', 'type':'approach'},
            {'model':'ax2', 'brand_id':'16', 'gender_id':'1', 'type':'approach'},
            {'model':'ax2', 'brand_id':'16', 'gender_id':'2', 'type':'approach'}
        ]
    )


def downgrade():
    pass
