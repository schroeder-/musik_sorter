import sqlite3
from os.path import isfile
from shutil import copyfile

class Title:
   def __init__(self, title, artist, length, filename, bpm=0.0, key=''):
       '''Inits a title'''
       self.title    = title
       self.artists  = artist
       self.length   = time_converter(length)
       self.bpm      = bpm
       self.key      = key
       self.filename = filename

   def __repr__(self, protocol):
       return "%s;%s;%d;%f;%d;%s" % (self.text, self.artist, self.length
                                    self.bpm, self.key, self.filename)

class CD:
    def __init__(self, name, titles, artists):
        '''Inits a cd'''
        self.name = name
        self.tracks = zip(self.titles, self.artist)

    def remove



def time_converter(time):
    '''convert time into int number'''
    #@todo
    return time

def title_adapter(title):
    '''converts Title class for sqlite3'''
    return str(title)

def title_converter(s):
    '''converts title sqlite type to a Python Title Class'''
    s = s.split(";")
    title, artist = s[0], s[1]
    length, key = int(s[2]), int(s[4])
    bpm = float(s[3])
    filename = s[5]
    return Title(title, artist, length, filename, bpm, key)

class Database:
    ''' Database Adapter for all transactions '''
    def __init__(self, filename):
        self._register_adapter()
        self._connect(filename)
        self._file = filename

    def _register_adapter(self):
        '''register all adpater for used Datatypes'''
        sqlite3.register_adapter(Title, title_adapter)
        sqlite3.register_converter("title", title_converter)

    def _connect(self, filen):
        '''Loads data base from @filen'''
        if isfile(filen):
            self._db = sqlite3.connect(filen)
        else:
            self._db = sqlite3.connect(filen)
            cur = self._db.cursor()
            cur.execute("creat table title_db(t title)")
            cur.close()

    def insert_titles(self, titles):
        '''Insert all elements of an list/tupel of titles into DB'''
        cur.execute("insert into title_db(t) values (?)",
                    (x for x in titles))

    def backup_database(target):
        '''Copy a backup to target dir'''
        copyfile(filen, target)
