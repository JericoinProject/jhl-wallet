import click
import getpass
from jhl_wallet.cli.utils_cli import (
    get_api,
)
from jhl_wallet.configuration import (
    Configuration,
)
from jhl_wallet.exceptions import (
    InsufficientFundsException,
    InvalidValueException,
    InvalidPasswordException,
    JscErrorException,
    InsufficientERC20FundsException,
    ERC20NotExistsException,
)
from web3.exceptions import (
    InvalidAddress,
)


@click.command()
@click.option('-t', '--to', default='', prompt='To address:',
              help='Jericoin address where to send amount.')
@click.option('-v', '--value', default='', prompt='Value to send:',
              help='JHL value to send.')
@click.option('--token', default=None,
              help='Token symbol.')
def send_transaction(to, value, token):
    """Sends transaction."""
    password = getpass.getpass('Password from keystore: ')  # Prompt the user for a password of keystore file

    configuration = Configuration().load_configuration()
    api = get_api()

    try:
        if token is None:
            # send JHL transaction
            tx_hash, tx_cost_eth = api.send_transaction(configuration,
                                                        password,
                                                        to,
                                                        value)
        else:
            # send erc20 transaction
            tx_hash, tx_cost_eth = api.send_transaction(configuration,
                                                        password,
                                                        to,
                                                        value,
                                                        token)

        click.echo('Hash of the transaction: %s' % str(tx_hash.hex()))
        click.echo('Transaction cost was: %sJHL' % str(tx_cost_eth))

    except InsufficientFundsException:
        click.echo('Insufficient JHL funds! Check balance on your address.')
    except InsufficientERC20FundsException:
        click.echo('Insufficient ERC20 token funds! Check balance on your address.')
    except InvalidAddress:
        click.echo('Invalid recipient(to) address!')
    except InvalidValueException:
        click.echo('Invalid value to send!')
    except InvalidPasswordException:
        click.echo('Incorrect password!')
    except JscErrorException:
        click.echo('Wallet is not connected to JSC network!')
    except ERC20NotExistsException:
        click.echo('This token is not added to the wallet!')


