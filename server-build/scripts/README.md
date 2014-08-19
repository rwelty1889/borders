Installation
============

the intended user shouls have sudo privileges.

from the user's home directory,

$ sudo bash
# /path/to/rails-port-root-install.
# exit
$ /path/to/rails-port-user-install

then tweak the permissions for postgresql

sudo su - postgres
edit /etc/postgresql/9.3/main/pg_hba.conf

near the bottom, change lines containing

peer and md5 to trust

and save. exit as user postgresql.

restart postgresql:

sudo service postgresql restart

test postgreqal connection

$ psql template1
template1=# \l
template1=# \q
$

the \l command should produce a list of databases including
openstreetmap, osm_test, postgres, template0 and template1. terminate
the \l output by typing 'q'

