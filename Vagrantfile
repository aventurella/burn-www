# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    # All Vagrant configuration is done here. The most common configuration
    # options are documented and commented below. For a complete reference,
    # please see the online documentation at vagrantup.com.

    # Every Vagrant virtual environment requires a box to build off of.
    config.vm.box = "precise64"
    config.vm.box_url = "http://files.vagrantup.com/precise64.box"
    
    config.vm.network :forwarded_port, guest: 5672, host: 5672   # rabbitmq
    config.vm.network :forwarded_port, guest: 6379, host: 6379   # redis
    config.vm.network :forwarded_port, guest: 9160, host: 9160   # cassandra rpc_port (cqlsh)
    config.vm.network :forwarded_port, guest: 9042, host: 9042   # cassandra native_transport_port (datastax python lib)
    config.vm.network :forwarded_port, guest: 5432, host: 5432   # postgres
    config.vm.network :forwarded_port, guest: 9200, host: 9200   # elasticsearch
    config.vm.network :forwarded_port, guest: 27017, host: 27017 # mongodb

    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--memory", 768]
    end

    ## For masterless, mount your salt file root
    config.vm.synced_folder "cloudseed/current/srv/", "/srv/"

    ## Use all the defaults:
    config.vm.provision :salt do |salt|
        salt.run_highstate = true
        salt.install_master = true
        salt.master_config = "cloudseed/current/salt/master"
        salt.minion_config = "cloudseed/current/vagrant/minion"
        salt.minion_key = "cloudseed/current/vagrant/minion.pem"
        salt.minion_pub = "cloudseed/current/vagrant/minion.pub"
        salt.bootstrap_script = "cloudseed/current/vagrant/bootstrap-salt.sh"
        salt.seed_master = {minion: salt.minion_pub}
    end
end
