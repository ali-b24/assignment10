from media import media

class clip(media):

    def __init__(self, name, director, imdb, url, duration, cast, genre):
        media.__init__(self, name, director, imdb, url, duration, cast, genre)
        

    def clip_edit(self):
        media.media_menu(self)
        n = int(input())
        while n<1 or n>7:
            print("wrong input! try again:")
            n = int(input())
        match n:
            case 1:
                new_name = input("Enter new name: ")
                self.name = new_name
            case 2:
                new_director = input("Enter new director: ")
                self.director = new_director
            case 3:
                new_imdb = input("Enter new IMDB: ")
                self.imdb = new_imdb
            case 4:
                new_url = input("Enter new URL: ")
                self.url = new_url
            case 5:
                new_duration = int(input("Enter new duration: "))
                self.duration = new_duration
            case 6:
                new_cast = input("Enter new cast: ")
                self.cast = new_cast
            case 7:
                new_genre = input("Enter new genre: ")
                self.genre = new_genre
        print("changes saved!")
    
    def show(self):
        media.show_info(self)