from typing import Dict
from typing import List
from ms_graph.session import GraphSession


class Calendar():


    def __init__(self, session: object) -> None:

        # Set the session.
        self.graph_session: GraphSession = session

        # Set the endpoint.
        self.endpoint = 'events'


    def get_all_events(self, object_to_selects: List = ['subject','body','bodyPreview','organizer','attendees','start','end','location']) -> Dict:

        selection = f'$select={",".join(object_to_selects)}' if object_to_selects is not None else ''
        endpoint = f'/me/calendar/{self.endpoint}?{selection}'
        print(endpoint)
        content = self.graph_session.make_request(
            method = 'get',
            endpoint = endpoint
            )

        return content

    def organize_new_event(self, event : Dict) -> Dict:

        content = self.graph_session.make_request(
            method='post',
            endpoint = f'/me/{self.endpoint}',
            json=event
        )

        return content

    def get_all_calendars (self) -> Dict:

        content = self.graph_session.make_request(
            method='get',
            endpoint = '/me/calendars'
        )

        return content







      

    

