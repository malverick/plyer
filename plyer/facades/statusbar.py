'''
Status Bar
==========

The status bar is horizontal bar present on the top of screen of mobile phones.
Status bar contains information such as network provider, network strength,
battery information, time.

The :class:`StatusBar` provides access to public methods to hide/unhide the
status bar and change the background color of status bar.

Simple Examples
---------------

To hide status bar::

    >>> from plyer import statusbar
    >>> statusbar.hide()

To unhide status bar::

    >>> from plyer import statusbar
    >>> statusbar.unhide()

To change the background color of status bar::

    >>> from plyer import statusbar
    >>> statusbar.change_color()

'''


class StatusBar(object):
    '''
    Status Bar facade.
    '''

    def hide(self):
        '''
        Hide the status bar.
        '''
        return self._hide()

    def unhide(self):
        '''
        Unhide the status bar.
        '''
        return self._unhide()

    def change_color(self):
        '''
        Change the background color of status bar.
        '''
        return self._change_color()

    #private

    def _hide(self):
        raise NotImplementedError()

    def _unhide(self):
        raise NotImplementedError()

    def _change_color(self):
        raise NotImplementedError()
