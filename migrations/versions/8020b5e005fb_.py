"""empty message

Revision ID: 8020b5e005fb
Revises: 
Create Date: 2020-04-25 01:26:53.857138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8020b5e005fb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pid_controller',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=180), nullable=True),
    sa.Column('P', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('I', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('D', sa.DECIMAL(precision=10, scale=2), nullable=True),
    sa.Column('mode', sa.Enum('Manual', 'Auto', 'Master'), nullable=True),
    sa.Column('output_port', sa.String(length=150), nullable=True),
    sa.Column('input_port', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pid_controller')
    # ### end Alembic commands ###