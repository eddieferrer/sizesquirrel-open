"""brand_salewa

Revision ID: 4c2a40f8ed4f
Revises: 238460a62248
Create Date: 2016-05-31 13:20:55.813837

"""

# revision identifiers, used by Alembic.
revision = '4c2a40f8ed4f'
down_revision = '238460a62248'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 15 Salewa
    brand_table = table('brand',
        column('name', String),
        column('sizing', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'salewa', 'sizing': 'US'}
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('type', String)
    )
    # Salewa List
    op.bulk_insert(item_table,
        [
            {'model':'firetail 3', 'brand_id':'15', 'gender_id':'2', 'type':'approach'},
            {'model':'firetail 3 gtx', 'brand_id':'15', 'gender_id':'2', 'type':'approach'},
            {'model':'wildfire pro gtx', 'brand_id':'15', 'gender_id':'2', 'type':'approach'},
            {'model':'wildfire pro', 'brand_id':'15', 'gender_id':'2', 'type':'approach'},
            {'model':'firetail evo mid gtx', 'brand_id':'15', 'gender_id':'2', 'type':'approach'},
            {'model':'wildfire s gtx', 'brand_id':'15', 'gender_id':'2', 'type':'approach'},
            {'model':'wildfire vent', 'brand_id':'15', 'gender_id':'2', 'type':'approach'},
            {'model':'firetail 3', 'brand_id':'15', 'gender_id':'1', 'type':'approach'},
            {'model':'firetail 3 gtx', 'brand_id':'15', 'gender_id':'1', 'type':'approach'},
            {'model':'wildfire pro gtx', 'brand_id':'15', 'gender_id':'1', 'type':'approach'},
            {'model':'wildfire pro', 'brand_id':'15', 'gender_id':'1', 'type':'approach'},
            {'model':'firetail evo mid gtx', 'brand_id':'15', 'gender_id':'1', 'type':'approach'},
            {'model':'wildfire s gtx', 'brand_id':'15', 'gender_id':'1', 'type':'approach'},
            {'model':'wildfire vent', 'brand_id':'15', 'gender_id':'1', 'type':'approach'}
        ]
    )
    op.bulk_insert(item_table,
        [
            {'model':'force', 'brand_id':'5', 'gender_id':'1'},
            {'model':'force', 'brand_id':'5', 'gender_id':'2'}
        ]
    )


def downgrade():
    pass
