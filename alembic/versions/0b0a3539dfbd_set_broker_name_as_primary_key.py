"""Set broker name as primary key

Revision ID: 0b0a3539dfbd
Revises: b86db2ce3893
Create Date: 2025-06-29 20:39:43.884454

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0b0a3539dfbd'
down_revision: Union[str, Sequence[str], None] = 'b86db2ce3893'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('broker', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('broker', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###
