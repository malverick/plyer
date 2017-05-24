'''
Broadcast
=========

Broadcasts or In App Notifocations are notifications send by an app which are
displayed when the user is active within the app itself.

The :class:`Broadcast` provides access to public methods to send and receive
in app notifications in your app itself.

Simple Examples
===============

To send a broadcast message::

    >>> from plyer import broadcast
    >>> broadcast.send()

To receive broadcast messsage::

    >>> from plyer import broadcast
    >>> broadcast.receive()

'''


class Broadcast(object):
    '''
    Broadcast facade.
    '''

    def send(self):
        '''
        Send broadcast to receiver.
        '''
        return self._send()

    def recieve(self):
        '''
        Register a broadcast receiver to receive notifications from other
        applications or the system itself.
        '''
        return self._receive()

    #private

    def _send(self):
        raise NotImplementedError()

    def _receive(self):
        raise NotImplementedError()
