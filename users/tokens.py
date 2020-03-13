from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()

class PasswordTokenGenerator(PasswordResetTokenGenerator):
    def _make_password_token(self, user):
        return(
            six.text_type(user.pk) + six.text_type(timestamp)
        )
password_reset_token = PasswordTokenGenerator()
