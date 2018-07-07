#Python
import webbrowser
class Movie():
    '''
       Class Name: Movie
       Des:
    '''
    def __init__(self, Title, StoryLine, PosterImage, TrailerYoutube):
        self.title = Title
        self.storyline = StoryLine
        self.poster_image_url = PosterImage
        self.trailer_youtube_url = TrailerYoutube

    def show(self):
        webbrowser.open(self.trailer_youtube_url)
