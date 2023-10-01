import pytest
from tests.conftest import (
    prepare_conf,
)
from tests.cli_tester import (
    call_jhl_wallet,
)
from jhl_wallet.cli.jhl_wallet_cli import (
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


def test_add_token(config):
    result = call_jhl_wallet(jhl_wallet_cli, parameters=["add-token",
                                                         "--contract", "0xB37920D1D3842716B719f997afB1959DD6889BFD",
                                                         "--symbol", "USDJ"])
    contract_address = config.contracts['USDJ']
    assert result.exit_code == 0
    assert f"New coin was added! USDJ " + contract_address + "\n" in result.output

    result = call_jhl_wallet(jhl_wallet_cli, parameters=["list-tokens"])
    assert result.exit_code == 0
    assert f"JHL\nUSDJ\n" in result.output
