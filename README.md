# fortimanager-ansible-generator
The private branch of fortimanager-ansible-generator
1. install dependencies:
```
#pip3 install -r requirements.txt
```
2. generate the modules:
```
#./generate.py
#./prepare_env.sh
#./format_generated_modules_with_autopep8.sh
```
 -  the generated modules are located under directory: `./modules` and sphinx docs material under directory: `./docgen`
 -  it's optional to format the generated modules to pep8 compatible.

3. before running test manually, make sure the hosts inventory is correct
 ```
#cd tests_collection
#ansible-playbook -i hosts/ -vvv script_set.yml
```
note some test cases playbook are outdated, upon errors, please refer to the generated document fox a fix.
