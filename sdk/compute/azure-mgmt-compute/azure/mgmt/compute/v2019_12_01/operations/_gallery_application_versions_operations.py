# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class GalleryApplicationVersionsOperations(object):
    """GalleryApplicationVersionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.compute.v2019_12_01.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        gallery_application_version_name,  # type: str
        gallery_application_version,  # type: "_models.GalleryApplicationVersion"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.GalleryApplicationVersion"
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GalleryApplicationVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
            'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
            'galleryApplicationVersionName': self._serialize.url("gallery_application_version_name", gallery_application_version_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(gallery_application_version, 'GalleryApplicationVersion')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize('GalleryApplicationVersion', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('GalleryApplicationVersion', pipeline_response)

        if response.status_code == 202:
            deserialized = self._deserialize('GalleryApplicationVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}'}  # type: ignore

    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        gallery_application_version_name,  # type: str
        gallery_application_version,  # type: "_models.GalleryApplicationVersion"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.GalleryApplicationVersion"]
        """Create or update a gallery Application Version.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version is to be created.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         created. Needs to follow semantic version name pattern: The allowed characters are digit and
         period. Digits must be within the range of a 32-bit integer. Format:
         :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`.
        :type gallery_application_version_name: str
        :param gallery_application_version: Parameters supplied to the create or update gallery
         Application Version operation.
        :type gallery_application_version: ~azure.mgmt.compute.v2019_12_01.models.GalleryApplicationVersion
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the ARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either GalleryApplicationVersion or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.compute.v2019_12_01.models.GalleryApplicationVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GalleryApplicationVersion"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                resource_group_name=resource_group_name,
                gallery_name=gallery_name,
                gallery_application_name=gallery_application_name,
                gallery_application_version_name=gallery_application_version_name,
                gallery_application_version=gallery_application_version,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('GalleryApplicationVersion', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
            'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
            'galleryApplicationVersionName': self._serialize.url("gallery_application_version_name", gallery_application_version_name, 'str'),
        }

        if polling is True: polling_method = ARMPolling(lro_delay, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}'}  # type: ignore

    def _update_initial(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        gallery_application_version_name,  # type: str
        gallery_application_version,  # type: "_models.GalleryApplicationVersionUpdate"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.GalleryApplicationVersion"
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GalleryApplicationVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-01"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._update_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
            'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
            'galleryApplicationVersionName': self._serialize.url("gallery_application_version_name", gallery_application_version_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(gallery_application_version, 'GalleryApplicationVersionUpdate')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GalleryApplicationVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _update_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}'}  # type: ignore

    def begin_update(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        gallery_application_version_name,  # type: str
        gallery_application_version,  # type: "_models.GalleryApplicationVersionUpdate"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.GalleryApplicationVersion"]
        """Update a gallery Application Version.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version is to be updated.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         updated. Needs to follow semantic version name pattern: The allowed characters are digit and
         period. Digits must be within the range of a 32-bit integer. Format:
         :code:`<MajorVersion>`.:code:`<MinorVersion>`.:code:`<Patch>`.
        :type gallery_application_version_name: str
        :param gallery_application_version: Parameters supplied to the update gallery Application
         Version operation.
        :type gallery_application_version: ~azure.mgmt.compute.v2019_12_01.models.GalleryApplicationVersionUpdate
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the ARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either GalleryApplicationVersion or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~azure.mgmt.compute.v2019_12_01.models.GalleryApplicationVersion]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GalleryApplicationVersion"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._update_initial(
                resource_group_name=resource_group_name,
                gallery_name=gallery_name,
                gallery_application_name=gallery_application_name,
                gallery_application_version_name=gallery_application_version_name,
                gallery_application_version=gallery_application_version,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize('GalleryApplicationVersion', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
            'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
            'galleryApplicationVersionName': self._serialize.url("gallery_application_version_name", gallery_application_version_name, 'str'),
        }

        if polling is True: polling_method = ARMPolling(lro_delay, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}'}  # type: ignore

    def get(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        gallery_application_version_name,  # type: str
        expand=None,  # type: Optional[Union[str, "_models.ReplicationStatusTypes"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.GalleryApplicationVersion"
        """Retrieves information about a gallery Application Version.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version resides.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         retrieved.
        :type gallery_application_version_name: str
        :param expand: The expand expression to apply on the operation.
        :type expand: str or ~azure.mgmt.compute.v2019_12_01.models.ReplicationStatusTypes
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GalleryApplicationVersion, or the result of cls(response)
        :rtype: ~azure.mgmt.compute.v2019_12_01.models.GalleryApplicationVersion
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GalleryApplicationVersion"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-01"
        accept = "application/json"

        # Construct URL
        url = self.get.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
            'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
            'galleryApplicationVersionName': self._serialize.url("gallery_application_version_name", gallery_application_version_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, 'str')
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = self._deserialize('GalleryApplicationVersion', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}'}  # type: ignore

    def _delete_initial(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        gallery_application_version_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-01"
        accept = "application/json"

        # Construct URL
        url = self._delete_initial.metadata['url']  # type: ignore
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
            'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
            'galleryApplicationVersionName': self._serialize.url("gallery_application_version_name", gallery_application_version_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 202, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    _delete_initial.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}'}  # type: ignore

    def begin_delete(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        gallery_application_version_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller[None]
        """Delete a gallery Application Version.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides.
        :type gallery_name: str
        :param gallery_application_name: The name of the gallery Application Definition in which the
         Application Version resides.
        :type gallery_application_name: str
        :param gallery_application_version_name: The name of the gallery Application Version to be
         deleted.
        :type gallery_application_version_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: Pass in True if you'd like the ARMPolling polling method,
         False for no polling, or your own initialized polling object for a personal polling strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either None or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[None]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._delete_initial(
                resource_group_name=resource_group_name,
                gallery_name=gallery_name,
                gallery_application_name=gallery_application_name,
                gallery_application_version_name=gallery_application_version_name,
                cls=lambda x,y,z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            if cls:
                return cls(pipeline_response, None, {})

        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
            'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
            'galleryApplicationVersionName': self._serialize.url("gallery_application_version_name", gallery_application_version_name, 'str'),
        }

        if polling is True: polling_method = ARMPolling(lro_delay, path_format_arguments=path_format_arguments,  **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions/{galleryApplicationVersionName}'}  # type: ignore

    def list_by_gallery_application(
        self,
        resource_group_name,  # type: str
        gallery_name,  # type: str
        gallery_application_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.GalleryApplicationVersionList"]
        """List gallery Application Versions in a gallery Application Definition.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param gallery_name: The name of the Shared Application Gallery in which the Application
         Definition resides.
        :type gallery_name: str
        :param gallery_application_name: The name of the Shared Application Gallery Application
         Definition from which the Application Versions are to be listed.
        :type gallery_application_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either GalleryApplicationVersionList or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.compute.v2019_12_01.models.GalleryApplicationVersionList]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.GalleryApplicationVersionList"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2019-12-01"
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_by_gallery_application.metadata['url']  # type: ignore
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'galleryName': self._serialize.url("gallery_name", gallery_name, 'str'),
                    'galleryApplicationName': self._serialize.url("gallery_application_name", gallery_application_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize('GalleryApplicationVersionList', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_gallery_application.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/galleries/{galleryName}/applications/{galleryApplicationName}/versions'}  # type: ignore
