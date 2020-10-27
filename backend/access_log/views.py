from .serializers import AccessLogSerializer

def log_access(shorten_url):
    serializer = AccessLogSerializer(data={"access_log_shorten_url":shorten_url})
    if serializer.is_valid():
        serializer.save()
    else:
        raise Exception("log_access error")