from .qt_precommit import find_tool, load_config

"""The command line interface for qt_precommit."""

import argparse
import subprocess


CONFIG_FILE_NAME = ".qt-precommit"


def qt_precommit_cli():
    """Command line interface for the pre-commit wrapper."""
    parser = argparse.ArgumentParser(
        description="Find a Qt tool in a configurable location and run it with input generated by pre-commit.")
    parser.add_argument(
        "-t", "--tool", help="The Qt tool to run")
    options, pre_commit_args = parser.parse_known_args()

    pre_commit_args = [a for a in pre_commit_args if a != "--"]

    config = load_config(CONFIG_FILE_NAME)

    tool = find_tool(options.tool, config)
    if not tool:
        print(f"Tool {options.tool} not found")
        exit(1)

    print(f"Found {options.tool} at: {tool}")
    output = subprocess.run([tool] + pre_commit_args)
    exit(output.returncode)
