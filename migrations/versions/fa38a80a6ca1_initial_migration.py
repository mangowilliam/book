"""Initial Migration

Revision ID: fa38a80a6ca1
Revises: 0d61de3baca7
Create Date: 2019-07-11 14:18:40.775055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa38a80a6ca1'
down_revision = '0d61de3baca7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('location', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('preferences', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'preferences')
    op.drop_column('users', 'location')
    # ### end Alembic commands ###
