
import click
import uvicorn
from starlette.applications import Starlette

# from comver.main import Router
from starlette.routing import Route
from starlette.responses import JSONResponse


@click.group()
def cli():
    pass

@click.command()
def server():
    # router = Router('')
    async def __generate_response(request):
        return JSONResponse({'a': 'b'})

    '''
    route = {
        '/hello': JSONResponse({'hello' : 'world'}),
        '/world': JSONResponse({'world' : 'hello'}),
    }
    

    generated_route = []
    for key, value in route.items():
        generated_route.append(Route(key, __generate_response(value)))
    '''

    app = Starlette(debug=True, routes=[
        Route('/hello', __generate_response),
        Route('/world', __generate_response)
    ])

    uvicorn.run(app, host="127.0.0.1", port=9000, log_level="info")


cli.add_command(server)

if __name__ == '__main__':
    cli()

