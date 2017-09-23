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


class FileInfo(Model):
    """Information about a image store file.

    :param file_size: The size of file in bytes.
    :type file_size: str
    :param file_version:
    :type file_version: :class:`FileVersion
     <azure.servicefabric.models.FileVersion>`
    :param modified_date: The date and time when the image store file was last
     modified.
    :type modified_date: datetime
    :param store_relative_path: The file path relative to the image store root
     path.
    :type store_relative_path: str
    """

    _attribute_map = {
        'file_size': {'key': 'FileSize', 'type': 'str'},
        'file_version': {'key': 'FileVersion', 'type': 'FileVersion'},
        'modified_date': {'key': 'ModifiedDate', 'type': 'iso-8601'},
        'store_relative_path': {'key': 'StoreRelativePath', 'type': 'str'},
    }

    def __init__(self, file_size=None, file_version=None, modified_date=None, store_relative_path=None):
        self.file_size = file_size
        self.file_version = file_version
        self.modified_date = modified_date
        self.store_relative_path = store_relative_path
