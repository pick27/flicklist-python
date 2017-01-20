import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # TODO: make a list with at least 5 movie titles
        movies = []
        movies.append("The Big Lebowski")
        movies.append("Star Wars")
        movies.append("Starman")
        movies.append("The Notebook")
        movies.append("The Day the Earth Stood Still")
        movies.append("Star Trek: The Movie")

        # TODO: randomly choose one of the movies, and return it
        movie_choice = random.choice(movies)

        return movie_choice

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        content += "<h1>Tommorow's Movie</h1>"
        movie2 = self.getRandomMovie()
        movie2 = movie
        while movie == movie2:
            movie2 = self.getRandomMovie()
        content += "<p>" + movie2 + "</p>"
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
