from dateutil.parser import parse

from rest_framework import serializers


def ValidateDate(date):
    try:
        date = parse(date)
    except Exception:
        raise serializers.ValidationError(
            {
                'error': 'Invalid date format'
            }
        )
    if date.day != 1:
        raise serializers.ValidationError(
            {
                'error': 'The day of the date must be one.'
            }
        )
