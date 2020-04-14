# Catacorn
Software for https://github.com/MermaidAllie/Candy-the-Catacorn

## kittylib.py

The functionality from @MermaidAllie's `main.py` that imports libraries and sets things up.

e.g. to use it to set the left eye to red:

```python
import kittylib as kl
kl.left_eye(255,0,0)
```

## main.py

Loaded by CircuitPython on boot.  Edit to make it load + execute the appropriate example.  Defaults to metronome.

## orig.py

A version of @MermaidAllie's `main.py` which uses kittylib.

## metronome.py

A simple metronome.  Ears cycle frequency and time signiture.

## pi.py

The https://github.com/UCL-RITS/pi_examples example for the Cacacorn board.  To use it import it and call `picalc`

```python
import pi
pi.picalc()     # Run with default iterations (4000)
pi.picalc(1000) # Run with 1000 iterations
```

## flash.sh

`flash.sh` checks all the `*.py` files in a current directory to see if they are different from the files with the same name on the Catacorn board and if so copys them over.  By default it assumes that the board is mounted on `/media/owain/NYANPY` but you can change this by passing it an argument e.g.

```
./flash.sh /media/bob/NYANPY
```

It's *not* recursive currently.

## Notes:

### Accessing the REPL.

The Catacorn board actually presents numerous USB devices, one of which is a serial line on `/dev/ttyACM0` (number will change if you have other devices).  On some operating systems (e.g. Ubuntu) you will need to add your user to the `dialout` group.

To connect to the micro-python based REPL, connect (115200 baud) and press `ctrl-c` followed by any key to drop into the REPL.  

E.g. if you use GNU Screen as your terminal:

```
screen /dev/ttyACM0 115200
```
