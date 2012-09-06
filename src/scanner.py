'''
    scanner.py

    @brief Scanner Classes to process files in the directorys
    @deps  rely on stagger
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

import os
import stagger
from stagger.id3 import * # contains ID3 frame types
from database import Title, Database

class Base_Scanner:
    files = ''

    def process_file(self, file):
        pass

    def process_dir_pre(self, dir):
        pass

    def process_dir_post(self, dir):
        pass

    def scann(self, dir):
        for item in os.listdir(dir):
            file = os.path.join(dir, item)
            if file == dir:
                pass
            elif os.path.isdir(file):
                self.process_dir_pre(dir)
                self.scann(file)
                self.process_dir_post(dir)
            elif os.path.isfile(file) and os.path.splitext(item)[1] in self.files:
                self.process_file(file)

class Full_Music_Scann(Base_Scanner):
    files = ['.mp3']
    def run(self, dir):
        '''scanns a dir and returns Title objects'''
        self._titles = []
        self.scann(dir)
        return self._titles

    def process_file(self, f):
        track = stagger.read_tag(f)
        self._titles.append(Title(track.title, track.artist,
                                  1,#track[TLEN].text[0],
                                  f, int(track[TBPM].text[0]),
                                  track[TKEY].text[0],
                                  track.genre))

if __name__ == '__main__':
    test = Full_Music_Scann()
    res = test.run('C:\\muisk\\beats mp3')
    #for x in res:
     #  print(x)
