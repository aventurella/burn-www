from burnlib.core.models import Model


class User(Model):

    # @classmethod
    # def from_blitz_auth(cls, auth):
    #     gpghome = settings.data['bigmethod:crypt']['gpg.home']
    #     crypt = CryptService(GPGCrypt.from_params(gpghome))
    #     data = json.loads(crypt.base64_decrypt(auth))

    #     if not data['ok']:
    #         raise ValueError(', '.join(data['errors']))

    #     user = cls()
    #     user.email = data['email']
    #     user.username = data['username']
    #     user.first_name = data['first_name']
    #     user.last_name = data['last_name']

    #     extras = UserExtra()
    #     extras.blitz_id = data['id']

    #     user.extras = extras

    #     return user

    def __init__(self):
        self.id = None
        self.username = None
        self.extras = None


class UserExtra(Model):
    def __init__(self):
        self.user = None
        self.game_center_id = None
