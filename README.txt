ansible-role-sshd
*****************

Role to setup OpenSSH


Variables
=========

sshd_package_release

   Package default release

sshd_package

   Packages with sshd

sshd_enable

   Enable sshd service

sshd_service

   sshd service name

sshd_restart

   Restart sshd when necessary

sshd_reload

   Reload sshd when necessary

sshd_config_dir

   Configuration directory

sshd_config_template

   sshd_config file template

sshd_client_config_template

   ssh_config file template

sshd_config

   sshd server configuration

   For default values see _sshd_config

sshd_client_config

   sshd global client configuration

   For default values see _sshd_client_config


Examples
========

   ---
   - hosts: instance
     tasks:
       - import_role:
           name: sshd
         vars:
           sshd_config:
             settings:
               PermitRootLogin: "no"
               X11Forwarding: "no"
             matches:
               'User test':
                 PermitTTY: "no"
           sshd_client_config:
             settings:
               User: "test"
             hosts:
               '*':
                 Port: 23



Documentation
=============

Compile:

   $ pip3 install -r requirements.txt
   $ make man

View:

   $ man ./docs/man/ansible-role-sshd.1
