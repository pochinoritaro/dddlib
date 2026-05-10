# dddlib

`dddlib` is a Python library that collects commonly used building blocks for DDD implementations.

This repository uses a workspace layout, and the library itself and the CLI are managed as separate packages.

[日本語版 README](README.ja.md)

## Packages

- [dddlib](packages/dddlib/README.md): Provides infrastructure for domain model base classes, value objects, entities, aggregate roots, domain events, errors, and messages.
- [dddlib_cli](packages/dddlib_cli/README.md): Provides a CLI built on `dddlib`.

## Branch Strategy

This repository follows GitFlow.

- `develop`: integration branch for daily development
- `feature/*`: individual features and fixes are developed from `develop` and merged back into `develop`
- `release/*`: final adjustments before release are developed from `develop` and merged into `main` and `develop`
- `hotfix/*`: urgent fixes are branched from `main` and merged into `main` and `develop`
- `main`: production branch

GitHub Actions is configured as follows:

- CI runs on pull requests and pushes for `develop`, `release/*`, and `hotfix/*`
- CD is triggered manually for a version tag on `main` and publishes to TestPyPI or PyPI

## Release Process

Release notes and publication follow these steps:

1. Prepare the release content on `release/*`.
2. Merge the release branch into `main`.
3. Tag the `main` commit with a version tag such as `v1.2.3`.
4. Write the release notes for that tag in GitHub Release or `CHANGELOG.md`.
5. Run the CD workflow manually with `publish_target=testpypi` and `release_ref=v1.2.3`.
6. Verify the package on TestPyPI.
7. Run the CD workflow again with `publish_target=pypi` and the same tag when the verification is successful.

## Start Here

Detailed usage is delegated to each package README.

- For installation and basic usage of the library, see [dddlib](packages/dddlib/README.md)
- For CLI startup instructions and command lists, see [dddlib_cli](packages/dddlib_cli/README.md)

## License

See [LICENSE.md](LICENSE.md) for this project.
