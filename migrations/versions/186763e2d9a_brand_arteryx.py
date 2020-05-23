"""brand arteryx

Revision ID: 186763e2d9a
Revises: 3dfa97f69c0f
Create Date: 2016-09-24 16:53:32.892217

"""

# revision identifiers, used by Alembic.
revision = '186763e2d9a'
down_revision = '3dfa97f69c0f'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 26 arcteryx
    brand_table = table('brand',
        column('name', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'arcteryx'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('type', String)
    )
    # Arcteryx Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'acrux SL GTX', 'brand_id':'26', 'gender_id':'1', 'type':'approach'},
            {'model':'acrux SL', 'brand_id':'26', 'gender_id':'1', 'type':'approach'},
            {'model':'arakys', 'brand_id':'26', 'gender_id':'1', 'type':'approach'},
            {'model':'acrux2 FL GTX', 'brand_id':'26', 'gender_id':'1', 'type':'approach'},
            {'model':'acrux FL GTX', 'brand_id':'26', 'gender_id':'1', 'type':'approach'},
            {'model':'acrux FL', 'brand_id':'26', 'gender_id':'1', 'type':'approach'},
            {'model':'acrux SL GTX', 'brand_id':'26', 'gender_id':'2', 'type':'approach'},
            {'model':'acrux SL', 'brand_id':'26', 'gender_id':'2', 'type':'approach'},
            {'model':'arakys', 'brand_id':'26', 'gender_id':'2', 'type':'approach'},
            {'model':'acrux2 FL GTX', 'brand_id':'26', 'gender_id':'2', 'type':'approach'},
            {'model':'acrux FL GTX', 'brand_id':'26', 'gender_id':'2', 'type':'approach'},
            {'model':'acrux FL', 'brand_id':'26', 'gender_id':'2', 'type':'approach'},
        ]
    )

def downgrade():
    pass
