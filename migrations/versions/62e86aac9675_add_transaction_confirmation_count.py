from alembic import op
import sqlalchemy as sa

revision = '62e86aac9675'
down_revision = 'cd6076e578ca'
branch_labels = None
depends_on = None

def upgrade():
	op.add_column('transaction', sa.Column('confirmations', sa.Integer(), nullable=False, server_default='0'))
	op.add_column('unconfirmed_transaction', sa.Column('confirmations', sa.Integer(), nullable=False, server_default='0'))

def downgrade():
	op.drop_column('transaction', 'confirmations')
	op.drop_column('unconfirmed_transaction', 'confirmations')
