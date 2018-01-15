# Source

The python code, i.e., the game engine.

## World Graph

The navigatable world is comprised of a *world graph*, an undirected graph where edges represent possible motions a player-character can make between scenes. Each graph node is a dyad of a Scene object, and a tag string. Scenes are loaded from an XML file by XMLP.

Each XML!Scene has a list of 'adjacent' scenes. These are scenes that are directly accesssible to be moved to from the current scene the player-character is in. For example, if scene_one is adjacent to scene_two, and scene_two is adjacent to scene_three, the user can move from scene_one to scene_two, but not to scene_three directly- but a user in scene_two can move to scene_three, and one in scene_three to scene_two.

In this scenario, scene_one is adjacent to scene_two, and scene_two to scene_one. This implies that the XML for both should list the other scene as adjacent to it in XML for them to be accessible from each other- the world graph automatically fills in this 'obvious' counter-adjacency, so only one has to be marked adjacent to the other. This makes the graph always undirected, and removes the possibility of some edges being left accidently directed by omission.

## XMLP

The XML loading code. All the 'meat' of a game loaded by this engine (which could be referenced as the MaRPG engine, after the game it is designed for). The full details of the engine's XML format are specified on in the README for the scripts/ folder.
