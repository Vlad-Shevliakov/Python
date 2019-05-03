# -*- coding: utf-8 -*-

from __future__ import print_function

import inspect
import sys

from commands import (
    ListCommand,
    NewCommand,
    ExitCommand,
    # DoneCommand,
    # UndoneCommand,
    UserExitException,
)

from models import Storage
from utils import get_input_function


def get_routes():
    
    return {
        ListCommand.label(): ListCommand,
        NewCommand.label(): NewCommand,
        ExitCommand.label(): ExitCommand,
        # DoneCommand.label(): DoneCommand,
    }


def perform_command(command):

    command = command.lower()
    routes = get_routes()

    try:
        command_class = routes[command]
        command_inst = command_class()

        storage = Storage()
        command_inst.perform(storage.items)
    except KeyError:
        print('Bad command, try again.')
    except UserExitException as ex:
        print(ex)
        raise


def parse_user_input():
    
    input_function = input

    message = 'Input your command: (%s): ' % '|'.join(
        {
            ListCommand.label(): ListCommand,
            NewCommand.label(): NewCommand,
            ExitCommand.label(): ExitCommand,
            # DoneCommand.label(): DoneCommand,
        }.keys()
    )
    return input_function(message)


def main():
    
    # Ctrl+C

    while True:
        try:
            command = parse_user_input()
            perform_command(command)
        except UserExitException:
            break
        except Exception as e:
            print('You have done something wrong!', e)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Shutting down, bye!')
