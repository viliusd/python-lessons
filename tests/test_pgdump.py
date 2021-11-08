import subprocess
import pytest

from pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_one"

def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with db url
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

#does not work yet

# def test_dump_handles_oserror(mocker):
#     """
#     pgdump.dump returns a reasonable if pg_dump isnt installed
#     """
#     mocker.patch('subprocess.Popen', side_affect=OSError('no such file'))
#     with pytest.raises(SystemExit):
#         pgdump.dump(url)