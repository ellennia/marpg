# Source

The python code, i.e., the game engine.


## User Input

Commands will be (currently are not) accessed in a radix tree. When a command is typed, you get the command most similar to what you typed.

b would be automatically completed to bearings, unless there was a command bake, where bake would win out because it is alphabetically first.

## World Graph

The navigatable world is comprised of a *world graph*, an undirected graph where edges represent possible motions a player-character can make between scenes. Each graph node is a dyad of a Scene object, and a tag string. Scenes are loaded from an XML file by XMLP.

Each XML!Scene has a list of 'adjacent' scenes. These are scenes that are directly accesssible to be moved to from the current scene the player-character is in. For example, if s1 is adjacent to s2, and s2 is adjacent to s3, the user can move from s1 to s2, but not to s3 directly- but a user in s2 can move to s3, and one in s3 to s2.

In this scenario, s1 is adjacent to s2, and s2 to s1. This implies that the XML for both should list the other scene as adjacent to it in XML for them to be accessible from each other- the world graph automatically fills in this 'obvious' counter-adjacency, so only one has to be marked adjacent to the other. This makes the graph always undirected, and removes the possibility of some edges being left accidently directed by omission.

## XMLP

The XML loading code. All the 'meat' of a game loaded by this engine (which could be referenced as the MaRPG engine, after the game it is designed for). The full details of the engine's XML format are specified on in the README for the scripts/ folder.

## NPCs

The NPC management is currently in-development, and unsettled.
