# content of conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--outfile", action="store", default=None, help="my option: type1 or type2"
    )


@pytest.fixture
def outfile(request, scope="session"):
    return  request.config.getoption("--outfile")


def pytest_configure(config):
    outfile = config.getoption('outfile')
    if outfile:
        with open(outfile, 'w') as f:
                f.write('')
    return

