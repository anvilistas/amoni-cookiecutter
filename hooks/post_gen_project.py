#!/usr/bin/env python
import shutil


def main():
    """Post project generation hook"""
    # Copy env.template to .env
    shutil.copy('env.template', '.env')


if __name__ == '__main__':
    main()
