#!/usr/bin/env python3      
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# This is the Zip file you downloaded
SECURE_CONNECT_BUNDLE = '/workspace/cassandra-workshop-series/week3-AppDev-crud/crud-python/creds.zip'
# This is the username, recommended value was KVUser
USERNAME = "KVUser";
# This is the password, recommended value was KVPassword
PASSWORD = "KVPassword1";
# This is the keyspace name, recommended value was killrvideo
KEYSPACE = "killrvideo"; 

class Connection:
    def __init__(self):
        self.secure_connect_bundle=SECURE_CONNECT_BUNDLE
        self.path_to_creds=''
        self.cluster = Cluster(
            cloud={
                'secure_connect_bundle': self.secure_connect_bundle
            },
            auth_provider=PlainTextAuthProvider(USERNAME, PASSWORD)
        )
        self.session = self.cluster.connect(KEYSPACE)
    def close(self):
        self.cluster.shutdown()
        self.session.shutdown()