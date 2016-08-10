Setup
============================
This is an ansible playbook that automatically installs and configures Gitlab v6.0 or v7.9 as a ready to use in-house source code management environment.

Make sure you have installed:
* [Vagrant](https://www.vagrantup.com/)
* [Ansible](http://www.ansible.com/home)
* [VirtualBox](https://www.virtualbox.org/)
* [Git](https://git-scm.com/downloads)

Clone the repository
* git clone https://github.com/brianleke/goCDAutomation.git

CD into the testmachineautomation directory
* cd goCDAutomation/gitlabAutomation

Modify the user details to match your settings with either VIM or nano etc
* vim .user-configurations.yml

Make sure the 
* GITLAB_URL, 
* mysql_root_password and 
* GITLAB_HOSTNAME, which is just the hostname for the gitlab_url without the http:// or https:// 

to your credentials required

Build virtual machine (Make sure nothing else is running on port 8081):
* vagrant up

Access Gitlab Interface
* Access http://localhost:8081 for the local instance of Gitlab running and login with the following credentials
* Gitlab v6.0, username: admin@local.host; password: 5iveL!fe
* Gitlab v7.9, username: root; password: 5iveL!fe
