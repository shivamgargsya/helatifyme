
from fabric.api import local, settings, task
from app_db import db
from sqlalchemy import DDL


@task
def new():
    """Creates an empty, tableless database"""
    import os
    local("PGPASSWORD=%s createdb -h %s -p %s -U %s %s" % (
        os.environ.get('DATABASE_PASSWORD'),
        os.environ.get('DATABASE_HOST'),
        os.environ.get('DATABASE_PORT'),
        os.environ.get('DATABASE_USER'),
        os.environ.get('DATABASE_NAME')
    ))


@task
def create():
    """Creates a new db and builds tables (short-circuiting migrations)"""
    db.engine.execute(DDL("CREATE SCHEMA IF NOT EXISTS hora"))
    db.create_all()


@task
def drop():
    import os
    """Drops database named in .env"""

    with settings(warn_only=True):
        local("PGPASSWORD=%s dropdb -h %s -p %s -U %s %s" % (
            os.environ.get('DATABASE_PASSWORD'),
            os.environ.get('DATABASE_HOST'),
            os.environ.get('DATABASE_PORT'),
            os.environ.get('DATABASE_USER'),
            os.environ.get('DATABASE_NAME')
        ))


@task
def reset():
    """Drops, creates, and seeds a new DB"""
    with settings(warn_only=True):
        drop()
        new()
    create()


@task
def setup():
    """Takes an existing DB and reforms/reseeds it.

    Better than reset for use with EB instances, or when the db is
    being accessed.

    """
    from .db import db
    conn = db.engine.connect()
    conn.execute("commit;")
    conn.execute("drop schema hora cascade;")
    conn.execute("create schema hora;")
    db.session.rollback()
    db.create_all()

