"""added missing NF and Zamberlan and other shoes

Revision ID: 14564cf2966d
Revises: 14c9f701c2d7
Create Date: 2017-08-31 18:33:32.057322

"""

# revision identifiers, used by Alembic.
revision = '14564cf2966d'
down_revision = '14c9f701c2d7'

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
    
    # 20|zamberlan|EUR
    op.bulk_insert(item_table,
        [
            {'model':'vioz GT', 'brand_id':'20', 'gender_id':'1', 'type':'mountain'},
            {'model':'vioz lux GTX RR', 'brand_id':'20', 'gender_id':'1', 'type':'mountain'},
            {'model':'vioz lux GTX RR', 'brand_id':'20', 'gender_id':'2', 'type':'mountain'},
            {'model':'vioz GTX', 'brand_id':'20', 'gender_id':'2', 'type':'mountain'},
            {'model':'yeren GTX RR', 'brand_id':'20', 'gender_id':'1', 'type':'mountain'},
            {'model':'yeren GTX RR', 'brand_id':'20', 'gender_id':'2', 'type':'mountain'},
            {'model':'trail lite EVO GTX', 'brand_id':'20', 'gender_id':'1', 'type':'mountain'},
            {'model':'trail lite EVO GTX', 'brand_id':'20', 'gender_id':'2', 'type':'mountain'},          
            {'model':'960 guide GT RR', 'brand_id':'20', 'gender_id':'1', 'type':'approach'},
            {'model':'quazar GTX RR', 'brand_id':'20', 'gender_id':'2', 'type':'mountain'},            
            {'model':'valles GTX RR', 'brand_id':'20', 'gender_id':'2', 'type':'mountain'},
            {'model':'cairn GTX RR', 'brand_id':'20', 'gender_id':'2', 'type':'mountain'},
            {'model':'SH crosser RR', 'brand_id':'20', 'gender_id':'2', 'type':'approach'}
        ]
    )
    # 23|the north face|US
    op.bulk_insert(item_table,
        [
            {'model':'shellista II', 'brand_id':'23', 'gender_id':'2', 'type':'mountain'},
            {'model':'chilkat 400', 'brand_id':'23', 'gender_id':'2', 'type':'mountain'},
            {'model':'endurus mid GTX', 'brand_id':'23', 'gender_id':'2', 'type':'approach'},
            {'model':'endurus mid GTX', 'brand_id':'23', 'gender_id':'1', 'type':'approach'},
            {'model':'hedgehog fastpack mid', 'brand_id':'23', 'gender_id':'2', 'type':'approach'},
            {'model':'hedgehog fastpack mid', 'brand_id':'23', 'gender_id':'1', 'type':'approach'}
        ]
    )
    
    # 1|evolv|US
    op.bulk_insert(item_table,
        [
            {'model':'shakra', 'brand_id':'1', 'gender_id':'2', 'type':'rock'},
            {'model':'ashima', 'brand_id':'1', 'gender_id':'2', 'type':'rock'}
            
        ]
    )
    
    # 2|five ten|US
    op.bulk_insert(item_table,
        [
            {'model':'urban approach', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'urban approach', 'brand_id':'2', 'gender_id':'2', 'type':'approach'},
            {'model':'approach pro', 'brand_id':'2', 'gender_id':'1', 'type':'approach'},
            {'model':'approach pro', 'brand_id':'2', 'gender_id':'2', 'type':'approach'},
            {'model':'gambit VCS', 'brand_id':'2', 'gender_id':'3', 'type':'rock'},
            {'model':'gambit lace', 'brand_id':'2', 'gender_id':'3', 'type':'rock'},
            {'model':'wall master', 'brand_id':'2', 'gender_id':'3', 'type':'rock'}
        ]
    )
    
    # 3|la sportiva|EUR
    op.bulk_insert(item_table,
        [
            {'model':'trango tower GTX', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'trango tower GTX', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'}
        ]
    )
    
    # 4|mad rock|US
    op.bulk_insert(item_table,
        [
            {'model':'anniversary mugen', 'brand_id':'4', 'gender_id':'3', 'type':'rock'}
        ]
    )
    
    # 7|tenaya|US
    op.bulk_insert(item_table,
        [
            {'model':'tanta', 'brand_id':'7', 'gender_id':'3', 'type':'rock'}
        ]
    )

def downgrade():
    pass
