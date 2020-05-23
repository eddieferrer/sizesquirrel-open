"""added missing red chili and other shoes

Revision ID: 14c9f701c2d7
Revises: 50fb9774558
Create Date: 2017-08-24 19:23:26.197868

"""

# revision identifiers, used by Alembic.
revision = '14c9f701c2d7'
down_revision = '50fb9774558'

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
    
    # Red Chili Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'durango vcr', 'brand_id':'9', 'gender_id':'1', 'type':'rock'},
            {'model':'amp', 'brand_id':'9', 'gender_id':'1', 'type':'rock'},
            {'model':'atomyc', 'brand_id':'9', 'gender_id':'1', 'type':'rock'},
            {'model':'durango lace', 'brand_id':'9', 'gender_id':'1', 'type':'rock'},
            {'model':'voltage', 'brand_id':'9', 'gender_id':'1', 'type':'rock'},
            {'model':'fusion vcr', 'brand_id':'9', 'gender_id':'1', 'type':'rock'},
            {'model':'fusion vcr', 'brand_id':'9', 'gender_id':'2', 'type':'rock'}
        ]
    )
    
    # Lowa Climbing Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'renegade gtx', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'camino gtx flex', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'zephyr mid', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'zephyr gtx mid tf', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'zephyr gtx hi tf', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'tibet gtx', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'tibet gtx hi', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'baffin pro', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'renegade ice gtx', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'trident ii gtx', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'tiago gtx mid', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'renegade gtx low', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'vantage gtx mid', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'arco gtx', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'baffin pro ii', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'renegade gtx mid', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'bormio gtx qc', 'brand_id':'19', 'gender_id':'1', 'type':'mountain'},
            {'model':'renegade gtx mid', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'mauria gtx flex', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'lady light gtx', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'bormio gtx mid', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'vantage gtx mid', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'phoenix gtx mid', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'ferrox gtx mid', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'sassa gtx mid', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'tibet gtx', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'},
            {'model':'levante gtx mid', 'brand_id':'19', 'gender_id':'2', 'type':'mountain'}
        ]
    )


def downgrade():
    pass
