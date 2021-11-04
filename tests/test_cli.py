import pytest

from pgbackup import cli

# $ pg backup postgres://user@example:5432/db_one --driver s3 backups

url = "postgres://user@example:5432/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    without specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_unknown_driver(parser):
    """
    The parser will exit if driver name is unknown
    """

    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_parameters(parser):
    """
    The parser will not exit if driver name is known
    """

    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])


def test_parser_with_driver(parser):
    """
    Parser will exit if receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])


def test_parser_with_driver_and_destination(parser):
    """
    Parser will not exit if receives driver with destination
    """

    args = parser.parse_args([url, "--driver", "local", "/some/path"])
    
    assert args.url ==  url
    assert args.driver == 'local'
    assert args.destination == '/some/path'