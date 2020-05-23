"""fix so ill and duplicate axioms, add scarpa freney

Revision ID: 390c0c492469
Revises: 4315029dd878
Create Date: 2017-03-06 19:45:55.212407

"""

# revision identifiers, used by Alembic.
revision = '390c0c492469'
down_revision = '4315029dd878'

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

    user_item_table = table('user_item',
        column('item_id', Integer)
    )

    op.execute(
        item_table.update().\
            where(item_table.c.medium_image_url.like("%shopify%")).\
            values({'small_image_url':None, 'medium_image_url':None })
            )

    op.execute(
        item_table.delete().\
            where(and_(item_table.c.model == 'axiom', item_table.c.model == '20' ))
            )

    op.execute(
        user_item_table.update().\
            where(user_item_table.c.item_id=='20').\
            values({'item_id':'2'})
            )

    # Scarpa Freney XT
    op.bulk_insert(item_table,
        [
            {'model':'freney XT', 'brand_id':'5', 'gender_id':'1', 'type':'mountain'}
        ]
    )

def downgrade():
    pass
