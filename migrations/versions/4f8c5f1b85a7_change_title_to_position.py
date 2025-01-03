"""change_title_to_position

Revision ID: 4f8c5f1b85a7
Revises: 
Create Date: 2025-01-03 12:33:41.253564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f8c5f1b85a7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('position', sa.String(length=100), nullable=True))
        batch_op.drop_column('organization')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('organization', sa.VARCHAR(length=200), nullable=True))
        batch_op.drop_column('position')

    # ### end Alembic commands ###
