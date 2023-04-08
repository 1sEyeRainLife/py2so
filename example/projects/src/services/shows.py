from flask.views import MethodView


class ShowService(MethodView):

    def get(self):
        return "Hello This is Show!"