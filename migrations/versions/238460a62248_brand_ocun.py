"""brand_ocun

Revision ID: 238460a62248
Revises: 4c576a619de2
Create Date: 2016-05-31 08:28:12.690991

"""

# revision identifiers, used by Alembic.
revision = '238460a62248'
down_revision = '4c576a619de2'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 14 ocun
    brand_table = table('brand',
        column('name', String),
        column('sizing', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'ocun', 'sizing': 'EUR'}
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )
    # Ocun List
    op.bulk_insert(item_table,
        [
            {'model':'diamond', 'brand_id':'14', 'gender_id':'3'},
            {'model':'ozone', 'brand_id':'14', 'gender_id':'3'},
            {'model':'ozone plus', 'brand_id':'14', 'gender_id':'3'},
            {'model':'ozone lady', 'brand_id':'14', 'gender_id':'2'},
            {'model':'oxi', 'brand_id':'14', 'gender_id':'3'},
            {'model':'rebel qc', 'brand_id':'14', 'gender_id':'3'},
            {'model':'rebel lu', 'brand_id':'14', 'gender_id':'3'},
            {'model':'pearl lu', 'brand_id':'14', 'gender_id':'3'},
            {'model':'strike qc', 'brand_id':'14', 'gender_id':'3'},
            {'model':'strike lu', 'brand_id':'14', 'gender_id':'3'},
            {'model':'crest qc', 'brand_id':'14', 'gender_id':'3'},
            {'model':'crest lu', 'brand_id':'14', 'gender_id':'3'},
            {'model':'rental qc', 'brand_id':'14', 'gender_id':'3'},
            {'model':'hero qc', 'brand_id':'14', 'gender_id':'4'}
        ]
    )


def downgrade():
    pass
