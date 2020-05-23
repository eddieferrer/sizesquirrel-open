"""size_in values in user_items

Revision ID: 4c576a619de2
Revises: 385e2996a83a
Create Date: 2016-05-21 16:07:54.013685

"""

# revision identifiers, used by Alembic.
revision = '4c576a619de2'
down_revision = '385e2996a83a'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    def convert_shoe_size_to_inches(size):
        if size is None:
            return ""
        size = float(size)
        # takes an agnostic shoe size, stores it as inches
        size_in_inches = 0;

        if size > 32:
            # we're inputing a EUR size
            size_in_inches = (( size - 31.333) / 1.333 + 1)/3 + 7.333
        else:
            # we're inputing a US size
            size_in_inches = (size * .333) + 7.333
        return float("{0:.2f}".format(size_in_inches))

    user_item_table = table('user_item',
        column('item_id', Integer),
        column('id', Integer),
        column('size', String),
        column('size_in', String)
    )

    item_table = table('item',
        column('id', Integer),
        column('gender_id', Integer)
    )

    conn = op.get_bind()
    res = conn.execute("select user_item.*, item.gender_id from user_item LEFT JOIN item ON user_item.item_id = item.id")
    results = res.fetchall()

    for result in results:
        if result.gender_id == 2:
             op.execute(
                 user_item_table.update().\
                     where(user_item_table.c.id==result.id).\
                     values({'size_in':convert_shoe_size_to_inches(result.size-1)})
                 )
        else:
             op.execute(
                 user_item_table.update().\
                     where(user_item_table.c.id==result.id).\
                     values({'size_in':convert_shoe_size_to_inches(result.size)})
                 )

def downgrade():
    pass
