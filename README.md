# CondaEnvManager

**CondaEnvManager** is a Python script that automates the process of creating and activating Conda virtual environments based on the current directory name. If a `requirements.txt` file is present, the script will also install the necessary packages. This tool simplifies environment management, making it easy for developers to quickly set up and work within Conda environments.

![image](https://github.com/user-attachments/assets/cce18f01-c84a-4295-b1d9-2820b3f7c3e1)

## Features

- **Automatic Environment Creation**: Automatically creates a Conda environment using the current directory name.
- **Package Installation**: Installs required packages from `requirements.txt` if it exists in the directory.
- **Environment Selection & Activation**: If the environment already exists, it lists available Conda environments for easy selection and activation.

## Getting Started

### Prerequisites

Before using CondaEnvManager, ensure the following are installed:

- **Anaconda or Miniconda**: Conda must be installed, and the `conda` command should be available in your system's PATH.
- **Python 3.6 or higher**: The script is written in Python 3 and requires version 3.6 or above.
- **A `requirements.txt` file** (optional): Lists packages to be installed in the virtual environment (if needed).

### Installation

1. **Clone the Repository**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/adalgu/CondaEnvManager.git
   cd CondaEnvManager
   ```

2. **Run the Script**

   Execute the script to create and activate a Conda environment:

   ```bash
   ./setup_env.py
   ```

   This will automatically create a Conda environment with the current directory name and install dependencies from `requirements.txt` if available.

## Usage

### Environment Creation and Activation

1. The script checks if a Conda environment with the current directory name already exists.
2. If the environment exists, it lists all available Conda environments, allowing you to select and activate one.
3. If the environment doesn't exist, it creates a new one using Python 3.8 and installs any dependencies listed in `requirements.txt`.
4. Finally, it displays the command to manually activate the environment.

### Example Workflow

1. Clone the repository into your project directory.
2. Run the script using `./setup_env.py`.
3. Follow the prompts to either activate an existing environment or create a new one.
4. After the environment is set up, manually activate it with:

   ```bash
   conda activate <env_name>
   ```

## Notes

- The script is compatible with both Windows and Unix-based systems.
- After the script finishes, you will need to manually activate the environment, as Python scripts cannot persistently change environments across sessions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
