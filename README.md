# mdcb
This is really just a personal project and a rework of my custom twitch bot.  I'm trying to add more usefulness, and interactivity to the bot while also learning more about python.

### Checklist of things I want to implement (expect this to grow!):
* Character system
  - good deal of work already done, check chatgame/characterController.py
* Monsters to fight
  - started working on random monster generation.  still needs work.
* Combat
  - Combat should be handled by the take_ and heal_ damage functions of the Monster and Character classes.
  - work needs to be done for adjusting damage amounts but thats a task for the Character class (Monster inherits from Character)
* Armorsmith
  - Not yet started
* Weaponsmith
  - Some prelimiary work done on this to generate random smiths, with random inventories.
* Apothecary
  - Not yet started
* Boss fights(?)
* Quests(?)
* Crafting(?)

### Other work on parts of the bot
* Twitter integration - send tweets from a channel command
* Mastodon integration - toot from channel command
* Potentially youtube Live integration
* connection to AWS RDS
* 