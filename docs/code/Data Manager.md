Data manager comes into play after data has been Read from the shared memory log by [Reader](Reader.md)

Data manager recieves the following set of fields as argument to it's addLogItem function.

*VxId, Request Type, Tag, Data*

Log data for client / backend request is read inside `addLogItem()` function.

`addLogItem()` is a dictionary (key: value structure).
