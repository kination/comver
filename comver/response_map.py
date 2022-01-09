
class ResponseMap(object):
    def __init__(self):
        self.resp_map = dict()

    def add_get(self, key, data):
        self.resp_map[key] = data

    def key_list(self):
        return [key for key, _ in self.resp_map.items()]

    def get_by_key(self, key):
        return self.resp_map[key]

