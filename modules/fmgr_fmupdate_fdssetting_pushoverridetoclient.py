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
module: fmgr_fmupdate_fdssetting_pushoverridetoclient
short_description: Enable/disable push updates, and override the default IP address and port used by FortiGuard to send antivirus and IPS push messages for...
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /cli/global/fmupdate/fds-setting/push-override-to-client
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
    schema_object0:
        methods: [get]
        description: 'Enable/disable push updates, and override the default IP address and port used by FortiGuard to send antivirus and IPS push messages f...'
        api_categories: [api_tag0]
        api_tag0:
    schema_object1:
        methods: [set, update]
        description: 'Enable/disable push updates, and override the default IP address and port used by FortiGuard to send antivirus and IPS push messages f...'
        api_categories: [api_tag0]
        api_tag0:
            data:
                announce-ip:
                    -
                        id:
                            type: int
                            default: 0
                            description: 'ID of the announce IP address (1 - 10).'
                        ip:
                            type: str
                            default: '0.0.0.0'
                            description: 'Announce IPv4 address.'
                        port:
                            type: int
                            default: 8890
                            description: 'Announce IP port (1 - 65535, default = 8890).'
                status:
                    type: str
                    default: 'disable'
                    description:
                     - 'Enable/disable push updates (default = disable).'
                     - 'disable - Disable setting.'
                     - 'enable - Enable setting.'
                    choices:
                        - 'disable'
                        - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /CLI/FMUPDATE/FDS-SETTING/PUSH-OVERRIDE-TO-CLIENT
      fmgr_fmupdate_fdssetting_pushoverridetoclient:
         method: <value in [set, update]>
         params:
            -
               data:
                  announce-ip:
                    -
                        id: <value of integer default: 0>
                        ip: <value of string default: '0.0.0.0'>
                        port: <value of integer default: 8890>
                  status: <value in [disable, enable] default: 'disable'>

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
            announce-ip:
               type: array
               suboptions:
                  id:
                     type: int
                     description: 'ID of the announce IP address (1 - 10).'
                     example: 0
                  ip:
                     type: str
                     description: 'Announce IPv4 address.'
                     example: '0.0.0.0'
                  port:
                     type: int
                     description: 'Announce IP port (1 - 65535, default = 8890).'
                     example: 8890
            status:
               type: str
               description: |
                  'Enable/disable push updates (default = disable).'
                  'disable - Disable setting.'
                  'enable - Enable setting.'
               example: 'disable'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/fmupdate/fds-setting/push-override-to-client'
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
            example: '/cli/global/fmupdate/fds-setting/push-override-to-client'

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
        '/cli/global/fmupdate/fds-setting/push-override-to-client'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
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
                        'announce-ip': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer',
                                    'default': 0,
                                    'example': 0
                                },
                                'ip': {
                                    'type': 'string'
                                },
                                'port': {
                                    'type': 'integer',
                                    'default': 8890,
                                    'example': 8890
                                }
                            }
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
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

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
