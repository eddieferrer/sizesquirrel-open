"""added missing garmont and asolo shoes

Revision ID: 50fb9774558
Revises: 51bf96c3293d
Create Date: 2017-08-15 20:45:55.797996

"""

# revision identifiers, used by Alembic.
revision = '50fb9774558'
down_revision = '51bf96c3293d'

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
    # 22|garmont|UK
    op.bulk_insert(item_table,
        [
            {'model':'tower trek GTX', 'brand_id':'22', 'gender_id':'1', 'type':'mountain'},
            {'model':'tower trek GTX', 'brand_id': '22', 'gender_id':'2', 'type':'mountain'},
            {'model':'rambler GTX', 'brand_id':'22', 'gender_id':'1', 'type':'mountain'},
            {'model':'rambler GTX', 'brand_id':'22', 'gender_id':'2', 'type':'mountain'},
            {'model':'santiago GTX low', 'brand_id':'22', 'gender_id':'1', 'type':'approach'},
            {'model':'santiago GTX mid', 'brand_id':'22', 'gender_id':'1', 'type':'mountain'},
            {'model':'prophet GTX low', 'brand_id':'22', 'gender_id':'1', 'type':'approach'},
            {'model':'prophet GTX mid', 'brand_id':'22', 'gender_id':'1', 'type':'mountain'},
            {'model':'mystic II GTX mid', 'brand_id':'22', 'gender_id':'1', 'type':'mountain'},
            {'model':'mystic II GTX mid', 'brand_id':'22', 'gender_id':'2', 'type':'mountain'},
            {'model':'ventura GTX', 'brand_id':'22', 'gender_id':'2', 'type':'mountain'}
        ]
    )
    # 18|asolo|EUR
    op.bulk_insert(item_table,
        [
            {'model':'power matic 200 GV', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'power matic 200 GV', 'brand_id': '18', 'gender_id':'2', 'type':'mountain'},
            {'model':'thyrus GV', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'thyrus GV', 'brand_id': '18', 'gender_id':'2', 'type':'mountain'},
            {'model':'falcon GV', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'falcon GV', 'brand_id': '18', 'gender_id':'2', 'type':'mountain'},
            {'model':'TPS 520 GV', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'TPS 520 GV', 'brand_id': '18', 'gender_id':'2', 'type':'mountain'},
            {'model':'fugitive GTX', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'drifter GV', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'megaton GV', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'fulton mid', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'reston', 'brand_id':'18', 'gender_id':'1', 'type':'mountain'},
            {'model':'tribe GV', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'cylios mid', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'fission GV', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'tacoma GTX', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'yuma WP', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'},
            {'model':'athena WP ML', 'brand_id':'18', 'gender_id':'2', 'type':'mountain'}
        ]
    )
    # 15|salewa|US
    op.bulk_insert(item_table,
        [
            {'model':'alp trainer mid', 'brand_id':'15', 'gender_id':'1', 'type':'mountain'},
            {'model':'alp trainer mid', 'brand_id': '15', 'gender_id':'2', 'type':'mountain'},
            {'model':'alpenrose mid', 'brand_id':'15', 'gender_id':'2', 'type':'mountain'},
            {'model':'mountain trainer mid GTX', 'brand_id': '15', 'gender_id':'1', 'type':'mountain'},
            {'model':'vultur GTX', 'brand_id': '15', 'gender_id':'3', 'type':'mountain'},
            {'model':'vultur vertical GTX', 'brand_id': '15', 'gender_id':'1', 'type':'mountain'}
        ]
    )


def downgrade():
    pass
