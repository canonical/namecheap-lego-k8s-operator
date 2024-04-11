#!/usr/bin/env python3
# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

"""Retrieves certificates from an ACME server using the namecheap dns provider."""

import logging
from typing import Dict, Optional, cast

from charms.lego_base_k8s.v0.lego_client import AcmeClient
from ops.main import main

logger = logging.getLogger(__name__)


class NamecheapLegoK8s(AcmeClient):
    """Main class that is instantiated every time an event occurs."""

    def __init__(self, *args):
        """Use the lego_client library to manage events."""
        super().__init__(*args, plugin="namecheap")

    @property
    def _namecheap_api_key(self) -> str:
        return cast(str, self.model.config.get("namecheap-api-key", ""))

    @property
    def _namecheap_api_user(self) -> str:
        return cast(str, self.model.config.get("namecheap-api-user", ""))

    @property
    def _namecheap_http_timeout(self) -> Optional[str]:
        return str(self.model.config.get("namecheap-http-timeout"))

    @property
    def _namecheap_polling_interval(self) -> Optional[str]:
        return str(self.model.config.get("namecheap-polling-interval"))

    @property
    def _namecheap_propagation_timeout(self) -> Optional[str]:
        return str(self.model.config.get("namecheap-propagation-timeout"))

    @property
    def _namecheap_ttl(self) -> Optional[str]:
        return str(self.model.config.get("namecheap-ttl"))

    @property
    def _namecheap_sandbox(self) -> Optional[str]:
        return cast(str, self.model.config.get("namecheap-sandbox"))

    @property
    def _plugin_config(self) -> Dict[str, str]:
        """Plugin specific additional configuration for the command."""
        additional_config = {}
        additional_config.update({"NAMECHEAP_API_USER": self._namecheap_api_user})
        additional_config.update({"NAMECHEAP_API_KEY": self._namecheap_api_key})
        if self._namecheap_ttl:
            additional_config.update({"NAMECHEAP_TTL": self._namecheap_ttl})
        if self._namecheap_sandbox:
            additional_config.update({"NAMECHEAP_SANDBOX": self._namecheap_sandbox})
        if self._namecheap_propagation_timeout:
            additional_config.update(
                {"NAMECHEAP_PROPAGATION_TIMEOUT": self._namecheap_propagation_timeout}
            )
        if self._namecheap_polling_interval:
            additional_config.update(
                {"NAMECHEAP_POLLING_INTERVAL": self._namecheap_polling_interval}
            )
        if self._namecheap_http_timeout:
            additional_config.update({"NAMECHEAP_HTTP_TIMEOUT": self._namecheap_http_timeout})
        return additional_config

    def _validate_plugin_config(self) -> str:
        """Check whether required config options are set.

        Returns:
            str: Error message if required options are not set.
        """
        if not self._namecheap_api_key or not self._namecheap_api_user:
            return "namecheap-api-key and namecheap-api-user must be set"
        return ""


if __name__ == "__main__":  # pragma: nocover
    main(NamecheapLegoK8s)
