#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import time
import logging
logger = logging.getLogger('ROOT')

class Watchdog(threading.Thread):
    def __init__(self, thread_id, job_params):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.job_id = job_params['job_id']
        self.job_state = job_params['job_state']
        self.job_start_time = job_params['job_start_time']
        self.run_event = job_params['run_event']

    def run(self):
        logger.info("Starting {}".format(self.thread_id))
        while self.run_event.is_set():
            self.trigger_event()
            self.job_state = "RUNNING"
            time.sleep(1)
        logger.info("Exiting thread: {} for Job ID: {}".format(self.thread_id, self.job_id))

    def trigger_event(self):
        msg = {
                "thread_id": self.thread_id,
                "job_id": self.job_id,
                "state": self.job_state,
                "start_time": self.job_start_time
            }
        logger.info(msg)