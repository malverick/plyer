'''
Sharing
=======

This API focuses on sharing data with different apps. For example, the built-in
Browser app can share the URL of the currently-displayed page as text with any
application. This is useful for sharing an article or website with friends via
email or social networking.

The :class:`Sharing` provides access to public methods to share data with
different apps in your device.

Simple Examples
===============

To share text::

    >>> from plyer import sharing
    >>> sharing.share_text(text)
    # A window will open asking the user to choose the app with which he wants
    to share the data.

'''


class Sharing(object):
    '''
    Sharing facade.
    '''

    def share_text(self, text):
        '''
        Share the text with different apps.

        :param text: Data to share
        :type text: String
        '''
        return self._share_text(text)

    def share_img(self):
        '''
        Share the image with different apps.
        '''
        return self._share_img()

    #private

    def _share_text(self, text):
        raise NotImplementedError()

    def _share_img(self):
        raise NotImplementedError()
