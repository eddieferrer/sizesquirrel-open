"""Initial Data

Revision ID: 35c6ceb8a0cb
Revises: 47f8e2618aae
Create Date: 2015-12-12 18:55:16.207016

"""

# revision identifiers, used by Alembic.
revision = '35c6ceb8a0cb'
down_revision = '47f8e2618aae'

from alembic import op
import sqlalchemy as sa
from datetime import date
from sqlalchemy.sql import table, column
from sqlalchemy import String, Integer, Date

def upgrade():
    # Create an ad-hoc table to use for the insert statement.
    gender_table = table('gender',
        column('name', String)
    )
    op.bulk_insert(gender_table,
        [
            {'name':'men'},
            {'name':'women'},
            {'name':'unisex'},
            {'name':'kids'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    brand_table = table('brand',
        column('name', String)
    )
    op.bulk_insert(brand_table,
        [
            {'name':'evolv'},
            {'name':'five ten'},
            {'name':'la sportiva'},
            {'name':'mad rock'},
            {'name':'scarpa'},
            {'name':'boreal'},
            {'name':'tenaya'},
            {'name':'climb x'},
        ]
    )

    # Create an ad-hoc table to use for the insert statement.
    item_table = table('item',
        column('model', String),
        column('brand_id', Integer),
        column('gender_id', Integer)
    )
    # Evolv Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'shaman', 'brand_id':'1', 'gender_id':'1'},
            {'model':'axiom', 'brand_id':'1', 'gender_id':'3'},
            {'model':'defy', 'brand_id':'1', 'gender_id':'3'},
            {'model':'elektra', 'brand_id':'1', 'gender_id':'2'},
            {'model':'royale', 'brand_id':'1', 'gender_id':'1'},
            {'model':'spark', 'brand_id':'1', 'gender_id':'1'},
            {'model':'venga', 'brand_id':'1', 'gender_id':'4'},
            {'model':'rockstar', 'brand_id':'1', 'gender_id':'2'},
            {'model':'elektra vtr', 'brand_id':'1', 'gender_id':'2'},
            {'model':'nikita', 'brand_id':'1', 'gender_id':'2'},
            {'model':'shaman lv', 'brand_id':'1', 'gender_id':'2'},
            {'model':'addict', 'brand_id':'1', 'gender_id':'3'},
            {'model':'kronos', 'brand_id':'1', 'gender_id':'1'},
            {'model':'kira', 'brand_id':'1', 'gender_id':'2'},
            {'model':'defy lace', 'brand_id':'1', 'gender_id':'3'},
            {'model':'astroman', 'brand_id':'1', 'gender_id':'1'},
            {'model':'nexxo', 'brand_id':'1', 'gender_id':'3'},
            {'model':'pontas II', 'brand_id':'1', 'gender_id':'3'},
            {'model':'prime sc', 'brand_id':'1', 'gender_id':'1'},
            {'model':'axiom', 'brand_id':'1', 'gender_id':'1'},
            {'model':'luchador sc', 'brand_id':'1', 'gender_id':'1'},
            {'model':'geshido', 'brand_id':'1', 'gender_id':'1'},
            {'model':'agro', 'brand_id':'1', 'gender_id':'1'},
            {'model':'rasta shaman', 'brand_id':'1', 'gender_id':'1'},
            {'model':'luchador', 'brand_id':'1', 'gender_id':'1'},
            {'model':'raptor', 'brand_id':'1', 'gender_id':'1'},
            {'model':'raven', 'brand_id':'1', 'gender_id':'2'},
        ]
    )

    # 5.10 Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'arrowhead', 'brand_id':'2', 'gender_id':'1'},
            {'model':'anasazi moccasym', 'brand_id':'2', 'gender_id':'1'},
            {'model':'anasazi vcs', 'brand_id':'2', 'gender_id':'1'},
            {'model':'anasazi guide', 'brand_id':'2', 'gender_id':'1'},
            {'model':'anasazi verde', 'brand_id':'2', 'gender_id':'1'},
            {'model':'anasazi high-top', 'brand_id':'2', 'gender_id':'1'},
            {'model':'anasazi lv', 'brand_id':'2', 'gender_id':'2'},
            {'model':'anasazi', 'brand_id':'2', 'gender_id':'1'},
            {'model':'rogue vcs', 'brand_id':'2', 'gender_id':'1'},
            {'model':'rogue vcs', 'brand_id':'2', 'gender_id':'2'},
            {'model':'rogue lace', 'brand_id':'2', 'gender_id':'1'},
            {'model':'rogue lace', 'brand_id':'2', 'gender_id':'2'},
            {'model':'dragon', 'brand_id':'2', 'gender_id':'1'},
            {'model':'stonelands vcs', 'brand_id':'2', 'gender_id':'1'},
            {'model':'stonelands', 'brand_id':'2', 'gender_id':'1'},
            {'model':'blackwing', 'brand_id':'2', 'gender_id':'1'},
            {'model':'blackwing', 'brand_id':'2', 'gender_id':'2'},
            {'model':'siren', 'brand_id':'2', 'gender_id':'2'},
            {'model':'hiangle', 'brand_id':'2', 'gender_id':'1'},
            {'model':'hiangle', 'brand_id':'2', 'gender_id':'2'},
            {'model':'coyote vcs', 'brand_id':'2', 'gender_id':'1'},
            {'model':'coyote vcs', 'brand_id':'2', 'gender_id':'2'},
            {'model':'spire', 'brand_id':'2', 'gender_id':'1'},
            {'model':'team 5.10', 'brand_id':'2', 'gender_id':'1'},
            {'model':'team vxi', 'brand_id':'2', 'gender_id':'1'},
            {'model':'verdon', 'brand_id':'2', 'gender_id':'1'},
            {'model':'verdon vcs', 'brand_id':'2', 'gender_id':'1'},
            {'model':'quantum', 'brand_id':'2', 'gender_id':'1'},
            {'model':'newton', 'brand_id':'2', 'gender_id':'1'},
            {'model':'hueco', 'brand_id':'2', 'gender_id':'1'},
            {'model':'mini mocc', 'brand_id':'2', 'gender_id':'4'},
        ]
    )

    # La Sportiva Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'tarantulace', 'brand_id':'3', 'gender_id':'1'},
            {'model':'tarantulace', 'brand_id':'3', 'gender_id':'2'},
            {'model':'tarantula', 'brand_id':'3', 'gender_id':'1'},
            {'model':'katana lace', 'brand_id':'3', 'gender_id':'1'},
            {'model':'solution', 'brand_id':'3', 'gender_id':'1'},
            {'model':'solution', 'brand_id':'3', 'gender_id':'2'},
            {'model':'oxygym', 'brand_id':'3', 'gender_id':'2'},
            {'model':'oxygym', 'brand_id':'3', 'gender_id':'1'},
            {'model':'nago', 'brand_id':'3', 'gender_id':'2'},
            {'model':'nago', 'brand_id':'3', 'gender_id':'1'},
            {'model':'miura', 'brand_id':'3', 'gender_id':'2'},
            {'model':'miura', 'brand_id':'3', 'gender_id':'1'},
            {'model':'miura vs', 'brand_id':'3', 'gender_id':'2'},
            {'model':'miura vs', 'brand_id':'3', 'gender_id':'1'},
            {'model':'mythos', 'brand_id':'3', 'gender_id':'1'},
            {'model':'mythos', 'brand_id':'3', 'gender_id':'2'},
            {'model':'katana', 'brand_id':'3', 'gender_id':'1'},
            {'model':'katana', 'brand_id':'3', 'gender_id':'2'},
            {'model':'genius', 'brand_id':'3', 'gender_id':'1'},
            {'model':'python', 'brand_id':'3', 'gender_id':'1'},
            {'model':'stickit', 'brand_id':'3', 'gender_id':'4'},
            {'model':'testarossa', 'brand_id':'3', 'gender_id':'1'},
            {'model':'futura', 'brand_id':'3', 'gender_id':'1'},
            {'model':'jeckyl vs', 'brand_id':'3', 'gender_id':'1'},
            {'model':'cobra', 'brand_id':'3', 'gender_id':'1'},
            {'model':'arco', 'brand_id':'3', 'gender_id':'1'},
            {'model':'tc pro', 'brand_id':'3', 'gender_id':'1'},
        ]
    )

    # Mad Rock Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'flash 2.0', 'brand_id':'4', 'gender_id':'1'},
            {'model':'drifter', 'brand_id':'4', 'gender_id':'1'},
            {'model':'mad monkey', 'brand_id':'4', 'gender_id':'4'},
            {'model':'nomad', 'brand_id':'4', 'gender_id':'1'},
            {'model':'m5', 'brand_id':'4', 'gender_id':'1'},
            {'model':'shark', 'brand_id':'4', 'gender_id':'1'},
            {'model':'pulse', 'brand_id':'4', 'gender_id':'1'},
            {'model':'concept 2.0', 'brand_id':'4', 'gender_id':'1'},
            {'model':'phoenix lace', 'brand_id':'4', 'gender_id':'1'},
            {'model':'redline', 'brand_id':'4', 'gender_id':'1'},
            {'model':'lyra', 'brand_id':'4', 'gender_id':'2'},
            {'model':'lotus', 'brand_id':'4', 'gender_id':'2'},
            {'model':'onsight', 'brand_id':'4', 'gender_id':'2'},
            {'model':'demon 2.0', 'brand_id':'4', 'gender_id':'1'},
            {'model':'mugen tech lace', 'brand_id':'4', 'gender_id':'1'},
            {'model':'conflict 2.0', 'brand_id':'4', 'gender_id':'1'},
            {'model':'badger', 'brand_id':'4', 'gender_id':'1'},
            {'model':'contact 2.0', 'brand_id':'4', 'gender_id':'1'},
            {'model':'phoenix', 'brand_id':'4', 'gender_id':'1'},
        ]
    )

    # Scarpa Rock Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'instinct vs', 'brand_id':'5', 'gender_id':'1'},
            {'model':'origin', 'brand_id':'5', 'gender_id':'3'},
            {'model':'vapor v', 'brand_id':'5', 'gender_id':'1'},
            {'model':'vapor v', 'brand_id':'5', 'gender_id':'2'},
            {'model':'helix', 'brand_id':'5', 'gender_id':'1'},
            {'model':'helix', 'brand_id':'5', 'gender_id':'2'},
            {'model':'booster', 'brand_id':'5', 'gender_id':'1'},
            {'model':'force x', 'brand_id':'5', 'gender_id':'1'},
            {'model':'force x', 'brand_id':'5', 'gender_id':'2'},
            {'model':'instinct s', 'brand_id':'5', 'gender_id':'1'},
            {'model':'instinct', 'brand_id':'5', 'gender_id':'1'},
            {'model':'reflex', 'brand_id':'5', 'gender_id':'1'},
            {'model':'reflex', 'brand_id':'5', 'gender_id':'2'},
            {'model':'boostic', 'brand_id':'5', 'gender_id':'1'},
            {'model':'mago', 'brand_id':'5', 'gender_id':'1'},
            {'model':'furia', 'brand_id':'5', 'gender_id':'1'},
            {'model':'techno x', 'brand_id':'5', 'gender_id':'1'},
            {'model':'veloce', 'brand_id':'5', 'gender_id':'1'},
            {'model':'veloce', 'brand_id':'5', 'gender_id':'2'},
            {'model':'sphinx', 'brand_id':'5', 'gender_id':'1'},
            {'model':'feroce', 'brand_id':'5', 'gender_id':'1'},
            {'model':'vision', 'brand_id':'5', 'gender_id':'1'},
            {'model':'stix', 'brand_id':'5', 'gender_id':'1'},
        ]
    )

    # Boreal Rock Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'silex', 'brand_id':'6', 'gender_id':'1'},
            {'model':'silex velcro', 'brand_id':'6', 'gender_id':'1'},
            {'model':'silex', 'brand_id':'6', 'gender_id':'2'},
            {'model':'diabolo', 'brand_id':'6', 'gender_id':'1'},
            {'model':'diabola', 'brand_id':'6', 'gender_id':'2'},
            {'model':'spider', 'brand_id':'6', 'gender_id':'1'},
            {'model':'joker', 'brand_id':'6', 'gender_id':'1'},
            {'model':'joker plus velcro', 'brand_id':'6', 'gender_id':'1'},
            {'model':'joker plus velcro', 'brand_id':'6', 'gender_id':'2'},
            {'model':'joker plus', 'brand_id':'6', 'gender_id':'1'},
            {'model':'joker velcro', 'brand_id':'6', 'gender_id':'1'},
            {'model':'sol', 'brand_id':'6', 'gender_id':'1'},
            {'model':'luna', 'brand_id':'6', 'gender_id':'2'},
            {'model':'q-x', 'brand_id':'6', 'gender_id':'1'},
            {'model':'ninja', 'brand_id':'6', 'gender_id':'1'},
            {'model':'ballet gold', 'brand_id':'6', 'gender_id':'1'},
            {'model':'ace', 'brand_id':'6', 'gender_id':'1'},
            {'model':'zephyr', 'brand_id':'6', 'gender_id':'1'},
            {'model':'ninja junior', 'brand_id':'6', 'gender_id':'4'},
            {'model':'satori', 'brand_id':'6', 'gender_id':'1'},
            {'model':'mutant', 'brand_id':'6', 'gender_id':'1'},
            {'model':'kintaro', 'brand_id':'6', 'gender_id':'1'},
            {'model':'kintaro', 'brand_id':'6', 'gender_id':'2'},
            {'model':'lynx', 'brand_id':'6', 'gender_id':'1'},
            {'model':'lynx', 'brand_id':'6', 'gender_id':'2'},
            {'model':'marduk', 'brand_id':'6', 'gender_id':'1'},
            {'model':'blade', 'brand_id':'6', 'gender_id':'1'},
            {'model':'dharma', 'brand_id':'6', 'gender_id':'1'},
        ]
    )

    # Tenaya Rock Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'iati', 'brand_id':'7', 'gender_id':'1'},
            {'model':'tarifa', 'brand_id':'7', 'gender_id':'1'},
            {'model':'oasi', 'brand_id':'7', 'gender_id':'1'},
            {'model':'ra', 'brand_id':'7', 'gender_id':'1'},
            {'model':'masai', 'brand_id':'7', 'gender_id':'1'},
            {'model':'inti', 'brand_id':'7', 'gender_id':'1'},
            {'model':'tatanka', 'brand_id':'7', 'gender_id':'1'},
        ]
    )

    # Climb X Rock Shoe List
    op.bulk_insert(item_table,
        [
            {'model':'rock star', 'brand_id':'8', 'gender_id':'1'},
            {'model':'red point', 'brand_id':'8', 'gender_id':'1'},
            {'model':'kinder', 'brand_id':'8', 'gender_id':'4'},
            {'model':'icon', 'brand_id':'8', 'gender_id':'1'},
            {'model':'technician lace', 'brand_id':'8', 'gender_id':'1'},
            {'model':'technician strap', 'brand_id':'8', 'gender_id':'1'},
            {'model':'rock-it', 'brand_id':'8', 'gender_id':'1'},
            {'model':'asylum', 'brand_id':'8', 'gender_id':'1'},
            {'model':'red point nlv', 'brand_id':'8', 'gender_id':'1'},
            {'model':'rock master', 'brand_id':'8', 'gender_id':'1'},
            {'model':'crush lace', 'brand_id':'8', 'gender_id':'1'},
            {'model':'rave', 'brand_id':'8', 'gender_id':'1'},
            {'model':'nomad lace', 'brand_id':'8', 'gender_id':'1'},
            {'model':'zion', 'brand_id':'8', 'gender_id':'1'},
            {'model':'e-motion', 'brand_id':'8', 'gender_id':'1'},
            {'model':'e-motion slipper', 'brand_id':'8', 'gender_id':'1'},
        ]
    )

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    op.drop_table('gender')
    op.drop_table('brand')

    op.create_table('brand',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('model', sa.String(length=64), nullable=False),
    sa.Column('gender_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['brand_id'], ['brand.id'], ),
    sa.ForeignKeyConstraint(['gender_id'], ['gender.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###
