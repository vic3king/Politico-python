"""User Model

Revision ID: 04ad8b0650ea
Revises: 
Create Date: 2019-07-12 04:31:15.007439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04ad8b0650ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=False),
        sa.Column('last_name', sa.String(), nullable=False),
        sa.Column('other_names', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('picture', sa.String(), nullable=True),
        sa.Column('user_type', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Column('created_at', sa.String(), nullable=False),
        sa.Column('updated_at', sa.String(), nullable=False),
        sa.UniqueConstraint('email')
    )


def downgrade():
    op.drop_table('users')
