#!/usr/bin/env python

# this is a sorting library written by @lintuxt to enhance some scripts

class Sort:
  def __init__(self, key):
    self.__key = key
  def __get_key(self, item):
    return item[self.__key]
  def sortList(self, list):
    return sorted(list, key=self.__get_key)
