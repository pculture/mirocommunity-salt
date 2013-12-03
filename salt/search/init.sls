java-jre:
  pkg.installed:
    - name: openjdk-7-jre-headless

elasticsearch:
  pkg.installed:
    - sources:
      - elasticsearch: https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.20.6.deb
    - require:
      - pkg: java-jre
  service.running:
    - name: elasticsearch
    - running: True
    - enable: True
    - require:
      - pkg: elasticsearch
    - watch:
      - file: /etc/elasticsearch/elasticsearch.yml
      - file: /etc/default/elasticsearch

/etc/default/elasticsearch:
  file.managed:
    - source: salt://search/default
    - template: jinja
    - required:
      - pkg: elasticsearch

/etc/elasticsearch/elasticsearch.yml:
  file.managed:
    - source: salt://search/elasticsearch.yml
    - template: jinja
    - user: elasticsearch
    - group: elasticsearch
    - mode: 664
    - required:
      - pkg: elasticsearch

/etc/elasticsearch/logging.yml:
  file.managed:
    - source: salt://search/logging.yml
    - template: jinja
    - user: elasticsearch
    - group: elasticsearch
    - mode: 664
    - required:
      - pkg: elasticsearch

/usr/share/elasticsearch/data:
  file.directory:
    - user: elasticsearch
    - group: elasticsearch
    - mode: 755
    - makedirs: True
    - required:
      - pkg: elasticsearch
