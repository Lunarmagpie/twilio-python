"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Notify
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.notify.v1.credential import CredentialList
from twilio.rest.notify.v1.service import ServiceList


class V1(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the V1 version of Notify

        :param domain: The Twilio.notify domain
        """
        super().__init__(domain)
        self.version = 'v1'
        self._credentials = None
        self._services = None
        
    @property
    def credentials(self) -> CredentialList:
        if self._credentials is None:
            self._credentials = CredentialList(self)
        return self._credentials

    @property
    def services(self) -> ServiceList:
        if self._services is None:
            self._services = ServiceList(self)
        return self._services

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Notify.V1>'
