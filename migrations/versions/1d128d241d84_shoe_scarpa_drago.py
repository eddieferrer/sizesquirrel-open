"""shoe-scarpa-drago

Revision ID: 1d128d241d84
Revises: 4319223af8d
Create Date: 2016-04-11 12:23:37.719556

"""

# revision identifiers, used by Alembic.
revision = '1d128d241d84'
down_revision = '4319223af8d'

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
    # Scarpa Drago
    op.bulk_insert(item_table,
        [
            {'model':'drago', 'brand_id':'5', 'gender_id':'1'},
        ]
    )


def downgrade():
    pass
