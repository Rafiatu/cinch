from app.action import Action


class LogoutAction(Action):
    arguments = ['request']

    def perform(self):
        user = self.request.user

        if not user:
            self.fail(dict(unrecognized_token='Your token was not recognized by the system.'))

        user.auth_token.delete()
        return dict(logged_out='You have been successfully logged out. Please login to get a new token.')
