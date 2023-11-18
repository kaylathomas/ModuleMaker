import click
from ModuleMaker.new.main import new_command
from ModuleMaker.export.main import export_command

@click.group()
def cli():
    pass

@cli.group()
def mm():
    pass

mm.add_command(new_command, name='new')
mm.add_command(export_command, name='export')

if __name__ == '__main__':
    cli()
