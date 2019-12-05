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

from .resource import Resource


class Timeseries(Resource):
    """Defines the Timeseries.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param endpoint: The endpoint associated with the Timeseries data point
    :type endpoint: str
    :param start_date_time_utc: The start DateTime of the Timeseries in UTC
    :type start_date_time_utc: str
    :param end_date_time_utc: The end DateTime of the Timeseries in UTC
    :type end_date_time_utc: str
    :param aggregation_interval: The aggregation interval of the Timeseries.
     Possible values include: 'Hourly', 'Daily'
    :type aggregation_interval: str or
     ~azure.mgmt.frontdoor.models.AggregationInterval
    :param timeseries_type: The type of Timeseries. Possible values include:
     'MeasurementCounts', 'LatencyP50', 'LatencyP75', 'LatencyP95'
    :type timeseries_type: str or ~azure.mgmt.frontdoor.models.TimeseriesType
    :param country: The country associated with the Timeseries. Values are
     country ISO codes as specified here-
     https://www.iso.org/iso-3166-country-codes.html
    :type country: str
    :param timeseries_data: The set of data points for the timeseries
    :type timeseries_data:
     list[~azure.mgmt.frontdoor.models.TimeseriesDataPoint]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
        'start_date_time_utc': {'key': 'properties.startDateTimeUTC', 'type': 'str'},
        'end_date_time_utc': {'key': 'properties.endDateTimeUTC', 'type': 'str'},
        'aggregation_interval': {'key': 'properties.aggregationInterval', 'type': 'str'},
        'timeseries_type': {'key': 'properties.timeseriesType', 'type': 'str'},
        'country': {'key': 'properties.country', 'type': 'str'},
        'timeseries_data': {'key': 'properties.timeseriesData', 'type': '[TimeseriesDataPoint]'},
    }

    def __init__(self, **kwargs):
        super(Timeseries, self).__init__(**kwargs)
        self.endpoint = kwargs.get('endpoint', None)
        self.start_date_time_utc = kwargs.get('start_date_time_utc', None)
        self.end_date_time_utc = kwargs.get('end_date_time_utc', None)
        self.aggregation_interval = kwargs.get('aggregation_interval', None)
        self.timeseries_type = kwargs.get('timeseries_type', None)
        self.country = kwargs.get('country', None)
        self.timeseries_data = kwargs.get('timeseries_data', None)