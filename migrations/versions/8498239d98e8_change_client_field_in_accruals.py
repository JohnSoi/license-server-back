"""change_client_field_in_accruals

Revision ID: 8498239d98e8
Revises: 6d84be9b6950
Create Date: 2022-07-31 16:43:39.605434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8498239d98e8'
down_revision = '6d84be9b6950'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accruals', sa.Column('client_id', sa.Integer(), nullable=True))
    op.drop_constraint('accruals_client_uuid_fkey', 'accruals', type_='foreignkey')
    op.create_foreign_key(None, 'accruals', 'clients', ['client_id'], ['id'])
    op.drop_column('accruals', 'client_uuid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accruals', sa.Column('client_uuid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'accruals', type_='foreignkey')
    op.create_foreign_key('accruals_client_uuid_fkey', 'accruals', 'clients', ['client_uuid'], ['id'])
    op.drop_column('accruals', 'client_id')
    # ### end Alembic commands ###
