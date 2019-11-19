# AnswerIQ Confidential and Proprietary
import os.path
import sys
from fabric.api import task, local

import tasks.migration as migration
import tasks.server as server
import tasks.db as db


@task(default="true")
def run_all():
    local("fab migration.run")
    local("fab migration.wait")

# Hax:

# We should be able to run fabric tasks even if the codebase is broken
# (bad imports, syntax errors). For that to work, we must import the
# code lazily in each fab task, as required.

# UNFORTUNATELY, fabric wraps tasks; wrapped tasks have a closure of
# __file__ but do NOT have the same path; we can't import local files
# inside of tasks. This awful thing modifies the path to include our
# project root directory -- to allow lazy importing.

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
