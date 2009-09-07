#!/usr/bin/env python

import sys
import os
import nanotron
import irc
import dispatcher
                                  
class TronError(Exception):
  pass

try:
    my_nanotron = nanotron.Nanotron()
    dispatcher = dispatcher.Dispatcher(my_nanotron)
    ircbot = irc.IRCBot(dispatcher)
    dispatcher.run()
    ircbot.start()
    dispatcher.shutdown()
    
except KeyboardInterrupt as e:
  ircbot.disconnect("Shutdown initiated by Ctrl+C")
  dispatcher.shutdown()
  
except TronError as e:
  print e
