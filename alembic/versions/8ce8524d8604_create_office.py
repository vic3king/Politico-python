"""create office

Revision ID: 8ce8524d8604
Revises: 41175f4bde73
Create Date: 2019-07-20 05:29:08.302730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ce8524d8604'
down_revision = '41175f4bde73'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'offices',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('office_name', sa.String(), nullable=False),
        sa.Column('age_limit', sa.Integer(), nullable=False),
        sa.Column('office_type', sa.String(), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Column('created_at', sa.String(), nullable=False),
        sa.Column('updated_at', sa.String(), nullable=False),
        sa.UniqueConstraint('office_name')
    )


def downgrade():
    op.drop_table('offices')
