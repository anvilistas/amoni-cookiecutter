#!/usr/bin/env python
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2021 The Amoni project team members listed at
# https://github.com/anvilistas/amoni-cookiecutter/graphs/contributors
#
# This software is published at https://github.com/anvilistas/amoni-cookiecutter

import os
import secrets
import string
import uuid

import yaml


def generate_uplink_key(prefix=""):
    """Generate a unique key using UUID4 (random UUID)"""
    # UUID4 provides 122 bits of randomness
    unique_id = str(uuid.uuid4()).replace("-", "").upper()
    return f"{prefix}{unique_id}"


def generate_secure_password():
    """Generate a secure random password that's safe for database connection strings.

    The password will:
    - Be 32 characters long
    - Include uppercase letters, lowercase letters, numbers
    - Include only safe special characters: .-_=+!*$
    - Have at least one character from each category
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    safe_special = ".-_=+!*$"

    # Ensure at least one from each set
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(safe_special),
    ]

    # Fill the rest with a mix of all allowed characters
    allowed_chars = lowercase + uppercase + digits + safe_special
    password.extend(secrets.choice(allowed_chars) for _ in range(28))

    # Shuffle the password characters
    shuffled = list(password)
    secrets.SystemRandom().shuffle(shuffled)

    return "".join(shuffled)


def create_env_file():
    """Create .env file with secure credentials"""
    # Read the template
    with open("env.template", "r") as f:
        env_content = f.read()

    # Generate secure credentials
    replacements = {
        "POSTGRES_PASSWORD=anvil": f"POSTGRES_PASSWORD={generate_secure_password()}"
    }

    # Replace placeholders with secure values
    for old, new in replacements.items():
        env_content = env_content.replace(old, new)

    # Write the .env file
    with open(".env", "w") as f:
        f.write(env_content)


def update_config_yaml():
    """Update config.yaml with secure uplink keys"""
    config_path = os.path.join("app", "config.yaml")

    # Read the current config
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    # Update uplink keys
    config["uplink-key"] = generate_uplink_key("server_")
    config["client-uplink-key"] = generate_uplink_key("client_")

    # Write back to config.yaml
    with open(config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False)


def main():
    """Post project generation hook"""
    create_env_file()
    update_config_yaml()


if __name__ == "__main__":
    main()
