packer Ansible role
===================

Installs and configures [Packer] for building VM images.

Unlike most community-maintained Packer installation roles, this role will
verify package integrity via a GPG-signed SHA256 checksum file prior to installing.

Role Variables
--------------

```yaml
# Hardcoded version string. Will be reused in multiple vars. Must be manually
# updated to install new versions. Checksums will be automatically verified.
doctl_version: 0.12.1

# Directory to store downloaded files, including checksum info.
doctl_download_dir: /usr/local/src

# Download URLs for fetching ZIP file of binaries and checksum verification info.
doctl_zip_url: "https://releases.hashicorp.com/packer/{{ doctl_version }}/doctl_{{ doctl_version }}_linux_amd64.zip"
doctl_checksum_url: "https://releases.hashicorp.com/packer/{{ doctl_version }}/doctl_{{ doctl_version }}_SHA256SUMS"
doctl_signature_url: "{{ doctl_checksum_url }}.sig"
```

Example Playbook
----------------

```yaml
- name: Install Packer.
  hosts: packer
  vars:
    doctl_version: 0.12.1
  roles:
    - role: freedomofpress.packer
      become: yes
      tags: packer
```

License
-------

MIT

Author Information
------------------

[Freedom of the Press Foundation]

[Packer]: https://packer.io/
[Freedom of the Press Foundation]: https://freedom.press/
