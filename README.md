# namecheap-acme-operator

## Description

Namecheap ACME operator implements the provider side of the `tls-certificates-interface`
to provide signed certificates from an ACME servers, using LEGO
(https://go-acme.github.io/lego).

## Usage

Deploy `namecheap-acme-operator`:

Create a YAML configuration file with the following fields:


```yaml
namecheap-acme-operator:
  email: <Account email address>
  namecheap-username: <Namecheap API user>
  namecheap-api-key: <Namecheap API key>
```
`juju deploy namecheap-acme-operator --config <yaml config file>`

Relate it to a `tls-certificates-requirer` charm:

`juju relate namecheap-acme-operator:certificates <tls-certificates-requirer>`

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

## Contributing

Please see the [Juju SDK docs](https://juju.is/docs/sdk) for guidelines on enhancements to this
charm following best practice guidelines, and
[CONTRIBUTING.md](https://github.com/canonical/namecheap-acme-operator/blob/main/CONTRIBUTING.md) for developer
guidance.
