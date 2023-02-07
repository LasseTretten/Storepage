from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_nobb(nobb):
    if len(str(nobb)) != 8:
        raise ValidationError(_('Nobb number consist of 8 digits.'))
