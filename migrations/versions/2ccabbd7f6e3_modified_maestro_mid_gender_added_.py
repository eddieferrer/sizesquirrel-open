"""modified maestro mid gender, added womens maestro mid

Revision ID: 2ccabbd7f6e3
Revises: 121c43b6b025
Create Date: 2018-06-16 10:19:45.153467

"""

# revision identifiers, used by Alembic.
revision = '2ccabbd7f6e3'
down_revision = '121c43b6b025'

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
    # change maestro from unisex to men
    op.execute(
        item_table.update().\
            where(item_table.c.model=='maestro mid').\
            values({'gender_id':'1'})
            )

    # insert womens maestro mid
    op.bulk_insert(item_table,
        [
            {'model':'maestro mid', 'brand_id':'5', 'gender_id':'2', 'type':'rock'}
        ]
    )


def downgrade():
    pass
