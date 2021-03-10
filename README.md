# youtube watchlater/playlist exporter

this project takes the code from your watchlater playist (or other playlist) and exports it into an easily-readable CSV file with the video titles and the links to the videos.

# how to use

at this time, there are some manual steps in this process. i am looking into minimizing these and any feedback would be greatly appreciated. near as i can tell, the main roadblock at automating the currently-manual steps is that youtube playlists only load the first 100 videos at a time and one needs to scroll down on the page to get additional (batches of 100) videos to load.

# steps

1. navigate to [https://www.youtube.com/playlist?list=WL](https://www.youtube.com/playlist?list=WL) or the preferred playlist of your choice
2. if the playlist is more than 100 items, scroll down until all items are loaded
3. right-click on the page and choose "inspect" (instructions are for Chrome, other browsers will vary)
4. at the top of the html, find the `<html...` tag and right-click on it (or, to copy less code, find the `<div id="contents"...` tag and right-click on it)
5. select `Copy > Copy Element`
6. open a text editor and paste this in there. save the file in a place you can easily find it.
7. execute the program. you will be prompted for the path/filename of the text file and a filename for the output `.csv` file.

# license

licensed under [![cc-by-nc-sa4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://github.com/TheRafeSCV/ytwl-export/blob/main/LICENSE.md)
