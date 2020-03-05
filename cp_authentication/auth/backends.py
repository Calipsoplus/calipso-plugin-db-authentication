import hashlib
import logging

from cp_authentication.models.auth_external_model import AuthDatabaseUser


class ExternalDatabaseAuthenticationBackend:
    logger = logging.getLogger(__name__)

    def authenticate(self, request, username=None, password=None):
        self.logger.info('Attempting to authenticate via external_db')
        try:
            if None in (username, password):
                self.logger.warning('Tried to authenticate user with missing fields, rejecting')
                return None

            # Fetch user from external_db
            self.logger.debug('Authenticating %s', username)
            try:
                auth_user = AuthDatabaseUser.objects.using('external_db').get(login=username)

                # Hash password
                hash = hashlib.md5()
                hash.update(password.encode('utf-8'))
                hashed_pass = hash.hexdigest()

                # Check match
                if hashed_pass == auth_user.password:
                    self.logger.info('Authenticated %s', username)
                    return auth_user
                return None

            except Exception as e:
                self.logger.error('%s not found in external_db', username)
                return None
        except Exception as e:
            self.logger.error(e)
            raise e


