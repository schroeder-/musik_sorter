'''
    Gui.py

    @brief  GUI code
    @author Alexander Schrode
    @date   18.07.2012
    @mail   midix01[at]googlemail.com

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


from PyQt4 import QtCore, QtGui

class File_Manager(QtGui.QWidget):

    def __init__(self, parent=None):
        super(File_Manager, self).__init__(parent)
        self._create_table(None)

    def _create_table(self, titels):
        self._table =


if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    main_window =
    main_window.show()
    sys.exit(app.exec_())
