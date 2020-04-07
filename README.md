# Catacorn
Software for https://github.com/MermaidAllie/Candy-the-Catacorn

## Notes:

### Accessing the REPL.

The Catacorn board actually presents numerous USB devices, one of which is a serial line on `/dev/ttyACM0` (number will change if you have other devices).  On some operating systems (e.g. Ubuntu) you will need to add your user to the `dialout` group.

To connect to the micro-python based REPL, connect (115200 baud) and press `ctrl-c` followed by any key to drop into the REPL.  

E.g. if you use GNU Screen as your terminal:

```
screen /dev/ttyACM0 115200
```
