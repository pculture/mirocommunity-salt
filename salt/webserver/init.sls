include:
  - circus
  - database

app-pkgs:
  pkg.installed:
    - names:
      - git-core
      - python-dev
      - libjpeg62

virtualenv:
  pkg.purged:
    - name: python-virtualenv
  pip.installed:
    - upgrade: true
    - require:
      - cmd: python-pip

webproject_user:
  user.present:
    - name: webproject
    - gid_from_name: True

webproject_dirs:
  file.directory:
    - user: webproject
    - group: webproject
    - makedirs: true
    - names:
      - {{ pillar['files']['media_dir'] }}
      - {{ pillar['files']['static_dir'] }}
    - require:
      - user: webproject

webproject_env:
  virtualenv.manage:
    - name: {{ pillar['files']['env_dir'] }}
    - requirements: salt://webserver/requirements.txt
    - no_site_packages: true
    - clear: false
    - require:
      - pkg: app-pkgs
      - pip: virtualenv
      - file: webproject_dirs

nginx:
  pkg:
    - latest
  service:
    - running

gunicorn_log:
  file.managed:
    - name: {{ pillar['files']['gunicorn_log'] }}
    - user: webproject
    - group: webproject
    - mode: 644

webproject_nginxconf:
  file.managed:
    - name: /etc/nginx/sites-enabled/webproject
    - source: salt://webserver/nginx.conf
    - template: jinja
    - makedirs: True
    - mode: 755
    - watch_in:
      - service: nginx

webproject_project:
  file.recurse:
    - user: webproject
    - group: webproject
    - name: {{ pillar['files']['webproject_dir'] }}
    - source: salt://webserver/webproject
    - template: jinja
    - require:
      - virtualenv: {{ pillar['files']['env_dir'] }}

webproject_gunicorn_circus:
  file.managed:
    - name: /etc/circus.d/webproject_gunicorn.ini
    - source: salt://webserver/gunicorn.ini
    - makedirs: True
    - template: jinja
    - require:
      - file: webproject_dirs
      - file: gunicorn_log
      - user: webproject_user
    - watch_in:
      - service: circusd
  cmd.wait:
    - name: circusctl restart gunicorn_webproject
    - watch:
      - file: webproject_project
      - virtualenv: webproject_env
