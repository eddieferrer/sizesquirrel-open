"""removed duplicate usernames

Revision ID: 10928070d7d1
Revises: 4ed9f7395cab
Create Date: 2017-09-14 17:46:14.549718

"""

# revision identifiers, used by Alembic.
revision = '10928070d7d1'
down_revision = '4ed9f7395cab'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date, and_

def upgrade():
    # These users made duplicate accounts 
    
    # 2|jgreitman 
    # delete 148 keep 614 
    
    # 2|gratusin
    #  delete 69 keep 117

    # 2|obnomad
    # delete 92 keep 377
    
    # 2|smartydh9
    # delete 756 keep 791
    
    # 2|trentbrown
    # delete 89 keep 88

    #  Create an ad-hoc table to use for the insert statement.
    user_table = table('user',
        column('id', Integer)
    )
    
    user_item_table = table('user_item',
        column('user_id', Integer)
    )
    

    op.execute(
        user_table.delete().\
            where(user_table.c.id == 148)
            )
            
    op.execute(
        user_item_table.delete().\
            where(user_item_table.c.user_id==148)
            )  
                    
    op.execute(
        user_table.delete().\
            where(user_table.c.id == 69)
            )
    op.execute(
        user_item_table.delete().\
            where(user_item_table.c.user_id==69)
            )
            
    op.execute(
        user_table.delete().\
            where(user_table.c.id == 92)
            )
    op.execute(
        user_item_table.delete().\
            where(user_item_table.c.user_id==92)
            )
            
    op.execute(
        user_table.delete().\
            where(user_table.c.id == 756)
            )
    op.execute(
        user_item_table.delete().\
            where(user_item_table.c.user_id==756)
            )
    op.execute(
        user_table.delete().\
            where(user_table.c.id == 89)
            )
    op.execute(
        user_item_table.delete().\
            where(user_item_table.c.user_id==89)
            )                                       

def downgrade():
    pass
