#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""test for FileBrowser"""
import unittest

from learnForIO.IOSample import FileBrowser

__author__ = 'Paul yang'

class testFor_FileBrowser(unittest.TestCase):
    def test_FileBrowserInit_noParameterInput_success(self):
        file = FileBrowser()
        self.assertEqual(file.filePath,'')

    def test_FileBrowserInit_correctFilePathInput_success(self):
        file = FileBrowser(r'C:\\')
        self.assertEqual(file.filePath,r'C:\\')


if __name__ == '__main__':
    unittest.main()