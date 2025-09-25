# age-weighted-roulette

This code was originally an age-weighted roulette used for personal use, to decide which series to watch and which games to play. I have a large list of games, movies and series to consume, but have a hard time deciding which one to go for.
But as it is easily extensible to general purpose, I decided to adapt it.

## Usage

First of all, you have to write the name of the elements you are giving to the script in singular form and after in plural form, e.g., "movie", "series" and "game". This is for the script to say "enter a movie" instead of "enter an element" and such things.

The elements of the list can be succeeded by a date field that represents when you added it to the list. This is the format:
> Darkwood, 29/02/2023

If you don't specify any date, the element's date will be set to the current time.

To finish the elements' introduction, write "$" as an element.