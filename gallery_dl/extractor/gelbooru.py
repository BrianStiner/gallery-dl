# -*- coding: utf-8 -*-

# Copyright 2014, 2015 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extract image-urls from http://gelbooru.com/"""

from .booru import XMLBooruExtractor

info = {
    "category": "gelbooru",
    "extractor": "GelbooruExtractor",
    "directory": ["{category}", "{tags}"],
    "filename": "{category}_{name}",
    "pattern": [
        r"(?:https?://)?(?:www\.)?gelbooru\.com/(?:index\.php)?\?page=post&s=list&tags=([^&]+).*",
    ],
}

class GelbooruExtractor(XMLBooruExtractor):

    def __init__(self, match, config):
        XMLBooruExtractor.__init__(self, match, config, info)
        self.api_url = "http://gelbooru.com/"
        self.params = {"page":"dapi", "s":"post", "q":"index", "tags":self.tags}

    def update_page(self, reset=False):
        if reset is False:
            self.params["pid"] += 1
        else:
            self.params["pid"] = 0