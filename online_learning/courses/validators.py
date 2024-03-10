from rest_framework import serializers


def validator_youtube(value):
    if value.startswith('https://www.youtube.com/'):
        raise serializers.ValidationError('ссылка только на youtube')
