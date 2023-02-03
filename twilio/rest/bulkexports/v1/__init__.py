"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Bulkexports
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.bulkexports.v1.export import ExportList
from twilio.rest.bulkexports.v1.export_configuration import ExportConfigurationList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Bulkexports

        :param domain: The Twilio.bulkexports domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._exports = None
        self._export_configuration = None
        
    @property
    def exports(self) -> ExportList:
        if self._exports is None:
            self._exports = ExportList(self)
        return self._exports

    @property
    def export_configuration(self) -> ExportConfigurationList:
        if self._export_configuration is None:
            self._export_configuration = ExportConfigurationList(self)
        return self._export_configuration

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Bulkexports.V1>'
