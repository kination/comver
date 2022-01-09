from urllib.parse import urlparse

from starlette.responses import JSONResponse
from starlette.routing import Route

from comver.response_map import ResponseMap


class Router(object):
    def __init__(self,
                type='cli',
                resp_map=ResponseMap(),
                data_path=''):
        self.resp_map = resp_map

    def get_route(self):
        generated_route = list()
        for key in self.resp_map.key_list():
            generated_route.append(
                Route(key, self.__generate_response)
            )
        
        return generated_route

    async def __generate_response(self, request):
        key = urlparse(str(request.url)).path
        return JSONResponse(self.resp_map.get_by_key(key))
