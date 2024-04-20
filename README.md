### Megaverse Challenge

This is a repo containing a Python solution to the megaverse challenge given by Crossmint.

To run it, just execute `challenge.py` and make sure to have your `CROSSMINT_CANDIDATE_ID` populated.

The repository is divided in three packages:

1. `models`: containing the megaverse board/map as well as the different megaverse objects (POLYanets, comETHs, SOLoons).
2. `factories`: it contains a factory class to parse the map onto the defined models.
3. `client`: it contains a client that abstract the low level API provided.

As this was a challenge only and not a real life service, I didn't go fully into the logging details.


### Testing

This was end to end manually tested by executing `challenge.py`.

I added some unit tests, mostly for the models and the factory.