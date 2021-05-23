mirror = False

siteName = "r2public"

mainObsCount = 30
observationsLimit = 150

customMain = ""
customHead = ""

hexdumpLimit = 50

syncCronInterval = 3600 # in s

killerCronInterval = 86400 # in s
observationTTL = 366 #in d

mirrorPATH = "static/"
mirrorURL  = "/static/"

db = {
    'host': 'mysql',
    'port': '3306',
    'user': 'root',
    'pass': 'XXXXXX',
    'db': 'r2public',
}

satellites = {
    "25338": {
        "name": "NOAA 15",
        "sources": [
            "APT": {
                "earthObservationImagery": True,
                "resolution": 6000, #6km/px
                "swath": 2900000 #m
            },

            "HRPT": {
                "earthObservationImagery": True,
                "resolution": 1000, #1km/px
                "swath": 2900000 #m
            }
        ]
    },

    "28654": {
        "name": "NOAA 18",
        "sources": [
            "APT": {
                "earthObservationImagery": True,
                "resolution": 6000, #6km/px
                "swath": 2900000 #m
            },

            "HRPT": {
                "earthObservationImagery": True,
                "resolution": 1000, #1km/px
                "swath": 2900000 #m
            }
        ]
    },

    "32789": {
        "name": "DELFI-C3 (DO-64)",
        "sources": ["TELEMETRY"]
    },

    "33591": {
        "name": "NOAA 19",
        "sources": [
            "APT": {
                "earthObservationImagery": True,
                "resolution": 6000, #6km/px
                "swath": 2900000 #m
            }

            "HRPT": {
                "earthObservationImagery": True,
                "resolution": 1000, #1km/px
                "swath": 2900000 #m
            }
        ]
    },

    "39430": {
        "name": "GOMX-1",
        "sources": ["TELEMETRY"]
    },

    "39444": {
        "name": "FUNCUBE-1 (AO-73)",
        "sources": ["TELEMETRY"]
    },

    "40069": {
        "name": "METEOR-M 2",
        "sources": [
            "LRPT": {
                "earthObservationImagery": True,
                "resolution": 1000, #1km/px
                "swath": 2800000 #m
            }
        ]
    },

    "41460": {
        "name": "AAUSAT 4",
        "sources": ["TELEMETRY"]
    },

    "42017": {
        "name": "NAYIF-1 (EO-88)",
        "sources": ["TELEMETRY"]
    },

    "42784": {
        "name": "PEGASUS",
        "sources": ["TELEMETRY"]
    },

    "42829": {
        "name": "TECHNOSAT",
        "sources": ["TELEMETRY"]
    },

    "43186": {
        "name": "S-NET D",
        "sources": ["TELEMETRY"]
    },

    "43187": {
        "name": "S-NET B",
        "sources": ["TELEMETRY"]
    },

    "43188": {
        "name": "S-NET A",
        "sources": ["TELEMETRY"]
    },

    "43189": {
        "name": "S-NET C",
        "sources": ["TELEMETRY"]
    },

    "43743": {
        "name": "REAKTOR HELLO WORLD",
        "sources": ["TELEMETRY"]
    },

    "43786": {
        "name": "ITASAT 1",
        "sources": ["TELEMETRY"]
    },

    "43792": {
        "name": "ESEO",
        "sources": ["TELEMETRY"]
    },

    "43798": {
        "name": "ASTROCAST 0.1",
        "sources": ["TELEMETRY"]
    },

    "43803": {
        "name": "JY1SAT (JO-97)",
        "sources": ["TELEMETRY"]
    },

    "43804": {
        "name": "SUOMI-100",
        "sources": ["TELEMETRY"]
    },

    "43814": {
        "name": "PW-SAT2",
        "sources": ["TELEMETRY"]
    },

    "43881": {
        "name": "D-STAR ONE (SPARROW)",
        "sources": ["TELEMETRY"]
    },

    "43908": {
        "name": "LUME 1",
        "sources": ["TELEMETRY"]
    },

    "44103": {
        "name": "AISTECHSAT-3",
        "sources": ["TELEMETRY"]
    },

    "44406": {
        "name": "LUCKY-7",
        "sources": ["TELEMETRY"]
    },

    "44878": {
        "name": "OPS-SAT",
        "sources": ["TELEMETRY"]
    },

    "44885": {
        "name": "FLORIPASAT-1",
        "sources": ["TELEMETRY"]
    },

    "45115": {
        "name": "SWAMPSAT-2",
        "sources": ["TELEMETRY"]
    },

    "45263": {
        "name": "QARMAN",
        "sources": ["TELEMETRY"]
    },

    "45598": {
        "name": "QUETZAL-1",
        "sources": ["TELEMETRY"]
    },

    "44083": {
        "name": "ASTROCAST 0.2",
        "sources": ["TELEMETRY"]
    },

    "43017": {
        "name": "RADFXSAT (FOX-1B)",
        "sources": ["TELEMETRY"]
    },

    "43770": {
        "name": "FOX-1CLIFF (AO-95)",
        "sources": ["TELEMETRY"]
    },

    "43137": {
        "name": "FOX-1D (AO-92)",
        "sources": ["TELEMETRY"]
    },

    "45119": {
        "name": "HUSKYSAT-1",
        "sources": ["TELEMETRY"]
    },

    "44365": {
        "name": "PAINANI 1",
        "sources": ["TELEMETRY"]
    },

    "43855": {
        "name": "CHOMPTT",
        "sources": ["TELEMETRY"]
    },

    "43880": {
        "name": "UWE-4",
        "sources": ["TELEMETRY"]
    },

    "40012": {
        "name": "UNISAT-6",
        "sources": ["TELEMETRY"]
    },

    "40042": {
        "name": "POLYITAN-1",
        "sources": ["TELEMETRY"]
    },

    "42775": {
        "name": "AALTO-1",
        "sources": ["TELEMETRY"]
    },

    "44352": {
        "name": "ARMADILLO",
        "sources": ["TELEMETRY"]
    },

    "44355": {
        "name": "BRICSAT2 (NO-103)",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "40014": {
        "name": "BUGSAT-1 (TITA)",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "42761": {
        "name": "ZHUHAI-1 01 (CAS-4A)",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "42759": {
        "name": "ZHUHAI-1 02 (CAS-4B)",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "40379": {
        "name": "GRIFEX",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "43793": {
        "name": "CSIM-FD",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "43666": {
        "name": "CUBEBEL-1 (BSUSAT-1)",
        "sources": ["TELEMETRY"]
    },

    "43617": {
        "name": "ELFIN-A",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "43616": {
        "name": "ELFIN-B",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "40377": {
        "name": "FIREBIRD 3",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "40378": {
        "name": "FIREBIRD 4",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "43693": {
        "name": "IRVINE01",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "44420": {
        "name": "LIGHTSAIL 2",
        "sources": ["TELEMETRY"]
    },

    "42768": {
        "name": "LITUANICASAT-2",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "43758": {
        "name": "MINXSS-2",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "43937": {
        "name": "NEXUS (FO-99)",
        "sources": ["TELEMETRY"]
    },

    "39440": {
        "name": "CUBEBUG-2 (LO-74)",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "42789": {
        "name": "SKCUBE",
        "sources": ["TELEMETRY"]
    },

    "43784": {
        "name": "SNUGLITE",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "44356": {
        "name": "TBEX-A",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "40043": {
        "name": "TIGRISAT",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "30776": {
        "name": "FALCONSAT-3",
        "sources": ["TELEMETRY"]
    },

    "44369": {
        "name": "ACRUX 1",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "43768": {
        "name": "AISTECHSAT 2",
        "sources": ["TELEMETRY"]
    },

    "41789": {
        "name": "ALSAT 1N",
        "sources": ["TELEMETRY"]
    },

    "40968": {
        "name": "BISONSAT",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "46494": {
        "name": "NORBI",
        "sources": ["TELEMETRY"]
    },

    "39090": {
        "name": "STRAND-1",
        "sources": ["TELEMETRY"]
    },

    "46495": {
        "name": "SALSAT",
        "sources": ["TELEMETRY"]
    },

    "44030": {
        "name": "DELPHINI",
        "sources": ["TELEMETRY"]
    },

    "43199": {
        "name": "SHAONIAN XING",
        "sources": ["TELEMETRY"]
    },

    "40909": {
        "name": "XW-2E",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "40910": {
        "name": "XW-2F",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "40907": {
        "name": "XW-2D",
        "sources": ["FSK_AX25_G3RUH"]
    },

    "46287": {
        "name": "AMICALSAT",
        "sources": ["TELEMETRY"]
    },

    "44332": {
        "name": "SPOOQY-1",
        "sources": ["TELEMETRY"]
    },

    "46489": {
        "name": "MEZNSAT",
        "sources": ["TELEMETRY"]
    },

    "43738": {
        "name": "INNOSAT-2",
        "sources": ["TELEMETRY"]
    },

    "43721": {
        "name": "FACSAT-1",
        "sources": ["TELEMETRY"]
    },

    "40931": {
        "name": "LAPAN-A2",
        "sources": ["TELEMETRY"]
    },

    "44426": {
        "name": "SWIATOWID",
        "sources": ["TELEMETRY"]
    },

    "46923": {
        "name": "NEUTRON-1",
        "sources": ["TELEMETRY"]
    },

    "42792": {
        "name": "ROBUSTA-1B",
        "sources": ["TELEMETRY"]
    },

    "40912": {
        "name": "KAITUO 1B",
        "sources": ["TELEMETRY"]  
    },

    "46922": {
        "name": "BOBCAT-1",
        "sources": ["TELEMETRY"]  
    }
}
