import os

from backends.flask.db import FlaskSqlalchemy
from backends.flask.serializers import MarshmallowJsonapi
from shared import BackendComponent


class Flask(BackendComponent):
    dependencies = [
        'flask'
    ]

    includes = [
        FlaskSqlalchemy, MarshmallowJsonapi
    ]

    output_files = [
        {
            'filename': 'app/__init__.py',
            'template': 'flask-templates/__init__.py.j2'
        },
        {
            'filename': 'app/views.py',
            'template': 'flask-templates/views.py.j2'
        },
        {
            'filename': 'app/config.py',
            'template': 'flask-templates/config.py.j2'
        }
    ]

    @classmethod
    def render_files(cls, app_dir_path):
        os.mkdir(os.path.join(app_dir_path, 'app'))
        return super().render_files(app_dir_path)