'''
In App Browser
==============

The in app browser displays the interactive web content within your app for the
given URL. It is a browser bundled inside your application.

The :class:`InAppBrowser` provides access to public methods to use in app
browser in your app.

Simple Examples
---------------

To loan a page with a given url::

	>>> from plyer import inappbrowser
	>>> inappbrowser.load_page(url)

To reload the current page::

	>>> from plyer import inappbrowser
	>>> inappbrowser.reload()

To go back in the history::

	>>> from plyer import inappbrowser
	>>> inappbrowser.go_back()

To go forward in the history::

	>>> from plyer import inappbrowser
	>>> inappbrowser.go_forward()

'''


class InAppBrowser(object):
    '''
    In App Browser facade.
    '''

    def load_page(self, url):
    	'''
    	Loads the given URL.
    	'''
        return self._load_page()

    def reload(self):
    	'''
    	Reload the current page.
    	'''
        return self._reload()

    def go_back(self):
    	'''
    	Go back in the history of current session.
    	'''
        return self._go_back()

    def go_forward(self):
    	'''
    	Go forward in the history of current session.
    	'''
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
