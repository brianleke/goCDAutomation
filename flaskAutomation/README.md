Setup
============================
This is an ansible playbook that automatically installs and configures NGINX, Flask and WSGI with a dummy app.py file that just shows flask is successfully running. This is run out of a virtual machine.

Make sure you have installed:
* [Vagrant](https://www.vagrantup.com/)
* [Ansible](http://www.ansible.com/home)
* [VirtualBox](https://www.virtualbox.org/)
* [Git](https://git-scm.com/downloads)

Clone the repository
* git clone https://github.com/brianleke/goCDAutomation.git

CD into the testmachineautomation directory
* cd goCDAutomation/flaskAutomation
This is an ansible playbook to set up a default flask application with a dummy application running on http://localhost:8082/
