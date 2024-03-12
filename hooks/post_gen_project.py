#!/usr/bin/env python
import subprocess
from security import safe_command

safe_command.run(subprocess.run, ['git', 'init'])
