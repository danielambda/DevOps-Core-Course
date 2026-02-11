# LAB 03 — Continuous Integration (CI/CD)

## 1. Overview

- Testing framework: pytest — chosen for its simple syntax, fixtures support, and strong community/plugins.

- Test coverage: All Python endpoints (GET /, GET /health) are tested for success, error cases, and JSON structure.

- CI workflow triggers: Runs on push and pull_request events for app_python/** files and .github/workflows/python-ci.yml.

- Versioning strategy: Calendar Versioning (CalVer) — YYYY.MM format, automatically applied for Docker image tags. Chosen for simple monthly releases and continuous deployment.

## 2. Workflow Evidence

- ✅ Successful workflow run: https://github.com/danielambda/DevOps-Core-Course/actions

- ✅ Tests passing locally:
```bash
 󰘧 pytest -v
===================== test session starts =====================
platform linux -- Python 3.13.11, pytest-9.0.2, pluggy-1.6.0 ...
cachedir: .pytest_cache
rootdir: /home/daniel/projects/python/DevOps-Core-Course/app_python
collected 7 items

tests/test_health.py::test_health_status_code PASSED                                                                                                                                  [ 14%]
tests/test_health.py::test_health_returns_json PASSED                                                                                                                                 [ 28%]
tests/test_health.py::test_health_response_content PASSED                                                                                                                             [ 42%]
tests/test_root.py::test_root_status_code PASSED                                                                                                                                      [ 57%]
tests/test_root.py::test_root_returns_json PASSED                                                                                                                                     [ 71%]
tests/test_root.py::test_root_json_structure PASSED                                                                                                                                   [ 85%]
tests/test_unknown_route.py::test_unknown_route_returns_404 PASSED                                                                                                                    [100%]
====================== 7 passed in 0.02s ======================
```

- ✅ Docker images on Docker Hub:
  - danielambda/app_python:2026.02
  - danielambda/app_python:latest
    https://hub.docker.com/r/danielambda/app_python/tags

- ✅ Status badge in README: ![Python CI Pipeline](https://github.com/danielambda/DevOps-Core-Course/actions/workflows/python-ci.yml/badge.svg)


## 3. Best Practices Implemented

- Dependency caching: Cached pip packages and Docker layers

- Fail fast: Tests run before Docker build; Docker only runs if tests and security pass.

- Concurrency: Cancels previous workflow runs for the same branch to avoid redundant builds.

- Snyk Security Scan: Scans Python dependencies for vulnerabilities; any issues are reported in GitHub Code Scanning (SARIF).


## 4. Key Decisions

- Versioning Strategy: CalVer chosen for simple, time-based releases. Docker tags: YYYY.MM and latest.

- Docker Tags: The CI creates version-specific (2026.02) and rolling latest tags.

- Workflow Triggers: Push and pull_request on app_python/** ensures CI only runs when Python app changes.

- Test Coverage: All endpoints covered; error handling tested; JSON field presence validated. Not covered: trivial getters, Flask config boilerplate.
