class InAppBrowser(object):
    '''
    In App Browser facade.
    '''

    def load_page(self):
        return self._load_page()

    def reload(self):
        return self._reload()

    def go_back(self):
        return self._go_back()

    def go_forward(self):
        return self._go_forward()

    #private

    def _load_page(self):
        raise NotImplementedError()

    def _reload(self):
        raise NotImplementedError()

    def _go_back(self):
        raise NotImplementedError()

    def _go_forward(self):
        raise NotImplementedError()
