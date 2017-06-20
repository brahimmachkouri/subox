Vagrant.configure("2") do |config|

    config.vm.box = "thesubmarine/subox"
    config.vm.network "private_network", ip: "192.168.33.11"
    config.vm.hostname = "subox"
    config.vm.synced_folder ".", "/var/www", :mount_options => ["dmode=777", "fmode=666"]
    
    # Optional NFS. Make sure to remove other synced_folder line too
    #config.vm.synced_folder ".", "/var/www", :nfs => { :mount_options => ["dmode=777","fmode=666"] }

end
