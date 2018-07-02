# Serializers define the API representation.
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'is_staff','first_name')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_staff=False)
    serializer_class = UserSerializer
    http_method_names = ('post', 'get', 'put', 'patch')
    permission_classes = []

