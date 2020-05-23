"""evolv bandit, bandit sc, instinct vsr

Revision ID: 4315029dd878
Revises: 245a11a7da11
Create Date: 2017-02-28 21:00:56.118095

"""

# revision identifiers, used by Alembic.
revision = '4315029dd878'
down_revision = '245a11a7da11'

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

    # evolv bandit, bandit sc, scarpa instinct vsr
    op.bulk_insert(item_table,
        [
            {'model':'instinct vsr', 'brand_id':'5', 'gender_id':'1', 'type':'rock'},
            {'model':'bandit', 'brand_id':'1', 'gender_id':'1', 'type':'rock'},
            {'model':'bandit sc', 'brand_id':'1', 'gender_id':'1', 'type':'rock'}
        ]
    )

def downgrade():
    pass
