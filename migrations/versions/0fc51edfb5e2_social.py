"""social

Revision ID: 0fc51edfb5e2
Revises: 38a4f934dc2a
Create Date: 2022-12-07 00:15:33.471140

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '0fc51edfb5e2'
down_revision = '38a4f934dc2a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('social',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['from_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('social')
    # ### end Alembic commands ###
