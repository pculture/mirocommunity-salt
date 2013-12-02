This salt repository will set up a basic Miro Community instance on a single server. It is known to work on AWS Ubuntu Precise (12.04) servers.

This quick setup does not include:

- how to get an AWS Ubuntu Precise server set up.
- how to acquire a domain name.
- how to point that domain name at your server.

How to use
==========

1. Install salt.

.. code:: console

	curl -L http://bootstrap.saltstack.org | sudo sh -s -- git develop

2. Install this repository to ``/srv/``

.. code:: console

	cd /
	sudo git clone https://github.com/pculture/mirocommunity-salt.git srv/

3. Customize the salt setup. You'll need to set the following values in ``/srv/pillar/settings.sls``:

  * ``settings: db: password:`` - currently set to PASSWORD. Should be a unique password.
  * ``settings: secret_key:`` - currently set to SECRET_KEY. Should be a unique secret key.
  * ``settings: server_name:`` - currently set to MYSITE.COM. Should be a space-separated list of domain names that may point at your server. See also: `Nginx server_name documentation <http://nginx.org/en/docs/http/server_names.html>`_.
  * Any API keys you want to use - for example, for social media authentication.

The easiest way to do this will probably be:

.. code:: console

	sudo nano /srv/pillar/settings.sls

4. Run salt.

.. code:: console

	sudo salt-call --local state.highstate

5. Go to your site!
