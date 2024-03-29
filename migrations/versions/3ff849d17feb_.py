"""empty message

Revision ID: 3ff849d17feb
Revises: 
Create Date: 2019-07-24 20:36:12.593477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ff849d17feb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('office_name', sa.String(), nullable=False),
    sa.Column('age_limit', sa.String(), nullable=False),
    sa.Column('office_type', sa.Enum('federal', 'legislative', 'local_government', 'state', name='officetype'), nullable=True),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('status', sa.Enum('new', 'updated', name='office_status'), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.Column('updated_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('office_name')
    )
    op.create_table('parties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('party_name', sa.String(), nullable=False),
    sa.Column('hq_address', sa.String(), nullable=False),
    sa.Column('logo_url', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('new', 'updated', name='party_status'), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.Column('updated_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('party_name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('other_names', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('picture', sa.String(), nullable=True),
    sa.Column('user_type', sa.Enum('admin', 'politician', 'citizen', name='usertype'), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.Column('updated_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('parties')
    op.drop_table('offices')
    # ### end Alembic commands ###
