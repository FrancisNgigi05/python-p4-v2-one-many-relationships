"""Deleted unwanted table

Revision ID: 044b2ec06a13
Revises: 910474d6adeb
Create Date: 2024-04-10 12:03:27.700953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '044b2ec06a13'
down_revision = '910474d6adeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tests')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###