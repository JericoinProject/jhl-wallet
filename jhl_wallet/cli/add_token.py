import click
from jhl_wallet.cli.utils_cli import (
    get_api,
)
from jhl_wallet.configuration import (
    Configuration,
)
from web3.exceptions import (
    InvalidAddress,
)
from jhl_wallet.exceptions import (
    JscErrorException,
)


@click.command()
@click.option('-c', '--contract', default='', prompt='Contract address',
              help='Contract address.')
@click.option('-s', '--symbol', default='', prompt='Token symbol',
              help='Token symbol.')
def add_token(contract, symbol):
    """Add new ERC20 contract."""
    configuration = Configuration().load_configuration()
    api = get_api()

    try:
        api.add_contract(configuration, symbol, contract)
        click.echo('New coin was added! %s %s' % (symbol, contract))
    except InvalidAddress:
        click.echo('Invalid address or wallet does not exist!')
    except JscErrorException:
        click.echo('Wallet is not connected to JSC network!')


