# langify-mobile
Python utility to translate values from iOS / Android resources

**langify-mobile** is a simple utility class that read the one localizable file from one platform (currently iOS and Android) and all the corresponding files for each platform and translated using Google Treanslate API

##Platforms available
- iOS
- Android

##Usage

Put ios.localizable or android.xml localizable file in *input* folder. All files have to be in a valid format for each platform, on the contrary the process will fail.

```<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="hello.world">Hello World!</string>
</resources>
```

```"hello.world" = "Hello world!";```


If you open config.py file you will a python dictionary with some keys and values. Change the values according your requirements.

```params = {
    'input' : 'android',
    'targets' : ['android'],
    'langs' : ['es','fr','en'],
    'save_cache' : True,
    'print_table' : True
}
```

You can configure the languages you need to translate your files using **langs** key, it needs an array of strings of locales to know what are the languages to deal with.

Configure **targets** key to obtain your localizable files in the platforms you need.

Usage **save_cache** as *True* to avoid unnecessary calls to Google Translate API. When the process ends it will persist all translations in a json. In future executions of the script if that keys exists in cache it will get the translation from it instead making a call to Google Translate API.

If key **print_table** is *True*, when the process ends the script will print all translated values in a table.
