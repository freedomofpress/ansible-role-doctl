import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


DOCTL_VERSION = "1.6.0"


def test_doctl_command_exits(Command):
    assert Command.exists("doctl")


def test_doctl_version(Command):
    version_string = "doctl version {}-release".format(DOCTL_VERSION)
    c = Command("doctl version")
    assert c.rc == 0
    assert version_string in c.stdout
