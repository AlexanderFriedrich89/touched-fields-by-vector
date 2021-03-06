# touched-fields-by-vector
### **Calculate touched fields by a vector**
---
**Known Issue:**
- Exeption 0 division not handled, will be fixed soon.
- 0 Division Error is fixed in source file but not yet implemented in distributions.
- updated distributions will follow.
---
Imagine you have a squared grid and each square represents a point with x and y coordinates, e.g. x|y = 0|0, 3|7, ... and so on.
With this Python-Script you can calculate all fields a vector goes through from a start point to an end point.
Just choose an option and enter integer values seperated with whitespace.
It also works in termux-android-app with python3 installed.

If you do not have Python installed use one of the builds in ```/dist```.

The directory ```/dist``` contains a standalone build for Linux and Windows.

- **Linux:**
Go into ```/dist/vector_linux``` and run the executable with 
```sh
./vector
```

- **Windows:**
Go into ```/dist/vector_win``` and double click .exe-file
```sh
vector.exe
```


Take a look at the example screenshot.

[![image](https://github.com/AlexanderFriedrich89/touched-fields-by-vector/blob/main/Screenshot_Termux_1.jpg?raw=true)](https://github.com/AlexanderFriedrich89/touched-fields-by-vector/blob/main/Screenshot_Termux_1.jpg?raw=true)

[![image](https://github.com/AlexanderFriedrich89/touched-fields-by-vector/blob/main/Screenshot_Termux_2.jpg?raw=true)](https://github.com/AlexanderFriedrich89/touched-fields-by-vector/blob/main/Screenshot_Termux_2.jpg?raw=true)

[![image](https://github.com/AlexanderFriedrich89/touched-fields-by-vector/blob/main/Screenshot_Termux_3.jpg?raw=true)](https://github.com/AlexanderFriedrich89/touched-fields-by-vector/blob/main/Screenshot_Termux_3.jpg?raw=true)
