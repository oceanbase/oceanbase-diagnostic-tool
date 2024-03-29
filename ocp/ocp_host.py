#!/usr/bin/env python
# -*- coding: UTF-8 -*
# Copyright (c) 2022 OceanBase
# OceanBase Diagnostic Tool is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.


"""
@time: 2022/6/24
# File       : ocp_host.py
# Description：
"""
import requests
from ocp import ocp_api


class Host():
    def __init__(self, url, auth, id=None, ip=None):
        self.url = url
        self.auth = auth
        self.id = id
        self.ip = ip

        # remote status
        self.clockDiffMillis = ""
        self.currentTime = ""
        self.diskUsage = ""
        self.timezone = ""

        # basic info
        self.alias = ""
        self.architecture = ""
        self.createTime = ""
        self.description = ""
        self.hostAgentId = ""
        self.hostAgentStatus = ""
        self.hostAgentVersion = ""
        self.idcDescription = ""
        self.idcId = ""
        self.idcName = ""
        self.innerIpAddress = ip
        self.kind = ""
        self.name = ""
        self.operatingSystem = ""
        self.operatingSystemRelease = ""
        self.publishPorts = ""
        self.regionDescription = ""
        self.regionId = ""
        self.regionName = ""
        self.serialNumber = ""
        self.services = []
        self.sshPort = ""
        self.status = ""
        self.typeDescription = ""
        self.typeId = ""
        self.typeName = ""
        self.updateTime = ""
        self.vpcId = ""
        self.vpcName = ""

        self.agent_list = []
        self.installHome = ""
        self.lastAvailableTime = ""
        self.logHome = ""
        self.agent_status = ""
        self.agent_version = ""

    def _seri_info(self, data):
        for k, v in data.items():
            setattr(self, k, v)

        self.ip = self.innerIpAddress

    def get_host_list(self):
        path = ocp_api.host
        response = requests.get(self.url + path, auth=self.auth)
        host_list = []
        host_data = response.json()["data"]["contents"]
        for data in host_data:
            h = Host(self)
            h._seri_info(data)
            host_list.append(h)
        return host_list

    def get_all_host(self):
        return self.get_host_list()
