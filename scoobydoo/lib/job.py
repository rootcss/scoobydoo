#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import logging
import threading
import time
from scoobydoo.util import helper
from scoobydoo.lib import Watchdog

logger = logging.getLogger('ROOT')

class Job(object):
    def __init__(self):
        self.job_id = 'job_' + str(int(time.time()))
        self.job_state = 'STARTED'
        self.job_start_time = helper.timenow()
        self.job_name = self.__class__.__name__

    def _decorator(run):
        def magic(self) :
            self.__init__()
            self.__set_event_handler()
            self.__start_status_thread()
            run(self)
            self.__finish_threads()
        return magic

    @_decorator
    def run(self):
        self.execute()

    @abc.abstractmethod
    def execute(self):
        logger.warning("execute() was not defined in the child class.")

    @staticmethod
    def job_params(self):
        return {
            "job_id": self.job_id,
            "job_state": self.job_state,
            "job_start_time": self.job_start_time,
            "run_event": self.run_event
        }

    def __set_event_handler(self):
        self.run_event = threading.Event()
        self.run_event.set()

    def __start_status_thread(self):
        self.thread1 = Watchdog(1, self.job_params(self))
        self.thread1.start()

    def __finish_threads(self):
        logger.info("Job Done. Joining the hearbeat thread here..")
        self.run_event.clear()
        self.thread1.join()
        self.state = 'COMPLETED'
        msg = {
            "status": self.state,
            "timestamp": helper.timenow()
        }
        logger.info("{}".format(msg))