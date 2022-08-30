"""create phone_number for column users

Revision ID: 2726c362e945
Revises: 
Create Date: 2022-08-29 00:16:29.736333

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2726c362e945'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=True))


def downgrade():
    op.drop_column('users', 'phone_number')
