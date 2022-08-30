"""create address_id to users

Revision ID: a9332041cedf
Revises: 4a4827b4e60d
Create Date: 2022-08-29 00:33:19.288829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9332041cedf'
down_revision = '4a4827b4e60d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users", referent_table="address",
                          local_cols=['address_id'], remote_cols=['id'], ondelete='CASCADE'
                          )


def downgrade():
    op.drop_constraint('address_users_fk', table_name='users')
    op.drop_column('users', 'address_id')
