"""remove prompt builder models from db

Revision ID: 47bdbd48cf42
Revises: 41f01cf84cc3
Create Date: 2024-01-11 13:34:47.055765

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '47bdbd48cf42'
down_revision: Union[str, None] = '41f01cf84cc3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prompt_style_category')
    op.drop_table('prompt_option')
    op.drop_table('prompt_variables')
    op.drop_table('prompt_variable_category')
    op.drop_table('prompt_category')
    op.drop_table('prompt_variable_category_weight')
    op.drop_table('prompts')
    op.drop_table('prompt_style')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prompt_style',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('style_category_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['style_category_id'], ['prompt_style_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prompts',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('category_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['prompt_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prompt_variable_category_weight',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('weight', sa.FLOAT(), nullable=True),
    sa.Column('prompt_category_id', sa.INTEGER(), nullable=True),
    sa.Column('variable_category_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['prompt_category_id'], ['prompt_category.id'], ),
    sa.ForeignKeyConstraint(['variable_category_id'], ['prompt_variable_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prompt_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('negative_prompt', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prompt_variable_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prompt_variables',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('value', sa.VARCHAR(), nullable=True),
    sa.Column('prompt_category_id', sa.INTEGER(), nullable=True),
    sa.Column('variable_category_id', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['prompt_category_id'], ['prompt_category.id'], ),
    sa.ForeignKeyConstraint(['variable_category_id'], ['prompt_variable_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prompt_option',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('prompt_id', sa.INTEGER(), nullable=True),
    sa.Column('text', sa.VARCHAR(), nullable=True),
    sa.Column('cond', sa.VARCHAR(), nullable=True),
    sa.Column('else_cond', sa.VARCHAR(), nullable=True),
    sa.Column('or_cond', sa.VARCHAR(), nullable=True),
    sa.Column('next_cond_id', sa.INTEGER(), nullable=True),
    sa.Column('next_cond', sa.INTEGER(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.ForeignKeyConstraint(['next_cond'], ['prompt_option.id'], ),
    sa.ForeignKeyConstraint(['next_cond_id'], ['prompt_option.id'], ),
    sa.ForeignKeyConstraint(['prompt_id'], ['prompts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('prompt_style_category',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('negative_prompt', sa.VARCHAR(), nullable=True),
    sa.Column('created_at', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
