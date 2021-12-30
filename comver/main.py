
import click
import uvicorn
from starlette.applications import Starlette

from comver.router import Router


@click.group()
def cli():
    pass

@click.command()
def server():
    router = Router('')
    app = Starlette(debug=True, routes=router.get_route())

    uvicorn.run(app, host="127.0.0.1", port=9000, log_level="info")


cli.add_command(server)

if __name__ == '__main__':
    cli()

