from django.core.exceptions import ValidationError


def validate_content(value):
    content = value
    if content == "abc":
        raise ValidationError(" El contenido No puede ser ABC desde validador externo")
    return value