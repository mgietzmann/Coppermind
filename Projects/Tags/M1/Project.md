>To build an "tag" that I could pull behind the boat to learn about dead reckoning with IMUs (as well as other peripherals)

### Steps

- [ ] Create a breadboard circuit
	- [ ] Using my MCU
	- [ ] Using computer power
	- [ ] Has pressure and temperature sensors, a clock, IMU, a light sensor, and onboard memory
		- [ ] Understand how each one works, how to evaluate the goodness of any particular sensor, etc. 
	- [ ] Figure out the power draw
	- [ ] Figure out how to transfer data on and off the chip
	- [ ] Figure out how to run the thing on and off and command it with something like a magnet or the like
- [ ] Turn into printed circuit board and (marine grade) waterproof it
	- [ ] Add batteries
	- [ ] Get it printed
	- [ ] Waterproof it
	- [ ] Tow it behind the boat along with GPS readings to see how well the dead reckoning can work

Not addressed - communication, model based location estimates, tag release, getting down to absolutely insane depths (i.e. integrity testing)

### Components

- [IMU](https://www.digikey.com/en/products/detail/nxp-usa-inc/FXLS8964AFR3/16647162?gclsrc=aw.ds&&utm_adgroup=General&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Supplier_NXP-Semiconductors_0568_Co-op&utm_term=&utm_content=General&utm_id=go_cmp-20628823145_adg-_ad-__dev-c_ext-_prd-16647162_sig-CjwKCAjwn6LABhBSEiwAsNJrjoHJUFf1h0rxxPXtyh5B-vGEyp2H0_-LXbsuRiPj5JlwLX4zKITCEBoCwSkQAvD_BwE&gad_source=1&gbraid=0AAAAADrbLlgcRABeFJ93OHBSDaeVkZSJX&gclid=CjwKCAjwn6LABhBSEiwAsNJrjoHJUFf1h0rxxPXtyh5B-vGEyp2H0_-LXbsuRiPj5JlwLX4zKITCEBoCwSkQAvD_BwE&gclsrc=aw.ds)
- [Temperature](https://www.digikey.com/en/products/detail/adafruit-industries-llc/1782/4990781?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Low%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20243063506_adg-_ad-__dev-c_ext-_prd-4990781_sig-CjwKCAjwn6LABhBSEiwAsNJrjn4yk2CFPTjcfztr2R62t46WOZEII0b9_OJyN-EMo-FIB-JiLn9i3RoCMmAQAvD_BwE&gad_source=1&gbraid=0AAAAADrbLlhbS8xtJZAHvTT2x9pSJri1O&gclid=CjwKCAjwn6LABhBSEiwAsNJrjn4yk2CFPTjcfztr2R62t46WOZEII0b9_OJyN-EMo-FIB-JiLn9i3RoCMmAQAvD_BwE&gclsrc=aw.ds)
- [Clock](https://www.digikey.com/en/products/detail/adafruit-industries-llc/3013/5875808?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Low%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20243063506_adg-_ad-__dev-c_ext-_prd-5875808_sig-CjwKCAjwn6LABhBSEiwAsNJrjvdNwGMmNX4aNhidQBjmbeGwCEQrxOJtbvBhSKlUfwVe6I4Rf3TwsRoC5W0QAvD_BwE&gad_source=1&gbraid=0AAAAADrbLlhbS8xtJZAHvTT2x9pSJri1O&gclid=CjwKCAjwn6LABhBSEiwAsNJrjvdNwGMmNX4aNhidQBjmbeGwCEQrxOJtbvBhSKlUfwVe6I4Rf3TwsRoC5W0QAvD_BwE&gclsrc=aw.ds)
- [Pressure](https://www.digikey.com/en/products/detail/te-connectivity-measurement-specialties/MS5837-02BA21/8276465?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Supplier_Focus%20Supplier&utm_term=&utm_content=&utm_id=go_cmp-20243063242_adg-_ad-__dev-c_ext-_prd-8276465_sig-CjwKCAjwn6LABhBSEiwAsNJrjj10FGYz8Sbi4xpo6hGRjvJ0gPCqtj-U9Os7EkrR8OGvrV61YFFcKhoC7-wQAvD_BwE&gad_source=1&gbraid=0AAAAADrbLlgmWkqUDtUhg4Zf_rWfaz_k3&gclid=CjwKCAjwn6LABhBSEiwAsNJrjj10FGYz8Sbi4xpo6hGRjvJ0gPCqtj-U9Os7EkrR8OGvrV61YFFcKhoC7-wQAvD_BwE&gclsrc=aw.ds)
- [Memory](https://www.digikey.com/en/products/detail/issi-integrated-silicon-solution-inc/IS25LP512MJ-RMLA3-TY/25675851?gad_source=1&gbraid=0AAAAADrbLlgk7QzER68U4aMwuBL59_Tjt&gclid=CjwKCAjwn6LABhBSEiwAsNJrjlvu6PKlzZXXuwAMvUjC524evqSvIpxGgfTaTkNodkxE9SWZPvrlHxoCqVgQAvD_BwE&gclsrc=aw.ds)
- [Light Sensor](https://www.digikey.com/en/products/detail/adafruit-industries-llc/4681/12760934?gQT=1)

### Understanding Components

#### Temperature

Let's start here. I'm going to get this - [Temperature](https://www.mouser.com/ProductDetail/Microchip-Technology/MCP9808-E-MS?qs=fgHA1UgJI8CbPdrkP5zjqQ%3D%3D&mgh=1&utm_id=22305010504&utm_source=google&utm_medium=cpc&utm_marketing_tactic=amercorp&gad_source=1&gbraid=0AAAAADn_wf3g3XjKU6ygr_Om_ZqebmG3r&gclid=CjwKCAjwn6LABhBSEiwAsNJrjlUc6xVthtraP2qz9hVhOyOMzfvD0r544THerbiYWSIN4pZZSJLnHxoCXiAQAvD_BwE) and then attempt to communicate with it by writing my own protocol. 512 kbit will be way to much [Memory](https://www.digikey.com/en/products/detail/macronix/MX25V5126FM1I/11560963?_gl=1*1o0rosx*_up*MQ..*_gs*MQ..&gclid=CjwKCAjwn6LABhBSEiwAsNJrjlvu6PKlzZXXuwAMvUjC524evqSvIpxGgfTaTkNodkxE9SWZPvrlHxoCqVgQAvD_BwE&gclsrc=aw.ds&gbraid=0AAAAADrbLlgk7QzER68U4aMwuBL59_Tjt) for this purpose. 

One question is, how will I get data off of this chip afterwards? I'll use this as my [Switch](https://www.digikey.com/en/products/detail/toshiba-semiconductor-and-storage/TCS40DLR-LF/5012763?_gl=1*1xhxqyz*_up*MQ..*_gs*MQ..&gclid=CjwKCAjwn6LABhBSEiwAsNJrjiq7hcSVa9P6szVXkjMlnZQB-Pib1I8V0HgVljGtac1JXNvz3WbNjRoCHz8QAvD_BwE&gclsrc=aw.ds&gbraid=0AAAAADrbLliu8YxYDbSEDi0Y7jqvLwgTa).

I need to look into battery chargers and batteries more to understand what's going on there. 

Charging circuit: https://www.youtube.com/watch?v=GRd9uTwg7r4

- [Diode](https://www.digikey.com/en/products/detail/onsemi/MMBD101LT1G/1139784?gQT=1)
- [P Channel Mosfet](https://www.digikey.com/en/products/detail/onsemi/NTR4502PT1G/1484950?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Medium%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20223376311_adg-_ad-__dev-c_ext-_prd-1484950_sig-CjwKCAjwwqfABhBcEiwAZJjC3pDmWPJPhdJ10RDExGo4ojELpzTlSiqnFgg9UUTRKYbhSsWmtV4q-hoCBkoQAvD_BwE&gad_source=1&gbraid=0AAAAADrbLlhETDSs4XLJBPqmgYP1eD_TA&gclid=CjwKCAjwwqfABhBcEiwAZJjC3pDmWPJPhdJ10RDExGo4ojELpzTlSiqnFgg9UUTRKYbhSsWmtV4q-hoCBkoQAvD_BwE&gclsrc=aw.ds)


https://www.falstad.com/circuit/

### Using Components

These things are tiny! I think I'll need to make breakout boards for each of the components so that I can then breadboard them together to play around with doing things in different ways. 

I also need to get much thinner solder and a thinner tip for my soldering iron.

Time to learn KiCad!

https://github.com/MalphasWats/hawk?tab=readme-ov-file

- [JST](https://www.digikey.com/en/products/detail/sparkfun-electronics/16766/12340136?gQT=1)
- 






