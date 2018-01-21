# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 18:13:39 2018

@author: Kevin
"""
import urllib2
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        else:
            response = urllib2.urlopen(url)
            if(response.getcode() == 200):
                print "download success"
                return response.read()
            else:
                print "download failed"
                return None