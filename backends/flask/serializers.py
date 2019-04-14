from shared import SerializerComponent


class MarshmallowJsonapi(SerializerComponent):
    dependencies = [
        'marshmallow-jsonapi'
    ]

    output_files = [
        {
            'filename': 'app/serializers.py',
            'template': 'serializer-templates/marshmallow-templates/marshmallow-jsonapi.py.j2'
        }
    ]
