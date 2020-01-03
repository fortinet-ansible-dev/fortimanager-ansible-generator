# ansible-fortimanager-generic

### What's the generic module?

The generic module is to fill the gap which exists between FortiManager features being published and Ansible modules reflecting those features.

### Setup the environment 
make sure you have `ansible>=2.8.0` installed with python2 or python3. run the `setup.py` to copy the generic module to ansible module directory.

```sh
$python3 setup.py 
$python2 setup.py # if you are using python2
```

### module usage

the generic module utilizes existing fortimanager plugin to encapsulate data to request FortiManager device. In specific, one request contains the payload with skeleton as below:

```
{
    "id": 1,
    "method": "...",
    "params": [ ... ],
    "session": "..."
}
```
with the generic fortimanager ansible module, the `id` and `session` are taken over by fortimanager httpapi plugin, users should ignore them, only `method` and `params` are from user input. 

there are two ways to write an ansible playbook with the generic fortimananger module.

#### `json` with plain text

the `json` is defined as a string, user must provide the json-formatted string, one example of this sort is given as below: 
```
- hosts: fortimanager01
  connection: httpapi
  vars:
    adom: "root"
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    -   name: 'create a script on fortimanager'
        fmgr_generic:
             json: |
                  {
                   "method":"add",
                   "params":[
                    {
                         "url":"/dvmdb/adom/root/script",
                         "data":[
                            {
                               "name": "user_script0",
                               "type": "cli", 
                               "desc": "The script is created by ansible fortimanager generic module",
                               "content": "the script content to be executed on FortiGate"
                            }
                          ]
                     }
                    ]
                  }
```