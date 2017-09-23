# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NodeResult(Model):
    """Contains information about a node that was targeted by a user-induced
    operation.

    :param node_name:
    :type node_name: str
    :param node_instance_id: The node instance id.
    :type node_instance_id: str
    """

    _attribute_map = {
        'node_name': {'key': 'NodeName', 'type': 'str'},
        'node_instance_id': {'key': 'NodeInstanceId', 'type': 'str'},
    }

    def __init__(self, node_name=None, node_instance_id=None):
        self.node_name = node_name
        self.node_instance_id = node_instance_id
