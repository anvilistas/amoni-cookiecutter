# SPDX-License-Identifier: MIT
#
# Copyright (c) 2021 The Amoni project team members listed at
# https://github.com/anvilistas/amoni-cookiecutter/graphs/contributors
#
# This software is published at https://github.com/anvilistas/amoni-cookiecutter

from ._anvil_designer import StartupTemplate


class Startup(StartupTemplate):
    def __init__(self, **properties):
        self.init_components(**properties)
