from mastodon import (
    Mastodon,
    MastodonNotFoundError,
    MastodonRatelimitError,
    StreamListener,
)
import csv, os, time, json
import couchdb

COUCH = couchdb.Server(f"http://{os.environ['COUCHDB_USER']}:{os.environ['COUCHDB_PASSWORD']}@{os.environ['COUCHDB_SERVER']}:5984/")


class Listener(StreamListener):
    def __init__(self,mastodon_server_config) -> None:
        super().__init__()
        self.couchdb_database = mastodon_server_config["couch_db_database_name"]
        self.db = COUCH[f"{self.couchdb_database}"]        

    def gettootmessage(self, raw_toot):
        print("================================")
        print("Parsing json toot to Python Dictionary")
        converted_toot_to_dict = json.loads(raw_toot)
        print("================================")
        return converted_toot_to_dict
    
    def savetoot(self,toot):
        self.db.save(toot)

    # Inherited method
    def on_update(self, status):
        raw_toot = json.dumps(status, indent=2, sort_keys=True, default=str)
        print(raw_toot)
        toot = self.gettootmessage(raw_toot)
        self.savetoot(toot)

def getVariablesFromCouchdb(mastodon_server_list):
    
    for mastodon_server_id in mastodon_server_list:
        doc = mastodon_server_list[mastodon_server_id]
        if mastodon_server_list[mastodon_server_id]["available"] == False:
            doc = {}
            continue
        doc["available"] = False
        doc["collector_name"] = os.uname()[1]
        mastodon_server_list.save(doc)
        break
    
    return doc

def main():

    # Get environment variables from couchdb database
    mastodon_server_list = COUCH["mastodon_server_list"]
    mastodon_server_config = getVariablesFromCouchdb(mastodon_server_list)

    if mastodon_server_config:
    
        m = Mastodon(
            api_base_url=f"{mastodon_server_config['server_url']}",
            access_token=mastodon_server_config["server_access_token"],
        )

        
        if f"{mastodon_server_config['timeline_type']}" == "public":
            m.stream_public(Listener(mastodon_server_config))
        else:
            m.stream_local(Listener(mastodon_server_config))
    else:
        print("No server available")
        print("Exiting...")
        return 0

# Run app
if __name__=='__main__':
    main()

