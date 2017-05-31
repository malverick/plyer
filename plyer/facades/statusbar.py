class StatusBar(object):
    '''
    Status Bar facade.
    '''

    def hide(self):
        return self._hide()

    def change_color(self):
        return self._change_color()

    #private

    def _hide(self):
        raise NotImplementedError()

    def _change_color(self):
        raise NotImplementedError()
