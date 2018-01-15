# RPG Engine XML Format

These files are loaded into the game on load, adding data and populating the world.

*Format*:

All data is encompessed in a data tag-

\<data class = "[CLASS]"\>
\</data\>

There are a number of different classes. The class used determines how the game will categorize and use the data within them.

## Classes:
+ species

	Contains a list of species (character classes) for the game.

+ npc

	Contains a list of NPCs (non-player-characters) for the game. Does not specify where or how they will appear.

+ scene

	Denotes the structure of the world and the scenes within it.
	
	\<scene name = "[NAME]"\>
		\<adjacent\>
		\</adjacent\>
	\</scene\>

+ script

	Special printouts that are formatted using the Jinja2 templating engine.
