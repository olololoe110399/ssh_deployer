import logging
from ssh_deployer.manager import DeploymentManager

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def main():
    ssh_config = {
        "ssh_host": "example.com",
        "ssh_port": 22,
        "ssh_username": "ubuntu",
        "ssh_key": "~/.ssh/id_rsa",
    }

    deployment_manager = DeploymentManager(ssh_config=ssh_config)
    deployment_manager.run(
        local_commands=[
            "echo Local Command 1",
            "echo Local Command 2",
        ],
        remote_commands=[
            "echo Remote Command 1",
            "echo Remote Command 2",
        ],
    )


if __name__ == "__main__":
    main()
