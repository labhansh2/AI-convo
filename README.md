# AI-Convo [Bing and Bard]

Had this idea of making bard and bing communicate with each other. Found it
nowhere so made it.

## Requirements

-   Python 3.8 or higher
-   A Microsoft account with access to https://bing.com/chat (required)
-   Checking access (required)
-   Latest version of Microsoft Edge installed
-   Cookie editor extension for Edge [You can get it here :
    https://tinyurl.com/4an6m8rs]

## Installation

1. Clone the repository:

    `git clone https://github.com/labhansh2/AI-convo.git`

2. Follow the steps from
   [Getting Started](https://github.com/labhansh2/AI-convo#getting-started)

3. Install the required dependencies:

    `pip install -r requirements.txt`

Note: You may need to install pip if you don't already have it installed.

## Getting Started

1. Open https://bing.com/chat and check if you have access to the chat feature.
2. If you have access, proceed to getting authentication.
3. Install the cookie editor extension for Chrome or Firefox.
4. Go to bing.com and open the extension.
5. Click "Export" on the bottom right, then "Export as JSON" (this saves your
   cookies to clipboard).
6. Paste your cookies into a file called "cookies.json".
7. Go to https://bard.google.com/
8. F12 for console
9. Session: Go to Application → Cookies → \_\_Secure-1PSID. Copy the value of
   that cookie.
10. Paste it in .env.template file and rename the file as .env

you are good to go for installation

## Usage

To run the main program, navigate to the project directory and run:

`python main.py`

This will start the program and you can simply enjoy.

### Also

-   You can change the initializing message to bard from .env file.
-   the conversation between AIs is being saved in the chat_logs directory
-   The "\_Secure-1PSID" can change, check the expiry where you find it

Have fun!!
