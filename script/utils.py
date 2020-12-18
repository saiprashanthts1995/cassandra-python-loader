from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

cloud_config= {
        'secure_connect_bundle': 'C:/Users/Sai Prashanth T S/Downloads/secure-connect-killrvideocluster.zip'
}
auth_provider = PlainTextAuthProvider('', '')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select * from killrvideo.a").one()
if row:
    print(row)
else:
    print("An error occurred.")