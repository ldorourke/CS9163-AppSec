from django.core.exceptions import ValidationError

class CustomPasswortValidator:

    def validate(value):

      #Protect against brute force attacks
      common_passwords = [line.rstrip('\n') for line in open('/home/djangoappsec/appsec/data/commonPasswords.txt')]
      if value in common_passwords:
        raise ValidationError(_('The password is too common.'))

      #Protect against SQL injections
      special_characters = "[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]"
      if any(char in special_characters for char in value):
        raise ValidationError(_('Password cannot contain special characters'))