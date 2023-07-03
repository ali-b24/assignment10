from media import media
from movie import movie
from clip import clip
from documentory import documentory
from series import series
from pyfiglet import Figlet

class main:
    def __init__(self):
        self.value = []

    def data(self):
        f = open('mediabase.txt' , 'r')
        l = f.read().split('\n')
        for i in range(len(l)-1):
            info = l[i].split(',')

            if info[0] == 'movie':
                Movie = movie(info[1], info[2], info[3], info[4], info[5], info[6], info[7])
                self.value.append(Movie)

            elif info[0] == 'series':
                Series = series(info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])
                self.value.append(Series)

            elif info[0] == 'documentory':
                Doc = documentory(info[1], info[2], info[3], info[4], info[5], info[6], info[7], info[8])
                self.value.append(Doc)
            
            elif info[0] == 'clip':
                Clip = clip(info[1], info[2], info[3], info[4], info[5], info[6], info[7])
                self.value.append(Clip)

    def welcome(self):
        y = Figlet(font='standard')
        print(y.renderText('Media Manager'))

    def show_menu(self):
        print("Menu:")
        print("1-Add media")
        print("2-search")
        print("3-advance search")
        print("4-Delete media")
        print("5-Edit media info")
        print("6-Show info")
        print("7-download")
        print("0-exit")
    
    def menu(self):
        self.show_menu()
        c = int(input())
        while c<0 or c>7:
            print("Wrong input! try again")
            c = int(input())
        match c:
            case 0:
                print("GoodBye!")
                exit()
            case 1:
                self.add_data()
            case 2:
                self.search()
            case 3:
                self.advance_search()
            case 4:
                self.delete_data()
            case 5:
                self.edit_data()
            case 6:
                self.show_data()
            case 7:
                media.download(self)

    def add_data(self):
        print("1-Add movie")
        print("2-Add series")
        print("3-Add documentory")
        print("4-Add clip")
        a = int(input())
        
        name = input("Enter name: ")
        director = input("Enter director: ")
        imdb = int(input("Enter the IMDB: "))
        url = input("Enter URL: ")
        duration = int(input("Enter duration: "))
        cast = input("Enter actors: ")
        genre = input("Enter genre: ")
        match a:
            case 1:
                self.value.append(movie(name, director, imdb, url, duration, cast, genre))
                print("movie added to mediabase!")
                self.save()
            case 2:
                episode = int(input("Enter number of episodes: "))
                self.value.append(series(name, director, imdb, url, duration, cast, genre, episode))
                print("series added to mediabase!")
                self.save()
            case 3:
                episode = int(input("Enter number of episodes: "))
                self.value.append(documentory(name, director, imdb, url, duration, cast,genre, episode))
                print("documentory added to mediabase!")
                self.save()
            case 4:
                self.value.append(clip(name, director, imdb, url, duration, cast,genre))
                print("clip added to mediabase!")
                self.save()
        self.menu()

    def search(self):
        flag = 1
        media_name = input("Enter media name: ")
        for i in range(len(self.value)):
            if media_name == self.value[i].name:
                print("media found!")
                flag = 0 
        if flag == 1:
            print("media does not exist!")
        self.menu()

    def advance_search(self):
        flag = 0
        t1 = int(input("Enter min time: "))
        t2 = int(input("Enter max time: "))
        print("---------------------------------------")
        for i in range(len(self.value)):
            if t1 <int(self.value[i].duration)< t2:
                self.value[i].show()
                print("---------------------------------------")
                flag = 1
        if flag == 0:
            print("no media with this duration!")
        self.menu()
   
    def edit_data(self):
        print("1-Edit movie")
        print("2-Edit series")
        print("3-Edit documentory")
        print("4-Edit clip")
        b = int(input())
        while b<1 or b>4:
            print("Wrong input! try again")
            b = int(input())
        flag = 1
        media_name = input("Enter media name: ")
        for i in range(len(self.value)):
            if media_name == self.value[i].name:
                flag = 0
                match b:
                    case 1:
                        movie.movie_edit(self.value[i])
                        self.save()
                    case 2:
                        series.series_edit(self.value[i])
                        self.save()
                    case 3:
                        documentory.doc_edit(self.value[i])
                        self.save()
                    case 4:
                        clip.clip_edit(self.value[i])
                        self.save()
        if flag == 1:
            print("media does not exist!")
        self.menu()

    def delete_data(self):
        media_name =input("Enter media name: ")
        for i in range(len(self.value)):
            if media_name == self.value[i].name:
                del(self.value[i])
                print("data deleted!")
            else:
                print("media does not exist!")
        self.save()
        self.menu()

    def show_data(self):
        for i in range(len(self.value)):
            self.value[i].show()
        self.menu()

    def save(self):
        f = open("mediabase.txt" , 'w')
        for i in self.value:
            if type(i).__name__ == 'movie':
                row = 'movie'+','+i.name+','+i.director+','+str(i.imdb)+','+i.url+','+str(i.duration)+','+i.cast+','+i.genre+'\n'
                f.write(row)
            elif type(i).__name__ == 'series':
                row = 'series'+','+i.name+','+i.director+','+str(i.imdb)+','+i.url+','+str(i.duration)+','+i.cast+','+i.genre+','+str(i.episode)+'\n'
                f.write(row)
            elif type(i).__name__ == 'documentory':
                row = 'documentory'+','+i.name+','+i.director+','+str(i.imdb)+','+i.url+','+str(i.duration)+','+i.cast+','+i.genre+','+str(i.episode)+'\n'
                f.write(row)
            elif type(i).__name__ == 'clip':
                row = 'clip'+','+i.name+','+i.director+','+str(i.imdb)+','+i.url+','+str(i.duration)+','+i.cast+','+i.genre+'\n'
                f.write(row)
        f.close()

x = main()
x.data()
x.welcome()
x.menu()

               