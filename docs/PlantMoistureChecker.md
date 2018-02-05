# plant moisture checker
The goal of the plant moisture checker is to report when a particular plant needs to be watered.
As the soil dries out, the resistance increases, and if above a certain value, a LED turns on.

# sensor
The actual moisture sensor is a 2 pin terminal block with 2 galvanized nails of about 5 cm pushed into the soil of the plant.
The resistance of the soil is measured by the voltage across it with an analog voltage input. The voltage across the wiring is
not active all the time, only when we want to measure.

Technically, one measurement is a look at the ADC value at one point in time. The measurements through earth can fluctuate a lot.
In the context of the *GpioPollAdc* interaction, one measurement is 10 individual measurements after each other, and averaged, to
deal with some of these fluctuations.

# circuit
The circuit is perhaps a bit Beaglebone specific because the switchable GPIO voltage sources are 3.3V but the ADC analog inputs
can handle a maximum of 1.8V. So, a voltage divider splits the 3.3V up.

![plant moisture sensor circuit][circuit]

The "base" earth resistance was about 220KΩ (which can probably differ depending on the type of soil and the amount of water in it).
So, to measure more normalized voltages, we add an extra resistor to the voltage measuring part.

To help test the circuit, and also easily change values, a [SPICE](http://bwrc.eecs.berkeley.edu/Classes/IcBook/SPICE/) file
has been [included](PlantMoistureCheckerCircuit.spice) in this repository. Execute like this to view the simulated voltages across
each part of the circuit.
```bash
spice < PlantMoistureCheckerCircuit.spice
```

# monitoring
Monitoring of the voltage level is provided by the *GpioOnAverageBelowThreshold* interactions, which checks if the rolling average
of the sensor has dropped below a specified value, and then turns on a GPIO. In the most simple use case, the GPIO is connected to
a LED, but it should be possible to connect this to a water dispenser as well.

What the threshold value is will depend on the type of soil, and type of plant as well. Basically, the interaction for each plant
should be calibrated to suit your needs.

[circuit]: https://github.com/wimmuskee/argoid/raw/master/docs/PlantMoistureCheckerCircuit.png "plant moisture sensor circuit"
