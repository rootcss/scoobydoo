#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import scoobydoo
import logging
logger = logging.getLogger('ROOT')

class ExampleTask(scoobydoo.Job):
    def execute(self):
        logger.info("Executing your task.")
        logger.info("Sleeping for sometime..")
        time.sleep(10)

    def validation(self):
        pass

ExampleTask().run()