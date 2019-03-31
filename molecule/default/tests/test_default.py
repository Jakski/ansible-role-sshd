import os

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_configuration(host):
    sshd = host.file('/etc/ssh/sshd_config')
    assert sshd.contains(r'^PermitRootLogin no$')
    assert sshd.contains(r'^X11Forwarding no$')
    assert sshd.contains(r'^UsePAM yes$')
    assert sshd.contains(r'\sPermitTTY no$')
    ssh = host.file('/etc/ssh/ssh_config')
    assert ssh.contains(r'^User test$')
    assert ssh.contains(r'^Host \*$')
    assert ssh.contains(r'\sPort 23$')


def test_service(host):
    ssh = host.service('ssh')
    assert ssh.is_running
    assert ssh.is_enabled
    assert host.socket('tcp://0.0.0.0:22').is_listening
