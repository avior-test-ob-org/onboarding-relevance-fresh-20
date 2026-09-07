import asyncio
import json
import os
from typing import NamedTuple

import httpx
from fastapi import FastAPI


class Peer(NamedTuple):
    repository: str
    url_environment_variable: str


SERVICE_NAME = "onboarding-relevance-fresh-20"
PEERS: tuple[Peer, ...] = (
    Peer("avior-test-ob-org/onboarding-relevance-fresh-01", "FRESH_01_URL"),
    Peer("avior-test-ob-org/onboarding-relevance-fresh-02", "FRESH_02_URL"),
)
app = FastAPI(title=SERVICE_NAME)


@app.get("/v1/identity")
async def identity() -> dict[str, str]:
    return {"repository": f"avior-test-ob-org/{SERVICE_NAME}"}


async def _fetch_identity(
    client: httpx.AsyncClient, peer: Peer
) -> dict[str, object]:
    peer_name = peer.repository.rsplit("/", maxsplit=1)[-1]
    default_url = f"https://{peer_name}.example.test"
    base_url = os.getenv(peer.url_environment_variable, default_url)
    try:
        response = await client.get(f"{base_url.rstrip(chr(47))}/v1/identity")
        response.raise_for_status()
        identity_data = response.json()
        if not isinstance(identity_data, dict) or not isinstance(
            identity_data.get("repository"), str
        ):
            raise ValueError("invalid peer identity payload")
        return {"repository": peer.repository, "identity": identity_data}
    except (httpx.HTTPError, json.JSONDecodeError, ValueError) as error:
        return {
            "repository": peer.repository,
            "status": "unavailable",
            "error": type(error).__name__,
        }


@app.get("/v1/peer-identities")
async def peer_identities() -> list[dict[str, object]]:
    async with httpx.AsyncClient(timeout=2.0) as client:
        return list(
            await asyncio.gather(*(_fetch_identity(client, peer) for peer in PEERS))
        )
