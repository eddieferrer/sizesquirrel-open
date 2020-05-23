"""removed duplicate shoe aescent

Revision ID: 23458c482852
Revises: 4f4e0d650c7e
Create Date: 2017-05-22 18:19:52.395978

"""

# revision identifiers, used by Alembic.
revision = '23458c482852'
down_revision = '4f4e0d650c7e'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date, and_


def upgrade():
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer),
        column('medium_image_url', String),
        column('small_image_url', String)
    )

    op.execute(
        item_table.delete().\
            where(and_(item_table.c.model == 'aescent', item_table.c.gender_id == '3' ))
            )


def downgrade():
    pass
