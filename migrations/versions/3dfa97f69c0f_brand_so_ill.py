"""brand so ill

Revision ID: 3dfa97f69c0f
Revises: 47c82daef901
Create Date: 2016-08-08 18:17:55.639417

"""

# revision identifiers, used by Alembic.
revision = '3dfa97f69c0f'
down_revision = '47c82daef901'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 25 butora
    brand_table = table('brand',
        column('name', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'so ill'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('small_image_url', String),
        column('medium_image_url', String)
    )
    # SoIll Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'the bowler', 'brand_id':'25', 'gender_id':'3', 'small_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Bowler-Product-1_large.jpg', 'medium_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Bowler-Product-1_large.jpg'},
            {'model':'kick', 'brand_id':'25', 'gender_id':'3', 'small_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Kick-Product-1_large.jpg', 'medium_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Kick-Product-1_large.jpg'},
            {'model':'kick lv', 'brand_id':'25', 'gender_id':'3', 'small_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Kick-LV-Product-1_large.jpg', 'medium_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Kick-LV-Product-1_large.jpg'},
            {'model':'runner', 'brand_id':'25', 'gender_id':'3', 'small_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Runner-Product-1_large.jpg', 'medium_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Runner-Product-1_large.jpg'},
            {'model':'runner lv', 'brand_id':'25', 'gender_id':'3', 'small_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Runner-LV-Product-1_large.jpg', 'medium_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/Runner-LV-Product-1_large.jpg'},
            {'model':'the street', 'brand_id':'25', 'gender_id':'3', 'small_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/The-Street-Product-1_large.jpg', 'medium_image_url':'http://cdn.shopify.com/s/files/1/0424/1145/products/The-Street-Product-1_large.jpg'},
        ]
    )

def downgrade():
    pass
