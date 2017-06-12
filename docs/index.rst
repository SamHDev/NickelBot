.. NickelBot documentation master file, created by
   sphinx-quickstart on Sun Jun 11 11:00:47 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to NickelBot's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


==================
API
==================


.. currentmodule:: NickelBot

NickelBot:
------------------

.. class:: plugin(name,version)

    The main interface class for interacting with the API and Bot.
    
    **Parameters:**
    
         +----------+----------+-----------+-----------------------------------------------------------------+
         | Argument | Optional | Type      | Description                                                     |
         +==========+==========+===========+=================================================================+
         | name     | No       | String    | Used to define tha name of the plugin.                          |
         +----------+----------+-----------+-----------------------------------------------------------------+
         | version  | No       | String    | Set the Version Id of your Plugin.                              |
         +----------+----------+-----------+-----------------------------------------------------------------+
         | author   | Yes      | String    | Give the Api the plugin creator's name.                         |
         +----------+----------+-----------+-----------------------------------------------------------------+
         | desc     | Yes      | String    | Give a short Description of the plugin.                         |
         +----------+----------+-----------+-----------------------------------------------------------------+         

    .. function:: getInfo()
    
        Used to get the set info for the plugin

        *Returns*: [name,version]

    .. function:: getLogger()
    
         Used to get the Logger for the Bot

        *Returns*: :class: 'logger'
        
    .. function:: getConfig(args)
    
         Used to get the Config Manager for the Bot

        *Returns*: :class:`Config`
        
    .. function:: getCmd(command)
    
         Used to get the Config Manager for the Bot
         
         **Parameters:**
         
         +----------+----------+-----------+-----------------------------------------------------------------+
         | Argument | Optional | Type      | Description                                                     |
         +==========+==========+===========+=================================================================+
         | command  | No       | String    | The Name of the command that is being requested                 |
         +----------+----------+-----------+-----------------------------------------------------------------+

        *Returns*: :class:`Command` 
        
    .. function:: addEvent(event,function)
         
         Used to add an Event Listner
         
         **Parameters:**
         
         +----------+----------+------------------+----------------------------------------------------------+
         | Argument | Optional | Type             | Description                                              |
         +==========+==========+==================+==========================================================+
         | event    | No       | :class:`Event`   | The Event name                                           |
         +----------+----------+------------------+----------------------------------------------------------+
         | function | No       | function         | The function used when event invoked.                    |
         +----------+----------+------------------+----------------------------------------------------------+        
  
.. class:: logger

    .. function:: info(text)
        
        Use to send info to the bot logs
        
         +----------+----------+-----------+-----------------------------------------------------------------+
         | Argument | Optional | Type      | Description                                                     |
         +==========+==========+===========+=================================================================+
         | text     | No       | String    | The Text to Log                                                 |
         +----------+----------+-----------+-----------------------------------------------------------------+
        
    .. function:: note(text)
        
        Use to send info/note to the bot logs
        
         +----------+----------+-----------+-----------------------------------------------------------------+
         | Argument | Optional | Type      | Description                                                     |
         +==========+==========+===========+=================================================================+
         | text     | No       | String    | The Text to Log                                                 |
         +----------+----------+-----------+-----------------------------------------------------------------+

    .. function:: ok(text)
        
        Use to send a sucessfull event to the bot logs
        
         +----------+----------+-----------+-----------------------------------------------------------------+
         | Argument | Optional | Type      | Description                                                     |
         +==========+==========+===========+=================================================================+
         | text     | No       | String    | The Text to Log                                                 |
         +----------+----------+-----------+-----------------------------------------------------------------+

    .. function:: warn(text)
        
        Use to send an non-fatal eror to the bot logs
        
         +----------+----------+-----------+-----------------------------------------------------------------+
         | Argument | Optional | Type      | Description                                                     |
         +==========+==========+===========+=================================================================+
         | text     | No       | String    | The Text to Log                                                 |
         +----------+----------+-----------+-----------------------------------------------------------------+
         
     .. function:: error(text)
        
        Use to send a bad error to the bot logs
        
         +----------+----------+-----------+-----------------------------------------------------------------+
         | Argument | Optional | Type      | Description                                                     |
         +==========+==========+===========+=================================================================+
         | text     | No       | String    | The Text to Log                                                 |
         +----------+----------+-----------+-----------------------------------------------------------------+

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


