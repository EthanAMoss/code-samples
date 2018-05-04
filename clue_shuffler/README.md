# Clue Deck Shuffler

For an AI class I took my last semester, we created agents that played a version of the classic board game Clue (aka Cluedo). I wanted to be able to "walk through" a game with my agent so that I could debug easier, so I came up with this in order to quickly setup a Clue game state. Given a JSON document with defined "cards" separated into three lists labeled `suspects`, `weapons`, and `rooms`, this script will create a valid Clue game state, printing out the answer and all player hands. 

### Run the script
Requires [Python](https://www.python.org/) and a valid `clueDeck.json` in the same directory

```bash
$ python clue_shuffler.py
```
