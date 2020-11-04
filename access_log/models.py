from django.db import models
from linkurl.models import Link


class AccessLog(models.Model):
    access_log_id = models.AutoField(primary_key=True)
    access_log_access_datetime = models.DateTimeField(auto_now_add=True)
    access_log_shorten_url = models.ForeignKey(
        Link, related_name="access", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        shorten_url = str(self.access_log_shorten_url).split("\n")[0]
        return f"[{str(self.access_log_access_datetime)}] {shorten_url}"
