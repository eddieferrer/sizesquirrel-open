"""added synchros, venom, aescent, miura xx, kataki

Revision ID: 4f4e0d650c7e
Revises: 46552fd73e3c
Create Date: 2017-05-22 17:59:43.472452

"""

# revision identifiers, used by Alembic.
revision = '4f4e0d650c7e'
down_revision = '46552fd73e3c'

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

    # 5.10 Aescent
    op.bulk_insert(item_table,
        [
            {'model':'aescent', 'brand_id':'2', 'gender_id':'3', 'type':'approach'}
        ]
    )
    
    # La Sportiva
    op.bulk_insert(item_table,
        [
            {'model':'kataki', 'brand_id':'3', 'gender_id':'1', 'type':'rock'},
            {'model':'kataki', 'brand_id':'3', 'gender_id':'2', 'type':'rock'},
            {'model':'miura xx', 'brand_id':'3', 'gender_id':'1', 'type':'rock'},
            {'model':'gripit', 'brand_id':'3', 'gender_id':'4', 'type':'rock'},
            {'model':'tarantula', 'brand_id':'3', 'gender_id':'2', 'type':'rock'},
            {'model':'maverink', 'brand_id':'3', 'gender_id':'4', 'type':'rock'}
        ]
    )



def downgrade():
    pass
