# LAB01 — DevOps Info Service

## 1. Framework Selection

### Chosen Framework: **Flask**

Flask was selected as the web framework for this lab because it is lightweight, easy to understand, and provides explicit control over request handling. For a DevOps-focused service that performs system introspection and exposes operational endpoints, Flask offers the right balance between simplicity and flexibility.

### Comparison with Alternatives

| Framework | Pros                                                   | Cons                                     | Decision |
| --------- | ------------------------------------------------------ | ---------------------------------------- | -------- |
| **Flask** | Lightweight, minimal magic, easy to debug, widely used | No built-in async, fewer defaults        | ✅       |
| FastAPI   | Async support, auto OpenAPI docs, modern               | More abstraction, steeper learning curve | ❌       |
| Django    | Full-featured, ORM, admin panel                        | Overbloated                              | ❌       |

Flask allows full visibility into how requests are handled, which is ideal for learning DevOps concepts such as health checks, logging, and observability.

---

## 2. Best Practices Applied

### Clean Code Organization

* Logical grouping of imports (standard library, third-party, local)
* Helper functions for uptime and system information
* PEP 8–compliant formatting

### Error Handling

Custom handlers were added for common HTTP errors to ensure consistent JSON responses:

```python
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
        'message': 'Endpoint does not exist'
    }), 404
```

This improves client usability and prevents default HTML error pages.

### Logging

Structured logging is enabled at application startup:

```python
logging.basicConfig(level=logging.INFO)
logger.info("Application starting")
```

Logging is critical for debugging, monitoring, and later integration with centralized logging systems.

### Configuration via Environment Variables

The application supports runtime configuration using environment variables:

* `HOST`
* `PORT`
* `DEBUG`

---

## 3. API Documentation

### GET /

Returns service metadata, system information, runtime details, request metadata, and available endpoints.

Example request:

```bash
curl http://localhost:5000/
```

Example response (excerpt):

```json
{
  "service": {
    "name": "devops-info-service",
    "version": "1.0.0",
    "framework": "Flask"
  },
  "system": {
    "hostname": "my-host",
    "platform": "Linux"
  }
}
```

### GET /health

Used for monitoring and readiness probes.

```bash
curl http://localhost:5000/health
```

Response:

```json
{
  "status": "healthy",
  "uptime_seconds": 3600
}
```

---

## 4. Testing Evidence

The following evidence is provided in the `screenshots/` directory:

* **01-main-endpoint.png** — Full JSON output from `GET /`
* **02-health-check.png** — Health endpoint response
* **03-formatted-output.png** — Pretty-printed JSON using `jq`

Terminal commands used:

```bash
curl http://localhost:5000/ | jq
curl http://localhost:5000/health
```

---

## 5. Challenges & Solutions

### Challenge: Accurate Uptime Calculation

Initially, uptime was calculated using local time, which could lead to timezone inconsistencies.

**Solution:**
The application uses `datetime.now(timezone.utc)` consistently for all time-related values.


## 6. GitHub Community

Starring repositories is a way to bookmark useful projects and support open-source maintainers by increasing visibility and engagement.

Following developers and classmates helps build a professional network, makes collaboration easier, and allows learning from others' activity and code throughout the course and beyond.
