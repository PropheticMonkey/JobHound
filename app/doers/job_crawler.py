

from app.models.job_profile import JobProfile
from app.models.job_opportunity import JobOpportunity

class JobCrawler():
#takes a job profile, crawls known job sources and returns a list of qualified leads.

    def __init__(self):
        self.state = "new"