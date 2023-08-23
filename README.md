# Fitness Telegram Bot
A Telegram bot built with Python that allow you to track your gym progress.
## Description
The Telegram Fitness Bot is designed to help users track their progress at the gym
This bot is built in Python and integrated with the Telegram Bot API.
## Features
- Allows you to choose trainer or athlete mode
- Check progress in the gym
- Provide feedback on the level of progress
- Easy to set up and use
- You can view the database of athletes
- Ability to create a training program
## Installation
* You must have an SSH key generated before executing the commands
1. Clone the repository:
   ```shell
   git clone git@github.com:vladysllav/FitnessBot.git
   ```
   because of the firewall settings, the command may not work, then we use
   ```shell
   git clone https://github.com/vladysllav/FitnessBot.git
   ```
2. Install the required dependencies using Poetry:
  *Check if Poetry is installed
   ```shell
   poetry --version
   ```
   if installed, execute

   ```shell
   cd FitnessBot/src/ poetry install
   ```

   if not installed, execute
   ```shell
   curl -sSL https://install.python-poetry.org | python -
   ```
   then add poerty to the PATH variable
Copy the path to the folder with the installed poetry. It is listed in the installation output and looks something like this:
C:\Users\273C~1\AppData\Roaming\Python\Scripts # example (You will have a different address)
Open the Control Panel and go to "System" (System) > "Advanced system settings" (Advanced system settings).
Click on the "Environment Variables..." button.
In the "User variables for [your username]" section, find the "Path" variable and select it.
Click on the "Edit..." button.
In the Edit Environment Variable window, click the New button.
Paste the copied path to the folder with the installed poetry and click "OK".
Click "OK" in all windows to save changes.
You should now be able to use poetry from any folder on the command line.
Try running:
   ```shell
   poetry --version
   ``` 
   and 

   ```shell
   cd FitnessBot/src/ poetry install
   ``` 

3. Create a `.env` file based on the `.env.example` file:
   ```shell
   cd FitnessBot
   ```
   ```shell
   cp .env.example .env
   ```
   Update the `.env` file with your actual Telegram bot token.
## Usage
   To start the Fitness Telegram Bot, run the following command:
   ```shell
   cd FitnessBot/src/
   ```
   ```shell
   poetry shell
   ```
   ```shell
   python main.py
   ```
The bot will be up and running