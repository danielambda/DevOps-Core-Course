# LAB02 — Docker Implementation Documentation

## Overview

This document describes the Docker implementation for the DevOps Info Service.
The focus is on applying Docker best practices, understanding design decisions, and validating container behavior.

---

## Docker Best Practices Applied

### Non-root User

**What was done:**
A dedicated non-root user was created and used to run the application.

```dockerfile
RUN groupadd --system appuser \
 && useradd --system --gid appuser --create-home appuser

USER appuser
```

**Why it matters:**
Running containers as root increases the impact of potential security vulnerabilities.
Using a non-root user follows the principle of least privilege and aligns with container security best practices.

---

### Layer Caching Optimization

**What was done:**
Dependencies were installed before copying application code.

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
```

**Why it matters:**
Docker caches layers. Dependency layers change less frequently than application code, so this ordering significantly speeds up rebuilds during development.

---

### Minimal Base Image

**What was done:**
The `python:3.13-slim` base image was selected.

```dockerfile
FROM python:3.13-slim
```

**Why it matters:**
Slim images reduce image size while maintaining compatibility with most Python packages.
This improves build speed, reduces attack surface, and lowers storage usage.

---

### .dockerignore Usage

**What was done:**
A `.dockerignore` file was added to exclude unnecessary files such as virtual environments, Git metadata, and cache files.

**Why it matters:**
Excluding files reduces build context size, speeds up builds, and prevents accidental inclusion of sensitive or irrelevant files.

---

## Image Information & Decisions

### Base Image Selection

* **Image:** `python:3.13-slim`
* **Justification:** Specific Python version ensures reproducibility, slim variant reduces size, and avoids Alpine compatibility issues.

### Final Image Size

* Relatively small compared to full Python images.
* Appropriate for production-ready service with minimal runtime dependencies.

### Layer Structure Explanation

1. Base Python image
2. Environment configuration
3. Non-root user creation
4. Dependency installation
5. Application code copy
6. Runtime execution command

This structure maximizes cache reuse and keeps runtime layers minimal.

### Optimization Choices

* Installed dependencies before application code to leverage layer caching
* Disabled pip cache during install
* Excluded unnecessary files via `.dockerignore`
* Avoided installing development tools in the image

---

## Build & Run Process

### Build Output

```text
[+] Building X.Xs (X/X) FINISHED
 => [internal] load build definition from Dockerfile
 => [internal] load .dockerignore
 => [1/6] FROM python:3.13-slim
 => [2/6] RUN groupadd --system appuser ...
 => [3/6] WORKDIR /app
 => [4/6] COPY requirements.txt .
 => [5/6] RUN pip install -r requirements.txt
 => [6/6] COPY app.py .
```

### Running Container

```text
$ docker run -p 5000:5000 app_python
 * Serving Flask app
 * Running on http://0.0.0.0:5000
```

### Endpoint Testing

```text
$ curl http://localhost:5000/health
{"status":"healthy","uptime_seconds":123}
```

### Docker Hub Repository

```
https://hub.docker.com/r/danielambda/app_python
```

---

## Technical Analysis

### Why the Dockerfile Works

The Dockerfile defines a complete, isolated runtime environment.
All dependencies are installed at build time, and the container starts the application consistently regardless of host system configuration.

### Impact of Changing Layer Order

If application files were copied before installing dependencies:

* Dependency layers would be invalidated on every code change
* Build times would increase significantly
* Cache efficiency would be lost

### Security Considerations

* Application runs as a non-root user
* Minimal base image reduces attack surface
* No secrets are embedded in the image
* Only required ports are exposed

### Role of .dockerignore

The `.dockerignore` file:

* Reduces build context size
* Speeds up builds
* Prevents accidental inclusion of local artifacts
* Improves overall image cleanliness

---

## Challenges & Solutions

### Issue: Large Build Context

**Problem:** Initial builds were slower due to unnecessary files being sent to the Docker daemon.

**Solution:** Added a `.dockerignore` file to exclude development artifacts and version control data.

### Issue: Understanding Layer Caching

**Problem:** Early Dockerfile versions rebuilt dependencies unnecessarily.

**Solution:** Reordered `COPY` instructions to leverage Docker’s layer caching mechanism.

### Key Learnings

* Dockerfile structure directly impacts performance
* Small design decisions have large effects on build speed
* Security best practices are easy to apply early
* Containerization improves consistency and reproducibility
