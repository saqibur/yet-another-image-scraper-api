from django.conf import settings
from django.core.management.base import BaseCommand

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger

from django_apscheduler import util
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler.jobstores import DjangoJobStore

from apps.image.api.v1.services import ScrapedImageService


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            ScrapedImageService.fetch_images_for_saved_urls(),
            trigger=CronTrigger(minute=settings.FETCH_URLS_FROM_SCRAPED_IMAGES_JOB_INTERVAL),
            id="fetch_images_for_scraped_urls",
            max_instances=1,
            replace_existing=True,
        )

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(day_of_week="mon", hour="00", minute="00"),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )

        try:
            print("Scheduler started")
            scheduler.start()
        except KeyboardInterrupt:
            scheduler.shutdown()
            print("Scheduler stopped")
            exit()
