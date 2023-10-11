"""new shoes oct2023

Revision ID: 766763c8769b
Revises: 15d014361866
Create Date: 2023-10-11 13:12:45.814955

"""

# revision identifiers, used by Alembic.
revision = '766763c8769b'
down_revision = '15d014361866'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
                       column('id', Integer),
                       column('model', String),
                       column('brand_id', Integer),
                       column('gender_id', Integer),
                       column('small_image_url', String),
                       column('medium_image_url', String),
                       column('type', String)
                       )
    
    user_item_table = table('user_item',
        column('item_id', Integer)
    )

    # 9|red chili|US
    op.bulk_insert(
        item_table, [
            {'model': 'mystix', 'brand_id': '9',
                'gender_id': '3', 'type': 'rock'},
        ]) 
    
    # 4|mad rock|US
    op.bulk_insert(
        item_table, [
            {'model':'drone CS HV', 'brand_id':'4', 'gender_id':'3', 'type':'rock'},
            {'model':'drone CS LV', 'brand_id':'4', 'gender_id':'3', 'type':'rock'},
        ])

    # 27|black diamond|US
    op.bulk_insert(
        item_table, [
            {'model': 'aspect pro', 'brand_id': '27',
                'gender_id': '3', 'type': 'rock'},                      
        ])
    
    # 5|scarpa|US
    op.bulk_insert(
        item_table, [
            {'model': 'generator mid', 'brand_id': '5',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'generator mid', 'brand_id': '5',
                'gender_id': '1', 'type': 'rock'}                
        ]) 
    
    # 1|evolv|US
    op.bulk_insert(
        item_table, [
            {'model': 'shaman pro', 'brand_id': '1',
                'gender_id': '1', 'type': 'rock'},     
            {'model': 'shaman pro lv', 'brand_id': '1',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'zenist pro', 'brand_id': '1',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'zenist pro lv', 'brand_id': '1',
                'gender_id': '2', 'type': 'rock'},                             
        ])    
    
    # 30|acopa|US
    op.bulk_insert(
        item_table, [
            {'model': 'fly', 'brand_id': '30',
                'gender_id': '3', 'type': 'rock'}
        ])

    # Change brand of quantix sf
    op.execute(
        item_table.update().
        where(item_table.c.model == 'quantix SF').
        values({'brand_id': '5'})
    )

    #remove duplicate item Scarpa Veloce 
    # id's:
    # 123 <- 845
    # 124 <- 844
    op.execute(
        user_item_table.update().\
            where(user_item_table.c.item_id==845).\
            values({'item_id':123})
        )
    op.execute(
        user_item_table.update().\
            where(user_item_table.c.item_id==844).\
            values({'item_id':124})
        )
    op.execute(
        item_table.delete().\
            where(item_table.c.id==844)
        )
    op.execute(
        item_table.delete().\
            where(item_table.c.id==845)
        )
