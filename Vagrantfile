# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "generic/ubuntu2204"

  config.vm.define "web-server" do |web|
    web.vm.hostname = "web-server"
    web.vm.network "private_network", ip: "192.168.56.xx"

  end

  config.vm.define "data-base" do |db|
    db.vm.hostname = "data-base"
    db.vm.network  "private_network", ip: "192.168.56.xx"
  end

  config.vm.define "file-server" do |fs|
    fs.vm.hostname = "file-server"
    fs.vm.network "private_network", ip: "192.168.56.xx"
  end

  config.vm.define"application-server" do |as|
    as.vm.hostname = "application-server"
    as.vm.network "private_network", ip: "192.168.56.xx"
  end

  config.vm.define "proxy-server" do |ps|
    ps.vm.hostname = "proxy-server"
    ps.vm.network "private_network", ip: "192.168.56.xx"
  end

  config.vm.define "mail-server" do |ms|
    ms.vm.hostname = "mail-server"
    ms.vm.network "private_network", ip: "192.168.56.xx"
  end
end
 