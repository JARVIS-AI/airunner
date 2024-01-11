"""removes current_version_stablediffusion from db

Revision ID: 4f6c367d8ffc
Revises: 0d6cd68b9c33
Create Date: 2024-01-11 11:11:40.023476

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f6c367d8ffc'
down_revision: Union[str, None] = '0d6cd68b9c33'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'current_version_stablediffusion')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('current_version_stablediffusion', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
