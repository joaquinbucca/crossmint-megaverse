import os
from typing import Dict, Optional, Any

import requests


class CustomerIdNotProvidedException(Exception):

    def __init__(self) -> None:
        super().__init__(
            "Customer Id wasn't provided. Hint: have you added it as an env variable called CROSSMINT_CANDIDATE_ID?"
        )


class CrossmintHttpClient:

    URL_PREFIX = "https://challenge.crossmint.io/api/"

    @property
    def _candidate_id(self) -> str:
        candidate_id = os.environ.get("CROSSMINT_CANDIDATE_ID")
        if not candidate_id:
            raise CustomerIdNotProvidedException()

        return candidate_id

    def get(self, path: str) -> Dict[str, Any]:
        return self._request("GET", path)

    def post(self, path: str, body: Dict[str, str]) -> Dict[str, Any]:
        return self._request("POST", path, body=self.enrich_body(body))

    def delete(self, path: str, body: Dict[str, str]) -> Dict[str, Any]:
        return self._request("DELETE", path, body=self.enrich_body(body))

    def enrich_body(self, body: Dict[str, str]) -> Dict[str, Any]:
        body["candidateId"] = self._candidate_id
        return body

    def _request(self, method: str, path: str, body: Optional[Dict[str, str]]=None) -> Dict[str, Any]:
        rsp = requests.request(method, self.URL_PREFIX + path, json=body, headers={'Content-type': 'application/json'})
        rsp.raise_for_status()

        return rsp.json()
