pgbackup
========

CLI for backup remote PostgreSQL database or localy or to S3

Preparing to Development
------------------------

1. Ensure using ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:viliusd/pgbackup``
3. ``cd`` into the repository
4. Fetch Development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver, and the destination

S3 Example w/ bucket name:

::

    $ pg backup postgres://user@example:5432/db_one --driver s3 backups

Local Example w/ local path:

::

    $ pg backup postgres://user@example:5432/db_one --driver lolca /var/local/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv is not active use:

::

    $ pipenv run make