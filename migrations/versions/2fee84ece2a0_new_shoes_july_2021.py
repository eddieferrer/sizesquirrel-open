"""new shoes july 2021

Revision ID: 2fee84ece2a0
Revises: dca9b5eea4e8
Create Date: 2021-07-19 17:26:37.948779

"""

# revision identifiers, used by Alembic.
revision = '2fee84ece2a0'
down_revision = 'dca9b5eea4e8'

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
    # 5|scarpa|EUR
    op.bulk_insert(
        item_table, [
            {'model': 'quantic', 'brand_id': '5',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'quantic', 'brand_id': '5',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'rapid gtx', 'brand_id': '5',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'rapid gtx', 'brand_id': '5',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'rapid', 'brand_id': '5',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'rapid', 'brand_id': '5',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'kalipe gtx', 'brand_id': '5',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'kalipe gtx', 'brand_id': '5',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'kalipe', 'brand_id': '5',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'kalipe', 'brand_id': '5',
                'gender_id': '2', 'type': 'approach'},   
            {'model': 'crux air', 'brand_id': '5',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'crux air', 'brand_id': '5',
                'gender_id': '2', 'type': 'approach'},                               
        ])

    # 3|la sportiva|EUR
    op.bulk_insert(
        item_table, [
            {'model': 'kubo', 'brand_id': '3',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'kubo', 'brand_id': '3',
                'gender_id': '2', 'type': 'rock'},
                                      
        ])
    # 12|butora|US
    op.bulk_insert(
        item_table, [
            {'model': 'wing', 'brand_id': '12',
                'gender_id': '3', 'type': 'approach'},
            {'model': 'icarus', 'brand_id': '12',
                'gender_id': '3', 'type': 'approach'},
                                      
        ])
    # 2|five ten|US
    op.bulk_insert(
        item_table, [
            {'model': 'crawe', 'brand_id': '2',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'crawe', 'brand_id': '2',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'NIAD Lace', 'brand_id': '2',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'NIAD Lace', 'brand_id': '2',
                'gender_id': '2', 'type': 'rock'},      
            {'model': 'NIAD VCS', 'brand_id': '2',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'NIAD VCS', 'brand_id': '2',
                'gender_id': '2', 'type': 'rock'},                          
                                      
        ])

    # 27|black diamond|US
    op.bulk_insert(
        item_table, [
            {'model': 'fuel', 'brand_id': '27',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'fuel', 'brand_id': '27',
                'gender_id': '2', 'type': 'approach'},      
            {'model': 'prime', 'brand_id': '27',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'prime', 'brand_id': '27',
                'gender_id': '2', 'type': 'approach'},     
            {'model': 'session', 'brand_id': '27',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'session', 'brand_id': '27',
                'gender_id': '2', 'type': 'approach'},       
            {'model': 'session suede', 'brand_id': '27',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'session suede', 'brand_id': '27',
                'gender_id': '2', 'type': 'approach'},    
            {'model': 'mission lt', 'brand_id': '27',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'mission lt', 'brand_id': '27',
                'gender_id': '2', 'type': 'approach'},     
            {'model': 'circuit', 'brand_id': '27',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'circuit', 'brand_id': '27',
                'gender_id': '2', 'type': 'approach'},      
            {'model': 'technician', 'brand_id': '27',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'technician', 'brand_id': '27',
                'gender_id': '2', 'type': 'approach'},                                                                                                      
        ])

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
