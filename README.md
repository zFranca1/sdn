## some commands

### send packages
echo "" > /dev/udp/10.0.0.2/80

echo "" > /dev/tcp/10.0.0.2/80

### switch flow stats
sudo ovs-ofctl dump-flows s1 | grep "tcp"

### run mininet topology
sudo -E mn --topo single,2 --mac --switch ovsk --controller remote

### run pox controller
sudo ./pox.py forwarding.l3_learning cap-packages

### pox with database
./pox.py forwarding.l3_learning vlan_controller_db --host=192.168.0.124 --dbname=sdn --user=docker --password=docker





