import fitbit
import json
from datetime import datetime, timedelta

class Fitbit:

    CLIENT_ID     = ""
    CLIENT_SECRET = ""
    ACCESS_TOKEN  = ""
    REFRESH_TOKEN = ""

    def __init__(self):
        self.client = fitbit.Fitbit(
                        self.CLIENT_ID,
                        self.CLIENT_SECRET,
                        access_token=self.ACCESS_TOKEN,
                        refresh_token=self.REFRESH_TOKEN)


if __name__ == "__main__":
    f = Fitbit()

    for d in range(0, 120):
        #out = f.client.sleep(date=datetime.today() - timedelta(days=d))

        # "activities/heart"
        # "activities/steps"
        # "activities/distance"
        # "activities/minutesSedentary"
        # "activities/minutesLightlyActive"
        # "activities/minutesFairlyActive"
        # "activities/minutesVeryActive"

        out = f.client.intraday_time_series(
                "activities/distance",
                base_date=datetime.today() - timedelta(days=d))

        print json.dumps(out)
