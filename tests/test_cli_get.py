import unittest
import requests
from multiprocessing import Process

import json
import time
from click.testing import CliRunner

from comver.main import server


def get_cli_command(runner, cli):
    runner.invoke(server, cli)


class TestCli(unittest.TestCase):
    
    def setUp(self):
        runner = CliRunner()
        self.proc = Process(
            target=get_cli_command,
            args=(runner, ['--get', '/hello', '{"name": "comver"}'])
        )
        
        self.proc.start()
        time.sleep(3)   # wait server to be prepared

    def tearDown(self) -> None:
        self.proc.terminate()

    def test_get(self):        
        response = requests.get('http://127.0.0.1:9000/hello')
        response_body = json.loads(json.loads(response.text))

        assert response.status_code == 200
        assert response_body['name'] == 'comver'


if __name__ == '__main__':
    unittest.main()

