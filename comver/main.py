
import click
import json
import uvicorn
from starlette.applications import Starlette

from comver.router import Router
from comver.response_map import ResponseMap


@click.group()
def cli():
    pass

@click.command()
@click.option('--log-level', default='debug')
@click.option('-p', '--port', type=int, default=9000)
@click.option('-g', '--get', multiple=True, type=(str, str))
def server(log_level, port, get):
    resp_map = ResponseMap()
    for data in get:
        resp_map.add_get(data[0], data[1])

    router = Router('', resp_map=resp_map)
    app = Starlette(debug=True, routes=router.get_route())

    uvicorn.run(app, host="127.0.0.1", port=port, log_level=log_level)


cli.add_command(server)

if __name__ == '__main__':
    cli()

