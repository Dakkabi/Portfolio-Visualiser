"""Increase char size for password hashes to 255 and convert data blobs (encrypted api keys) to TEXT

Revision ID: dc5e8fb07590
Revises: 79891ed2f5bc
Create Date: 2025-07-05 20:04:04.536112

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc5e8fb07590'
down_revision: Union[str, Sequence[str], None] = '79891ed2f5bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('api_keys', 'api_key',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Text(),
               existing_nullable=False)
    op.alter_column('api_keys', 'private_key',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.Text(),
               existing_nullable=False)
    op.create_unique_constraint(None, 'brokers', ['name'])
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=255),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.drop_constraint(None, 'brokers', type_='unique')
    op.alter_column('api_keys', 'private_key',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    op.alter_column('api_keys', 'api_key',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=128),
               existing_nullable=False)
    # ### end Alembic commands ###
