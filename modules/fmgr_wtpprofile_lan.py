#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_wtpprofile_lan
short_description: WTP LAN port mapping.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lan
    - /pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lan
    - Examples include all parameters and values need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
            wtp-profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'WTP LAN port mapping.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - 'object member'
                    - 'chksum'
                    - 'datasrc'
    schema_object1:
        methods: [set, update]
        description: 'WTP LAN port mapping.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                port-mode:
                    type: str
                    description: 'LAN port mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port-ssid:
                    type: str
                    description: 'Bridge LAN port to SSID.'
                port1-mode:
                    type: str
                    description: 'LAN port 1 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port1-ssid:
                    type: str
                    description: 'Bridge LAN port 1 to SSID.'
                port2-mode:
                    type: str
                    description: 'LAN port 2 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port2-ssid:
                    type: str
                    description: 'Bridge LAN port 2 to SSID.'
                port3-mode:
                    type: str
                    description: 'LAN port 3 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port3-ssid:
                    type: str
                    description: 'Bridge LAN port 3 to SSID.'
                port4-mode:
                    type: str
                    description: 'LAN port 4 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port4-ssid:
                    type: str
                    description: 'Bridge LAN port 4 to SSID.'
                port5-mode:
                    type: str
                    description: 'LAN port 5 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port5-ssid:
                    type: str
                    description: 'Bridge LAN port 5 to SSID.'
                port6-mode:
                    type: str
                    description: 'LAN port 6 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port6-ssid:
                    type: str
                    description: 'Bridge LAN port 6 to SSID.'
                port7-mode:
                    type: str
                    description: 'LAN port 7 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port7-ssid:
                    type: str
                    description: 'Bridge LAN port 7 to SSID.'
                port8-mode:
                    type: str
                    description: 'LAN port 8 mode.'
                    choices:
                        - 'offline'
                        - 'bridge-to-wan'
                        - 'bridge-to-ssid'
                        - 'nat-to-wan'
                port8-ssid:
                    type: str
                    description: 'Bridge LAN port 8 to SSID.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LAN
      fmgr_wtpprofile_lan:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LAN
      fmgr_wtpprofile_lan:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  port-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port-ssid: <value of string>
                  port1-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port1-ssid: <value of string>
                  port2-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port2-ssid: <value of string>
                  port3-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port3-ssid: <value of string>
                  port4-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port4-ssid: <value of string>
                  port5-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port5-ssid: <value of string>
                  port6-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port6-ssid: <value of string>
                  port7-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port7-ssid: <value of string>
                  port8-mode: <value in [offline, bridge-to-wan, bridge-to-ssid, ...]>
                  port8-ssid: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            port-mode:
               type: str
               description: 'LAN port mode.'
            port-ssid:
               type: str
               description: 'Bridge LAN port to SSID.'
            port1-mode:
               type: str
               description: 'LAN port 1 mode.'
            port1-ssid:
               type: str
               description: 'Bridge LAN port 1 to SSID.'
            port2-mode:
               type: str
               description: 'LAN port 2 mode.'
            port2-ssid:
               type: str
               description: 'Bridge LAN port 2 to SSID.'
            port3-mode:
               type: str
               description: 'LAN port 3 mode.'
            port3-ssid:
               type: str
               description: 'Bridge LAN port 3 to SSID.'
            port4-mode:
               type: str
               description: 'LAN port 4 mode.'
            port4-ssid:
               type: str
               description: 'Bridge LAN port 4 to SSID.'
            port5-mode:
               type: str
               description: 'LAN port 5 mode.'
            port5-ssid:
               type: str
               description: 'Bridge LAN port 5 to SSID.'
            port6-mode:
               type: str
               description: 'LAN port 6 mode.'
            port6-ssid:
               type: str
               description: 'Bridge LAN port 6 to SSID.'
            port7-mode:
               type: str
               description: 'LAN port 7 mode.'
            port7-ssid:
               type: str
               description: 'Bridge LAN port 7 to SSID.'
            port8-mode:
               type: str
               description: 'LAN port 8 mode.'
            port8-ssid:
               type: str
               description: 'Bridge LAN port 8 to SSID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lan'
return_of_api_category_0:
   description: items returned for method:[set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lan'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lan',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lan'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'wtp-profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'port-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port-ssid': {
                            'type': 'string'
                        },
                        'port1-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port1-ssid': {
                            'type': 'string'
                        },
                        'port2-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port2-ssid': {
                            'type': 'string'
                        },
                        'port3-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port3-ssid': {
                            'type': 'string'
                        },
                        'port4-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port4-ssid': {
                            'type': 'string'
                        },
                        'port5-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port5-ssid': {
                            'type': 'string'
                        },
                        'port6-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port6-ssid': {
                            'type': 'string'
                        },
                        'port7-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port7-ssid': {
                            'type': 'string'
                        },
                        'port8-mode': {
                            'type': 'string',
                            'enum': [
                                'offline',
                                'bridge-to-wan',
                                'bridge-to-ssid',
                                'nat-to-wan'
                            ]
                        },
                        'port8-ssid': {
                            'type': 'string'
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
        }
    }

    module_arg_spec = {
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    method = module.params['method']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()