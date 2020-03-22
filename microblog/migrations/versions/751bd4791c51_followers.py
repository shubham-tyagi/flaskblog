"""followers

Revision ID: 751bd4791c51
Revises: a0d64a5e2c92
Create Date: 2020-02-16 19:02:12.244911

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '751bd4791c51'
down_revision = 'a0d64a5e2c92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###