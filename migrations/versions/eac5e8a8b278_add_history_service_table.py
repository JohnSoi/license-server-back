"""add_history_service_table

Revision ID: eac5e8a8b278
Revises: c683b4f5a2bf
Create Date: 2022-07-12 11:25:11.321997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eac5e8a8b278'
down_revision = 'c683b4f5a2bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('history_service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('delete_at', sa.DateTime(), nullable=True),
    sa.Column('object_id', sa.Integer(), nullable=True),
    sa.Column('type', sa.Text(), nullable=True),
    sa.Column('area', sa.Text(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_history_service_area'), 'history_service', ['area'], unique=False)
    op.create_index(op.f('ix_history_service_text'), 'history_service', ['text'], unique=False)
    op.create_index(op.f('ix_history_service_type'), 'history_service', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_history_service_type'), table_name='history_service')
    op.drop_index(op.f('ix_history_service_text'), table_name='history_service')
    op.drop_index(op.f('ix_history_service_area'), table_name='history_service')
    op.drop_table('history_service')
    # ### end Alembic commands ###
