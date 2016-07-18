###PiCTA

This project uses the Chicago Transit Authority API to track the bus outside my house. I made it because I'm always checking and rechecking this information on my phone. PiCTA only displays the predicitions I care about and updates them automatically without any interaction on my part. 

Most of these components were sponsored by [Newark / Element14](http://www.newark.com/) - thanks guys!

###BOM

Part | Cost
| :--- | ---: |
| [RPi 7" touchscreen](http://www.newark.com/raspberry-pi/raspberrypi-display/display-7-touch-screen-rpi-sbc/dp/49Y1712?MER=bn_level5_3NP_EngagementRec_1) | $75 |
| [RPi 7" touchscreen enclosure](https://www.adafruit.com/products/2033) | $15 |
| [Raspberry Pi board](http://www.newark.com/raspberry-pi/rpi2-modb-8gb-noobs/sbc-raspberry-pi-2-model-b-8gb/dp/38Y6469?selectedCategoryId=&exaMfpn=true&categoryId=&searchRef=SearchLookAhead&iscrfnonsku=false) (tested on B2 v1.1) | $40 |
| [USB wifi dongle](http://www.newark.com/adafruit-industries/814/miniature-wifi-module-raspberry/dp/53W6285?ost=53W6285&selectedCategoryId=&categoryNameResp=All%2BCategories&iscrfnonsku=false) | $12 |
| [Mini USB power supply](https://www.adafruit.com/product/1995) | $8 |
| Total | $150 |

###Instructions

2. Assemble [touchscreen/case](https://cdn-shop.adafruit.com/product-files/2718/2718build.jpg)
3. Install [NOOBS/Jessie](http://computers.tutsplus.com/tutorials/how-to-install-noobs-on-a-raspberry-pi-with-a-mac--mac-57831) (Wheezy didn't work)
2. ```    sudo nano /boot/config.txt```
3. Add ```lcd_rotate=2``` at the end
4. reboot
5. ```sudo raspi-config```
 * Set time (important for CTA tracking)
 * Enable SSH
 * Disable overscan
6. reboot
7. Connect to wifi (icon at top right)
8. Determine Pi IP address
9. SSH to Pi
8. ```sudo apt-get update```
8. ```sudo apt-get upgrade```
9. ```sudo apt-get install apache2 -y```
10. ```sudo apt-get install php5 libapache2-mod-php5 -y```
11. ```cd /var/www```
12. ```sudo chown pi: html```
13. Replace default index.html page with the code from this repository
13. ```sudo apt-get install iceweasel```
15. Navigate RPi browser to RPi IP (do not open local file directly)
16. Follow [these instructions for Firefox](https://github.com/elalemanyo/raspberry-pi-kiosk-screen) to setup kiosk mode