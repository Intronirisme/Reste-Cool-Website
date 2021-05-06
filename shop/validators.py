from django.core.exceptions import ValidationError

def stripScripts(value):
    if value.find('<script') != -1:
        raise ValidationError("No script allowed")
    else:
        return value