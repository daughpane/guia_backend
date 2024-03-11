from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class UppercaseValidator(object):
    def validate(self, password, user=None):
        # Check for at least 1 uppercase letter
        if not any(char.isupper() for char in password):
            raise ValidationError(
                _("The password must contain at least one uppercase letter."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter."
        )

class NumericValidator(object):
    def validate(self, password, user=None):
        # Check for at least 1 number
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                _("The password must contain at least one digit."),
                code='password_no_digit',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit."
        )

class SpecialCharacterValidator(object):
    def validate(self, password, user=None):
        # Check for at least 1 special character
        special_characters = "!@#$%&"
        if not any(char in special_characters for char in password):
            raise ValidationError(
                _("The password must contain at least one special character: !@#$%&"),
                code='password_no_special',
            )
    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character: !@#$%&"
        )

class UnderscoreValidator(object):
    def validate(self, password, user=None):
        # Check for at most 1 underscore, embedded
        if password.count('_') > 1 or password[0]=='_' or password[len(password)-1]=='_':
            raise ValidationError(
                _("The password can have at most one underscore, embedded."),
                code='password_too_many_underscores',
            )
    def get_help_text(self):
        return _(
            "Your password can have at most one underscore, embedded."
        )

class LengthValidator(object):
    def validate(self, password, user=None):
        # Check for at most 1 underscore, embedded
        if len(password)<8:
            raise ValidationError(
                _("The password must have at least 8 characters."),
                code='password_few_characters',
            )
    def get_help_text(self):
        return _(
            "Your password must have at least 8 characters."
        )