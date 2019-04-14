import os
from abc import ABC, abstractmethod

from jinja2 import Environment, FileSystemLoader


class Component(ABC):
    env = Environment(loader=FileSystemLoader('./templates'))
    dependencies = []

    @classmethod
    def get_dependencies_for_requirements(cls):
        subclasses = cls.__subclasses__()

        dependencies = set()
        for subclass in subclasses:
            for dep in subclass.dependencies:
                dependencies.add(dep)
        return '\n'.join(dependencies)

    @classmethod
    def render_files(cls, app_dir_path):
        for output in cls.output_files:
            template = cls.env.get_template(output['template'])
            content = template.render()

            with open(os.path.join(app_dir_path, output['filename']), 'w') as final_file:
                final_file.write(content)

class BackendComponent(Component):
    layer = 'backend'


class DbComponent(Component):
    layer = 'db'


class SerializerComponent(Component):
    layer = 'serializer'
