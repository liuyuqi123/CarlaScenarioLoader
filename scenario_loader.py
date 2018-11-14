#!/usr/bin/env python

# Copyright (c) 2018 Christoph Pilz
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import inspect
import os
import sys

from test_control import TestControl


def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "help":
            print(inspect.getfile(inspect.currentframe()) + " help - get this message")
            print(inspect.getfile(inspect.currentframe()) +
                  " <Carla> <OpenScenario> <OpenScenario-file> - for standard execution")
            exit()
        else:
            print("[Error] Wrong command line parameters, try: \"" +
                  inspect.getfile(inspect.currentframe()) + " help\"")
            exit()
    # TODO check later for > 5, for more scenarios ;)
    elif len(sys.argv) == 5:
            # check for Scenario-file
        if os.path.isfile(sys.argv[4]):
            # create TestControl class
            testControl = TestControl(sys.argv[1], sys.argv[2], 2000, 2.0, sys.argv[3])
            # try to load scenario-config
            if not testControl.setupTestWithConfig(sys.argv[4]):
                print("[Error] TestControl-Setup failed")
                exit()
            testControl.executeTest()
            # Simulation is built up
            # Simulation is executed
            testControl.cleanupTest()
            # Simulation environment is stopped

        else:
            print("[Error] third parameter has to be a valid filepath")
            exit()
    else:
        print("[Error] try \"" + inspect.getfile(inspect.currentframe()) + " help\"")


if __name__ == '__main__':

    main()
