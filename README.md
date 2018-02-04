# argoid
Scheduler for sensor driven interactions on single board computers like the Beaglebone.

# usage
After starting, the client continues executing each provided interaction in the client config file.
A typical interaction looks like the following (from the Beaglebone [interaction config example](client/argoid-client.conf.example)).
```json
"interaction_name": {
    "attributes": [
        "P9_12",
        "/sys/devices/ocp.3/helper.10/AIN4"
    ],
    "recurring": 600,
    "offset": 10,
    "method": "GpioPollAdc"
}
```
An interaction name should be unique within the config, furthermore
 - *recurring*: specifies the nr of seconds between the execution of that interaction
 - *offset*: specifies nr of seconds to wait before execution, and provide a way to stack interactions
 - *method*: the interaction method to execute
 - *attributes*: a list of attributes to provide to the method
After starting the client, 610 seconds later, the *GpioPollAdc* is called on the *P9_12* GPIO identifier,
and reading input from */sys/devices/ocp.3/helper.10/AIN4*. Following the next call after 600 seconds, and so on.

Each interaction is logged to the syslog for statistics gathering. The log contains the "argoid" programname, as
well as the sensorname and a value (comma separated).

# requirements
- Python2/3 with threading support
- [jsonschema](https://github.com/Julian/jsonschema)
- [adafruit-beaglebone-io-python](https://github.com/adafruit/adafruit-beaglebone-io-python) for Beaglebone boards
