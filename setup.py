#!/usr/bin/env python
# -*- coding: utf-8 -*-

from node_manager import NodeManager

class CentOS8Manager(NodeManager):
    def fix_ssh(self):
        self.run_cmd("sudo sed -ri 's/#?MaxStartups.*/MaxStartups 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo sed -ri 's/#?MaxSessions.*/MaxSessions 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo systemctl restart sshd")

    def install_docker(self):
        self.run_cmd("sudo yum install -y yum-utils device-mapper-persistent-data lvm2")
        self.run_cmd(
            "sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo"
        )
        self.run_cmd("sudo yum install docker-ce --nobest")
        self.run_cmd("sudo systemctl enable docker")
        self.run_cmd("sudo systemctl start docker")
        self.run_cmd("sudo usermod -aG docker $(whoami)")

    def deploy(self):
        self.install_docker()


class CentOS7Manager(NodeManager):
    def fix_ssh(self):
        self.run_cmd("sudo sed -ri 's/#?MaxStartups.*/MaxStartups 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo sed -ri 's/#?MaxSessions.*/MaxSessions 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo systemctl restart sshd")

    def install_docker(self):
        self.run_cmd("sudo yum install -y yum-utils device-mapper-persistent-data lvm2")
        self.run_cmd(
            "sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo"
        )
        self.run_cmd("sudo yum install -y docker-ce")
        self.run_cmd("sudo systemctl enable docker")
        self.run_cmd("sudo systemctl start docker")
        self.run_cmd("sudo usermod -aG docker $(whoami)")

    def deploy(self):
        self.install_docker()


class AmazonLinux1Manager(NodeManager):
    def fix_ssh(self):
        self.run_cmd("sudo sed -ri 's/#?MaxStartups.*/MaxStartups 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo sed -ri 's/#?MaxSessions.*/MaxSessions 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo service sshd restart")

    def install_docker(self):
        self.run_cmd("sudo yum -y update && " + "sudo yum -y install docker && " +
                     "sudo service docker start && " + "sudo usermod -aG docker ec2-user")

    def deploy(self):
        self.install_docker()


class AmazonLinux2Manager(NodeManager):
    def fix_ssh(self):
        self.run_cmd("sudo sed -ri 's/#?MaxStartups.*/MaxStartups 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo sed -ri 's/#?MaxSessions.*/MaxSessions 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo systemctl restart sshd")

    def install_docker(self):
        self.run_cmd("sudo yum -y update && " + "sudo yum -y install docker && " +
                     "sudo systemctl start docker && " + "sudo usermod -aG docker ec2-user && " +
                     "sudo systemctl enable docker")

    def deploy(self):
        self.install_docker()
