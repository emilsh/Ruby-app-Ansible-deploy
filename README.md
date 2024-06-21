# Ansible: Ruby Application Deployment with Nginx Load Balancer

This Ansible role automates the deployment and management of a Ruby on Rails application called xpaste_practicum on CentOS 7 servers, using Nginx as a reverse proxy and load balancer. It includes tasks for installing dependencies, deploying the application code, configuring Nginx, and starting the application service.

## Features

- Installs and configures Postgres server.
- Installs nodejs.
- Installs necessary build dependencies and Ruby-related packages.
- Deploys the Ruby on Rails application code.
- Configures Nginx as a reverse proxy to balance traffic to the application servers.
- Sets up systemd service for the Ruby application.
- Manages application environment variables securely.

## Requirements

- Target servers must be running CentOS 7.
- Ansible 2.9 or higher installed on the control node.
- Access to the Internet or local package repository for package installation.

## Run the playbook:
ansible-playbook playbook.yml

## Access your application:
Once deployed, your Ruby application should be accessible via the Nginx load balancer. Adjust your DNS or host file accordingly.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please submit an issue or a pull request.
