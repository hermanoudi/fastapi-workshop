"""social

Revision ID: 2a6e9045634e
Revises: 0fc51edfb5e2
Create Date: 2022-12-07 00:18:21.781894

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '2a6e9045634e'
down_revision = '0fc51edfb5e2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('social', sa.Column('to_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'social', 'user', ['to_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'social', type_='foreignkey')
    op.drop_column('social', 'to_id')
    # ### end Alembic commands ###
