"""add andrea boldrini

Revision ID: 54970e52b86b
Revises: 549a4db82c99
Create Date: 2016-06-08 08:43:39.898200

"""

# revision identifiers, used by Alembic.
revision = '54970e52b86b'
down_revision = '549a4db82c99'

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
        column('type', String)
    )
    # Scarpa Vapor
    op.bulk_insert(item_table,
        [
            {'model':'vapor', 'brand_id':'5', 'gender_id':'1', 'type':'rock'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    # brand 17 andrea boldrini
    brand_table = table('brand',
        column('name', String),
        column('sizing', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'andrea boldrini', 'sizing': 'EUR'}
        ]
    )

    # andrea boldrini List
    op.bulk_insert(item_table,
        [
            {'model':'apache talisman FCS', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'apache 5', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'apache 4', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'scorpio', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'pantera', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'tiger', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'tiger evo', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'apache light', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'pantera light', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'lynx', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'puma', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'crack', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'rex', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'bamby', 'brand_id':'17', 'gender_id':'3', 'type':'rock'},
            {'model':'squalo', 'brand_id':'17', 'gender_id':'3', 'type':'rock'}
        ]
    )

def downgrade():
    pass
