# COMP90024 – Cluster and Cloud Computing - Team 4
# Assignment 2 – Australia Social Media Analytics on the Cloud
# Melbourne, Australia
#
# 1405461 - Andres Gutierrez
# 1110071 - Haining Xie
# 1025543 - Hernán Romano
# 1132915 - Zixuan Xiao
# 1298396 – Claudia Caro

import requests

from query.query2CouchDB import getServerAddr

couch_address = getServerAddr()


class NotificationController:
    def __init__(self) -> None:
        self.last_toot_id_reviewed = self.get_last_toot_from_db()

    def queryCoudchDB(self, last_toot_id_reviewed):
        url_get_latest_toots = f"{couch_address}mastodon_world_social_raw/_design/TootDoc/_view/RetrieveLatestToots?startkey={last_toot_id_reviewed}&descending=false&limit=3"
        r = requests.get(
            f"{url_get_latest_toots}", headers={"Accept": "application/json"}
        )
        return r.json()

    def get_latest_toots_from_CouchDB_Cluster(self, last_toot_id_reviewed):
        latest_toot = self.queryCoudchDB(last_toot_id_reviewed)
        return latest_toot

    def get_last_toot_from_db(self):
        url_get_latest_toots = f"{couch_address}mastodon_world_social_raw/_design/TootDoc/_view/RetrieveLatestToots?descending=true&limit=1"
        r = requests.get(
            f"{url_get_latest_toots}", headers={"Accept": "application/json"}
        )
        last_toot = r.json()
        if last_toot["rows"]:
            last_toot_id = last_toot["rows"][0]["key"]
            return last_toot_id
        return 0
