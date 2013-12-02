nginx:
  pkg:
    - latest
  service:
    - running
    - require:
      - pkg: nginx

nginx_default_site:
  file.absent:
    - names:
      - /etc/nginx/sites-enabled/default
      - /etc/nginx/sites-available/default
    - watch_in:
      - service: nginx

/etc/nginx/conf.d:
  file.directory:
    - clean: true
    - require:
      - pkg: nginx
    - require_in:
      - service: nginx
