config = {
    "openai": {
        "api_key": "OPENAI_KEY"
    },
    "kafka": {
        "sasl.username": "KAFKA_CLUSTER_API_KEY",
        "sasl.password": "KAFKA_CLUSTER_API_SECRET",
        "bootstrap.servers": "KAFKA_CLUSTER_BOOTSTRAP_SERVER_URL:PORT",
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'session.timeout.ms': 50000
    },
    "schema_registry": {
        "url": "SCHEMA_REGISTRY_URL",
        "basic.auth.user.info": "SR_API_KEY:SR_API_SECRET"

    }
}