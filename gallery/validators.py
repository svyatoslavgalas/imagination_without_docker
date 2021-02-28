from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.file.size
    if file_size > 2 * 1024 * 1024:
       raise ValidationError('Файл должен быть не больше 2 мб')
