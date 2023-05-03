from rest_framework.serializers import Serializer,CharField


class LinkSerializer(Serializer):
    link = CharField(required=True,min_length = 10)
    