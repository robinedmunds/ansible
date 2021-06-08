# Robin's Ansible roles

This repo contains personal ansible roles and inventories. Repo follows the [**roles directory structure**](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#role-directory-structure).

## Usage

1. `git clone https://github.com/robinedmunds/ansible.git`
2. `python -m venv venv`
3. `source venv/bin/activate`
4. `pip install ansible`
5. `ansible-galaxy collection install community.general`

## ansible.cfg

Show lines that deviate from ansible defaults: -

`ansible-config dump --only-changed`