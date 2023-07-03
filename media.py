import pytube

class media:
    def __init__(self, name, director, imdb, url, duration, cast, genre):
        self.name = name
        self.director = director
        self.imdb = imdb
        self.url = url
        self.duration = duration
        self.cast = cast
        self.genre = genre

    def media_menu(self):
        print("1-Edit name")
        print("2-Edit director")
        print("3-Edit IMDB")
        print("4-Edit URL")
        print("5-Edit duration")
        print("6-Edit cast")
        print("7-Edit genre")
        
    def show_info(self):
        print('Name:', self.name, '\n', 'Director:', self.director, '\n', 'IMDB:', self.imdb, '\n', 'URL:',
              self.url, '\n', 'Duration:', self.duration, '\n', 'Cast:', self.cast, '\n', 'genre:', self.genre)

    def download(self):
        link = input('Enter URL for downloading: ')
        first_stream = pytube.YouTube(link).streams.first()
        first_stream.download(output_path='./', filename='test.mp4')
        print('Download completed!')
