# langify-mobile
Python utility to translate values from iOS / Android / Ionic translation resources

**langify-mobile** is a simple utility class that read the one localizable file from yours iOS/ Android / Ionic project and generates all translated files using Google Translate API for each platform and language you need. The usage of Google Tanslate API has an affordable cost.

## Installation

* Enable Google Translate API into your google developer account.
* Save google_service.json int he same directory you will execute langify.py
* Open a terminal and execute export GOOGLE_APPLICATION_CREDENTIALS='service_account.json'

## Execution

* Configure your requirements needs in config.py
* Configure and run your *virtualenv*
* call python langify.py

### Platforms available
- iOS
- Android
- Ionic (JSON)

## Usage

Put ios.localizable / android.xml or ionic.json localizable file in *input* folder. All files have to be in a valid format for each platform, on the contrary the process will fail. The following examples are valid format for Android and iOS respectively.

```<?xml version="1.0" encoding="utf-8"?>
<resources>
    <!-- Andorid valid line -->
    <string name="hello.world">Hello World!</string>
</resources>
```

```"hello.world" = "Hello world!";```

```params = {
    'input' : 'android',
    'targets' : ['android'],
    'langs' : ['es','fr','en'],
    'save_cache' : True,
    'print_table' : True,
    'log' : True
}
```

Langify runs as follows:
```
langify.py --i=android -p=True --t=android,ios,ionic --langs=es,en
``

You can configure the languages you need to translate your files using **langs** key, it needs an array of strings of locales to know what are the languages to deal with.

Configure **--t** (targets) key to obtain your localizable files in the platforms you need.

Usage **--c** as *True* to avoid unnecessary calls to Google Translate API. When the process ends it will persist all translations in a json. In future executions of the script if that keys exists in cache it will get the translation from it instead of making a call to Google Translate API that has a fee.

If key **--p** is *True*, when the process ends the script will print in console all translated values in a table

Use **--l** key to log the process for each word.

## Create your own engines

If you need to create some specific engine that fits your needs you can override EngineBase class and implement all necessary methods. Take a look to EngineIOS or EngineAndroid to see how an enigne looks like.
