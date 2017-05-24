class Broadcast(object):
    '''
    Broadcast facade.
    '''

    def send(self):
        return self._send()

    def recieve(self):
        return self._receive()

    #private

    def _send(self):
        raise NotImplementedError()

    def _receive(self):
        raise NotImplementedError()
