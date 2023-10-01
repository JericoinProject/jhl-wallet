from jhl_wallet.cli.jhl_wallet_cli import(
    jhl_wallet_cli,
)
from click.testing import(
    CliRunner,
)


def call_jhl_wallet(fnc=None, parameters=None, envs=None):
    """
    Creates testing environment for cli application
    :param fnc: command to run
    :param parameters: program cmd argument
    :param envs:
    :return: invoked cli runner
    """
    fnc = fnc or jhl_wallet_cli
    runner = CliRunner()
    envs = envs or {}
    parameters = parameters or []
    # catch exceptions enables debugger
    return runner.invoke(fnc, args=parameters, env=envs, catch_exceptions=False)
