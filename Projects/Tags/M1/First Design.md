## Blocks

### Sensor Array (I2C Bus)

- Temperature
	- [Search](https://www.digikey.com/en/products/filter/temperature-sensors/analog-and-digital-output/518?s=N4IgjCBcoCwdIDGUBmBDANgZwKYBoQB7KAbRAA4AGAJkoGYYQCrqBWGOpim%2B1rgdlbUYlPgUHU6YRsx51yXOqwBsATjAKAugQAOAFyggAynoBOASwB2AcxABfAgz4JkkdNnxFSIOvP7VqRXlyQSDyEOUQbRB9QxMLG3sCDRhIl1RMXAJiSDJ%2BZWV%2BVVUucgC6SkpS6Ukq8QKqOpAYVRpWCAIW1Tp%2BBXEYQP7OfpkQfhgxMdSBVkoODqn%2BATVqyPFqf0o%2Bimo1naXmam2OXeoFspLmCtKpLmV2ZR6BNppSgq5W0dbJ1r31QZAqgGHw4ING5HYwRBPxgB0BrB%2BKi4E1YPQB-iKrG2xQBYEqf26HyBRJ%2BxSJcOKkWisUgxjMVlsDnA5FhUFArncWS8uRAZ12YDhfNmgrAwl6XEkykoqj2wmo3QWcvUWl0Blp8QZSXAqnIJXSbkynhyZCqmjsTLSoHMABNDCk9jS6QlbAQ9ABPHQ4QxoLDIc1AA)
	- [MCP9804-E/MS](https://www.digikey.com/en/products/detail/microchip-technology/MCP9804-E-MS/2179247) (highly addressable, 0.25 degree typical accuracy, low power draw)
		- $2
- Pressure
	- Pressure sensor will be something like this [PS02](https://www.digikey.com/en/products/filter/pressure-sensors-transducers/512?s=N4IgjCBcoLQCxVAYygMwIYBsDOBTANCAG4B2aWehA9lANogDMAHGHEyALqEAOALlCBABfEUA)
		- $65
- Light
	- Let's give this one a go [VEML6030](https://www.digikey.com/en/products/detail/vishay-semiconductor-opto-division/VEML6030-GS15/6221149)
	- We'll need some kind of switching to scan through a bunch of these as they will all have the exact same address
		- $1.5 x 4
		- I can use this [bus](https://www.digikey.com/en/products/detail/texas-instruments/TCA9548APWR/3615458)
- We're looking at 0.2 + 0.2 + 3mA while we take a reading
- 

### Memory

- SPI Bus (connection to external)
- Memory itself
	- [Memory](https://www.digikey.com/en/products/detail/issi-integrated-silicon-solution-inc/IS25LP512MJ-RMLA3-TY/25675851?gad_source=1&gbraid=0AAAAADrbLlgk7QzER68U4aMwuBL59_Tjt&gclid=CjwKCAjwn6LABhBSEiwAsNJrjlvu6PKlzZXXuwAMvUjC524evqSvIpxGgfTaTkNodkxE9SWZPvrlHxoCqVgQAvD_BwE&gclsrc=aw.ds)


### Control

- Magnetic switch to turn things on and off
- Magnetic button to check status 
- MCU
	- https://www.digikey.com/en/products/detail/stmicroelectronics/STM32WL33CCV6/22519711

### Connection

- SPI Connection
- Power
	- [Battery](https://www.digikey.com/en/products/detail/jauch-quartz/LI21700JSV-50-PCM-FUSE-3-WIRES-70MM/18997198?_gl=1*ztu9ue*_up*MQ..*_gs*MQ..&gclid=CjwKCAjw6NrBBhB6EiwAvnT_rsPb51z3NqxSY-6UHtDoqnygyo5mfVpIG36oLfmtmO32BH73rRFGgRoCX4kQAvD_BwE&gclsrc=aw.ds&gbraid=0AAAAADrbLlgZBeffc8gadgZqznFXSX-91)
- Programming
- Reset Button

### Power

- [Buck/Boost](https://www.digikey.com/en/products/detail/texas-instruments/TPS63001DRCR/1016476)
- [Charger](https://www.digikey.com/en/products/detail/microchip-technology/MCP73811T-420I-OT/1626617)
- 


https://www.youtube.com/watch?v=d-f-SBC0GrU
https://www.youtube.com/watch?v=X3Rc1s6EpSI

https://www.youtube.com/watch?v=sKiBZhx0QHs

