python-pip:
  pkg.purged:
    - name: python-pip
  cmd:
    - run
    - cwd: /
    - name: easy_install --script-dir=/usr/bin -U pip
    - reload_modules: true
    - unless: hash pip 2>/dev/null
    - require:
      - pkg: python-pip

circus:
  pip.installed:
    - require:
      - cmd: python-pip

circus_upstart:
  file.managed:
    - name: /etc/init/circusd.conf
    - source: salt://circus/circusd.conf

circus_conf:
  file.managed:
    - name: /etc/circus.ini
    - source: salt://circus/circus.ini
    - require:
      - pip: circus

circus_dir:
  file.directory:
    - name: /etc/circus.d

circusd:
  service:
    - running
    - require:
      - file: circus_upstart
      - file: circus_dir
      - file: circus_conf
