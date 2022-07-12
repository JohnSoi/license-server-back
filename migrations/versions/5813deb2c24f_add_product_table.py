"""add_product_table

Revision ID: 5813deb2c24f
Revises: 6359fdb36f27
Create Date: 2022-07-12 11:34:08.436242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5813deb2c24f'
down_revision = '6359fdb36f27'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.Column('delete_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('license_id', sa.Integer(), nullable=True),
    sa.Column('photo_url', sa.Text(), nullable=True),
    sa.Column('create_user_id', sa.Integer(), nullable=True),
    sa.Column('update_user_id', sa.Integer(), nullable=True),
    sa.Column('delete_user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['create_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['delete_user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['license_id'], ['licenses.id'], ),
    sa.ForeignKeyConstraint(['update_user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_products_name'), 'products', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_name'), table_name='products')
    op.drop_table('products')
    # ### end Alembic commands ###
