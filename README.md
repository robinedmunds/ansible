# Robin's ansible roles

This repo contains personal ansible roles and inventories. Repo follows the [**roles directory structure**](https://docs.ansible.com/ansible/latest/user_guide/playbooks_reuse_roles.html#role-directory-structure).

## Roles

### common

Initial setup of freshly installed linux distros.

1. Set hostname of target machine to inventory alias
2. Update system and install list of essential packages
3. Setup **whoops** recovery user with sudo privileges
4. Setup **ansible** user with sudo privileges. *For ansible remote execution*
5. Set random password and lock password of **root** user
6. Setup **robin** user with sudo privileges. *My personal login*
7. Clone my personal environment aliases and configs and symlink them appropriately

### debian-docker

Installs docker daemon from official docker repository, [following this guide](https://docs.docker.com/engine/install/debian/). Installs docker-compose via pip.

1. Install docker dependencies
2. Install docker gpg key
3. Add docker repo to sources.list
4. Install docker
5. Enable docker service
6. Add users to docker group

### debian-harden

Changes sshd port and hardens sshd_config. Installs ufw firewall and adds common rules.

1. Set sshd port to 1444
2. Install ufw firewall
3. Default **allow** inbound traffic
4. Allow inbound traffic on port 1444
5. Allow inbound traffic on ports 80, 443
6. Default **drop** inbound traffic

### debian-terse

For quickly provisioning containerised web servers in the cloud. Setup web server and reverse proxy containers.

1. Install ansible's docker dependencies on target
2. Copy files and generate docker-compose files from templates
3. Start the services via docker-compose module

## Usage

1. `git clone https://github.com/robinedmunds/ansible.git`
2. `python -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt`
5. `ansible-galaxy collection install community.general`

## ansible.cfg

Show lines that deviate from ansible defaults: -

`ansible-config dump --only-changed`

