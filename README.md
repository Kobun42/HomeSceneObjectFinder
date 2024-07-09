# HomeSceneObjectFinder
Scene Object UUID finder for PlayStation Home.

Requires Python 3.6 or higher. Likely will fail with a lot of edge case scenes, but works with most SCE-developed scenes and the LOOT space station. Your mileage may vary with whatever scene you try this with. Further updates will be made to make it less janky, but for now this remains a simple proof of concept.

Intended to aid those who need a list of UUIDs in a scene file for any reason (usually for when working on a HDK build or locating a broken object). The program will automatically remove duplicate UUIDs from the list prior to output.
