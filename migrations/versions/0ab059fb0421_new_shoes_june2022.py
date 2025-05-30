"""new shoes june2022

Revision ID: 0ab059fb0421
Revises: 2fee84ece2a0
Create Date: 2022-06-08 12:05:40.464817

"""

# revision identifiers, used by Alembic.
revision = '0ab059fb0421'
down_revision = '2fee84ece2a0'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer

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

    # 27|black diamond|US
    op.bulk_insert(
        item_table, [
            {'model': 'method', 'brand_id': '27',
                'gender_id': '3', 'type': 'rock'},                      
        ])

    # change phantom from unisex to men
    op.execute(
        item_table.update().\
            where(item_table.c.model=='phantom').\
            values({'gender_id':'1'})
            )

    # 1|evolv|US
    op.bulk_insert(
        item_table, [
            {'model': 'shaman lace', 'brand_id': '1',
                'gender_id': '1', 'type': 'rock'},     
            {'model': 'shaman lace lv', 'brand_id': '1',
                'gender_id': '2', 'type': 'rock'},    
            {'model': 'phantom lv', 'brand_id': '1',
                'gender_id': '2', 'type': 'rock'},                                   
        ])        

    # 14|Ocun|EUR
    op.bulk_insert(item_table,
        [
            {'model':'ozone hv', 'brand_id':'14', 'gender_id':'3'},
            {'model':'bullit', 'brand_id':'14', 'gender_id':'3'},
            {'model':'oxi qc', 'brand_id':'14', 'gender_id':'3'},
            {'model':'oxi lu', 'brand_id':'14', 'gender_id':'3'},
        ]
    )

def downgrade():
    # ### command
    # s auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
