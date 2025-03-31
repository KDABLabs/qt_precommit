#!/usr/bin/env python3

"""A pre-commit wrapper for Qt tools."""

import configparser
import os
import shutil


def get_qt_path(config):
    """Get the Qt path from the configuration file."""
    if "Qt" in config:
        qt_config = config["Qt"]
        if "path" in qt_config:
            return qt_config["path"]
    return None


def find_tool(tool_name, config):
    """Find the specified Qt tool in the configured paths."""
    return shutil.which(tool_name, path=get_qt_path(config))


def load_config(config_path):
    """Load the configuration file."""
    config = configparser.ConfigParser()
    if os.path.isfile(config_path):
        with open(config_path, "r") as config_file:
            config.read_file(config_file)
    return config
