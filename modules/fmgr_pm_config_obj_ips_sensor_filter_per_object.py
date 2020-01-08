#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019 Fortinet, Inc.
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
module: fmgr_pm_config_obj_ips_sensor_filter_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get move set update ] the following apis.
    - /pm/config/adom/{adom}/obj/ips/sensor/{sensor}/filter/{filter}
    - /pm/config/global/obj/ips/sensor/{sensor}/filter/{filter}
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
            sensor:
                type: str
            filter:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'IPS sensor filter.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                action:
                    type: str
                    description: 'Action of selected rules.'
                    choices:
                        - 'pass'
                        - 'block'
                        - 'default'
                        - 'reset'
                application:
                    -
                        type: str
                location:
                    -
                        type: str
                log:
                    type: str
                    description: 'Enable/disable logging of selected rules.'
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'default'
                log-packet:
                    type: str
                    description: 'Enable/disable packet logging of selected rules.'
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'default'
                name:
                    type: str
                    description: 'Filter name.'
                os:
                    -
                        type: str
                protocol:
                    -
                        type: str
                quarantine:
                    type: str
                    description: 'Quarantine IP or interface.'
                    choices:
                        - 'none'
                        - 'attacker'
                        - 'both'
                        - 'interface'
                quarantine-expiry:
                    type: int
                    description: 'Duration of quarantine in minute.'
                quarantine-log:
                    type: str
                    description: 'Enable/disable logging of selected quarantine.'
                    choices:
                        - 'disable'
                        - 'enable'
                severity:
                    -
                        type: str
                status:
                    type: str
                    description: 'Selected rules status.'
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'default'
    schema_object1:
        methods: [delete]
        description: 'IPS sensor filter.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'IPS sensor filter.'
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
    schema_object3:
        methods: [move]
        description: 'IPS sensor filter.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                choices:
                    - 'before'
                    - 'after'
            target:
                type: str
                description: 'Key to the target entry.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}/FILTER/{FILTER}
      fmgr_pm_config_obj_ips_sensor_filter_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
            filter: <value of string>
         params:
            -
               data:
                  action: <value in [pass, block, default, ...]>
                  application:
                    - <value of string>
                  location:
                    - <value of string>
                  log: <value in [disable, enable, default]>
                  log-packet: <value in [disable, enable, default]>
                  name: <value of string>
                  os:
                    - <value of string>
                  protocol:
                    - <value of string>
                  quarantine: <value in [none, attacker, both, ...]>
                  quarantine-expiry: <value of integer>
                  quarantine-log: <value in [disable, enable]>
                  severity:
                    - <value of string>
                  status: <value in [disable, enable, default]>

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}/FILTER/{FILTER}
      fmgr_pm_config_obj_ips_sensor_filter_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
            filter: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}/FILTER/{FILTER}
      fmgr_pm_config_obj_ips_sensor_filter_per_object:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
            filter: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, move, set, update]
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
            example: '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/filter/{filter}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            action:
               type: str
               description: 'Action of selected rules.'
            application:
               type: array
               suboptions:
                  type: str
            location:
               type: array
               suboptions:
                  type: str
            log:
               type: str
               description: 'Enable/disable logging of selected rules.'
            log-packet:
               type: str
               description: 'Enable/disable packet logging of selected rules.'
            name:
               type: str
               description: 'Filter name.'
            os:
               type: array
               suboptions:
                  type: str
            protocol:
               type: array
               suboptions:
                  type: str
            quarantine:
               type: str
               description: 'Quarantine IP or interface.'
            quarantine-expiry:
               type: int
               description: 'Duration of quarantine in minute.'
            quarantine-log:
               type: str
               description: 'Enable/disable logging of selected quarantine.'
            severity:
               type: array
               suboptions:
                  type: str
            status:
               type: str
               description: 'Selected rules status.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/filter/{filter}'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible.module_utils.network.fortimanager.common import FAIL_SOCKET_MSG
from ansible.module_utils.network.fortimanager.common import DEFAULT_RESULT_OBJ
from ansible.module_utils.network.fortimanager.common import FMGRCommon
from ansible.module_utils.network.fortimanager.common import FMGBaseException
from ansible.module_utils.network.fortimanager.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/filter/{filter}',
        '/pm/config/global/obj/ips/sensor/{sensor}/filter/{filter}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'sensor',
            'type': 'string'
        },
        {
            'name': 'filter',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'action': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'block',
                                'default',
                                'reset'
                            ]
                        },
                        'application': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'location': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'default'
                            ]
                        },
                        'log-packet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'default'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'os': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'protocol': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'quarantine': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'attacker',
                                'both',
                                'interface'
                            ]
                        },
                        'quarantine-expiry': {
                            'type': 'integer'
                        },
                        'quarantine-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'severity': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'default'
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
            ],
            'object1': [
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
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
            'object3': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'before',
                            'after'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'target',
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
            'move': 'object3',
            'set': 'object0',
            'update': 'object0'
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
                'clone',
                'delete',
                'get',
                'move',
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