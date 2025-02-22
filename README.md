# SSH BeARacer

A Python library for managing SSH connections and automating remote deployments.

## Introduction

**SSH Deployer** simplifies the process of managing SSH connections, executing remote commands, and deploying applications to remote servers. It's a handy tool for developers looking to automate deployment workflows.

## Features

- **Secure SSH Connection Management**: Easily establish and manage SSH connections.
- **Local and Remote Command Execution**: Execute commands locally or on remote servers.
- **Automated Deployment**: Automate build and deployment processes.
- **Easy Integration**: Seamlessly integrates into existing CI/CD pipelines.

## Installation

Install the library via `pip`:

```bash
pip install ssh-bearacer
```

## Usage

Here’s an example of how to use **SSH Deployer** in your project:

```python
from ssh_deployer.manager import DeploymentManager

ssh_config = {
    "ssh_host": "your_remote_host",
    "ssh_port": 22,
    "ssh_username": "your_username",
    "ssh_key": "~/.ssh/id_rsa",
}

deployment_manager = DeploymentManager(ssh_config=ssh_config)
deployment_manager.run(
    local_commands=[
        "git checkout develop",
        "git pull origin develop",
        "bun run build",
        "rsync -avP .output user@remote_host:~/app_directory",
    ],
    remote_commands=[
        "cd app_directory",
        "docker-compose up -d --build",
        "yes | docker system prune",
    ],
)
```

### Components Overview

- **SSHConnectionManager**: Handles secure SSH connections and tunnel establishment.
- **CommandExecutor**: Executes commands locally or on remote servers.
- **RemoteBuilder**: Manages application deployment on remote servers.
- **DeploymentManager**: Orchestrates the entire deployment process, from build to deployment.

## Contribution

We welcome contributions from the community. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request for review.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or feedback, feel free to reach out via email: [duynn100198@gmail.com](mailto:duynn100198@gmail.com).

## References

- [Paramiko Documentation](https://www.paramiko.org/)
- [sshtunnel Documentation](https://sshtunnel.readthedocs.io/)