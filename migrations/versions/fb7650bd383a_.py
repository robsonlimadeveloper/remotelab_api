"""empty message

Revision ID: fb7650bd383a
Revises: 
Create Date: 2021-01-24 12:43:43.337959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb7650bd383a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('discipline_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experiments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('url_socket_server', sa.String(length=255), nullable=False),
    sa.Column('url_stream_server', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('features',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('institutes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('code', sa.String(length=45), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=45), nullable=False),
    sa.Column('total_hours', sa.Integer(), nullable=True),
    sa.Column('is_active', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experiment_disciplines',
    sa.Column('id_experiment_fk', sa.Integer(), nullable=False),
    sa.Column('id_discipline_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_discipline_fk'], ['discipline_types.id'], ),
    sa.ForeignKeyConstraint(['id_experiment_fk'], ['experiments.id'], ),
    sa.PrimaryKeyConstraint('id_experiment_fk', 'id_discipline_fk')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=45), nullable=False),
    sa.Column('phone', sa.String(length=45), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('total_hours', sa.Integer(), nullable=True),
    sa.Column('id_user_type_fk', sa.Integer(), nullable=True),
    sa.Column('id_user_institute_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_user_institute_fk'], ['institutes.id'], ),
    sa.ForeignKeyConstraint(['id_user_type_fk'], ['user_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('experiment_sessions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('date_time_begin', sa.DateTime(), nullable=False),
    sa.Column('date_time_end', sa.DateTime(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('id_experiment_fk', sa.Integer(), nullable=False),
    sa.Column('id_user_fk', sa.Integer(), nullable=False),
    sa.Column('id_institute_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_experiment_fk'], ['experiments.id'], ),
    sa.ForeignKeyConstraint(['id_institute_fk'], ['institutes.id'], ),
    sa.ForeignKeyConstraint(['id_user_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id', 'id_experiment_fk', 'id_user_fk', 'id_institute_fk')
    )
    op.create_table('user_experiment',
    sa.Column('id_user_fk', sa.Integer(), nullable=False),
    sa.Column('id_experiment_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_experiment_fk'], ['experiments.id'], ),
    sa.ForeignKeyConstraint(['id_user_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id_user_fk', 'id_experiment_fk')
    )
    op.create_table('user_features',
    sa.Column('id_user_fk', sa.Integer(), nullable=False),
    sa.Column('id_feature_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_feature_fk'], ['features.id'], ),
    sa.ForeignKeyConstraint(['id_user_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id_user_fk', 'id_feature_fk')
    )
    op.create_table('users_institute',
    sa.Column('id_user_fk', sa.Integer(), nullable=False),
    sa.Column('id_institute_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_institute_fk'], ['institutes.id'], ),
    sa.ForeignKeyConstraint(['id_user_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id_user_fk', 'id_institute_fk')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_institute')
    op.drop_table('user_features')
    op.drop_table('user_experiment')
    op.drop_table('experiment_sessions')
    op.drop_table('users')
    op.drop_table('experiment_disciplines')
    op.drop_table('user_types')
    op.drop_table('institutes')
    op.drop_table('features')
    op.drop_table('experiments')
    op.drop_table('discipline_types')
    # ### end Alembic commands ###
