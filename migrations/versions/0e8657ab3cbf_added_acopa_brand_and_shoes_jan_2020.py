"""added acopa brand and shoes jan 2020

Revision ID: 0e8657ab3cbf
Revises: 13c7241d70b5
Create Date: 2020-02-03 18:55:26.232987

"""

# revision identifiers, used by Alembic.
revision = '0e8657ab3cbf'
down_revision = '13c7241d70b5'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # brand 30 Acopa
    brand_table = table('brand',
                        column('name', String)
                        )
    op.bulk_insert(brand_table,
                   [
                       {'name': 'acopa'},
                   ]
                   )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
                       column('model', String),
                       column('brand_id', Integer),
                       column('gender_id', Integer),
                       column('small_image_url', String),
                       column('medium_image_url', String),
                       column('type', String)
                       )

    # 30|acopa|US
    op.bulk_insert(
        item_table, [
            {'model': 'aztec', 'brand_id': '30',
                'gender_id': '3', 'type': 'rock'},
            {'model': 'spectre', 'brand_id': '30',
                'gender_id': '3', 'type': 'rock'},
            {'model': 'merlin', 'brand_id': '30',
                'gender_id': '3', 'type': 'rock'},
            {'model': 'legend', 'brand_id': '30',
                'gender_id': '3', 'type': 'rock'},
            {'model': 'jb', 'brand_id': '30',
                'gender_id': '3', 'type': 'rock'},
        ])

    # 2|five ten|US
    op.bulk_insert(
        item_table, [
            {'model': 'kirigami', 'brand_id': '2',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'kirigami', 'brand_id': '2',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'kirigami', 'brand_id': '2',
                'gender_id': '4', 'type': 'rock'},
        ])

    # 1|evolv|US
    op.bulk_insert(
        item_table, [
            {'model': 'rave', 'brand_id': '1',
                'gender_id': '3', 'type': 'rock'},
        ])

    # 5|scarpa|US
    op.bulk_insert(
        item_table, [
            {'model': 'booster', 'brand_id': '5',
                'gender_id': '1', 'type': 'rock'},
        ])


def downgrade():
    pass



