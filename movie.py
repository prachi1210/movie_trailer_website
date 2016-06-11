import webbrowser

class Movie():
    def __init__(self, movie_title, poster_image):
        self.title=movie_title
        self.poster=poster_image

    def show_trailer(self):
        webbrowser.open(self.trailer)
