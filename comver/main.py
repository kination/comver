
import click
import json
import uvicorn
from starlette.applications import Starlette

from comver.router import Router


@click.group()
def cli():
    pass

@click.command()
@click.option('--log-level', default='debug')
@click.option('-g', '--get', type=(str, str))
def server(log_level, get):
    res = json.loads(get[1])
    router = Router('')
    app = Starlette(debug=True, routes=router.get_route())

    uvicorn.run(app, host="127.0.0.1", port=9000, log_level=log_level)


cli.add_command(server)

if __name__ == '__main__':
    cli()

