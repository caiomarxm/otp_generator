import click
from otp_generator.two_factor.generate_otp import generate_totp_from_secret

@click.command()
@click.option('--secret', 'secret', help='', required=True, type=str)
def from_secret(
    secret: str
):
    click.echo(generate_totp_from_secret(secret=secret))
