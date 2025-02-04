#!/usr/bin/env python
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2021 The Amoni project team members listed at
# https://github.com/anvilistas/amoni-cookiecutter/graphs/contributors
#
# This software is published at https://github.com/anvilistas/amoni-cookiecutter

import shutil


def main():
    """Post project generation hook"""
    # Copy env.template to .env
    shutil.copy("env.template", ".env")


if __name__ == "__main__":
    main()
