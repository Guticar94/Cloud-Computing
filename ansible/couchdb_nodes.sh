#!/bin/bash
#/tmp/couchdb_node.sh
user=$1
pass=$2
inst=$3
uuid=$4
scrt=$5
main=$6

# Now, bind the clustered interface to all IP addresses available on this machine
curl -X PUT http://${user}:${pass}@${inst}:5984/_node/_local/_config/chttpd/bind_address -d '"0.0.0.0"'

# Set the UUID of the node to the first UUID you previously obtained:
curl -X PUT http://${user}:${pass}@${inst}:5984/_node/_local/_config/couchdb/uuid -d '"'"${uuid}"'"'

# Finally, set the shared http secret for cookie creation to the second UUID:
curl -X PUT http://${user}:${pass}@${inst}:5984/_node/_local/_config/chttpd_auth/secret -d '"'"${scrt}"'"'

curl -XPOST "http://${user}:${pass}@${main}:5984/_cluster_setup" \
  --header "Content-Type: application/json"\
  --data "{\"action\": \"enable_cluster\", \"bind_address\":\"0.0.0.0\",\
		 \"username\": \"${user}\", \"password\":\"${pass}\", \"port\": \"5984\",\
		 \"remote_node\": \"${inst}\", \"node_count\": \"3\",\
		 \"remote_current_user\":\"${user}\", \"remote_current_password\":\"${pass}\"}"

curl -XPOST "http://${user}:${pass}@${main}:5984/_cluster_setup"\
  --header "Content-Type: application/json"\
  --data "{\"action\": \"add_node\", \"host\":\"${inst}\",\
		 \"port\": \"5984\", \"username\": \"${user}\", \"password\":\"${pass}\"}"
