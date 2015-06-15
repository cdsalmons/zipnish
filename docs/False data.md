
****DB Schema****

Spans

```
span_id
parent_id
trace_id
span_name
debug
duration
created_ts
```

Annotations

```
span_id
trace_id
span_name
service_name
value
ipv4
port
a_timestamp
duration
```
All timestamps are in micro-seconds. Durations (difference between timestamps) are also in micro-seconds.

Python function to generate timestamp / microsecond

```
import time
int ( time.time() * 1000000 )
```
