# Contributing

You can use the environments created by `tox` for development:

```bash
tox --notest -e unit
source .tox/unit/bin/activate
```

Use `tox` to run the tests:

```bash
tox -e unit  # Unit tests
tox -e static  # Static analysis
tox -e lint  # Linting
tox -e integration  # Integration tests
```
