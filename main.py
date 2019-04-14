# -*- coding: utf-8 -*-
import os

from jinja2 import Environment, FileSystemLoader

# This should be loaded dynamically, depending on the choices
# made by the user. Currently it doesn't matter, as only
# one option per Component type is available.

env = Environment(loader=FileSystemLoader('./templates'))

app_name = 'testujemy'


from backends.flask import backend, db, serializers


class Project:
    def __init__(self, app_name, backend_component, db_component, serializer_component):
        self.app_name = app_name
        self.app_dir_path = os.path.join(os.getcwd(), app_name)
        self.backend_component = backend_component
        self.db_component = db_component
        self.serializer_component = serializer_component

    def get_path_for(self, file_name):
        return os.path.join(self.app_dir_path, file_name)

    def prepare_structure(self):
        self.backend_component.render_files(self.app_dir_path)
        self.db_component.render_files(self.app_dir_path)
        self.serializer_component.render_files(self.app_dir_path)

    def prepare_requirements_file(self):
        with open(self.get_path_for('requirements.txt'), 'w') as req_file:
            req_file.write(self.backend_component.get_dependencies_for_requirements())
            req_file.write('\n')
            req_file.write(self.db_component.get_dependencies_for_requirements())
            req_file.write('\n')
            req_file.write(self.serializer_component.get_dependencies_for_requirements())
            req_file.write('\n')

    def create_project(self):
        os.mkdir(self.app_dir_path)

        self.prepare_requirements_file()
        self.prepare_structure()
        print('App "{app_name}" "created in "{app_dir_path}".'.format(app_name=self.app_name, app_dir_path=self.app_dir_path))


project = Project(app_name, backend.Flask, db.FlaskSqlalchemy, serializers.MarshmallowJsonapi)

project.create_project()