import click

from git_branching_test import __version__
from git_branching_test import main


@click.group()
@click.version_option(version=__version__)
def cli():
    pass


@cli.command()
@click.argument("name")
def hello(name):
    print(main.hello(name))


if __name__ == "__main__":
    cli()
