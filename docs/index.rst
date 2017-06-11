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

    .. attribute:: getInfo()
    
        Used to get the set info for the plugin

        *Returns: * [``name``,``version``,``author``]

    .. attribute:: getLogger()
    
         Used to get the Logger for the Bot

        *Returns: :class: 'Logger'
     


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


