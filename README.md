# HomeSceneObjectFinder
Scene Object UUID finder for PlayStation Home.

Requires Python 3.6 or higher. Likely will fail with some edge case scenes, but works with most SCE-developed scenes, LOOT Space Station, Hudson Gate, and plenty of others. Your mileage may vary with whatever scene you try this with.

Intended to aid those who need a list of UUIDs in a scene file for any reason (usually for when working on a HDK build or locating a broken object). The program will automatically remove duplicate UUIDs from the list prior to output.

## Usage
```
python main.py "PATH\TO\SCENEFILE.SCENE" [-f (all,sceneObjectOnly,luaGameOnly,arcadeGameOnly)] [-p]
```
Run the script with the -h tag and nothing else to see a brief decription of the two switches currently available.

Download using the Code button, don't download the scripts individually unless you know what the heck you're doing. Downloading main.py by itself won't work due to its' reliance on a module contained within the repo.
