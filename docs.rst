ansible-role-sshd
================================================================================

Role to setup OpenSSH

Variables
--------------------------------------------------------------------------------

sshd_package_release

   Package default release

.. autoyaml:: defaults/main.yml

Examples
--------------------------------------------------------------------------------

.. literalinclude:: molecule/default/playbook.yml
   :language: yaml

Documentation
--------------------------------------------------------------------------------

Compile::

   $ pip3 install -r requirements.txt
   $ make man

View::

   $ man ./docs/man/ansible-role-sshd.1
