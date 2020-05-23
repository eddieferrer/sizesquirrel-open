"""arco fix nepal evo

Revision ID: 48cea04e8a87
Revises: 186763e2d9a
Create Date: 2016-12-23 14:49:14.079611

"""

# revision identifiers, used by Alembic.
revision = '48cea04e8a87'
down_revision = '186763e2d9a'

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
    op.execute(
        item_table.update().\
            where(item_table.c.model=='arco').\
            values({'model':'arco velcro', 'small_image_url':'', 'medium_image_url':''})
            )

    # Nepal Evo GTX
    op.bulk_insert(item_table,
        [
            {'model':'nepal evo gtx', 'brand_id':'3', 'gender_id':'1', 'type':'mountain'},
            {'model':'nepal evo gtx', 'brand_id':'3', 'gender_id':'2', 'type':'mountain'}
        ]
    )


def downgrade():
    pass
