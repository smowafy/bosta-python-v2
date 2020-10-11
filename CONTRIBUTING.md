# Contributing

We are open to, and grateful for, any contributions made by the community. By contributing to bosta, you agree to abide by the[code of conduct](https: // github.com / bostaapp / bosta - python / tree / master / CODE_OF_CONDUCT.md).

# Code Style

- Please follow the[PEP 8 - - Coding Standard](https: // www.python.org / dev / peps / pep - 0008 /) .
- To check style linting run the following command:
    ```bash
    pip install pycodestyle

    pycodestyle {source_file_or_directory}

    ```
- To fix style linting run the following command:
    ```bash
     pip install - -upgrade autopep8

     autopep8 - - in -place - -aggressive - -aggressive < filename >
    ```


# Commit Messages

Commit messages should be verb based, using the following pattern:

- `Fixing ...`
- `Adding ...`
- `Updating ...`
- `Removing ...`

# Documentation

Please update the[docs](README.md) accordingly so that there are no discrepancies between the API and the documentation.

# Developing

- `composer install` install dependencies

# Releasing

- **Consider our release cycle ** - We try to follow[SemVer v2.0.0](http: // semver.org /) . Randomly breaking public APIs is not an option.

- **Create feature branches ** - Don't ask us to pull from your master branch.

- **One pull request per feature ** - If you want to do more than one thing, send multiple pull requests.

- **Send coherent history ** - Make sure each individual commit in your pull request is meaningful. If you had to make multiple intermediate commits while developing, please[squash them](http: // www.git - scm.com / book / en / v2 / Git - Tools - Rewriting - History  # Changing-Multiple-Commit-Messages) before submitting.


# Running Tests

``` bash
$ composer test
```
