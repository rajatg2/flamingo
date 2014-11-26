print "Enter the type of deployement"
print "Press 1 for LAMP"
print "Press 2 for Only Web"
print "Press 3 for Only App"
print "Press 4 for Only DB"
print "Press 5 for Web outside and DB inside"


x = int(raw_input("Enter the option"))

if ( x==1 ):
    my_str = '''
heat_template_version: 2014-10-05

parameters:
  key_name:
    type: string
    description: Enter the key name
  image: 
    type: string
    description: enter image name
  flavor:
    type: string
    description: type the flavour
  public_net_id: 
    type: string
    description: type the public net id
  public_subnet_id: 
    type: string
    description: type the public subnet id
  private_net_id:
    type: string
    description: type the pvt net id
  private_subnet_id: 
    type: string
    description: type the pvt subnet id

  
resources:
  server1:
    type: OS::Nova::Server
    properties:
      name: Server1
      image: { get_param: image }
      flavor: { get_param: flavor }
      key_name: { get_param: key_name }
      networks: [{ "port": { get_resource: server1_port_pvt}}, {"port": { get_resource: server1_port_ext }}]
     # networks:
      #  - port: { get_resource: server1_port_ext } 

  server1_port_pvt:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: private_net_id }
      fixed_ips:
        - subnet_id: { get_param: private_subnet_id }
        
  server1_port_ext:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: public_net_id }
      fixed_ips:
        - subnet_id: { get_param: public_subnet_id }

  #server1_floating_ip:
   # type: OS::Neutron::FloatingIP
    #properties:
     # floating_network_id: { get_param: public_net_id }
      #port_id: { get_resource: server1_port }

  server2:
    type: OS::Nova::Server
    properties:
      name: Server2
      image: { get_param: image }
      flavor: { get_param: flavor }
      key_name: { get_param: key_name }
      networks:
        - port: { get_resource: server2_port }

  server2_port:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: private_net_id }
      fixed_ips:
        - subnet_id: { get_param: private_subnet_id }
        
  server3:
    type: OS::Nova::Server
    properties:
      name: Server3
      image: { get_param: image }
      flavor: { get_param: flavor }
      key_name: { get_param: key_name }
      networks:
        - port: { get_resource: server3_port }

  server3_port:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: private_net_id }
      fixed_ips:
        - subnet_id: { get_param: private_subnet_id }

 # server2_floating_ip:
  #  type: OS::Neutron::FloatingIP
  #  properties:
   #   floating_network_id: { get_param: public_net_id }
    #  port_id: { get_resource: server2_port }

outputs:
  server1_private_ip:
    description: IP address of server1 in private network
    value: { get_attr: [ server1, first_address ] }
  #server1_public_ip:
   # description: Floating IP address of server1 in public network
    #value: { get_attr: [ server1_floating_ip, floating_ip_address ] }
  server2_private_ip:
    description: IP address of server2 in private network
    value: { get_attr: [ server2, first_address ] }
  #server2_public_ip:
  #  description: Floating IP address of server2 in public network
   # value: { get_attr: [ server2_floating_ip, floating_ip_address ] }
  server3_private_ip:
    description: IP address of server3 in private network
    value: { get_attr: [ server3, first_address ] }'''

    print "hello"
    f = open('temp.yaml','w+')
    f.write(my_str)
    f.close()

elif (x==2 or x==3 or x==4):
    my_str = '''
heat_template_version: 2014-10-05

parameters:
  key_name:
    type: string
    description: Enter the key name
  image: 
    type: string
    description: enter image name
  flavor:
    type: string
    description: type the flavour
  public_net_id: 
    type: string
    description: type the public net id
  public_subnet_id: 
    type: string
    description: type the public subnet id

  
resources:
  server1:
    type: OS::Nova::Server
    properties:
      name: Server1
      image: { get_param: image }
      flavor: { get_param: flavor }
      key_name: { get_param: key_name }
      networks: [{"port": { get_resource: server1_port_ext }}]
       
  server1_port_ext:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: public_net_id }
      fixed_ips:
        - subnet_id: { get_param: public_subnet_id }


outputs:
  server1_public_ip:
    description: IP address in public network
    value: { get_attr: [ server1, first_address ] }'''

    f = open('temp.yaml', 'w+')
    f.write(my_str)
    f.close()

elif(x==5):
    my_str= '''
heat_template_version: 2014-10-05

parameters:
  key_name:
    type: string
    description: Enter the key name
  image: 
    type: string
    description: enter image name
  flavor:
    type: string
    description: type the flavour
  public_net_id: 
    type: string
    description: type the public net id
  public_subnet_id: 
    type: string
    description: type the public subnet id
  private_net_id:
    type: string
    description: type the pvt net id
  private_subnet_id: 
    type: string
    description: type the pvt subnet id

  
resources:
  server1:
    type: OS::Nova::Server
    properties:
      name: Server1
      image: { get_param: image }
      flavor: { get_param: flavor }
      key_name: { get_param: key_name }
      networks: [{ "port": { get_resource: server1_port_pvt}}, {"port": { get_resource: server1_port_ext }}]
     # networks:
      #  - port: { get_resource: server1_port_ext } 

  server1_port_pvt:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: private_net_id }
      fixed_ips:
        - subnet_id: { get_param: private_subnet_id }
        
  server1_port_ext:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: public_net_id }
      fixed_ips:
        - subnet_id: { get_param: public_subnet_id }

  #server1_floating_ip:
   # type: OS::Neutron::FloatingIP
    #properties:
     # floating_network_id: { get_param: public_net_id }
      #port_id: { get_resource: server1_port }

  server2:
    type: OS::Nova::Server
    properties:
      name: Server2
      image: { get_param: image }
      flavor: { get_param: flavor }
      key_name: { get_param: key_name }
      networks:
        - port: { get_resource: server2_port }

  server2_port:
    type: OS::Neutron::Port
    properties:
      network_id: { get_param: private_net_id }
      fixed_ips:
        - subnet_id: { get_param: private_subnet_id }
        

outputs:
  server1_private_ip:
    description: IP address of server1 in private network
    value: { get_attr: [ server1, first_address ] }
  #server1_public_ip:
   # description: Floating IP address of server1 in public network
    #value: { get_attr: [ server1_floating_ip, floating_ip_address ] }
  server2_private_ip:
    description: IP address of server2 in private network
    value: { get_attr: [ server2, first_address ] }
  #server2_public_ip:
  #  description: Floating IP address of server2 in public network
   # value: { get_attr: [ server2_floating_ip, floating_ip_address ] }'''

    f = open('temp.yaml', 'w+')
    f.write(my_str)
    f.close()















