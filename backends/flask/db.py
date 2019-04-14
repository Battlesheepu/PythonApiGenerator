from shared import DbComponent


class FlaskSqlalchemy(DbComponent):
    dependencies = [
        'Flask-SQLAlchemy'
    ]

    output_files = [
        {
            'filename': 'app/db.py',
            'template': 'db-templates/sqlalchemy-templates/db.py.j2'
        },
        {
            'filename': 'app/models.py',
            'template': 'db-templates/sqlalchemy-templates/models.py.j2'
        },
    ]
