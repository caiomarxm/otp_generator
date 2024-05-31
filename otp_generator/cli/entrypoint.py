import click

from otp_generator.cli.commands import from_secret


@click.group
def otp():
    pass

otp.add_command(from_secret)
