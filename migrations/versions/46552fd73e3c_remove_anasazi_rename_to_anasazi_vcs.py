"""remove anasazi, rename to anasazi vcs

Revision ID: 46552fd73e3c
Revises: 18efa38e0b89
Create Date: 2017-05-04 17:39:29.349004

"""

# revision identifiers, used by Alembic.
revision = '46552fd73e3c'
down_revision = '18efa38e0b89'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String)
    )
    user_item_table = table('user_item',
        column('item_id', String)
    )
    # get anasazi id
    conn = op.get_bind()
    res = conn.execute("select * from item where model = 'anasazi'")
    results = res.first()
    # get anasazi vcs id
    res2 = conn.execute("select * from item where model = 'anasazi vcs'")
    results2 = res2.first()

    op.execute(
        user_item_table.update().\
            where(user_item_table.c.item_id==results.id).\
            values({'item_id':results2.id})
        )
        
    op.execute(
        item_table.delete().\
            where(item_table.c.model=='anasazi')
        )


def downgrade():
    pass
