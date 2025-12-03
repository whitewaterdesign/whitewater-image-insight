from app.prompting.extractor import PromptExtractorFactory
from app.baml_client.sync_client import BamlHttpRequestClient,BamlSyncClient


class Prompts(PromptExtractorFactory):
    _client: BamlHttpRequestClient

    def __init__(self, client: BamlSyncClient):
        self._client = client.request

    def extract_resume(self, resume: str) -> str:
        return self.extract_prompt(self._client.ExtractResume(resume))

    @property
    def visual_verifier(self) -> str:
        return self.extract_prompt(self._client.VisualVerifier())

    @property
    def analysis_description(self) -> str:
        return self.extract_prompt(self._client.AnalysisDescription())