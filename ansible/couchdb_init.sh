#!/bin/bash
#/tmp/couchdb_node.sh
user=$1
pass=$2
inst=$3
uuid=$4
scrt=$5

# Now, bind the clustered interface to all IP addresses available on this machine
curl -X PUT http://${user}:${pass}@${inst}:5984/_node/_local/_config/chttpd/bind_address -d '"0.0.0.0"'

# Set the UUID of the node to the first UUID you previously obtained:
curl -X PUT http://${user}:${pass}@${inst}:5984/_node/_local/_config/couchdb/uuid -d '"'"${uuid}"'"'

# Finally, set the shared http secret for cookie creation to the second UUID:
curl -X PUT http://${user}:${pass}@${inst}:5984/_node/_local/_config/chttpd_auth/secret -d '"'"${scrt}"'"'
