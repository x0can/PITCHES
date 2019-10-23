"""empty message

Revision ID: c62313f9ddd3
Revises: 8fcd574ce2a5
Create Date: 2019-10-22 23:18:27.529571

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c62313f9ddd3'
down_revision = '8fcd574ce2a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.add_column('pitches', sa.Column('actual_pitch', sa.String(), nullable=True))
    op.add_column('pitches', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('pitches', sa.Column('date_posted', sa.DateTime(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'pitch_categories', ['category_id'], ['id'])
    op.drop_column('pitches', 'posted')
    op.drop_column('pitches', 'pitch')
    op.add_column('users', sa.Column('pass_secure', sa.String(length=255), nullable=True))
    op.drop_index('ix_users_username', table_name='users')
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    op.create_index('ix_users_username', 'users', ['username'], unique=True)
    op.drop_column('users', 'pass_secure')
    op.add_column('pitches', sa.Column('pitch', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'date_posted')
    op.drop_column('pitches', 'category_id')
    op.drop_column('pitches', 'actual_pitch')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    # ### end Alembic commands ###
