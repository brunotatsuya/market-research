"""Add domain metrics to serp analysis item table

Revision ID: d68be93770c0
Revises: ad2c0afc4dcd
Create Date: 2024-08-21 21:32:11.910076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'd68be93770c0'
down_revision: Union[str, None] = 'ad2c0afc4dcd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('serp_analysis_items', sa.Column('backlinks', sa.Integer(), nullable=True))
    op.add_column('serp_analysis_items', sa.Column('referring_domains', sa.Integer(), nullable=True))
    op.add_column('serp_analysis_items', sa.Column('nofollow_backlinks', sa.Integer(), nullable=True))
    op.add_column('serp_analysis_items', sa.Column('dofollow_backlinks', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('serp_analysis_items', 'dofollow_backlinks')
    op.drop_column('serp_analysis_items', 'nofollow_backlinks')
    op.drop_column('serp_analysis_items', 'referring_domains')
    op.drop_column('serp_analysis_items', 'backlinks')
    # ### end Alembic commands ###
