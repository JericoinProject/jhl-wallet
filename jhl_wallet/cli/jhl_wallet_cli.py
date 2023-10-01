import click
from jhl_wallet.cli.new_wallet import (
    new_wallet,
)
from jhl_wallet.cli.get_wallet import (
    get_wallet,
)
from jhl_wallet.cli.reveal_seed import (
    reveal_seed
)
from jhl_wallet.cli.get_balance import (
    get_balance,
)
from jhl_wallet.cli.send_transaction import (
    send_transaction,
)
from jhl_wallet.cli.restore_wallet import (
    restore_wallet,
)
from jhl_wallet.cli.add_token import (
    add_token,
)
from jhl_wallet.cli.list_tokens import (
    list_tokens,
)
from jhl_wallet.cli.network import (
    network,
)


@click.group()
def jhl_wallet_cli():
    pass


jhl_wallet_cli.add_command(new_wallet)
jhl_wallet_cli.add_command(get_wallet)
jhl_wallet_cli.add_command(reveal_seed)
jhl_wallet_cli.add_command(get_balance)
jhl_wallet_cli.add_command(send_transaction)
jhl_wallet_cli.add_command(restore_wallet)
jhl_wallet_cli.add_command(add_token)
jhl_wallet_cli.add_command(list_tokens)
jhl_wallet_cli.add_command(network)

if __name__ == "__main__":
    jhl_wallet_cli()
