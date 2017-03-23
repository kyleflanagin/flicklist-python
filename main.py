import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

            #list of possible movies
            movies = [
            "The Princess Bride",
            "The Hitchhiker's Guide to the Galaxy",
            "The LEGO Movie",
            "Snakes on a Plane",
            "Land Before Time VI: Secret of Saurus Rock"
            ]

            #randomly select a movie
            index = random.randint(0,4)

            return movies[index]

    def get(self):
        # choose a movie by invoking our new function
        todays_movie = self.getRandomMovie()
        tomorrows_movie = self.getRandomMovie()

        # build the response string
        todays_content = "<h1>Movie of the Day</h1>"
        todays_content += "<p>" + todays_movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"
        tomorrows_content = "<h1>Tomorrow's Movie</h1>"
        tomorrows_content += "<p>" + tomorrows_movie + "</p>"

        self.response.write(todays_content + tomorrows_content)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
