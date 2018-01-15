# Source

The Python code, i.e., the game engine.


## User Interface

Commands are accessed in a trie. When a command is typed, you get the command most similar to what you typed.

b would be automatically completed to bearings, unless there was a command bake, where bake would win out because it is alphabetically first.

## World Graph

The navigatable world is comprised of a *world graph*, an [undirected graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics#Undirected_graph) where edges represent possible motions a player-character can make between scenes. Each graph node is a dyad of a Scene object, and a tag string. Scenes are loaded from an XML file by XMLP.

Each scene has a list of 'adjacent' scenes. These are scenes that are directly accesssible to be moved to from the current scene the player-character is in. For example, if s1 is adjacent to s2, and s2 is adjacent to s3, the user can move from s1 to s2, but not to s3 directly- but a user in s2 can move to s3, and one in s3 to s2.

In this scenario, s1 is adjacent to s2, and s2 to s1. This implies that the XML for both should list the other scene as adjacent to it in XML for them to be accessible from each other- the world graph automatically fills in this 'obvious' counter-adjacency, so only one has to be marked adjacent to the other. This makes the graph always undirected, and removes the possibility of some edges being left accidently directed by omission.

In addition, the world graph should also be a *connected* graph. That is to say- if you have nodes that aren't connected to the others, they are inaccessible, and there is no way to reach them in the game engine. The game starts the player-character off in a default, hardcoded scene/node named 'DEFNODE'- there should be exactly one scene in the XML adjacent to DEFNODE. The player-character will spawn in that scene. If multiple scenes are adjacent to DEFNODE then the one with the first name alphabetically will be chosen. DEFNODE will not appear in the game (i.e. with 'bearings' or other commands) and therefore the player cannot move back onto it.

There is no error checking and the engine won't tell you if your new scenes aren't connected to the rest of the graph. The one exception to this is that the engine WILL throw an error if there are no nodes are connected to DEFNODE, since without one being there, the game can't meaningfully start.

## XMLP

The XML loading code. All the 'meat' of a game loaded by this engine (which could be referenced as the MaRPG engine, after the game it is designed for). The full details of the engine's XML format are specified on in the README for the scripts/ folder.

## NPCs

The NPC management is currently in-development, and unsettled.
