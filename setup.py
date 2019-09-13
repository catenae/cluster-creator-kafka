#!/usr/bin/env python
# -*- coding: utf-8 -*-

from node_manager import NodeManager


class AwsSetupNodeManager(NodeManager):
    def fix_ssh(self):
        self.run_cmd("sudo sed -ri 's/#?MaxStartups.*/MaxStartups 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo sed -ri 's/#?MaxSessions.*/MaxSessions 100/' /etc/ssh/sshd_config")
        self.run_cmd("sudo systemctl restart sshd")

    def install_docker(self):
        self.run_cmd("sudo yum -y update && " + "sudo yum -y install docker && " +
                     "sudo systemctl start docker && " + "sudo usermod -aG docker ec2-user && " +
                     "sudo systemctl enable docker")

    def deploy(self):
        self.fix_ssh()
        self.install_docker()
