This salt file will set up a basic Miro Community instance on a single server.

How to use
==========

1. Install salt.

.. code:: console

	curl -L http://bootstrap.saltstack.org | sudo sh -s -- git develop

2. Install this repository to ``/srv/``

.. code:: console

	cd /
	sudo git clone git://path_to_repo.git srv/

3. Customize the salt setup. You'll need to set the following values in ``/srv/pillar/settings.sls``:

	* ``settings: db: password:`` - currently set to PASSWORD. Should be a unique password.
	* ``settings: secret_key:`` - currently set to SECRET_KEY. Should be a unique secret key.
	* ``settings: server_name:`` - currently set to MYSITE.COM. Should be a space-separated list of domain names that may point at your server.
		.. seealso:: http://nginx.org/en/docs/http/server_names.html
	* Any API keys you want to use - for example, for social media authentication.

4. Run salt.

.. code:: console

	sudo salt-call --local state.highstate

5. Go to your site!
