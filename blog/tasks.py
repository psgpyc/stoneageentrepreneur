from celery.schedules import crontab
from celery.task import periodic_task
from blog.utils import update_featured_flag


@periodic_task(
    run_every=(crontab(minute=0, hour=0)),
    name="task_update_featured_flag",
    ignore_result=True
)
def task_update_featured_flag():
    """
    Updates the flags to 0 after reaching a threshold
    """
    update_featured_flag()
