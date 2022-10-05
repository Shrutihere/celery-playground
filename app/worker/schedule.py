from datetime import datetime, timedelta
from json import dumps


class CancelSchedule(Exception):
    """When raised by the task function, the next run is not scheduled.
    This is analogous to StopIteration in iterators."""
    pass


class TaskScheduler(object):
    """Task scheduler class."""

    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    @classmethod
    def strftime(cls, _datetime):
        """Returns the datetime representation in string according to
        TaskScheduler.DATE_FORMAT format.

        Arguments:
            _datetime (datetime): Datetime instance.

        Returns:
            str: Formatted datetime string.
        """
        return _datetime.strftime(cls.DATE_FORMAT) if _datetime else None


    @classmethod
    def strptime(cls, _datetime_string):
        """Returns a datetime instance from its string format. The
        string format should be same as TaskScheduler.DATE_FORMAT.

        Arguments:
            _datetime_string (datetime): Formatted datetime string.

        Returns:
            datetime: Datetime instance.
        """
        return datetime.strptime(_datetime_string, cls.DATE_FORMAT) if _datetime_string else None

    @staticmethod
    def schedule(func, description, args=None, kwargs=None, rrule_string=None,
                 trigger_at=None, until=None):
        """Schedules a task based on the schedule rules.

        Arguments:
            func (function): Function to run on schedule.
            description (str): Task description.
            args (list): Optional. Arguments to be passed to the
                function. All values must be JSON serializable.
            kwargs (dict): Optional. Keyword arguments to be passed to
                the function. All values must be JSON serializable.
            rrule_string (str): Optional. RRule string. If not
                specified, the task will be executed just once.
            trigger_at (datetime): Optional. Sets the schedule for the
                first run. If not specified, task is executed immediately.
            until (datetime): Optional. Sets the end of schedule and
                tasks won't be executed after this time. If not
                specified, tasks will run as long as the rrule permits.

        Returns:
            uuid: Scheduled task ID.
        """

        now = datetime.utcnow() + timedelta(seconds=1)
        # _trigger_at = trigger_at or now
        if rrule_string and rrule_string.dtstart:
            rrule_string = rrule_string.dict()
            _trigger_at =  datetime.utcfromtimestamp(int(rrule_string.get("dtstart", None)))
        else:
            _trigger_at = now


        kwargs = kwargs or dict()
        kwargs.update({
            # 'scheduled_task_id': scheduled_task.id,
            'rrule_string': rrule_string,
            'first_eta': TaskScheduler.strftime(_trigger_at),
            'eta': TaskScheduler.strftime(_trigger_at),
            'until': TaskScheduler.strftime(until),
        })

        scheduled_task_id = func.apply_async(eta=_trigger_at, args=args, kwargs=kwargs)
        return scheduled_task_id

    # @staticmethod
    # def cancel(scheduled_task_id):
    #     """Cancels the scheduled task.

    #     Arguments:
    #         scheduled_task_id (uuid): Scheduled Task ID.

    #     Returns:
    #         ScheduledTask: Scheduled task instance.
    #     """
    #     scheduled_task = ScheduledTask.objects.get(pk=scheduled_task_id)
    #     scheduled_task.save_status(ScheduledTask.STATUS_CANCELLED)
    #     return scheduled_task

    @staticmethod
    def calculate_next_eta(rrule_=None, current_eta=None):
        """Calculates the next datetime in the sequence generated by
        the rrule string.

        Arguments:
            rrule_ (rrule): Optional. RRule instance.
            current_eta (datetime): Optional. Timezone-aware datetime
                object of the current datetime.

        Returns:
            datetime: Timezone-aware datetime object of the next
                datetime. If no suitable datetime is found, the
                function returns None.
        """

        # In most of the quick delay tasks, there won't be any. Skip
        # finding the datetime.
        if not rrule_:
            return

        # If the task never executed, return the first datetime in the
        # sequence. Else fetch the first datetime greater than the
        # current datetime.
        for _datetime in rrule_:
            if not current_eta:
                return _datetime

            if _datetime > current_eta:
                return _datetime