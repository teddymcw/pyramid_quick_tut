import logging
log = logging.getLogger(__name__)

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
        log.debug('In home view')
        return {'name': 'Home View'}

    #/howdy
    @view_config(route_name='hello')
    def hello(self):
        log.debug('In hello view')
        return {'name': 'Hello View'}