Setup
============================
This is an ansible playbook that automatically installs and configures GoCD with one main pipeline and three dependent pipelines. This is meant to be a skeleton configuration and can be modified as seen fit.

Make sure you have installed:
* [Vagrant](https://www.vagrantup.com/)
* [Ansible](http://www.ansible.com/home)
* [VirtualBox](https://www.virtualbox.org/)
* [Git](https://git-scm.com/downloads)

Clone the repository
* git clone https://github.com/brianleke/goCDAutomation.git

CD into the testmachineautomation directory
* cd goCDAutomation/goCD

Make sure the access configuration file exists by copying the .user-access-config.ex.yml to .user-access-config.yml
* cp .user-access-config.ex.yml .user-access-config.yml

Modify the user details to match you settings with either VIM or nano etc
* vim .user-access-config.yml

Make sure repositories required are correctly configured by modifying the 
* REPO_USER_NAME and 
* REPO_PASSWORD 

to your repo's access credentials which can permit you clone

Modify 
* REPOSITORY_NAME (Main repository), 
* PIPELINE_ONE_REPO, 
* PIPELINE_TWO_REPO, 
* PIPELINE_THREE_REPO, 
* Delete any of the parameters which are not necessary and make sure you delete those on the playbook.yml steps as well as in the base-config.xml file with all reference to them.

Configure Steps per pipeline
* Look in the base-config.xml file and configure the different stages in each of the pipelines. There are dummy examples for executing commands in the "dummy_configs.xml" file thanks to the team at ThoughtWorks Studios.

Build virtual machine (Make sure nothing else is running on port 9001):
* vagrant up

Access goCD Interface
* Access http://localhost:9001 for the local instance of GoCD running. Not that this will be polling the repositories. Also make sure that the right steps are configured in the base-config.xml before running the "vagrant up"
