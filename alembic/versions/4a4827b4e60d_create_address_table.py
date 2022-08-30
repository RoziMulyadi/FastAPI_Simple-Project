"""create address table

Revision ID: 4a4827b4e60d
Revises: 2726c362e945
Create Date: 2022-08-29 00:26:58.485687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a4827b4e60d'
down_revision = '2726c362e945'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'address',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('address1', sa.String(), nullable=False),
        sa.Column('address2', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('state', sa.String(), nullable=False),
        sa.Column('country', sa.String(), nullable=False),
        sa.Column('postalcode', sa.String(), nullable=False),
    )


def downgrade():
    op.drop_table('address')
