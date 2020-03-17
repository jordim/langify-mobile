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

Langify runs as follows:

```langify.py --i=android --t=ios --langs=es,en```

## Arguments

*--i* platform from you want to translate the key values. Possibles values: ios, android, ionic

*--t* platforms on which you want to generate the locations. Possible values: android, ios, ionic

*--l* logs all the processes done by langify. Default is False

*--langs* languages on which you want to translate to.

*--c* caches all translated key names for avoid unnecesary calls to google cloud. Default is True

