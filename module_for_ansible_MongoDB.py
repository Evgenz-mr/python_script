ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: my_sample_module

short_description: This is my sample module

version_added: "2.4"

description:
    - "This is my longer description explaining my sample module"

options:
    name:
        description:
            - This is the message to send to the sample module
        required: true
    new:
        description:
            - Control to demo if the result of this module is changed or not
        required: false

extends_documentation_fragment:
    - azure

author:
    - Evgeny Mrykhin (evgenz-mr@ya.ru)
'''

EXAMPLES = '''
# Pass in a message
- name: Test with a message
  my_new_test_module:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_new_test_module:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_new_test_module:
    name: fail me
'''

RETURN = '''
original_message:
    description: The original name param that was passed in
    type: str
    returned: always
message:
    description: The output message that the sample module generates
    type: str
    returned: always
'''

import os
from ansible.module_utils.basic import AnsibleModule
from distutils.version import LooseVersion


def mongo_db_version(self):
    self.rhel55-3.0.14 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-rhel55-3.0.14.tgz
    self.rhel64-3.0.14 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-rhel64-3.0.14
    self.rhel70-3.0.14 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-rhel64-3.0.14
    self.ubuntu1804-4.1.13 = https://www.mongodb.org/dl/linux/ongodb-linux-x86_64-rhel70-3.0.14
    self.ubuntu1604-3.6.13 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-ubuntu1604-3.6.13
    self.ubuntu1604-3.0.15 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-ubuntu1604-3.0.15
    self.debian81-3.6.13 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-debian81-3.6.13
    self.debian92-3.6.13 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-debian92-3.6.13
    self.debian92-4.1.13 = https://www.mongodb.org/dl/linux/mongodb-linux-x86_64-debian92-4.1.13.tgz




def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )
