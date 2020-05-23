"""added butora narsha

Revision ID: 58de193e09cc
Revises: 570ebb24f72f
Create Date: 2017-12-09 08:43:20.086642

"""

# revision identifiers, used by Alembic.
revision = '58de193e09cc'
down_revision = '570ebb24f72f'

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

    # La Sportiva
    op.bulk_insert(item_table,
        [
            {'model':'narsha blue', 'brand_id':'12', 'gender_id':'3', 'type':'rock'},
            {'model':'narsha orange', 'brand_id':'12', 'gender_id':'3', 'type':'rock'}
        ]
    )
    op.execute(
        item_table.update().\
            where(item_table.c.model=='blue acro').\
            values({'model':'acro blue'})
            )

    op.execute(
        item_table.update().\
            where(item_table.c.model=='orange acro').\
            values({'model':'acro orange'})
            )
def downgrade():
    pass
