"""added additional shoes - scarpa furia, tohers

Revision ID: 1bca6839bca7
Revises: 2fbb33e99560
Create Date: 2018-10-11 20:13:54.029717

"""

# revision identifiers, used by Alembic.
revision = '1bca6839bca7'
down_revision = '2fbb33e99560'

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

    # 5|scarpa|UK
    op.bulk_insert(
        item_table, [
            {'model': 'furia s', 'brand_id': '5',
                'gender_id': '1', 'type': 'rock'},
            {'model': 'mescalito', 'brand_id': '5',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'mescalito', 'brand_id': '5',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'mescalito mid gtx', 'brand_id': '5',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'mescalito mid gtx', 'brand_id': '5',
                'gender_id': '2', 'type': 'approach'}
        ])

    op.execute(
        item_table.update().
        where(item_table.c.model == 'skwama').
        values({'gender_id': '1'})
    )

    op.execute(
        item_table.update().
        where(item_table.c.model == 'futura').
        values({'gender_id': '1'})
    )

    # 3|la sportiva
    op.bulk_insert(
        item_table, [
            {'model': 'futura', 'brand_id': '3',
                'gender_id': '2', 'type': 'rock'},
            {'model': 'skwama', 'brand_id': '3',
                'gender_id': '2', 'type': 'rock'}
        ])


def downgrade():
    pass
