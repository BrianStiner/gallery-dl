Configuration
#############

Contents
========

1) `General Options`_
2) `Output Options`_
3) `Downloader Options`_
4) `Extractor Options`_
5) `Extractor-specific Options`_


General Options
===============

base-directory
--------------
=========== =====
Type        ``string``
Default     ``"./gallery-dl/"``
Description Directory path used as the base for all download destinations.
=========== =====


cache.file
----------
=========== =====
Type        ``string``
Default     ``tempfile.gettempdir() + ".gallery-dl.cache"``
Description Path of the SQLite3 database used to cache login sessions,
            smaller cookies and API tokens.

            Set this value to an invalid path or simply ``null`` to disable
            this cache.
=========== =====


Output Options
==============

output.mode
-----------
=========== =====
Type        ``string``
Default     ``"auto"``
Description Controls the output string format and status indicators.

            * ``"null"``: No output
            * ``"pipe"``: Suitable for piping to other processes or files
            * ``"terminal"``: Suitable for the standard Windows console
            * ``"color"``: Suitable for terminals that understand ANSI escape codes and colors
            * ``"auto"``: Automatically choose the best suitable output mode
=========== =====


output.shorten
--------------
=========== =====
Type        ``bool``
Default     ``"true"``
Description Controls whether the output strings should be shortened to fit
            on one console line.
=========== =====

output.progress
---------------
=========== =====
Type        ``bool`` or ``string``
Default     ``true``
Description Controls the progress indicator when ``gallery-dl`` is run with
            multiple URLs as arguments.

            * ``true``: Show the default progress indicator
              (``"[{current}/{total}] {url}"``)
            * ``false``: Do not show any progress indicator
            * Any ``string``: Show the progress indicator using this
              as a custom `format string`_. Possible replacement keys are
              ``current``, ``total``  and ``url``.
=========== =====


Downloader Options
==================

downloader.http.retries
-----------------------
=========== =====
Type        ``integer``
Default     ``5``
Description Number of times a failed download is retried before giving up.
=========== =====


downloader.http.timeout
-----------------------
=========== =====
Type        ``float`` or ``null``
Default     ``null``
Description Amount of time (in seconds) to wait for a successful connection
            and a response from a remote server.

            This value gets internally used as the ``timeout`` parameter for the
            `requests.get()`_ method.
=========== =====


Extractor Options
=================

extractor.*.filename
--------------------
=========== =====
Type        ``string``
Example     ``"{manga}_c{chapter}_{page:>03}.{extension}"``
Description A `format string`_ to build the resulting filename
            for a downloaded file.
=========== =====


extractor.*.directory
---------------------
=========== =====
Type        ``list`` of ``strings``
Example     ``["{category}", "{manga}", "c{chapter} - {title}"]``
Description A list of `format strings`_ for the resulting target directory.
=========== =====


extractor.*.skip
----------------
=========== =====
Type        ``bool`` or ``string``
Default     ``true``
Description Controls the behavior when downloading a file whose filename
            already exists.

            * ``true``: Skip the download
            * ``false``: Overwrite the already existing file
            * ``"abort"``: Abort the current extractor run
            * ``"exit"``: Exit the program altogether
=========== =====


extractor.*.username
--------------------
=========== =====
Type        ``string``
Default     ``null``
Description The username to use when attempting to log in to another site.

            This value is required for the ``pixiv``, ``nijie`` and ``seiga``
            modules and optional (but strongly recommended) for ``batoto`` and
            ``exhentai``.

            This value can also be specified via the ``-u/--username``
            command-line option (see Authentication_)
=========== =====


extractor.*.password
--------------------
=========== =====
Type        ``string``
Default     ``null``
Description The password belonging to the username.
=========== =====


Extractor-specific Options
==========================

extractor.deviantart.mature
---------------------------
=========== =====
Type        ``bool``
Default     ``true``
Description Enable mature content.

            This option simply sets the ``mature_content`` parameter for API
            calls to either ``"true"`` or ``"false"`` and does not do any other
            form of content filtering.
=========== =====


extractor.exhentai.original
---------------------------
=========== =====
Type        ``bool``
Default     ``true``
Description | Always download the original image or
            | download the down-sampled version for larger images.
=========== =====


extractor.exhentai.wait-min
---------------------------
=========== =====
Type        ``float``
Default     ``3.0``
Description Minimum wait time in seconds between each image

            Exhentai detects and blocks automated downloaders.
            ``gallery-dl`` waits a randomly selected number of
            seconds between ``wait-min`` and ``wait-max`` after
            each image to prevent getting blocked.
=========== =====


extractor.exhentai.wait-max
---------------------------
=========== =====
Type        ``float``
Default     ``6.0``
Description Maximum wait time in seconds
=========== =====


extractor.exhentai.cookies
---------------------------
=========== =====
Type        ``object``
Default     ``null``
Description
=========== =====


extractor.flickr.access-token
-----------------------------
=========== =====
Type        ``string``
Default     ``null``
Description The ``access_token`` value you get from linking your Flickr account
            to ``gallery-dl``.
=========== =====


extractor.flickr.access-token-secret
------------------------------------
=========== =====
Type        ``string``
Default     ``null``
Description The ``access_token_secret`` belonging to the ``access_token``.
=========== =====


extractor.flickr.metadata
-------------------------
=========== =====
Type        ``bool``
Default     ``false``
Description Load additional metadata when using the single-image extractor.
=========== =====


extractor.gfycat.format
-----------------------
=========== =====
Type        ``string``
Default     ``"mp4"``
Description The name of the preferred animation format, which can be one of
            ``"mp4"``, ``"webm"``, ``"gif"``, ``"webp"`` or ``"mjpg"``.

            If the selected format is not available, ``"mp4"``, ``"webm"``
            and ``"gif"`` (in that order) will be tried instead, until an
            available format is found.
=========== =====


extractor.imgur.mp4
-------------------
=========== =====
Type        ``bool`` or ``string``
Default     ``true``
Description Controls whether to choose the GIF or MP4 version of an animation

            * ``true``: Follow Imgur's advice and only choose MP4 if the
              ``prefer_video`` flag in an image's metadata is set.
            * ``false``: Always choose GIF
            * ``"always"``: Always choose MP4
=========== =====


extractor.pixiv.ugoira
----------------------
=========== =====
Type        ``bool``
Default     ``true``
Description Download Pixiv's Ugoira animations or ignore them.

            These animations come as a ``.zip`` file containing all the single
            animation frames in JPEG format.
=========== =====


extractor.reddit.comments
-------------------------
=========== =====
Type        ``integer`` or ``string``
Default     ``200``
Description The value of the ``limit`` parameter when loading
            a submission and its comments.
            This number (roughly) specifies the total amount of comments
            being retrieved with the first API call.

            Reddit's internal default and maximum values for this parameter
            appear to be 200 and 500 respectively.

            The value `0` ignores all comments and significantly reduces to time
            required when scanning a subreddit.
=========== =====


extractor.reddit.date-min
-------------------------
=========== =====
Type        ``integer`` (UTC timestamp)
Default     ``0``
Description Ignore all submissions posted before this timestamp.
=========== =====


extractor.reddit.date-max
-------------------------
=========== =====
Type        ``integer`` (UTC timestamp)
Default     ``253402210800`` (timestamp of ``datetime.max``)
Description Ignore all submissions posted after this timestamp.
=========== =====


extractor.reddit.recursion
--------------------------
=========== =====
Type        ``integer``
Default     ``0``
Description Reddit extractors can recursively visit other submissions
            linked to in the initial set of submissions.
            This value sets the maximum recursion depth.

            Special values:

            * ``0``: Recursion is disabled
            * ``-1``: Infinite recursion (don't do this)
=========== =====


extractor.reddit.refresh-token
------------------------------
=========== =====
Type        ``string``
Default     ``null``
Description The ``refresh_token`` value you get from linking your Reddit account
            to ``gallery-dl``.
=========== =====


.. _`requests.get()`: http://docs.python-requests.org/en/latest/user/advanced/#timeouts
.. _format string:    https://docs.python.org/3/library/string.html#formatstrings
.. _format strings:   https://docs.python.org/3/library/string.html#formatstrings
.. _Authentication:   https://github.com/mikf/gallery-dl#5authentication