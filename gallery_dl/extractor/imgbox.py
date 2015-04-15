# -*- coding: utf-8 -*-

# Copyright 2014, 2015 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extract images from galleries at http://imgbox.com/"""

from .common import AsynchronousExtractor, Message
import re

info = {
    "category": "imgbox",
    "extractor": "ImgboxExtractor",
    "directory": ["{category}", "{title} - {gallery-key}"],
    "filename": "{num:>03}-{name}",
    "pattern": [
        r"(?:https?://)?(?:www\.)?imgbox\.com/g/(.+)",
    ],
}

class ImgboxExtractor(AsynchronousExtractor):

    url_base = "http://imgbox.com"

    def __init__(self, match, config):
        AsynchronousExtractor.__init__(self, config)
        self.key = match.group(1)
        self.metadata = {}

    def items(self):
        page = self.request(self.url_base + "/g/" + self.key).text
        self.metadata = self.get_job_metadata(page)
        yield Message.Version, 1
        yield Message.Directory, self.metadata
        for match in re.finditer(r'<a href="([^"]+)"><img alt="', page):
            text = self.request(self.url_base + match.group(1)).text
            yield Message.Url, self.get_file_url(text), self.get_file_metadata(text)

    def get_job_metadata(self, page):
        """Collect metadata for extractor-job"""
        match = re.search(r"<h1>(.+) \(([^ ]+) ([^ ]+) \w+\) - (\d+)", page)
        return {
            "category": info["category"],
            "gallery-key": self.key,
            "title": match.group(1),
            "date": match.group(2),
            "time": match.group(3),
            "count": match.group(4),
        }

    def get_file_metadata(self, text):
        """Collect metadata for a downloadable file"""
        data = self.metadata.copy()
        data["num"]      , pos = self.extract(text, '</a> &nbsp; ', ' of ')
        data["image-key"], pos = self.extract(text, '/i.imgbox.com/', '?download', pos)
        data["name"]     , pos = self.extract(text, ' title="', '"', pos)
        return data

    def get_file_url(self, text):
        """Extract download-url"""
        base = "http://i.imgbox.com/"
        path, _ = self.extract(text, base, '"')
        return base + path