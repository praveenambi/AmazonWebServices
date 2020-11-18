'''

1. Regions ------>  geo location
    1.USA
    2. India
    3. Jakarta
    4.UK
    5.Australia

2. AZs ---------> availablity zones
    availablity zones means the data centers/ Buildings  , where the complete infrastructure is developed
    There should be minimum of 2 availabiloity zones. This is requirfed for jigh availability

3. VPC  ---------> virtual private network
    set up a virtual netowork in private cloud

4. Subnets ------> different subnetworks
    subnets means , different sub networks  under an VPC for different webservers , like jenkins , microservies.


5. AMI ----------> Amazon machine image
     AMI means , just a name like docker images, for different OS+softwwares

6. security groups--->
in the data security point  of view, we have to define some firewall rules for AWS instances.

7. IAM ------->Identity access management'
    Ths is to control or give access to perticular user permissions/ roles

8. AWS command to remote connect to the AWS instance  through SSH
    ssh -i praveenambi.pem ece2-use@pblic_IP_instance


8. How to remove the  java from AWS instance
    command to remove the java from AWS instance
    sudo yum remove java-y


9. How to install the java JDK 1.8
    sudo yum install java-1.8.0-openjdk -y
























'''