base_info = {
    'directories': [
        'Data',
        'Data/pkl',
        'Data/chromedriver',
        'Data/download',
        'log',
    ],
}

selenium_info = {
    'options': [
        'ignore-certificate-errors',
        'dns-prefetch-disable',
        'disable-extensions',
        'headless',
    ],
    'prefs': {'download.default_directory' : 'Data/chrome_driver'},
}
