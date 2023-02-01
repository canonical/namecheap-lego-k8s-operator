# namecheap-acme-operator

## Description

Use the Namecheap ACME operator in your Juju model to secure your web application with 
TLS certificates from Let's Encrypt or any other ACME server.

## Pre-requisites

Charms that require those certificates need to implement the requirer side of the [`tls-certificates-interface`](https://github.com/canonical/tls-certificates-interface).

## Usage

Create a YAML configuration file with the following fields:

```yaml
namecheap-acme-operator:
  email: <Account email address>
  namecheap-username: <Namecheap API user>
  namecheap-api-key: <Namecheap API key>
```

Deploy `namecheap-acme-operator`:

```bash
juju deploy namecheap-acme-operator --config <yaml config file>
```

Relate it to a `tls-certificates-requirer` charm:

```bash
juju relate namecheap-acme-operator:certificates <tls-certificates-requirer>
```

## Config

### Required configuration properties
```
email: <Account email address>
namecheap-username: <Namecheap API user>
namecheap-api-key: <Namecheap API key>
```

### Optional configuration properties
```
namecheap-http-timeout: <API request timeout in seconds>
namecheap-polling-interval: <Time between DNS propagation checks in seconds>
namecheap-propagation-timeout: <Maximum waiting time for DNS propagation in seconds>
namecheap-ttl: <The TTL of the TXT record used for the DNS challenge>
namecheap-sandbox: <Use Namecheap sandbox API>
```

## Relations

`certificates`: `tls-certificates-interface` provider

## OCI Images
-  [Lego Rock Image](https://github.com/canonical/lego-rock)
