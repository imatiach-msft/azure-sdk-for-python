# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import functools
from typing import TYPE_CHECKING, overload
import warnings

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from msrest import Serializer

from .. import models as _models
from .._patch import (
    _validate_text_records,
    _get_positional_body,
    _verify_qna_id_and_question,
    _handle_metadata_filter_conversion,
)

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar("T")
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
# fmt: off

def build_get_answers_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]
    project_name = kwargs.pop('project_name')  # type: str
    deployment_name = kwargs.pop('deployment_name')  # type: str

    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/:query-knowledgebases')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['projectName'] = _SERIALIZER.query("project_name", project_name, 'str')
    query_parameters['deploymentName'] = _SERIALIZER.query("deployment_name", deployment_name, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_answers_from_text_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    api_version = "2021-10-01"
    accept = "application/json"
    # Construct URL
    url = kwargs.pop("template_url", '/:query-text')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

# fmt: on
class QuestionAnsweringClientOperationsMixin(object):
    @overload
    def get_answers(
        self,
        options,  # type: "_models.AnswersOptions"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AnswersResult"
        pass

    @overload
    def get_answers(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AnswersResult"
        pass

    @distributed_trace
    def get_answers(
        self,
        *args,  # type: "_models.AnswersOptions"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AnswersResult"
        """Answers the specified question using your knowledge base.

        :param options: Positional only. POST body of the request. Provide either `options`, OR
         individual keyword arguments. If both are provided, only the options object will be used.
        :type options: ~azure.ai.language.questionanswering.models.AnswersOptions
        :keyword project_name: The name of the knowledge base project to use.
        :paramtype project_name: str
        :keyword deployment_name: The name of the specific deployment of the project to use.
        :paramtype deployment_name: str
        :keyword qna_id: Exact QnA ID to fetch from the knowledge base, this field takes priority over
         question.
        :paramtype qna_id: int
        :keyword question: User question to query against the knowledge base.
        :paramtype question: str
        :keyword top: Max number of answers to be returned for the question.
        :paramtype top: int
        :keyword user_id: Unique identifier for the user.
        :paramtype user_id: str
        :keyword confidence_threshold: Minimum threshold score for answers, value ranges from 0 to 1.
        :paramtype confidence_threshold: float
        :keyword answer_context: Context object with previous QnA's information.
        :paramtype answer_context: ~azure.ai.language.questionanswering.models.KnowledgeBaseAnswerContext
        :keyword ranker_kind: Type of ranker to be used. Possible
         values include: "Default", "QuestionOnly".
        :paramtype ranker_kind: str
        :keyword filters: Filter QnAs based on given metadata list and knowledge base sources.
        :paramtype filters: ~azure.ai.language.questionanswering.models.QueryFilters
        :keyword short_answer_options: To configure Answer span prediction feature.
        :paramtype short_answer_options: ~azure.ai.language.questionanswering.models.ShortAnswerOptions
        :keyword include_unstructured_sources: (Optional) Flag to enable Query over Unstructured
         Sources.
        :paramtype include_unstructured_sources: bool
        :return: AnswersResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        options = _get_positional_body(*args, **kwargs) or _models.AnswersOptions(
            qna_id=kwargs.pop("qna_id", None),
            question=kwargs.pop("question", None),
            top=kwargs.pop("top", None),
            user_id=kwargs.pop("user_id", None),
            confidence_threshold=kwargs.pop("confidence_threshold", None),
            answer_context=kwargs.pop("answer_context", None),
            ranker_kind=kwargs.pop("ranker_kind", None),
            filters=kwargs.pop("filters", None),
            short_answer_options=kwargs.pop("short_answer_options", None),
            include_unstructured_sources=kwargs.pop("include_unstructured_sources", None),
        )
        _verify_qna_id_and_question(options)
        options = _handle_metadata_filter_conversion(options)
        cls = kwargs.pop("cls", None)  # type: ClsType["_models.AnswersResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]
        project_name = kwargs.pop("project_name")  # type: str
        deployment_name = kwargs.pop("deployment_name")  # type: str

        json = self._serialize.body(options, "AnswersOptions")

        request = build_get_answers_request(
            content_type=content_type,
            project_name=project_name,
            deployment_name=deployment_name,
            json=json,
            template_url=self.get_answers.metadata["url"],
        )
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("AnswersResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_answers.metadata = {"url": "/:query-knowledgebases"}  # type: ignore

    @overload
    def get_answers_from_text(
        self,
        options,  # type: "_models.AnswersFromTextOptions"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AnswersFromTextResult"
        pass

    @overload
    def get_answers_from_text(
        self, **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AnswersFromTextResult"
        pass

    @distributed_trace
    def get_answers_from_text(
        self,
        *args,  # type: "_models.AnswersFromTextOptions"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AnswersFromTextResult"
        """Answers the specified question using the provided text in the body.

        :param options: Positional only. POST body of the request. Provide either `options`, OR
         individual keyword arguments. If both are provided, only the options object will be used.
        :type options: ~azure.ai.language.questionanswering.models.AnswersFromTextOptions
        :keyword question: User question to query against the given text records.
        :paramtype question: str
        :keyword text_documents: Text records to be searched for given question.
        :paramtype text_documents: list[str or ~azure.ai.language.questionanswering.models.TextDocument]
        :keyword language: Language of the text records. This is BCP-47 representation of a language.
         For example, use "en" for English; "es" for Spanish etc. If not set, use "en" for English as
         default.
        :paramtype language: str
        :return: AnswersFromTextResult
        :rtype: ~azure.ai.language.questionanswering.models.AnswersFromTextResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        options = _get_positional_body(*args, **kwargs) or _models.AnswersFromTextOptions(
            question=kwargs.pop("question"),
            text_documents=kwargs.pop("text_documents"),
            language=kwargs.pop("language", self._default_language),
        )
        try:
            options["records"] = _validate_text_records(options["records"])
        except TypeError:
            options.text_documents = _validate_text_records(options.text_documents)

        cls = kwargs.pop("cls", None)  # type: ClsType["_models.AnswersFromTextResult"]
        error_map = {401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop("error_map", {}))
        content_type = kwargs.pop("content_type", "application/json")  # type: Optional[str]

        json = self._serialize.body(options, "AnswersFromTextOptions")

        request = build_get_answers_from_text_request(
            content_type=content_type,
            json=json,
            template_url=self.get_answers_from_text.metadata["url"],
        )
        path_format_arguments = {
            "Endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("AnswersFromTextResult", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get_answers_from_text.metadata = {"url": "/:query-text"}  # type: ignore
