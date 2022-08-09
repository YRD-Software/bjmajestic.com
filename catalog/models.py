from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


def validate_file_extension(value):
    """validate_file_extension validates the file extension of the uploaded file

    Args:
        value: represents the uploaded file

    Raises:
        ValidationError: is the file extension is not .pdf or .jpg, raises a validation error
    """
    import os
    extension = os.path.splitext(value.name)[1]
    if not extension in ['.pdf']:
        raise ValidationError(u'Unsupported file extension.')


class Catalog(models.Model):
    """Catalog defines a catalog file for a given year.

    Args:
        models (models): provide fields for the model.
    """
    year = models.SmallIntegerField(unique=True)
    file = models.FileField(upload_to='catalogs/%Y/',
                            validators=[validate_file_extension])
