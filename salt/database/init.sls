mysql-pkgs:
  pkg.installed:
    - names:
      - mysql-client
      - python-mysqldb
      - libmysqlclient-dev
      - mysql-server

mysql-conf:
  file.managed:
    - name: /etc/my.cnf
    - source: salt://database/my.cnf

mysql:
  service:
    - running
    - require:
      - pkg: mysql-pkgs
    - watch:
      - file: mysql-conf

clear_defaults:
  mysql_database.absent:
    - name: test
    - require:
      - service: mysql

webproject_db:
  mysql_grants.present:
    - grant: all privileges
    - database: webproject.*
    - user: webproject
    - host: localhost
    - require:
      - mysql_database: webproject
      - mysql_user: webproject
  # Can't specify database collation. Should be UTF8.
  mysql_database.present:
    - name: webproject
    - require:
      - service: mysql
  mysql_user.present:
    - name: webproject
    - hostname: localhost
    - password: {{ pillar['settings']['db']['password'] }}
    - require:
      - service: mysql
