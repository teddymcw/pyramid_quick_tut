from pyramid.view import (
    view_config,
    view_defaults
    )

@view_defaults(renderer='home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request 

    # First view, available at http://localhost:6543/
    @view_config(route_name='home')
    def home(self):
        return {'name': 'Home View'}

    #/howdy
    @view_config(route_name='hello')
    @view_config(route_name='hello_json', renderer='json')
    def hello(self):
        return {'name': 'Hello View'}