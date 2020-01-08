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
module: fmgr_pm_config_obj_waf_profile_constraint
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint
    - /pm/config/global/obj/waf/profile/{profile}/constraint
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
            profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'WAF HTTP protocol restrictions.'
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
        description: 'WAF HTTP protocol restrictions.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                content-length:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    length:
                        type: int
                        description: 'Length of HTTP content in bytes (0 to 2147483647).'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                exception:
                    -
                        address:
                            type: str
                            description: 'Host address.'
                        content-length:
                            type: str
                            description: 'HTTP content length in request.'
                            choices:
                                - 'disable'
                                - 'enable'
                        header-length:
                            type: str
                            description: 'HTTP header length in request.'
                            choices:
                                - 'disable'
                                - 'enable'
                        hostname:
                            type: str
                            description: 'Enable/disable hostname check.'
                            choices:
                                - 'disable'
                                - 'enable'
                        id:
                            type: int
                            description: 'Exception ID.'
                        line-length:
                            type: str
                            description: 'HTTP line length in request.'
                            choices:
                                - 'disable'
                                - 'enable'
                        malformed:
                            type: str
                            description: 'Enable/disable malformed HTTP request check.'
                            choices:
                                - 'disable'
                                - 'enable'
                        max-cookie:
                            type: str
                            description: 'Maximum number of cookies in HTTP request.'
                            choices:
                                - 'disable'
                                - 'enable'
                        max-header-line:
                            type: str
                            description: 'Maximum number of HTTP header line.'
                            choices:
                                - 'disable'
                                - 'enable'
                        max-range-segment:
                            type: str
                            description: 'Maximum number of range segments in HTTP range line.'
                            choices:
                                - 'disable'
                                - 'enable'
                        max-url-param:
                            type: str
                            description: 'Maximum number of parameters in URL.'
                            choices:
                                - 'disable'
                                - 'enable'
                        method:
                            type: str
                            description: 'Enable/disable HTTP method check.'
                            choices:
                                - 'disable'
                                - 'enable'
                        param-length:
                            type: str
                            description: 'Maximum length of parameter in URL, HTTP POST request or HTTP body.'
                            choices:
                                - 'disable'
                                - 'enable'
                        pattern:
                            type: str
                            description: 'URL pattern.'
                        regex:
                            type: str
                            description: 'Enable/disable regular expression based pattern match.'
                            choices:
                                - 'disable'
                                - 'enable'
                        url-param-length:
                            type: str
                            description: 'Maximum length of parameter in URL.'
                            choices:
                                - 'disable'
                                - 'enable'
                        version:
                            type: str
                            description: 'Enable/disable HTTP version check.'
                            choices:
                                - 'disable'
                                - 'enable'
                header-length:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    length:
                        type: int
                        description: 'Length of HTTP header in bytes (0 to 2147483647).'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                hostname:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                line-length:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    length:
                        type: int
                        description: 'Length of HTTP line in bytes (0 to 2147483647).'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                malformed:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                max-cookie:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    max-cookie:
                        type: int
                        description: 'Maximum number of cookies in HTTP request (0 to 2147483647).'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                max-header-line:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    max-header-line:
                        type: int
                        description: 'Maximum number HTTP header lines (0 to 2147483647).'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                max-range-segment:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    max-range-segment:
                        type: int
                        description: 'Maximum number of range segments in HTTP range line (0 to 2147483647).'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                max-url-param:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    max-url-param:
                        type: int
                        description: 'Maximum number of parameters in URL (0 to 2147483647).'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                method:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                param-length:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    length:
                        type: int
                        description: 'Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes (0 to 2147483647).'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                url-param-length:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    length:
                        type: int
                        description: 'Maximum length of URL parameter in bytes (0 to 2147483647).'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
                        choices:
                            - 'disable'
                            - 'enable'
                version:
                    action:
                        type: str
                        description: 'Action.'
                        choices:
                            - 'allow'
                            - 'block'
                    log:
                        type: str
                        description: 'Enable/disable logging.'
                        choices:
                            - 'disable'
                            - 'enable'
                    severity:
                        type: str
                        description: 'Severity.'
                        choices:
                            - 'low'
                            - 'medium'
                            - 'high'
                    status:
                        type: str
                        description: 'Enable/disable the constraint.'
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

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/CONSTRAINT
      fmgr_pm_config_obj_waf_profile_constraint:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WAF/PROFILE/{PROFILE}/CONSTRAINT
      fmgr_pm_config_obj_waf_profile_constraint:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  content-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  exception:
                    -
                        address: <value of string>
                        content-length: <value in [disable, enable]>
                        header-length: <value in [disable, enable]>
                        hostname: <value in [disable, enable]>
                        id: <value of integer>
                        line-length: <value in [disable, enable]>
                        malformed: <value in [disable, enable]>
                        max-cookie: <value in [disable, enable]>
                        max-header-line: <value in [disable, enable]>
                        max-range-segment: <value in [disable, enable]>
                        max-url-param: <value in [disable, enable]>
                        method: <value in [disable, enable]>
                        param-length: <value in [disable, enable]>
                        pattern: <value of string>
                        regex: <value in [disable, enable]>
                        url-param-length: <value in [disable, enable]>
                        version: <value in [disable, enable]>
                  header-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  hostname:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  line-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  malformed:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-cookie:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-cookie: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-header-line:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-header-line: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-range-segment:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-range-segment: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  max-url-param:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     max-url-param: <value of integer>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  method:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  param-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  url-param-length:
                     action: <value in [allow, block]>
                     length: <value of integer>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>
                  version:
                     action: <value in [allow, block]>
                     log: <value in [disable, enable]>
                     severity: <value in [low, medium, high]>
                     status: <value in [disable, enable]>

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
            content-length:
               action:
                  type: str
                  description: 'Action.'
               length:
                  type: int
                  description: 'Length of HTTP content in bytes (0 to 2147483647).'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            exception:
               type: array
               suboptions:
                  address:
                     type: str
                     description: 'Host address.'
                  content-length:
                     type: str
                     description: 'HTTP content length in request.'
                  header-length:
                     type: str
                     description: 'HTTP header length in request.'
                  hostname:
                     type: str
                     description: 'Enable/disable hostname check.'
                  id:
                     type: int
                     description: 'Exception ID.'
                  line-length:
                     type: str
                     description: 'HTTP line length in request.'
                  malformed:
                     type: str
                     description: 'Enable/disable malformed HTTP request check.'
                  max-cookie:
                     type: str
                     description: 'Maximum number of cookies in HTTP request.'
                  max-header-line:
                     type: str
                     description: 'Maximum number of HTTP header line.'
                  max-range-segment:
                     type: str
                     description: 'Maximum number of range segments in HTTP range line.'
                  max-url-param:
                     type: str
                     description: 'Maximum number of parameters in URL.'
                  method:
                     type: str
                     description: 'Enable/disable HTTP method check.'
                  param-length:
                     type: str
                     description: 'Maximum length of parameter in URL, HTTP POST request or HTTP body.'
                  pattern:
                     type: str
                     description: 'URL pattern.'
                  regex:
                     type: str
                     description: 'Enable/disable regular expression based pattern match.'
                  url-param-length:
                     type: str
                     description: 'Maximum length of parameter in URL.'
                  version:
                     type: str
                     description: 'Enable/disable HTTP version check.'
            header-length:
               action:
                  type: str
                  description: 'Action.'
               length:
                  type: int
                  description: 'Length of HTTP header in bytes (0 to 2147483647).'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            hostname:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            line-length:
               action:
                  type: str
                  description: 'Action.'
               length:
                  type: int
                  description: 'Length of HTTP line in bytes (0 to 2147483647).'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            malformed:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            max-cookie:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               max-cookie:
                  type: int
                  description: 'Maximum number of cookies in HTTP request (0 to 2147483647).'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            max-header-line:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               max-header-line:
                  type: int
                  description: 'Maximum number HTTP header lines (0 to 2147483647).'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            max-range-segment:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               max-range-segment:
                  type: int
                  description: 'Maximum number of range segments in HTTP range line (0 to 2147483647).'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            max-url-param:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               max-url-param:
                  type: int
                  description: 'Maximum number of parameters in URL (0 to 2147483647).'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            method:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            param-length:
               action:
                  type: str
                  description: 'Action.'
               length:
                  type: int
                  description: 'Maximum length of parameter in URL, HTTP POST request or HTTP body in bytes (0 to 2147483647).'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            url-param-length:
               action:
                  type: str
                  description: 'Action.'
               length:
                  type: int
                  description: 'Maximum length of URL parameter in bytes (0 to 2147483647).'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
            version:
               action:
                  type: str
                  description: 'Action.'
               log:
                  type: str
                  description: 'Enable/disable logging.'
               severity:
                  type: str
                  description: 'Severity.'
               status:
                  type: str
                  description: 'Enable/disable the constraint.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint'
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
            example: '/pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint'

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
        '/pm/config/adom/{adom}/obj/waf/profile/{profile}/constraint',
        '/pm/config/global/obj/waf/profile/{profile}/constraint'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile',
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
                        'content-length': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'length': {
                                'type': 'integer'
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'exception': {
                            'type': 'array',
                            'items': {
                                'address': {
                                    'type': 'string'
                                },
                                'content-length': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'header-length': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'hostname': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'line-length': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'malformed': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'max-cookie': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'max-header-line': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'max-range-segment': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'max-url-param': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'method': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'param-length': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'pattern': {
                                    'type': 'string'
                                },
                                'regex': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'url-param-length': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'version': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                }
                            }
                        },
                        'header-length': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'length': {
                                'type': 'integer'
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'hostname': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'line-length': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'length': {
                                'type': 'integer'
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'malformed': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'max-cookie': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'max-cookie': {
                                'type': 'integer'
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'max-header-line': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'max-header-line': {
                                'type': 'integer'
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'max-range-segment': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'max-range-segment': {
                                'type': 'integer'
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'max-url-param': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'max-url-param': {
                                'type': 'integer'
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'method': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'param-length': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'length': {
                                'type': 'integer'
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'url-param-length': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'length': {
                                'type': 'integer'
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
                        },
                        'version': {
                            'action': {
                                'type': 'string',
                                'enum': [
                                    'allow',
                                    'block'
                                ]
                            },
                            'log': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            },
                            'severity': {
                                'type': 'string',
                                'enum': [
                                    'low',
                                    'medium',
                                    'high'
                                ]
                            },
                            'status': {
                                'type': 'string',
                                'enum': [
                                    'disable',
                                    'enable'
                                ]
                            }
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