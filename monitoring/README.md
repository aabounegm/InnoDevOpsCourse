# Monitoring

Monitoring consists of logging and reporting metrics.

## Logging

Please check [logging.md](./LOGGING.md) for more information.

## Metrics

For metrics, Prometheus is added to the Docker Compose file to collect metrics from the logs.
For some reason, adding log rotation on Windows causes an infinite loop where Docker does not even create the containers.
Additionally, Loki and Promtail sometimes panic and go into an infinite loop on Windows, which prevented access to Grafana dashboards. This persisted even after purging everything in Docker and restarting the engine multiple times.
