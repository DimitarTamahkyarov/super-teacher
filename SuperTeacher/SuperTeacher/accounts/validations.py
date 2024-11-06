from django.core.exceptions import ValidationError


def validate_file_size(image):
    if image.size > 2 * 1024 * 1024:
        raise ValidationError('The maximum size that can be uploaded is 2MB')