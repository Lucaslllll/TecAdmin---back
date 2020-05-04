from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

# verification of my tokens tables
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )
account_activation_token = TokenGenerator()


# check_token(user, kwargs['token'])
# make_token(table)
