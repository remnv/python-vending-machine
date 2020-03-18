## Description
Vending Machine Challenge


## Application Python
    Python      : 3.7.6


## Installation
```bash
#requirement
$ pip install -r requirements.txt
```
    

## Running Apps
```bash
#run unit test
$ python unit_test.py

#run application
$ python main.py
```



## Standard input method
```
Input method
	Input [command number + space + arguments] into prompt

For example: “1 500” (Insert 500 JPY coin by Command number (1))
*Console image. In fact, execute from Eclipse(Editor) is OK

Command (1)
	Command name     : Insert coins
	Command number   : 1
	Argument         : int, coin types (any of 10, 50, 100, 500)
For example: “1 500” (Insert 500 JPY coin)

Command (2)
	Command name     : Choose item to purchase
	Command number   : 2
	Argument         : int, item types (any of item numbers)
For example: “2 1” (1: Choose Canned coffee)

Command (3)
	Command name     : Get items
	Command number   : 3
	Argument         : None
For example: “3” (Get items)

Command (4)
	Command name     : Return coins
	Command number   : 4
	Argument         : None
For example: “4” (Pull Return lever)

Command (5)
	Command name     : Get returned coins
	Command number   : 5
	Argument         : None
For example: “5” (Get returned coins)
```
