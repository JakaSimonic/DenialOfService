from django.db import models
from datetime import timedelta
from django.utils import timezone

MAX_REQUESTS_PER_TIMEFRAME = 5
TIMEFRAME_LENGTH = timedelta(seconds=5)

class DosData(models.Model):
    client_id = models.IntegerField(primary_key=True)
    timeframe_start = models.DateTimeField(auto_now_add = True)
    request_counter = models.IntegerField(default=0)

    def is_request_allowed(self):
        current_datetime = timezone.now()
        valid_timeframe = self.timeframe_start > current_datetime - TIMEFRAME_LENGTH

        if valid_timeframe and self.request_counter <= MAX_REQUESTS_PER_TIMEFRAME:
            pass
        elif not valid_timeframe:
            self.timeframe_start = current_datetime
            self.request_counter = 1
        else:
            return False
        
        return True

