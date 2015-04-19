"""create users table

Revision ID: 1343dd270387
Revises: None
Create Date: 2015-04-18 14:15:42.819059

"""

# revision identifiers, used by Alembic.
revision = '1343dd270387'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False, unique=True),
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('first_name', sa.String(length=255)),
        sa.Column('last_name', sa.String(length=255)),
        sa.Column('created_at', sa.DateTime(timezone=True)),

        sa.Column('active', sa.Boolean()),
        sa.Column('staff', sa.Boolean()),
        sa.Column('superuser', sa.Boolean()),

        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
    )


def downgrade():
    op.drop_table('users')
