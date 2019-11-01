# "Tempo, Kleine Fische!" Simulator  

![Build Status](https://travis-ci.com/VinceCabs/kleine-fische-simulator.svg?branch=master "Build status")

Pretty simple simulator for the famous "Tempo, kleine Fische" board game.

![Kleine Fische](./docs/img/kleine-fische-2.jpg "Tempo, klein Fische!")

## Some interesting learnings from the simulator

*...and what to expect.*

If we simulate a great number of games, we can get some interesting stats:

* you should **always take the fish team**, they have 50.4% chance to win!
* an average game lasts **22.9 turns**
* fishermen have 25.9% chance to win,  23.7% chance to have draw game

## Running

No need to install extra packages. Just define the number of games you want to simulate (10,000 by default)

```sh
# windows
cd src
python kleine_fische.py
# linux
cd src
python3 kleine_fische.py
```

## Contributing & comments

I am a complete rookie in Python programming. **Comments or advices are very much welcome**.
