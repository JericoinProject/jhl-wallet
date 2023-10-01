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
    ERC20NotExistsException,
)


@click.command()
@click.option('-t', '--token', default=None,
              help='Token symbol.')
def get_balance(token):
    """Get address balance."""
    configuration = Configuration().load_configuration()
    api = get_api()
    try:
        if token is None:
            eth_balance, address = api.get_balance(configuration)
            click.echo('Balance on address %s is: %sJHL' % (address, eth_balance))
        else:
            token_balance, address = api.get_balance(configuration, token)
            click.echo('Balance on address %s is: %s%s' % (address, token_balance, token))
    except InvalidAddress:
        click.echo('Invalid address or wallet does not exist!')
    except JscErrorException:
        click.echo('Wallet is not connected to JSC network!')
    except ERC20NotExistsException:
        click.echo('This token is not added to the wallet!')


