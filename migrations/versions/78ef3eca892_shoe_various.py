"""shoe-various

Revision ID: 78ef3eca892
Revises: 5875072d00cf
Create Date: 2016-04-08 11:43:44.587252

"""

# revision identifiers, used by Alembic.
revision = '78ef3eca892'
down_revision = '5875072d00cf'

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
        column('gender_id', Integer)
    )

    # La Sportiva Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'speedster', 'brand_id':'3', 'gender_id':'1'},
            {'model':'otaki', 'brand_id':'3', 'gender_id':'1'},
            {'model':'otaki', 'brand_id':'3', 'gender_id':'2'},
        ]
    )
    # Evolv Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'elektra lace', 'brand_id':'1', 'gender_id':'2'},
        ]
    )

def downgrade():
    pass
