"""Create exam and exam question tables.

Revision ID: fd27cccb76f7
Revises: 34a134ab27ba
Create Date: 2017-11-27 11:37:54.705955

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd27cccb76f7'
down_revision = '34a134ab27ba'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('exam',
                    sa.Column('id',sa.Integer,primary_key=True),
                    sa.Column('slug',sa.String,nullable=False))

    op.create_table('exam_question',
                    sa.Column('slug',sa.String,nullable=False),
                    sa.Column('question_id',sa.Integer,sa.ForeignKey('question.id'),nullable=True),
                    sa.Column('exam_id',sa.Integer,sa.ForeignKey('exam.id'),nullable=False))

def downgrade():
    op.drop_table('exam_question')
    op.drop_table('exam')
