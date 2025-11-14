import click
from core.current import current
from core.search import search
from core.access import get_auth

MODES = ['s', 'c']

# TODO: Create all possible modes here
COPTS = ['p','s','r','f','b','u','q','n','v']
SOPTS = ['a', 'p', 'r', 'q', 's', '.', 'm']

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

    # Mode is c or s
    if not mode in MODES:
        raise click.ClickException("Mode input must be 's' or 'c'")
    
    # Options are valid
    if mode == 'c':
        for opt in opts:
            if not opt in COPTS:
                raise click.ClickException(f"Option [{opt}] not in current song options")
            
        results = current(opts, inp)
    else:
        for opt in opts:
            if not opt in SOPTS:
                raise click.ClickException(f"Option [{opt}] not in search options")
            
        results = search(opts, inp)

    command = f"The command line input was mode {mode} with options {opts} and the input {inp}"
    click.echo(command)
    click.echo(results)

if __name__ == "__main__":
    main()