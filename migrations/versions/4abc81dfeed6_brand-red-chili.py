"""empty message

Revision ID: 4abc81dfeed6
Revises: 528b2edccf31
Create Date: 2016-04-06 21:53:40.450985

"""

# revision identifiers, used by Alembic.
revision = '4abc81dfeed6'
down_revision = '528b2edccf31'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date


def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    # brand 9 red chili
    brand_table = table('brand',
        column('name', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'red chili'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )
    # Red Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'nacho', 'brand_id':'9', 'gender_id':'1'},
            {'model':'denim', 'brand_id':'9', 'gender_id':'1'},
            {'model':'spirit vcr', 'brand_id':'9', 'gender_id':'1'},
            {'model':'corona vcr', 'brand_id':'9', 'gender_id':'1'},
            {'model':'spice', 'brand_id':'9', 'gender_id':'2'},
            {'model':'denim durango', 'brand_id':'9', 'gender_id':'1'},
            {'model':'habanero lace-up', 'brand_id':'9', 'gender_id':'1'},
            {'model':'spirit lady vcr', 'brand_id':'9', 'gender_id':'2'},
            {'model':'octan', 'brand_id':'9', 'gender_id':'1'},
            {'model':'sausalito', 'brand_id':'9', 'gender_id':'1'},
            {'model':'stratos', 'brand_id':'9', 'gender_id':'1'},
            {'model':'matador vcr', 'brand_id':'9', 'gender_id':'1'},
        ]
    )

def downgrade():
    brand_table = table('brand',
        column('name', String)
    )

    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )

    user_item_table = table('user_item',
        column('item_id', Integer)
    )

    conn = op.get_bind()
    res = conn.execute("select * from brand where name = 'red chili'")
    results = res.first()

    op.execute(
        brand_table.delete().\
            where(brand_table.c.name=='red chili')
        )

    if results is not None:
        conn = op.get_bind()
        res2 = conn.execute("select * from item where brand_id ='" + str(results.id) + "'")

        op.execute(
            item_table.delete().\
                where(item_table.c.brand_id==results.id)
            )
        if res2 is not None:
            for result_item in res2:
                op.execute(
                    user_item_table.delete().\
                        where(user_item_table.c.item_id==result_item.id)
                    )
