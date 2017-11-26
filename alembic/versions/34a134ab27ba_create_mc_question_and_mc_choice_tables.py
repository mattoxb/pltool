"""Create mc question and mc choice tables.

Revision ID: 34a134ab27ba
Revises: 
Create Date: 2017-11-26 17:07:02.995175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34a134ab27ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('mc_question',
            sa.Column('id',sa.Integer,primary_key=True),
            sa.Column('slug',sa.String(80),nullable=False),
            sa.Column('uuid',sa.String(80),nullable=False),
            sa.Column('text',sa.String,nullable=False))
    op.create_table('mc_choices',
            sa.Column('id',sa.Integer,primary_key=True),
            sa.Column('mc_question_id',sa.Integer,sa.ForeignKey('mc_question.id')),
            sa.Column('number',sa.Integer,nullable=False),
            sa.Column('correct',sa.Boolean,nullable=False))

def downgrade():
    pass
