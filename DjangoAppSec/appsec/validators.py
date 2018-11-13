from django.core.exceptions import ValidationError

class CustomPasswortValidator:

    def validate(value):

      # check for digit
      if not any(char.isdigit() for char in value):
          raise ValidationError(_('Password must contain at least 1 digit.'))

      # check for letter
      if not any(char.isalpha() for char in value):
          raise ValidationError(_('Password must contain at least 1 letter.'))

      # check for special character
      special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
      if any(char in special_characters for char in value):
        raise ValidationError(_('Password cannot contain special characters'))