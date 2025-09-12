"""Tests for the HinenOpen API client."""

import pytest

from hinen_open_api.client import HinenOpen


@pytest.mark.asyncio
async def test_client_initialization():
    """Test client initialization with auth parameters."""
    async with HinenOpen(
        host="https://api.example.com",
        app_id="test_app_id",
        app_secret="test_app_secret"
    ) as client:
        assert client.host == "https://api.example.com"
        assert client.app_id == "test_app_id"
        assert client.app_secret == "test_app_secret"
        assert client.auto_refresh_auth is True
        assert client.session is not None


@pytest.mark.asyncio
async def test_client_initialization_without_auth():
    """Test client initialization without auth parameters."""
    async with HinenOpen(host="https://api.example.com") as client:
        assert client.host == "https://api.example.com"
        assert client.app_id is None
        assert client.app_secret is None
        assert client.auto_refresh_auth is False
        assert client.session is not None