def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S.%f %Z%z')

#print(aslocaltimestr(datetime(2010,  6, 6, 17, 29, 7, 730000)))
#print(aslocaltimestr(datetime(2010, 12, 6, 17, 29, 7, 730000)))
#print(aslocaltimestr(datetime.utcnow()))


from datetime import datetime, timezone

def utc_to_local():
    return datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(tz=None)

print(utc_to_local())
