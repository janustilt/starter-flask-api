from threading import Lock

qrs = [
        {
            'qrcode' : '406f0859-fc2c-4d70-ac29-4b3302049703',
            'filename' : '123456_AZERTY_20240124180212_OR.TXT',
            'type' : 'TPM',
            'rest_home_name' : 'Paix du soir',
            'logistic_tag' : '1erEtage',
            'officine' : '159',
            'site' : 'SPL',
            'statut' : 'PMI',
            'creation_date' : '2024-01-24 18:06:12',
            'qui' : 'addQRcode'
        },
        {
            'qrcode' : '66051d36-a268-4292-b6fd-6187aa7871d3',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'LEGACY',
            'rest_home_name' : 'Silence',
            'logistic_tag' : 'rez',
            'officine' : '38',
            'site' : 'LIEGE',
            'statut' : 'PMI',
            'creation_date' : '2024-01-24 18:10:12',
            'qui' : 'addQRcode'
        },
        {
            'qrcode' : 'c1cf5616-7a54-426c-b5b1-8c61e58de0e2',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'EXTRA',
            'rest_home_name' : '',
            'logistic_tag' : '',
            'officine' : '721',
            'site' : 'LIEGE',
            'statut' : 'EXTRA',
            'creation_date' : '2024-01-24 18:10:12',
            'qui' : 'addQRcode'
        },
        {
            'qrcode' : '1f19866b-3c48-46a9-ace5-330d564c8aa2',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'RC',
            'rest_home_name' : 'ARCADIA',
            'logistic_tag' : 'top',
            'officine' : '721',
            'site' : '721',
            'statut' : 'RC',
            'creation_date' : '2024-01-24 8:00:12',
            'qui' : 'addQRcodeRC'
        },
        {
            'qrcode' : 'ab6d9f53-0d8c-47cb-9af0-fa58af2907d9',
            'filename' : '123456_70123456789_20240124181002_OR.TXT',
            'type' : 'RC',
            'rest_home_name' : 'ARCADIA',
            'logistic_tag' : 'ciel',
            'officine' : '721',
            'site' : '721',
            'statut' : 'RC',
            'creation_date' : '2024-01-24 8:00:13',
            'qui' : 'addQRcodeRC'
        },
        {
            'qrcode' : '2a8888ea-6079-4653-a79a-f4356baa2d18',
            'filename' : '239801_76027313210_20240119102035_OR.TXT',
            'type' : 'LEGACY',
            'rest_home_name' : 'Releghem',
            'logistic_tag' : 'Afdeling 3',
            'officine' : '150',
            'site' : 'SPL',
            'statut' : 'LEGACY',
            'creation_date' : '2024-01-19 8:00:13',
            'qui' : 'addQRcodeRC'
        },
        {
            'qrcode' : 'e0f886f2-61a7-473e-b9de-2822a1741001',
            'filename' : '237708_73261922110_20240119101926_OR.TXT',
            'type' : 'RC',
            'rest_home_name' : 'Le Gibloux',
            'logistic_tag' : 'C',
            'officine' : '159',
            'site' : 'SPL',
            'statut' : 'TPM',
            'creation_date' : '2024-01-19 8:00:13',
            'qui' : 'addQRcodeRC'
        },
        {
            'qrcode' : '27526a23-4bff-4a36-a8f2-5c7a1c41d7d1',
            'filename' : '237708_74114235110_20240119101056_OR.TXT',
            'type' : 'TPM',
            'rest_home_name' : 'Val des Fleurs',
            'logistic_tag' : 'London',
            'officine' : '159',
            'site' : 'SPL',
            'statut' : 'TPM',
            'creation_date' : '2024-01-19 8:00:13',
            'qui' : 'addQRcodeRC'
        },
        {
            'qrcode' : 'b60e4240-f7e2-4b69-b6d6-ea859b78f859',
            'filename' : '237708_73269147110_20240119100641_OR.TXT',
            'type' : 'LEGACY',
            'rest_home_name' : 'Chateau Belle chasse',
            'logistic_tag' : '2ME',
            'officine' : '159',
            'site' : 'SPL',
            'statut' : 'LEGACY',
            'creation_date' : '2024-01-19 8:00:13',
            'qui' : 'addQRcodeRC'
        },
        {
            'qrcode' : '6ce1f85b-7789-407d-aafe-363209a3b238',
            'filename' : '211604_00000BRUGGE_20240119093023_OR.txt',
            'type' : 'RC',
            'rest_home_name' : 'PC BRUGGE LEGE WEG',
            'logistic_tag' : 'ciel',
            'officine' : '721',
            'site' : '721',
            'statut' : 'RC',
            'creation_date' : '2024-01-24 8:00:13',
            'qui' : 'addQRcodeRC'
        }
]

qrs_lock = Lock()



