"""add_client_table

Revision ID: 6359fdb36f27
Revises: bfd46d3661df
Create Date: 2022-07-12 11:32:54.435484

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '6359fdb36f27'
down_revision = 'bfd46d3661df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('delete_at', sa.DateTime(), nullable=True),
    sa.Column('uuid', postgresql.UUID(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('inn', sa.Text(), nullable=True),
    sa.Column('kpp', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('photo', sa.Text(), nullable=True),
    sa.Column('phone', sa.Text(), nullable=True),
    sa.Column('email', sa.Text(), nullable=True),
    sa.Column('license_id', sa.Integer(), nullable=True),
    sa.Column('photo_url', sa.Text(), nullable=True),
    sa.Column('create_user_id', sa.Integer(), nullable=True),
    sa.Column('update_user_id', sa.Integer(), nullable=True),
    sa.Column('delete_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['create_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['delete_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['license_id'], ['licenses.id'], ),
    sa.ForeignKeyConstraint(['update_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_clients_name'), 'clients', ['name'], unique=False)
    op.add_column('licenses', sa.Column('license_id', sa.Integer(), nullable=True))
    op.drop_constraint('licenses_group_id_fkey', 'licenses', type_='foreignkey')
    op.create_foreign_key(None, 'licenses', 'licenses', ['license_id'], ['id'])
    op.drop_column('licenses', 'group_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('licenses', sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'licenses', type_='foreignkey')
    op.create_foreign_key('licenses_group_id_fkey', 'licenses', 'licenses', ['group_id'], ['id'])
    op.drop_column('licenses', 'license_id')
    op.drop_index(op.f('ix_clients_name'), table_name='clients')
    op.drop_table('clients')
    # ### end Alembic commands ###
