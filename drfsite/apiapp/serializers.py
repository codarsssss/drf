from rest_framework import serializers
from .models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'software', 'version')


# class DataSerializer(serializers.Serializer):
#     id = serializers.CharField(max_length=255)
#     software = serializers.CharField()
#     version = serializers.CharField()
#
#     def create(self, validated_data):
#         return Data.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = instance.id
#         instance.software = validated_data.get('software', instance.software)
#         instance.version = validated_data.get('version', instance.version)
#         instance.save()
#         return instance
