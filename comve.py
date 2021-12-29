
import click
import uvicorn

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


@click.group()
def cli():
    pass

@click.command()
def server():
    async def homepage(request):
        return JSONResponse({'hello': 'world'})

    app = Starlette(debug=True, routes=[
        Route('/', homepage),
    ])

    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")


cli.add_command(server)

if __name__ == '__main__':
    cli()
