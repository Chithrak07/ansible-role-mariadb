mariadb
======

![.github/workflows/molecule.yml](https://github.com/AcroMedia/ansible-role-mariadb/workflows/.github/workflows/molecule.yml/badge.svg)

For setting up MariaDB on Ubuntu.


Requirements
------------
* Ubuntu 14.04 or newer.

Role Variables
--------------
### Performance tweaks
* mysql_max_allowed_packet
* mysql_max_connections
* mysql_expire_logs_days
* mysql_general_log_file
* mysql_general_log
* mysql_slow_query_log
* mysql_slow_query_log_file
* mysql_long_query_time

### Drupal commerce performance
* mysql_transaction_isolation
* mysql_binlog_format

### Server + Client or or Client Only
* client_only (boolean): Only install the client, not the server.

### Connectivity
* **mysql_bind_address**: Defaults to `127.0.0.1`
* **mysql_allow_from**: What address(es) to accept connections by *root* to manage the system from.

  Can be a single string:
  ```yaml
  mysql_allow_from: '10.5.0.6'
  ```
  Or a list:
  ```yaml
  mysql_allow_from:
    - '10.5.0.11'
    - '10.5.0.12'
  ```
  Specify anything that mysql would normally support for the host field.

### Non-Trivial, Potentially Destructive

WARNING: Don't use any of the following unless you absolutely know what you're doing. These are only exposed here so you can override defaults during a new installation. They shouldn't be changed in your ansible playbook once the server is running, except in cases where the playbook is being updated to match the changes that have already been affected on the server.

* **mysql_innodb_log_file_size** - affects `innodb_log_file_size` if specified. Has no default value in the playbook.
* **mysql_datadir** - has no default value in the playbook. Most systems default to `/var/lib/mysql`.
* **mariadb_version** (string)
  - Defaults to `auto` which will let Ubuntu install whatever default version comes with Apt.
  - Can be `auto`, `10.1`, `10.2` or any other supported version.
  - When not `auto`, the value for this is used to construct the repo URL
  - If sepecifying this, you may also need to specify **mariadb_mirror**, **mariadb_mirror_proto**, and **mariadb_repo_deb_arch** - See defaults/main.yml. Visit https://downloads.mariadb.org/mariadb/repositories to dermine the best value for these.


Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: dbmaster
  become: true
  gather_facts: true
  roles:
    - role: acromedia.mariadb
      vars:
        mysql_bind_address: 0.0.0.0
        mysql_allow_from:
          - 10.8.8.5
          - 10.8.8.6

- hosts: app-nodes
  roles:
    - role: acromedia.mariadb
      vars:
        client_only: true
```

License
-------

GPLv3

Author Information
------------------

Acro Media Inc.
https://www.acromedia.com/
