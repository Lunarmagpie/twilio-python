"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from twilio.base.version import Version
from twilio.base.domain import Domain
from twilio.rest.preview.understand.assistant import AssistantListInstance


class Understand(Version):

    def __init__(self, domain: Domain):
        """
        Initialize the Understand version of preview

        :param domain: The Twilio.preview domain
        """
        super().__init__(domain)
        self.version = 'understand'
        self._assistants = None
        
    @property
    def assistants(self) -> AssistantListInstance:
        if self._assistants is None:
            self._assistants = AssistantListInstance(self)
        return self._assistants

    def __repr__(self) -> str:
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.preview.Understand>'
