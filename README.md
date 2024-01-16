# Namecheap LEGO Operator (K8s)
[![CharmHub Badge](https://charmhub.io/namecheap-lego-k8s/badge.svg)](https://charmhub.io/namecheap-lego-k8s)

Let's Encrypt certificates in the Juju ecosystem for Namecheap users.

## Pre-requisites

Charms that require those certificates need to implement the requirer side of the [`tls-certificates-interface`](https://github.com/canonical/tls-certificates-interface).

## Usage

Create a YAML configuration file with the following fields:

```yaml
namecheap-lego-k8s:
  email: <Account email address>
  namecheap-username: <Namecheap API user>
  namecheap-api-key: <Namecheap API key>
```

Deploy `namecheap-lego-k8s`:

```bash
juju deploy namecheap-lego-k8s --config <yaml config file>
```

Relate it to a `tls-certificates-requirer` charm:

```bash
juju relate namecheap-lego-k8s:certificates <tls-certificates-requirer>
```

## Config

### Required configuration properties

- email: Account email address
- namecheap-username: Namecheap API user
- namecheap-api-key: Namecheap API key

### Optional configuration properties

- server: Let's Encrypt server to use (default: `https://acme-v02.api.letsencrypt.org/directory`)
- namecheap-http-timeout: API request timeout in seconds (default: `60`)
- namecheap-polling-interval: Time between DNS propagation checks in seconds (default: `15`)
- namecheap-propagation-timeout: Maximum waiting time for DNS propagation in seconds (default: `3600`)
- namecheap-ttl: The TTL of the TXT record used for the DNS challenge in seconds (default: `120`)
- namecheap-sandbox: Use Namecheap sandbox API (default: `false`)


## Relations

`certificates`: `tls-certificates-interface` provider

## OCI Images

-  [Lego Rock Image](https://github.com/canonical/lego-rock)
