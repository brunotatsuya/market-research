"""empty message

Revision ID: 48700093bcbf
Revises: 23a14aaec65b
Create Date: 2024-08-02 21:49:45.039985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '48700093bcbf'
down_revision: Union[str, None] = '23a14aaec65b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('serp_analysis_items', 'url',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('serp_analysis_items', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('serp_analysis_items', 'domain',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('serp_analysis_items', 'position',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('serp_analysis_items', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('serp_analysis_items', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('serp_analysis_items', 'position',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('serp_analysis_items', 'domain',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('serp_analysis_items', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('serp_analysis_items', 'url',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
