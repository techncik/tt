import click
from core.current import current
from core.search import search
from core.access import get_auth
from core.server import app
import subprocess

MODES = ['s', 'c', 'start']

# TODO: Create all possible modes here
COPTS = ['p','s','r','f','b','u','q','n','v']
SOPTS = ['a', 'p', 'r', 'q', 's', '.', 'm']
# running = False

# TODO: I should add the ability to refine a search.
# Eg to look up a song by an artist.
# This could be done with a --by flag after the song?
# SO you could search 'tt s . song1 -by artistnane'
# Or 'tt s a album name -by artist name (mode = s, search input = album name, artist name = artistname)

@click.command
@click.argument('mode', nargs=1)
@click.argument('opts', nargs=1)
@click.argument('inp', nargs=-1)
def main(mode: str, opts: str, inp: tuple[str]):

    # global running 

    # Mode is c or s
    if not mode in MODES:
        raise click.ClickException("Mode input must be 's' or 'c'")
    
    # If start mode, spin up server, get access_token, set RUNNING = True
    if mode == 'start':
        print("start the server here")

        #TODO: Logic might be better to go in a different startup file
        # Once starting up, spin server, then open a new terminal window for
        # the python cli.py commands to go into. And run this script from
        # that terminal
        # So from root call `python startup` which opens new terminal which
        # runs this exact file on some while loop, waiting for input.
        # Then in that window I can use all the commands from this file
        # by simply typing `s . song1` >enter

        # IMPORTANT: This line worked, and ran the server.
        #app.run(host='0.0.0.0', debug=True)


        # running = True
        # subprocess.call('start /wait python cli.py', shell=True)
        results = "Server started"


    # Options are valid
    elif mode == 'c':
        # if not running:
        #     raise click.ClickException(f"Application hasn't been started")
        for opt in opts:
            if not opt in COPTS:
                raise click.ClickException(f"Option [{opt}] not in current song options")
            
        results = current(opts, inp)
    else:
        # if not running:
        #     raise click.ClickException(f"Application hasn't been started")
        for opt in opts:
            if not opt in SOPTS:
                raise click.ClickException(f"Option [{opt}] not in search options")
            
        results = search(opts, inp)

    command = f"The command line input was mode {mode} with options {opts} and the input {inp}"
    click.echo(command)
    click.echo(results)

if __name__ == "__main__":
    main()