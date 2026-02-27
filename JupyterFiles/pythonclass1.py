import boto3
import pprint
sess=boto3.session.Session()


res=sess.resource('ec2')
clnt=sess.client('ec2')


#vpc :


vpc=res.create_vpc(CidrBlock='192.168.0.1/24')
vpc.create_tags(Tags=[
        {
            'Key': 'Name',
            'Value': 'testVPC'
        },
    ]
)
print(vpc.id)

# gateway

ig=res.create_internet_gateway()
vpc.attach_internet_gateway(InternetGatewayId=ig.id)
print(ig.id)


#rote table

route_table = vpc.create_route_table()
route = route_table.create_route(DestinationCidrBlock='0.0.0.0/0',GatewayId=ig.id)
print(route_table.id)


#subnet

subnet=res.create_subnet(CidrBlock='192.168.0.1/24',VpcId=vpc.id)
route_table.associate_with_subnet(SubnetId=subnet.id)

print(subnet.id)

#sec group :

sc_group=res.create_security_group(Description="for class demo",
                                   GroupName="demogroup",VpcId=vpc.id)

sc_group.authorize_ingress(FromPort=-1,ToPort=-1,CidrIp='0.0.0.0/0',IpProtocol='-1')

print(sc_group.group_id)

#instance:

insts=res.create_instances(ImageId='ami-007020fd9c84e18c7',InstanceType='t2.micro',
                           MaxCount=1,MinCount=1,KeyName='krawskey2',
                           NetworkInterfaces=[{'AssociatePublicIpAddress':True,
                                               'DeviceIndex':0,
                                               'SubnetId':subnet.id,
                                               'Groups': [sc_group.group_id]}])


list(insts)[0].wait_until_running()
print(list(insts)[0].id)









