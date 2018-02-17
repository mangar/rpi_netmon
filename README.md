# RPi NetMon



## Motivation

Monitors your network using a Raspberry Pi by hiting external websites.




## Responses

The response is produced by turning on or fleshing two leds: Red and Green

- __Red led turned on__ Problems when trying to connect to more then 50%of the websites eligible (registered at command.py)

- __Green led turned on__ 100% of websites registered returned without problems

- __Green led flashing__ More than 50% of the eligible websites returned without any problems.


__Internal Errors__

- __Green and Red flashing 3 times + Green flashes twice__ Problem to update the ```command.py```






## Developing

Yo can use a docker machine to test

__Run the check__

	docker run -v `pwd`:/app --rm python:3 python /app/user/bin/command_dev.py






__Updating the websites__

	docker run -v `pwd`:/app --rm python:3 bash -c "/bin/bash /app/update.sh"






## Configuring and installing on your RPi


- install cron
- install auto run
- wires at RPi 

