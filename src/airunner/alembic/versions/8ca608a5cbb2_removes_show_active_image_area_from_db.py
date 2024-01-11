"""removes show_active_image_area from db

Revision ID: 8ca608a5cbb2
Revises: 521e5b4bf13b
Create Date: 2024-01-11 10:27:26.776270

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ca608a5cbb2'
down_revision: Union[str, None] = '521e5b4bf13b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'show_active_image_area')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('show_active_image_area', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###
