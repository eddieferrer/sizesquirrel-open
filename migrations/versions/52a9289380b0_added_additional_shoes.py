"""added additional shoes

Revision ID: 52a9289380b0
Revises: 1137f4cdac18
Create Date: 2018-08-28 20:50:18.573274

"""

# revision identifiers, used by Alembic.
revision = '52a9289380b0'
down_revision = '1137f4cdac18'

from alembic import op
import sqlalchemy as sa

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

    # Asolo
    op.bulk_insert(item_table,
                   [
                       {'model': 'mont blanc gv', 'brand_id': '18',
                           'gender_id': '1', 'type': 'mountain'}
                   ]
                   )

    # Boreal
    op.bulk_insert(item_table,
                   [
                       {'model': 'synergy', 'brand_id': '6',
                        'gender_id': '3', 'type': 'rock'}
                   ]
                   )

    # La Sportiva
    op.bulk_insert(item_table,
                   [
                       {'model': 'G5', 'brand_id': '3',
                        'gender_id': '3', 'type': 'mountain'},
                       {'model': 'G2', 'brand_id': '3',
                        'gender_id': '3', 'type': 'mountain'}
                   ]
                   )

    # Lowa
    op.bulk_insert(item_table,
                   [
                       {'model': 'alpine pro gtx', 'brand_id': '19',
                        'gender_id': '1', 'type': 'mountain'}
                   ]
                   )

    # Zamberlan
    op.bulk_insert(item_table,
                   [
                       {'model': 'mountain pro evo gtx', 'brand_id': '20',
                        'gender_id': '1', 'type': 'mountain'},
                       {'model': 'mountain pro evo gtx', 'brand_id': '20',
                        'gender_id': '2', 'type': 'mountain'},
                       {'model': 'karka evo RR', 'brand_id': '20',
                        'gender_id': '1', 'type': 'mountain'},
                       {'model': 'eiger evo RR', 'brand_id': '20',
                        'gender_id': '1', 'type': 'mountain'},
                       {'model': 'everest evo RR', 'brand_id': '20',
                        'gender_id': '1', 'type': 'mountain'},
                       {'model': 'expert pro gtx RR', 'brand_id': '20',
                        'gender_id': '1', 'type': 'mountain'},
                       {'model': 'sparrow RR', 'brand_id': '20',
                        'gender_id': '2', 'type': 'approach'},
                       {'model': 'intrepid RR', 'brand_id': '20',
                        'gender_id': '1', 'type': 'approach'},
                   ]
                   )

    # Evolv
    op.bulk_insert(item_table,
                   [
                       {'model': 'zender', 'brand_id': '1',
                        'gender_id': '3', 'type': 'approach'}
                   ]
                   )

    # Mad Rock
    op.bulk_insert(item_table,
                   [
                       {'model': 'frenzy ez', 'brand_id': '4',
                        'gender_id': '3', 'type': 'rock'},
                       {'model': 'frenzy lace', 'brand_id': '4',
                                                'gender_id': '3', 'type': 'rock'},
                       {'model': 'banshee', 'brand_id': '4',
                        'gender_id': '2', 'type': 'rock'},
                       {'model': 'mugen tech 2.0', 'brand_id': '4',
                        'gender_id': '3', 'type': 'rock'},
                       {'model': 'maniac', 'brand_id': '4',
                        'gender_id': '3', 'type': 'rock'}
                   ]
                   )


def downgrade():
    pass
