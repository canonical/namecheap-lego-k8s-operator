# Copyright 2022 Canonical Ltd.
# See LICENSE file for licensing details.

import unittest

from charm import NamecheapLegoK8s
from ops.model import ActiveStatus, BlockedStatus
from ops.testing import Harness


class TestCharm(unittest.TestCase):
    def setUp(self):
        self.harness = Harness(NamecheapLegoK8s)
        self.harness.set_leader(True)
        self.harness.set_can_connect("lego", True)
        self.addCleanup(self.harness.cleanup)
        self.harness.begin()
        self.r_id = self.harness.add_relation("certificates", "remote")
        self.harness.add_relation_unit(self.r_id, "remote/0")

    def test_given_config_changed_when_email_is_valid_then_status_is_active(self):
        self.harness.update_config(
            {
                "email": "example@email.com",
                "namecheap-api-user": "example",
                "namecheap-api-key": "example",
            }
        )
        self.harness.evaluate_status()
        self.assertEqual(self.harness.model.unit.status, ActiveStatus())

    def test_given_config_changed_when_email_is_invalid_then_status_is_blocked(self):
        self.harness.update_config(
            {
                "email": "invalid-email",
                "namecheap-api-user": "example",
                "namecheap-api-key": "example",
            }
        )
        self.harness.evaluate_status()
        self.assertEqual(self.harness.model.unit.status, BlockedStatus("Invalid email address"))

    def test_given_config_changed_when_api_user_is_not_provided_then_status_is_blocked(self):
        self.harness.update_config(
            {
                "email": "example@email.com",
            }
        )
        self.harness.evaluate_status()
        self.assertEqual(
            self.harness.model.unit.status,
            BlockedStatus("namecheap-api-key and namecheap-api-user must be set"),
        )

    def test_given_complete_namecheap_config_when_config_changed_then_dict_containing_namecheap_config_is_returned(  # noqa: E501
        self,
    ):
        namecheap_api_user = "example-user"
        namecheap_api_key = "example-key"
        namecheap_http_timeout = 10
        namecheap_propagation_timeout = 11
        namecheap_polling_interval = 12
        namecheap_ttl = 13
        self.harness.update_config(
            {
                "email": "admin@gmail.com",
                "server": "https://acme-staging-v02.api.letsencrypt.org/directory",
                "namecheap-api-user": namecheap_api_user,
                "namecheap-api-key": namecheap_api_key,
                "namecheap-http-timeout": namecheap_http_timeout,
                "namecheap-propagation-timeout": namecheap_propagation_timeout,
                "namecheap-polling-interval": namecheap_polling_interval,
                "namecheap-ttl": namecheap_ttl,
            }
        )

        plugin_config = self.harness.charm._plugin_config

        self.assertEqual(
            {
                "NAMECHEAP_API_USER": namecheap_api_user,
                "NAMECHEAP_API_KEY": namecheap_api_key,
                "NAMECHEAP_HTTP_TIMEOUT": str(namecheap_http_timeout),
                "NAMECHEAP_POLLING_INTERVAL": str(namecheap_polling_interval),
                "NAMECHEAP_PROPAGATION_TIMEOUT": str(namecheap_propagation_timeout),
                "NAMECHEAP_TTL": str(namecheap_ttl),
            },
            plugin_config,
        )

    def test_given_minimal_namecheap_config_when_config_changed_then_dict_containing_namecheap_config_is_returned(  # noqa: E501
        self,
    ):
        namecheap_api_user = "example-user"
        namecheap_api_key = "example-key"
        self.harness.update_config(
            {
                "email": "admin@gmail.com",
                "server": "https://acme-staging-v02.api.letsencrypt.org/directory",
                "namecheap-api-user": namecheap_api_user,
                "namecheap-api-key": namecheap_api_key,
            }
        )

        plugin_config = self.harness.charm._plugin_config

        self.assertEqual(
            {
                "NAMECHEAP_API_USER": namecheap_api_user,
                "NAMECHEAP_API_KEY": namecheap_api_key,
                "NAMECHEAP_HTTP_TIMEOUT": "60",
                "NAMECHEAP_POLLING_INTERVAL": "15",
                "NAMECHEAP_PROPAGATION_TIMEOUT": "3600",
                "NAMECHEAP_TTL": "120",
            },
            plugin_config,
        )
