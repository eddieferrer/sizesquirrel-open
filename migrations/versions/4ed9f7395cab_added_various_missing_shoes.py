"""added various missing shoes

Revision ID: 4ed9f7395cab
Revises: 14564cf2966d
Create Date: 2017-09-12 20:25:07.184970

"""

# revision identifiers, used by Alembic.
revision = '4ed9f7395cab'
down_revision = '14564cf2966d'

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

    # 6|boreal|US
    op.bulk_insert(item_table,
        [
            {'model':'alpha', 'brand_id':'6', 'gender_id':'1', 'type':'rock'}
        ]
    )
    
    # 21|mammut|UK
    op.bulk_insert(item_table,
        [
            {'model':'magic high gtx', 'brand_id':'21', 'gender_id':'1', 'type':'mountain'},
            {'model':'magic high gtx', 'brand_id':'21', 'gender_id':'2', 'type':'mountain'},
            {'model':'magic guide high gtx', 'brand_id':'21', 'gender_id':'1', 'type':'mountain'}
        ]
    )
    
    # 24|millet|UK
    op.bulk_insert(item_table,
        [
            {'model':'grepon 4S gtx', 'brand_id':'24', 'gender_id':'1', 'type':'mountain'}
        ]
    )
    # change 522
    op.execute(
        item_table.update().\
            where(item_table.c.model=='everest summer gtx').\
            values({'model':'everest summit gtx', 'small_image_url':'', 'medium_image_url':''})
            )
            
    # 15|salewa|US
    op.bulk_insert(item_table,
        [
            {'model':'wildfire gtx', 'brand_id':'15', 'gender_id':'1', 'type':'approach'},
            {'model':'wildfire gtx', 'brand_id':'15', 'gender_id':'2', 'type':'approach'}
        ]
    )
    
    # 5|scarpa|EUR
    op.bulk_insert(item_table,
        [
            {'model':'zodiac tech gtx', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'},
            {'model':'zodiac mid gtx', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'},
            {'model':'zodiac plus gtx', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'},
            {'model':'zodiac plus gtx', 'brand_id':'5', 'gender_id':'2', 'type':'mountain'}
        ]
    )
    
    # 3|la sportiva|EUR
    op.bulk_insert(item_table,
        [
            {'model':'trango TRK', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'trango TRK', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'},
            {'model':'nucleo high GTX', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'nucleo high GTX', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'}
        ]
    )
def downgrade():
    pass
