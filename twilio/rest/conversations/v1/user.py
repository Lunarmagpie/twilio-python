# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class UserList(ListResource):

    def __init__(self, version):
        """
        Initialize the UserList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.conversations.v1.user.UserList
        :rtype: twilio.rest.conversations.v1.user.UserList
        """
        super(UserList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Users'.format(**self._solution)

    def create(self, identity, friendly_name=values.unset, attributes=values.unset,
               role_sid=values.unset, x_twilio_webhook_enabled=values.unset):
        """
        Create the UserInstance

        :param unicode identity: The string that identifies the resource's User
        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode attributes: The JSON Object string that stores application-specific data
        :param unicode role_sid: The SID of a service-level Role to assign to the user
        :param UserInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The created UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        data = values.of({
            'Identity': identity,
            'FriendlyName': friendly_name,
            'Attributes': attributes,
            'RoleSid': role_sid,
        })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.create(method='POST', uri=self._uri, data=data, headers=headers, )

        return UserInstance(self._version, payload, )

    def stream(self, limit=None, page_size=None):
        """
        Streams UserInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.user.UserInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists UserInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.user.UserInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of UserInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return UserPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of UserInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return UserPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to fetch

        :returns: twilio.rest.conversations.v1.user.UserContext
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a UserContext

        :param sid: The SID of the User resource to fetch

        :returns: twilio.rest.conversations.v1.user.UserContext
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        return UserContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserList>'


class UserPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the UserPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.conversations.v1.user.UserPage
        :rtype: twilio.rest.conversations.v1.user.UserPage
        """
        super(UserPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of UserInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.user.UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        return UserInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.UserPage>'


class UserContext(InstanceContext):

    def __init__(self, version, sid):
        """
        Initialize the UserContext

        :param Version version: Version that contains the resource
        :param sid: The SID of the User resource to fetch

        :returns: twilio.rest.conversations.v1.user.UserContext
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        super(UserContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Users/{sid}'.format(**self._solution)

    def update(self, friendly_name=values.unset, attributes=values.unset,
               role_sid=values.unset, x_twilio_webhook_enabled=values.unset):
        """
        Update the UserInstance

        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode attributes: The JSON Object string that stores application-specific data
        :param unicode role_sid: The SID of a service-level Role to assign to the user
        :param UserInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The updated UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        data = values.of({'FriendlyName': friendly_name, 'Attributes': attributes, 'RoleSid': role_sid, })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers, )

        return UserInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the UserInstance

        :param UserInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        return self._version.delete(method='DELETE', uri=self._uri, headers=headers, )

    def fetch(self):
        """
        Fetch the UserInstance

        :returns: The fetched UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return UserInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.UserContext {}>'.format(context)


class UserInstance(InstanceResource):

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the UserInstance

        :returns: twilio.rest.conversations.v1.user.UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        super(UserInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'chat_service_sid': payload.get('chat_service_sid'),
            'role_sid': payload.get('role_sid'),
            'identity': payload.get('identity'),
            'friendly_name': payload.get('friendly_name'),
            'attributes': payload.get('attributes'),
            'is_online': payload.get('is_online'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: UserContext for this UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserContext
        """
        if self._context is None:
            self._context = UserContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def chat_service_sid(self):
        """
        :returns: The SID of the Conversation Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['chat_service_sid']

    @property
    def role_sid(self):
        """
        :returns: The SID of a service-level Role assigned to the user
        :rtype: unicode
        """
        return self._properties['role_sid']

    @property
    def identity(self):
        """
        :returns: The string that identifies the resource's User
        :rtype: unicode
        """
        return self._properties['identity']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def attributes(self):
        """
        :returns: The JSON Object string that stores application-specific data
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def is_online(self):
        """
        :returns: Whether the User is actively connected to the Service instance and online
        :rtype: bool
        """
        return self._properties['is_online']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: An absolute URL for this user.
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, friendly_name=values.unset, attributes=values.unset,
               role_sid=values.unset, x_twilio_webhook_enabled=values.unset):
        """
        Update the UserInstance

        :param unicode friendly_name: The string that you assigned to describe the resource
        :param unicode attributes: The JSON Object string that stores application-specific data
        :param unicode role_sid: The SID of a service-level Role to assign to the user
        :param UserInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The updated UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            attributes=attributes,
            role_sid=role_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    def delete(self, x_twilio_webhook_enabled=values.unset):
        """
        Deletes the UserInstance

        :param UserInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete(x_twilio_webhook_enabled=x_twilio_webhook_enabled, )

    def fetch(self):
        """
        Fetch the UserInstance

        :returns: The fetched UserInstance
        :rtype: twilio.rest.conversations.v1.user.UserInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.UserInstance {}>'.format(context)
