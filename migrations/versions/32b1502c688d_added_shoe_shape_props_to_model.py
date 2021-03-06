"""added shoe shape props to model

Revision ID: 32b1502c688d
Revises: da82b2787ad
Create Date: 2019-07-28 20:49:04.394242

"""

# revision identifiers, used by Alembic.
revision = '32b1502c688d'
down_revision = 'da82b2787ad'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('average_rating_celtic', sa.String(length=64), nullable=True))
    op.add_column('item', sa.Column('average_rating_egyptian', sa.String(length=64), nullable=True))
    op.add_column('item', sa.Column('average_rating_germanic', sa.String(length=64), nullable=True))
    op.add_column('item', sa.Column('average_rating_greek', sa.String(length=64), nullable=True))
    op.add_column('item', sa.Column('average_rating_roman', sa.String(length=64), nullable=True))
    op.add_column('item', sa.Column('count_celtic', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('count_egyptian', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('count_germanic', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('count_greek', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('count_roman', sa.Integer(), nullable=True))
    op.add_column('item', sa.Column('popular_foot_shape', sa.String(length=64), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'popular_foot_shape')
    op.drop_column('item', 'count_roman')
    op.drop_column('item', 'count_greek')
    op.drop_column('item', 'count_germanic')
    op.drop_column('item', 'count_egyptian')
    op.drop_column('item', 'count_celtic')
    op.drop_column('item', 'average_rating_roman')
    op.drop_column('item', 'average_rating_greek')
    op.drop_column('item', 'average_rating_germanic')
    op.drop_column('item', 'average_rating_egyptian')
    op.drop_column('item', 'average_rating_celtic')
    ### end Alembic commands ###
