import Model.login as ml


class LoginController:

    def __init__(self):
        self.model = ml.LoginModel()

    def verify_login(self, username, password):
        return self.model.BuscarLogin(username, password)

    