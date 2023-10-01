import click
from jhl_wallet.cli.utils_cli import (
    get_api,
)
from jhl_wallet.configuration import (
    Configuration,
)


@click.command()
def network():
    """Get connected network (Mainnet) defined in EIP155."""
    configuration = Configuration().load_configuration()
    api = get_api()
    chain_id = api.get_network(configuration)
    if chain_id == 707007:
        click.echo('You are connected to the JSC Mainnet network!')
    else:
        click.echo(f'You are connected another network (Your Chain ID is : {chain_id}')
