#!/usr/bin/env python

# this is a prompt library written by @lintuxt to enhance some scripts

class Prompt:
  def __init__(self, prompt_string = ':) ', not_executed_cb = None):
    self.__exit = False
    self.__cmd = ''
    self.__callbacks = []
    self.__executed = False
    self.__prompt_string = prompt_string
    self.__not_executed_cb = not_executed_cb
    self.__disabled_commands = ['exit', '', '\n']
  def register_callback(self, cmd, callback):
    if(not(cmd in self.__disabled_commands)):
      self.__callbacks.append([cmd, callback])
  def run(self):
    while(not(self.__exit) and self.__cmd != 'exit'):
      self.__cmd = raw_input(self.__prompt_string)
      for (cmd, callback) in self.__callbacks:
        if cmd == self.__cmd:
          self.__executed = True
          callback()
          break
      if(self.__cmd in self.__disabled_commands):
        self.__executed = True
      if(not(self.__executed) and self.__not_executed_cb != None):
        self.__not_executed_cb()
      self.__executed = False
