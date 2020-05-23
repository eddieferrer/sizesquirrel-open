"""added vapor womens, chimera, remora, agama

Revision ID: 570ebb24f72f
Revises: 1fd8d1703986
Create Date: 2017-11-17 17:39:43.274674

"""

# revision identifiers, used by Alembic.
revision = '570ebb24f72f'
down_revision = '1fd8d1703986'

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
        column('type', String)
    )

    # scarpa vapor women, scarpa chimera
    op.bulk_insert(item_table,
        [
            {'model':'vapor', 'brand_id':'5', 'gender_id':'2', 'type':'rock'},
            {'model':'chimera', 'brand_id':'5', 'gender_id':'1', 'type':'rock'}
        ]
    )

    # mad rock remora, agama
    op.bulk_insert(item_table,
        [
            {'model':'remora', 'brand_id':'4', 'gender_id':'3', 'type':'rock'},
            {'model':'agama', 'brand_id':'4', 'gender_id':'3', 'type':'rock'}
        ]
    )

def downgrade():
    pass
