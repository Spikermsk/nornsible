#!/usr/bin/env python
inv = """
{
  "all": {
      "virl": {
        "children": [
          "asa",
          "ios"
        ],
        "hosts": [],
        "vars": {}
      },
      "asa": {
        "children": [],
        "hosts": [
          "asa1"
        ],
        "vars": {
          "ansible_become": "yes",
          "ansible_become_method": "enable",
          "ansible_network_os": "asa",
          "ansible_persistent_command_timeout": 30,
          "cisco_asa": true,
          "network_os": "asa"
        }
      },
      "ios": {
        "children": [
          "access",
          "dist",
          "routers"
        ],
        "hosts": [],
        "vars": {
          "network_os": "ios",
          "nornir_nos": "ios",
          "platform": "ios"
        }
      },
      "access": {
        "children": [],
        "hosts": [
          "access1"
        ],
        "vars": {}
      },
      "dist": {
        "children": [],
        "hosts": [
          "dist1",
          "dist2"
        ],
        "vars": {}
      },
      "routers": {
        "children": [],
        "hosts": [
          "iosv-1",
          "iosv-2"
        ],
        "vars": {}
      }
  },
  "_meta": {
    "hostvars": {
      "asa1": {
        "ansible_host": "10.255.0.2",
        "dot1x": true
      },
      "access1": {
        "ansible_host": "10.255.0.6"
      },
      "dist1": {
        "ansible_host": "10.255.0.5"
      },
      "dist2": {
        "ansible_host": "10.255.0.11"
      },
      "iosv-1": {
        "ansible_host": "10.255.0.12"
      },
      "iosv-2": {
        "ansible_host": "10.255.0.13"
      }
    }
  },
  "vars": {
    "ansible_connection": "network_cli",
    "ansible_network_os": "ios",
    "ansible_python_interpreter": "python",
    "ansible_ssh_common_args": "-o ProxyCommand=\\"ssh -W %h:%p -p 10000 guest@10.105.152.50\\"",
    "env": "staging"
  }
}
"""


print(inv)
