#!/bin/bash
user=$1
pass=$2
inst=$3
uuid=$4
scrt=$5
main=$6

couch="-H Content-Type:application/json -X PUT http://${user}:${pass}@${main}:5984"; \


curl -XPOST "http://${user}:${pass}@${main}:5984/_cluster_setup"\
    --header "Content-Type: application/json" --data "{\"action\": \"finish_cluster\"}"

curl $couch/photon; curl https://raw.githubusercontent.com/ermouth/couch-photon/master/photon.json | \
curl $couch/photon/_design/photon -d @- ; curl $couch/photon/_security -d '{}' ; \
curl $couch/_node/_local/_config/csp/attachments_enable -d '"false"' ; \
curl $couch/_node/_local/_config/chttpd_auth/same_site -d '"lax"' ;
