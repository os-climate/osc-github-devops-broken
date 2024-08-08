# OS-Climate GitHub Actions and Reusable Workflows

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD013 -->
[![OS-Climate](https://img.shields.io/badge/OS-Climate-blue)](https://os-climate.org/) [![Source Code](https://img.shields.io/badge/GitHub-100000?logo=github&logoColor=white)](https://github.com/os-climate/osc-github-devops) [![Slack](https://img.shields.io/badge/slack-osclimate-brightgreen.svg?logo=slack)](https://os-climate.slack.com) [![PyPI](https://img.shields.io/pypi/v/pdm?logo=python&logoColor=%23cccccc)](https://pypi.org/project/osc-github-devops) [![pdm-managed](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json)](https://pdm-project.org) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) [![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

<!-- markdownlint-disable-next-line MD013 -->
[![🧪 GitHub Actions CI/CD workflow tests badge]][GHA workflow runs list] [![pre-commit.ci status badge]][pre-commit.ci results page] [![Dependabot Updates](https://github.com/os-climate/osc-github-devops/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/os-climate/osc-github-devops/actions/workflows/dependabot/dependabot-updates) [![🔐 CodeQL](https://github.com/os-climate/osc-github-devops/actions/workflows/codeql.yaml/badge.svg)](https://github.com/os-climate/osc-github-devops/actions/workflows/codeql.yaml)
<!-- prettier-ignore-end -->

## Composite actions and reusable workflows for Python projects

### OS-Climate and FINOS are both Linux Foundation projects

- [https://os-climate.org/](https://os-climate.org/)
- [https://www.finos.org/](https://www.finos.org/)
- [https://www.linuxfoundation.org/](https://www.linuxfoundation.org/)

### Description

This repository contains a number of GitHub composite actions, reusable workflows,
and workflows. The purpose of these is to provide small modular components and
larger pieces of shared DevOps functionality which may be helpful to the OS-Climate
community, and indeed other open-source projects. Right now, the current focus is\
on Python and the tooling around Python projects, since that is the language
currently used for the vast majority of OS-Climate projects and repositories.

### Python Template Code

The repository also contains some sample Python code which is published to the Python
package index repository and is installable with the Python "pip" command. The
dummy sample project ensures Python packages can be built, tested and published
using the supplied GitHub composite actions, reusable workflows, and workflows.

Relevant link to the Python package index project page:

- [osc-github-devopss](https://pypi.org/project/osc-github-devops)

Detailed documentation will be supplied here, once further development is done.

In the meantime, here is some general documentation covering the relevant topics:

- [Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [How to start using reusable workflows with GitHub Actions](https://github.blog/2022-02-10-using-reusable-workflows-github-actions/)
- [Create reusable workflows in GitHub Actions](https://resources.github.com/learn/pathways/automation/intermediate/create-reusable-workflows-in-github-actions/)
- [The Ultimate Guide to GitHub Reusable Workflows](https://www.dhiwise.com/post/the-ultimate-guide-to-github-reusable-workflows-maximize-efficiency-and-collaboration)

<!--
[comment]: # SPDX-License-Identifier: Apache-2.0
[comment]: # SPDX-FileCopyrightText: 2024 The Linux Foundation <https://linuxfoundation.org>
-->

<!--
[comment]: # Section below is sourced by the badges displayed under the project heading
-->

[🧪 GitHub Actions CI/CD workflow tests badge]: https://github.com/os-climate/osc-github-devops/actions/workflows/repository.yaml/badge.svg?branch=main&event=push
[GHA workflow runs list]: https://github.com/os-climate/osc-github-devops/actions/workflows/repository.yaml?query=branch%3Amain
[pre-commit.ci results page]: https://results.pre-commit.ci/latest/github/os-climate/osc-github-devops/main
[pre-commit.ci status badge]: https://results.pre-commit.ci/badge/github/os-climate/osc-github-devops/main.svg
