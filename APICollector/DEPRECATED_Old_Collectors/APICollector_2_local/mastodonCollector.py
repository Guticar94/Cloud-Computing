from mastodon import (
    Mastodon,
    MastodonNotFoundError,
    MastodonRatelimitError,
    StreamListener,
)
import csv, os, time, json
import couchdb

m = Mastodon(
    api_base_url=f"{os.environ['MASTODON_SERVER']}",
    access_token=os.environ["MASTODON_ACCESS_TOKEN"],
)


class Listener(StreamListener):
    def __init__(self) -> None:
        super().__init__()
        self.couchdbsettings()

    def couchdbsettings(self):
        self.couch = couchdb.Server(f"http://admin:{os.environ['COUCHDB_PASSWORD']}@couchserver:5984/")
        self.db = self.couch[f"{os.environ['COUCHDB_DATABASE']}"]

    def gettootmessage(self, raw_toot):
        print("================================")
        print("Parsing json toot to Python Dictionary")

        # Comment to FILTER raw_toot
        # toot = {
        #     "toot_id": raw_toot["id"],
        #     "toot_date": raw_toot["created_at"].strftime("%Y-%m-%d %H:%M:%S"),
        #     "toot_content": raw_toot["content"],
        #     "toot_language": raw_toot["language"],
        #     "toot_account_id": raw_toot["account"]["id"],
        #     "toot_account_username": raw_toot["account"]["username"],
        #     "toot_account_note": raw_toot["account"]["note"],
        # }
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

if f"{os.environ['MASTODON_TIMELINE']}" == "public":
    m.stream_public(Listener())
else:
    m.stream_local(Listener())