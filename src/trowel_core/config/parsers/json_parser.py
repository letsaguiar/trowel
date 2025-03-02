import click
import json

class ConfigParserJson:
    @staticmethod
    def parse(path: str) -> dict:
        try:
            with open(path) as file:
                data = json.loads(file.read())
            return (data)
        except FileNotFoundError:
            click.echo("Error: trowel config not found.", err=True)
            raise click.Abort()
