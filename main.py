# -*- coding: utf-8 -*-

from scrapy.cmdline import execute
import sys
import os

projDir = os.path.dirname(os.path.abspath(__file__))
print("projDir: " + projDir)
sys.path.append(projDir)
execute(["scrapy", "crawl", "jobbole"])