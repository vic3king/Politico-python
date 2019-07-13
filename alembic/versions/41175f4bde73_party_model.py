"""Party Model

Revision ID: 41175f4bde73
Revises: 04ad8b0650ea
Create Date: 2019-07-12 04:35:43.945945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41175f4bde73'
down_revision = '04ad8b0650ea'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'parties',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('party_name', sa.String(), nullable=False),
        sa.Column('hq_address', sa.String(), nullable=False),
        sa.Column('logo_url', sa.String(), nullable=False),
        sa.Column('status', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.Column('created_at', sa.String(), nullable=False),
        sa.Column('updated_at', sa.String(), nullable=False),
        sa.UniqueConstraint('party_name')
    )


def downgrade():
    op.drop_table('parties')
