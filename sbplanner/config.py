#/bin/python

"""
This module contains functions for config management.
"""

import os
import platform
import yaml

def to_full_path(path, subfolder, filename, create=False):
    """
    Parse a base directory; sub directory and a file for the correct string
    If create flag is set; it creates the leading directory 
    """
    if subfolder:
        path = os.path.join(path, subfolder)

    if create:
        os.makedirs(path, exist_ok=True)

    if filename:
        path = os.path.join(path, filename)

    return path

def get_home_path():
    """
    Expand the home directory path for the current user
    """
    try:
        path = os.path.expanduser('~')
    except Exception:
        path = ''

    if os.path.isdir(path):
        return path
    else:
        for env_var in ('HOME', 'USERPROFILE', 'TMP'):
            path = os.environ.get(env_var, '')
            if os.path.isdir(path):
                return path
            else:
                path = ''

        if not path:
            raise RuntimeError('HOME directory not found')

def get_config_path():
    """
    Return the default location to the config file
    """
    if platform.system() == 'Linux':
        # Try to expand XDG_CONFIG_HOME
        confpath = os.environ.get('XDG_CONFIG_HOME',
                to_full_path(get_home_path(), '.config'))
        if os.path.isdir(confpath):
            # Check if there is a non-subdirectory config to fall on
            if os.path.exists(to_full_path(confpath, filename='sbplanner.yaml')):
                confpath = to_full_path(confpath, filename='sbplanner.yaml')
            else:
                confpath = to_full_path(confpath, 'sbplanner', 'config.yaml')
        else:
            confpath = to_full_path(get_home_path, filename='.sbplanner.yaml')
    else:
        raise RuntimeError('Platform not supported')

class UserConfig():
    """
    UserConfig class; for storing configuration related to overall behavior.
    Runtime configuration options should not be here.
    Contains:
        path: Loaded from (and saved to) this file
        basedir: Where info files are located
    May contain:
        units: Unit choice (imperial vs standart)
            Internally; all calculations are made using SI units.
            This only should effect printing
    """
    def __init__(self, **vars):
        pass

    @classmethod
    def load_from_yaml(cls, fpath):
        pass





def getConfigLocation():

