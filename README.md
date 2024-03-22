# SchoolGPT
By victorAsksWhy

Made in 2024
## Description
SchoolGPT is a general-purpose AI powered assistant, but disallows use in schoolwork, generating a random
example instead. (This can be configured in the settings). It does this by either using AI or using a list of blacklisted words to detect if someone is using it for schoolwork. It was originally a submission to the 2024 SHS Hackathon, but the code is now available on GitHub. The executable was compiled using [PyInstaller](https://pyinstaller.org/en/stable/).
## Usage
### Setup
Download the latest release (.exe file) in the releases section. Or, if you prefer, get the python source code. If you use the executable, you should be all set. If you use the source code version, it requires python 3, as well as the openai module, so in the terminal run 
`pip install openai`
For both versions, you may need to set up an API key (Try it without one first.) To do this, refer to the
[OpenAI API Documentation](https://platform.openai.com/docs/quickstart?context=python)
### Basic Usage
Double-Click the executable and the app will run. It will open a new instance of terminal. Simply type your prompt in, and it will generate an answer.
For the python source, you can either open it in your prefered IDE and run it, or run it from the terminal. To run it from the terminal, first navigate to the right directory. It will likely be in your downloads, which you can get to using
`cd \Users\username\Downloads\SchoolGPT` and then you can use
`py main.py` to run it.
### Settings
Settings can be found in the `config.json` file. Here is how to use it:
`aiBlacklist` - Whether or not to use AI for blacklisting. Accepts true or false
`blacklistedWords` - If not using AI for blacklisting, the words on the blacklist. Accepts any string value.
`alllowExamples` - Whether or not to allow randomly-generated examples. Accepts true or false.