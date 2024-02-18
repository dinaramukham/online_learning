from rest_framework import serializers


def validator_youtube(value):
    if 'youtube.com' in value:
        raise serializers.ValidationError('ссылка только на youtube')
