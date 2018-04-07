import media
import fresh_tomatoes

# Set often used url formats for poster art and youtube url
wikipedia_image = "https://upload.wikimedia.org/wikipedia/en{}.jpg"
youtube_url = "https://www.youtube.com/watch?v={}"

# Initialize first BTTF movie
btf = media.Movie("Back to the Future",
    "In this 1980s sci-fi classic, a small-town California teen is thrown back into"
    " the '50s when an experiment by his eccentric scientist friend goes awry.",
    wikipedia_image.format("/d/d2/Back_to_the_Future"),
    youtube_url.format("qvsgGtivCgs"))

# Initialize second BTTF movie
btf2 = media.Movie("Back to the Future Part II",
    "In this zany sequel, the time-traveling duo return from saving Marty's "
    "future son from disaster, only to discover their own time transformed.",
    wikipedia_image.format("/c/c2/Back_to_the_Future_Part_II"),
    youtube_url.format("MdENmefJRpw"))

# Initialize third BTTF movie
btf3 = media.Movie("Back to the Future Part III",
    "In this final chapter, Marty obtains a 70-year-old message from his"
    " time-traveling friend, in which he informs Marty that he has retired"
    " to a small town in the Old West.",
    wikipedia_image.format("/4/4e/Back_to_the_Future_Part_III"),
    youtube_url.format("3C8c3EoEfw4"))

# Create array of movies, display each twice for some height to webpage
back_to_the_futures = [btf, btf2, btf3, btf, btf2, btf3]
# Ouput movies to html page and open page in web browser
fresh_tomatoes.open_movies_page(back_to_the_futures)
