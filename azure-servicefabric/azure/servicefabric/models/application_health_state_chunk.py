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

from .entity_health_state_chunk import EntityHealthStateChunk


class ApplicationHealthStateChunk(EntityHealthStateChunk):
    """Represents the health state chunk of a application.
    The application health state chunk contains the application name, its
    aggregated health state and any children services and deployed applications
    that respect the filters in cluster health chunk query description.
    .

    :param health_state: Possible values include: 'Invalid', 'Ok', 'Warning',
     'Error', 'Unknown'
    :type health_state: str or :class:`enum <azure.servicefabric.models.enum>`
    :param application_name:
    :type application_name: str
    :param application_type_name:
    :type application_type_name: str
    :param service_health_state_chunks:
    :type service_health_state_chunks: :class:`ServiceHealthStateChunkList
     <azure.servicefabric.models.ServiceHealthStateChunkList>`
    :param deployed_application_health_state_chunks:
    :type deployed_application_health_state_chunks:
     :class:`DeployedApplicationHealthStateChunkList
     <azure.servicefabric.models.DeployedApplicationHealthStateChunkList>`
    """

    _attribute_map = {
        'health_state': {'key': 'HealthState', 'type': 'str'},
        'application_name': {'key': 'ApplicationName', 'type': 'str'},
        'application_type_name': {'key': 'ApplicationTypeName', 'type': 'str'},
        'service_health_state_chunks': {'key': 'ServiceHealthStateChunks', 'type': 'ServiceHealthStateChunkList'},
        'deployed_application_health_state_chunks': {'key': 'DeployedApplicationHealthStateChunks', 'type': 'DeployedApplicationHealthStateChunkList'},
    }

    def __init__(self, health_state=None, application_name=None, application_type_name=None, service_health_state_chunks=None, deployed_application_health_state_chunks=None):
        super(ApplicationHealthStateChunk, self).__init__(health_state=health_state)
        self.application_name = application_name
        self.application_type_name = application_type_name
        self.service_health_state_chunks = service_health_state_chunks
        self.deployed_application_health_state_chunks = deployed_application_health_state_chunks
