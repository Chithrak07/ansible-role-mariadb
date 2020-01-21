import os
import pytest
import docker

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


""" helper functions"""


def get_docker_image_name():
    client = docker.from_env()
    test_container = client.containers.list()[0]
    return test_container.attrs['Config']['Image']


def check_file(filepath, user, group, permission):

    assert filepath.exists
    assert filepath.user == user
    assert filepath.group == group
    assert oct(filepath.mode) == permission


# passable test for debugging baseline (get something working!)
def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


""" tasks/main.yml tests """


@pytest.mark.parametrize('files', [
    '/etc/mysql/mariadb.conf.d/99-acromedia-client-overrides.cnf',
    '/etc/mysql/mariadb.conf.d/99-acromedia-server-overrides.cnf',
    'root/my.cnf'
])
def test_file_paths_ubuntu1804(host, files):
    if host.system_info.release == '18.04' \
            and host.system_info.distribution == 'Ubuntu':
        test_files = [files]
        [check_file(host.file(x), 'root', 'root', '0o644') for x in test_files]


@pytest.mark.parametrize('files', [
    '/etc/mysql/conf.d/acro.cnf',
    'root/my.cnf'
])
def test_file_paths_ubuntu1604(host, files):
    if host.system_info.release == '16.04' \
            and host.system_info.distribution == 'Ubuntu':
        test_files = [files]
        [check_file(host.file(x), 'root', 'root', '0o644') for x in test_files]
