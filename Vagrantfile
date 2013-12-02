# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.network :forwarded_port, guest: 80, host: 8080

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network :private_network, ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network :public_network

  config.vm.synced_folder "pillar", "/srv/pillar"
  config.vm.synced_folder "salt", "/srv/salt"

  config.vm.provision :salt do |salt|

    salt.install_type = "git"
    salt.install_args = "2fecfab8786ac34e3932152d38fb0f729047d0e6"
    salt.minion_config = "salt.conf"
    salt.run_highstate = true

  end
end
