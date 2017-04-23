[![Build Status](https://travis-ci.org/freedomofpress/ansible-role-doctl.svg?branch=master)](https://travis-ci.org/freedomofpress/ansible-role-doctl)

doctl Ansible role
===================

Installs and configures [doctl] for interacting with the 
[DigitalOcean] API.

Fetches tarball from GitHub and verifies the SHA256 checksum from same.
Unfortunately there does not appear to be a GPG signature available
for the checksum file, so HTTPS via GitHub is the best authenticity
we can provide.

Role Variables
--------------

```yaml
# Hardcoded version string. Will be reused in multiple vars. Must be manually
# updated to install new versions. Checksums will be automatically verified
doctl_version: 1.6.0

# Directory to store downloaded files, including checksum info.
doctl_download_dir: /usr/local/src

# Download URLs for fetching archive of binaries and checksum verification info.
doctl_tarball_url: "https://github.com/digitalocean/doctl/releases/download/v{{ doctl_version }}/doctl-{{ doctl_version }}-linux-amd64.tar.gz"
doctl_checksum_url: "https://github.com/digitalocean/doctl/releases/download/v{{ doctl_version }}/doctl-{{ doctl_version }}-linux-amd64.sha256"

# Couldn't find a GPG signature for the checksum file.
#doctl_signature_url: "{{ doctl_checksum_url }}.sig"
```

Example Playbook
----------------

```yaml
- name: Install dotctl.
  hosts: workstations
  roles:
    - role: freedomofpress.doctl
      become: yes
      tags: doctl
```

License
-------

MIT

Author Information
------------------

[Freedom of the Press Foundation]

[DigitalOcean]: https://digitalocean.com/
[doctl]: https://github.com/digitalocean/doctl/
[Freedom of the Press Foundation]: https://freedom.press/
