"""removes current tool from db

Revision ID: 9967c64348be
Revises: c3fe2868537d
Create Date: 2024-01-11 11:02:14.638144

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9967c64348be'
down_revision: Union[str, None] = 'c3fe2868537d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('settings', 'current_tool')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('current_tool', sa.VARCHAR(), nullable=True))
    # ### end Alembic commands ###
