![Python 3.8](https://img.shields.io/badge/Python%20version-Python%203.8-yellow?logo=python&logoColor=yellow)![Download count](https://img.shields.io/github/downloads/gptgit/language_translator/total?label=%F0%9F%93%A5%20Downloads&color=%236ac5fe)
# Language Translator
A simple CLI Language Translator application in Python.

## Download
1. Clone the repository: `git clone https://github.com/gptgit/language_translator.git`
2. Change into the directory: `cd language_translator`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python main.py`

## Documentation
### Usage
Enter the language to translate (e.g. en, es, fr) and the text to translate. The application will translate the text and print the result.

### Supported Languages
The application supports translations to and from the following languages:
* English (en)
* Spanish (es)
* French (fr)
* German (de)
* Italian (it)
* Portuguese (pt)
* Chinese (zh)
* Japanese (ja)
* Korean (ko)

### Error Handling
The application will handle errors and print a professional error message if an error occurs during translation.

### Tests
The application includes a set of tests to ensure it works correctly. You can run the tests using the following command: `python -m unittest tests/test_translator.py`

### Credits
This application uses the `googletrans` library for translation.

### License
This application is licensed under the MIT License. See `LICENSE` for more information.

### GitHub
You can find the source code for this application on GitHub: https://github.com/gptgit/language_translator