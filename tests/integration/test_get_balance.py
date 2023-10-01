import pytest
from tests.conftest import (
    prepare_conf,
)
from tests.cli_tester import (
    call_jhl_wallet,
)
from jhl_wallet.cli.jhl_wallet_cli import(
    jhl_wallet_cli,
)


@pytest.fixture
def config(tmp_path, mocker):
    test_configuration = prepare_conf(tmp_path)
    mocker.patch('jhl_wallet.configuration.Configuration.load_configuration',
                 return_value=test_configuration)
    mocker.patch('getpass.getpass',
                 return_value="my-password")
    call_jhl_wallet(jhl_wallet_cli, parameters=["new-wallet"])
    return test_configuration


def test_get_balance(config):
    result = call_jhl_wallet(jhl_wallet_cli, parameters=["get-balance"])
    address = config.eth_address
    assert result.exit_code == 0
    assert f"Balance on address " + address + " is: 0JHL\n" in result.output


def test_unknown_token(config):
    result = call_jhl_wallet(jhl_wallet_cli, parameters=["get-balance",
                                                         "--token", "invalid-token"])
    assert result.exit_code == 0
    assert f"This token is not added to the wallet!" in result.output
