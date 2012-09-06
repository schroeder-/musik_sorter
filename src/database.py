'''
    Database.py

    @brief Handles Database represation and Database handling
    @author Alexander Schrode
    @date   16.07.2012
    @mail   midix01[at]googlemail.com

    @attention: sqlite converters are not award of malicous code
                but it should need for this kind of software.

    Copyright (c) 2012 Alexander Schrode

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

'''
import sqlite3
from os.path import isfile
from shutil import copyfile

class Title:
   def __init__(self, title, artist, length, filename, bpm=0.0, key='', genre=''):
       '''Inits a title'''
       self.title    = title
       self.artist  = artist
       self.length   = length
       self.genre    = genre
       self.bpm      = bpm
       self.key      = key
       self.filename = filename

   def __str__(self):
       return "%s;%s;%d;%f;%s;%s;%s" % (self.title, self.artist, self.length,
                                        self.bpm, self.key, self.genre, self.filename)

class CD:
    def __init__(self, name, titles, artists):
        '''Inits a cd'''
        self.name = name
        self.tracks = zip[titles, artists]

    def __str__(self):
        tracks, artists = [[x[0], x[1]] for x in self.tracks]
        return "%s;%s;%s" % (self.name, '#'.join(tracks), '#'.join(artists))

def title_adapter(title):
    '''converts Title class for sqlite3'''
    return str(title)

def title_converter(s):
    '''converts title sqlite type to a Python Title Class'''
    print(s)
    s = s.split(";")
    title, artist = s[0], s[1]
    length, key = int(s[2]), int(s[4])
    bpm = float(s[3])
    genre = s[5]
    filename = s[6]
    return Title(title, artist, length, filename, bpm, key, genre)

def cd_adapter(cd):
    '''converts CD class for sqlite3'''
    return str(cd)

def cd_converter(s):
    '''converts cd sqlite type to a Python CD Class'''
    s = s.split(";")
    return CD(s[0], s[1].split('#'), s[2].split('#'))


class Database:
    ''' Database Adapter for all transactions '''

    self.titel_keys = ['name', 'artist', 'key', 'bpm', 'genre', 'file']

    def __init__(self, filename):
        self._register_adapter()
        self._connect(filename)
        self._file = filename

    def _register_adapter(self):
        '''register all adpater for used Datatypes'''
        sqlite3.register_adapter(Title, title_adapter)
        sqlite3.register_adapter(CD, cd_adapter)
        sqlite3.register_converter("cd", cd_converter)
        sqlite3.register_converter("title", title_converter)

    def _connect(self, filen):
        '''Loads data base from @filen'''
        self._db = sqlite3.connect(filen)
        cur = self._db.cursor()
        cur.execute("create table if not exists title_db(t title)")
        cur.execute("create table if not exists cd_db(c cd)")
        cur.close()

    def insert_titles(self, titles):
        '''Insert all elements of an list/tupel of titles into DB'''
        cur = self._db.cursor()
        for elem in titles:
           cur.execute("insert into title_db(t) values (?)",
                       (elem,))
        self._db.commit()
        cur.close()

    def insert_cd(self, cd):
        '''Insert all elements of an list/tupel of cds into DB'''
        cur = self._db.cursor()
        for elem in cd:
           cur.execute("insert into cd_db(c) values (?)", (elem,))
        self._db.commit()
        cur.close()

    def get_all_titles(self):
       '''Get all Titles from DB'''
       cur = self._db.cursor()
       cur.execute('select t as "t [title]" from title_db')
       ret = cur.fetchall()[0]
       #@todo add correct handling
       cur.close()
       return ret
'''
    def get_by_parameter_titel(search, key):
       if key not in self.titel_keys:
          pass
       else:
          return None
'''
    def backup_database(target):
        '''Copy a backup to target dir'''
        copyfile(filen, target)
