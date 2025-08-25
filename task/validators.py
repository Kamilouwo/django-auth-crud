import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class ComplejidadPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(_("La contraseña debe tener al menos 8 caracteres."))
        if not re.search(r'[A-Z]', password):
            raise ValidationError(_("La contraseña debe contener al menos una letra mayúscula."))
        if not re.search(r'[a-z]', password):
            raise ValidationError(_("La contraseña debe contener al menos una letra minúscula."))
        if not re.search(r'\d', password):
            raise ValidationError(_("La contraseña debe contener al menos un número."))
        if not re.search(r'[@$!%*?&]', password):
            raise ValidationError(_("La contraseña debe contener al menos un carácter especial (@$!%*?&)."))

    def get_help_text(self):
        return _("Tu contraseña debe incluir mayúsculas, minúsculas, números y caracteres especiales.")

class MinLengthSpanishValidator:
    def __init__(self, min_length=8):
        self.min_length = min_length

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                _("La contraseña es demasiado corta, debe tener al menos %(min_length)d caracteres."),
                code='password_too_short',
                params={'min_length': self.min_length},
            )

    def get_help_text(self):
        return _("Tu contraseña debe contener al menos %(min_length)d caracteres.") % {'min_length': self.min_length}
