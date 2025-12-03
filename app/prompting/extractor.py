from typing import Any
from abc import ABC, abstractmethod
from baml_py.baml_py import HTTPRequest

class PromptExtractor(ABC):
    def _get_json(self, request: HTTPRequest) -> dict[str, Any]:
        return request.body.json()

    @abstractmethod
    def extract_prompt(self, _request: HTTPRequest) -> str:
        pass

class AzurePromptExtractor(PromptExtractor):
    def extract_prompt(self, request: HTTPRequest) -> str:
        prompt = ""
        request_body = self._get_json(request)

        if request_body is None:
            return prompt

        for message in request_body.get("messages", []):
            for content in message.get("content", []):
                prompt += content.get("text", "")

        return prompt

class OpenAIPromptExtractor(PromptExtractor):
    def extract_prompt(self, request: HTTPRequest) -> str:
        prompt = ""
        request_body = self._get_json(request)

        if request_body is None:
            return prompt

        for request_input in request_body.get('inputs', []):
            for content in request_input.get("content", []):
                prompt += content.get("text", "")

        return prompt


# This can change if we change the prompt type
class PromptExtractorFactory(AzurePromptExtractor):
    pass