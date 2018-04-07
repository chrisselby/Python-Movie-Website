# Back to the Future Movies Website

## Overview
A basic website displaying all three Back to the Future movies with poster art, titles, and storylines. The movie trailer automatically plays when a movie tile is clicked.

## Generating the Website

### Requirements
Python is required to run this app. Download it [here](https://www.python.org/).

### Steps:
1. Fork this repository on Github.
2. Clone the forked repository to your local machine.
3. In a terminal, `cd` into the cloned project
4. Run `python entertainment_center.py`
6. A window should open in your default web browser with the generated website. If not, you can manually drag the generated html file from the project folder into your web browser of choice.

> Note: If you make any changes, run the `python entertainment_center.py` command again to regenerate the website.

### Adding a Movie
Each movie is an instance of the `Movie` class, found in `media.py`. When creating an instance of the `Movie` class, you should include the title, storyline, poster image url, and youtube url where the movie trailer can be found. An example of this can be found in `entertainment_center.py`.
