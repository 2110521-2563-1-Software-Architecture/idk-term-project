from django.db import models
from linkurl.models import Link


class AccessLog(models.Model):
    access_log_id = models.AutoField(primary_key=True)
    access_log_acess_datetime = models.DateTimeField(auto_now_add=True)
    access_log_shorten_url = models.ForeignKey(
        Link, related_name="access", on_delete=models.CASCADE, null=True
    )
