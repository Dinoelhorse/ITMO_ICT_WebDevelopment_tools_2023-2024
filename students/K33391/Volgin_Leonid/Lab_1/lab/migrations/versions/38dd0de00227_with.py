"""with

Revision ID: 38dd0de00227
Revises: b0599cc706b8
Create Date: 2024-05-20 14:37:34.892276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '38dd0de00227'
down_revision: Union[str, None] = 'b0599cc706b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('wishlist', sa.Column('aboba', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('wishlist', 'aboba')
    # ### end Alembic commands ###
