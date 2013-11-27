settings:
  secret_key: "SECRET_KEY"
  server_name: "MYSITE.COM"
  # Email the server sends "from".
  server_email: "SERVER_EMAIL@MYSITE.COM"
  # Email that error messages will be sent to.
  error_email: ""
  db:
    engine: django.db.backends.mysql
    name: webproject
    user: webproject
    password: "PASSWORD"
    host: ""
    port: ""
  apis:
    facebook:
      app_id: ""
      api_secret: ""
    twitter:
      consumer_key: ""
      consumer_secret: ""
    vimeo:
      api_key: ""
      api_secret: ""
    ustream:
      api_key: ""
    youtube:
      api_key: ""
    google_analytics:
      ua: ""
      domain: ""
    # You probably don't need this.
    recaptcha:
      public_key: ""
      private_key: ""
  haystack:
    engine: haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine
    url: http://127.0.0.1:9200/
    index_name: haystack
  cache:
    backend: django.core.cache.backends.memcached.MemcachedCache
    location: 127.0.0.1:11211
  debug: false
  time_zone: UTC
