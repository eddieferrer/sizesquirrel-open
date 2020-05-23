"""added mammut shoes

Revision ID: 4a20f1abdea
Revises: 52a9289380b0
Create Date: 2018-09-11 18:08:25.449092

"""

# revision identifiers, used by Alembic.
revision = '4a20f1abdea'
down_revision = '52a9289380b0'

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

    # 21|mammut|UK
    op.bulk_insert(
        item_table, [
            {'model': 'nordwand light mid gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'mountain'},
            {'model': 'ayako low gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'mountain'},
            {'model': 'ayako high gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'mountain'},
            {'model': 'ayako low gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'mountain'},
            {'model': 'ayako high gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'mountain'},
            {'model': 'kento high gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'mountain'},
            {'model': 'kento high gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'mountain'},
            {'model': 'hueco advanced mid gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'hueco mid gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'hueco low gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'hueco low lth', 'brand_id': '21',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'alnasca knit low gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'alnasca knit low', 'brand_id': '21',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'alnasca low gtx', 'brand_id': '21',
                'gender_id': '1', 'type': 'approach'},
            {'model': 'hueco advanced mid gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'hueco mid gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'hueco low gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'hueco low lth', 'brand_id': '21',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'alnasca knit low gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'alnasca knit low', 'brand_id': '21',
                'gender_id': '2', 'type': 'approach'},
            {'model': 'alnasca low gtx', 'brand_id': '21',
                'gender_id': '2', 'type': 'approach'}
        ])


def downgrade():
    pass
