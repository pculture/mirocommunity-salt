mysql-pkgs:
  pkg.installed:
    - names:
      - mysql
      - MySQL-python
      - mysql-devel
      - mysql-server

mysql-conf:
  file.managed:
    - name: /etc/my.cnf
    - source: salt://database/my.cnf

mysqld:
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
      - service: mysqld

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
      - service: mysqld
  mysql_user.present:
    - name: webproject
    - hostname: localhost
    - password: {{ pillar['settings']['db']['password'] }}
    - require:
      - service: mysqld
