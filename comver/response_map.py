# Test class / data
resp_map = {
    '/hello': {'hello' : 'world'},
    '/world': {'world' : 'hello'}
}

class ResponseMap(object):
    def __init__(self):
        pass

    def key_list(self):
        return ['/hello', '/world']

    def get_by_key(self, key):
        return resp_map[key]
