"""Core pipeline class."""

from typing import List

from kalam.jobs import Job
from .runner import Runner


class Pipeline:
    """Constructs a pipeline."""

    jobs: List[Job] = []
    runner: Runner = None

    def add_job(self: "Pipeline", job: Job) -> None:
        """Add a job to the pipeline.

        Use this method to add jobs to the pipeline in sequence.

        Args:
            job: Job object.
        """
        self.jobs.append(job)

    def run(self: "Pipeline") -> None:
        """Executes the pipeline."""
        for job in self.jobs:
            try:
                self.runner.execute(job)
            except BaseException:
                # TODO: handle exceptions cleanly later.
                pass
