# DevOps Info Service

## Overview

The DevOps Info Service is a Python web application that provides runtime, system, and request information via a REST API.

## Features

* Exposes system and runtime information
* Health check endpoint for monitoring
* Configurable via environment variables
* Clean, production-ready Flask application

## Tech Stack

* Python 3.11+
* Flask 3.1.0

## Prerequisites

Ensure the following are installed:

* Python 3.11 or newer
* pip package manager
* Optional: jq for formatted JSON output

Check Python version:

```bash
python --version
```

## Installation

Clone the repository and set up a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Application

Start the application with default settings:

```bash
python app.py
```

Access the service at:

```
http://localhost:5000
```

### Custom Configuration

Set environment variables to customize host, port, and debug mode:

```bash
HOST=127.0.0.1 PORT=8080 DEBUG=true python app.py
```

## API Endpoints

### GET /

Returns service metadata, system info, runtime details, request metadata, and available endpoints.

Example:

```bash
curl http://localhost:5000/
```

Pretty-printed output:

```bash
curl http://localhost:5000/ | jq
```

### GET /health

Health check endpoint for monitoring and readiness probes.

Example:

```bash
curl http://localhost:5000/health
```

Response:

```json
{
  "status": "healthy",
  "timestamp": "2026-01-07T14:30:00Z",
  "uptime_seconds": 3600
}
```

## Configuration

| Environment Variable | Default | Description               |
| -------------------- | ------- | ------------------------- |
| HOST                 | 0.0.0.0 | Network interface to bind |
| PORT                 | 5000    | Application port          |
| DEBUG                | False   | Enable Flask debug mode   |

