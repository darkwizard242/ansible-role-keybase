[![build-test](https://github.com/darkwizard242/ansible-role-keybase/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-keybase/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-keybase/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-keybase/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/53764?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/53764?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/53764?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-keybase&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-keybase) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-keybase&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-keybase) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-keybase&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-keybase) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-keybase&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-keybase) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-keybase?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-keybase?color=orange&style=flat-square)

# Ansible Role: keybase

Role to install (_by default_) [keybase](https://keybase.io) package or uninstall (_if passed as var_) on Debian based systems and EL based systems. Keybase is capable of End-to-end encryption for things that matter and provides secure messaging and file-sharing.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables List:

```yaml
keybase_app: keybase
keybase_app_desired_state: present

# Debian family based
keybase_debian_pre_reqs: gnupg
keybase_debian_pre_reqs_desired_state: present
keybase_repo_debian_gpg_keyid: '47484E50656D16C7'
keybase_repo_debian_gpg_keyserver: keyserver.ubuntu.com
keybase_repo_debian: "deb http://prerelease.keybase.io/deb stable main"
keybase_repo_debian_filename: "{{ keybase_app }}"
keybase_repo_debian_desired_state: present

# EL family based
keybase_repo_el: http://prerelease.keybase.io/rpm/x86_64
keybase_repo_el_name: keybase
keybase_repo_el_description: keybase
keybase_repo_el_enabled: yes
keybase_repo_el_gpgcheck: yes
keybase_repo_el_gpgkey: https://keybase.io/docs/server_security/code_signing_key.asc
keybase_repo_el_filename: keybase
keybase_repo_el_desired_state: present
```

### Variables table:

Variable                              | Description
------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
keybase_app                           | Name of keybase application package require to be installed i.e. `keybase`
keybase_app_desired_state             | State of the keybase_app package. Whether to install, verify if available or to uninstall (i.e. ansible apt module values: `present`, `latest`, or `absent`)
keybase_debian_pre_reqs               | Keybase recommends the installation of both these packages on Debian family systems and as such, they are considered pre-requisites.
keybase_debian_pre_reqs_desired_state | Desired state for Keybase pre-requisite apps on Debian family systems.
keybase_repo_debian_gpg_keyid         | Keybase GPG Key ID required on Debian family systems.
keybase_repo_debian_gpg_keyserver     | Keybase GPG Key Server required on Debian family systems.
keybase_repo_debian                   | Keybase repo URL for Debain family systems.
keybase_repo_debain_filename          | Name of the repository file that will be stored at `/etc/apt/sources.list.d/` on Debian based systems.
keybase_repo_debian_desired_state     | `present` indicates creating the repository file if it doesn't exist on Debian based systems. Alternative is `absent`.
keybase_repo_el                       | Repository `baseurl` for Keybase on EL based systems.
keybase_repo_el_name                  | Repository name for Keybase on EL based systems.
keybase_repo_el_description           | Description to be added in EL based repository file for Keybase.
keybase_repo_el_gpgcheck              | Boolean for whether to perform gpg check against Keybase on EL based systems.
keybase_repo_el_gpgkey                | Keybase GPG Key required on EL family systems.
keybase_repo_el_enabled               | Boolean to set so that Keybase repository is enabled on EL based systems.
keybase_repo_el_filename              | Name of the repository file that will be stored at `/yum/sources.list.d/keybase.repo` on EL based systems.
keybase_repo_el_desired_state         | `present` indicates creating the repository file if it doesn't exist on EL based systems. Alternative is `absent` (not recommended as it will prevent from installation of **keybase** package).

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **keybase** package) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.keybase
```

For customizing behavior of role (i.e. installing latest verion of **keybase**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.keybase
  vars:
    keybase_app_desired_state: latest
```

For customizing behavior of role (i.e. un-installation of **keybase** packages) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.keybase
  vars:
    keybase_app_desired_state: absent
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-keybase/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.alimuahmmad.dev/).
