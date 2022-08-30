"""add apt num column

Revision ID: 6ddfeab81d40
Revises: a9332041cedf
Create Date: 2022-08-29 01:22:46.525387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ddfeab81d40'
down_revision = 'a9332041cedf'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('address', sa.Column('apt_num', sa.Integer(), nullable=True))


def downgrade():
    op.drop_column('address', 'apt_num')
