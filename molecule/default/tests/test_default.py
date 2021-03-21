import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'keybase'
PACKAGE_BINARY = '/usr/bin/keybase'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/keybase.list'
EL_REPO_FILE = '/etc/yum.repos.d/keybase.repo'


def test_keybase_package_installed(host):
    """
    Tests if keybase is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_keybase_binary_exists(host):
    """
    Tests if keybase binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_keybase_binary_file(host):
    """
    Tests if keybase binary is file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_keybase_binary_which(host):
    """
    Tests the output to confirm keybase's binary location.
    """
    assert host.check_output('which keybase') == PACKAGE_BINARY


def test_keybase_repo_exists(host):
    """
    Tests if keybase's DEBIAN/EL repo file exists.
    """
    assert host.file(DEBIAN_REPO_FILE).exists or \
        host.file(EL_REPO_FILE).exists


def test_keybase_repo_file(host):
    """
    Tests if keybase's DEBIAN/EL repo file is file type.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file or \
        host.file(EL_REPO_FILE).is_file
