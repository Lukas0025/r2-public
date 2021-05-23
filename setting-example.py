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
        "source": "APT",
        "earthObservationImagery": True,
        "resolution": 6000, #6km/px
        "swath": 2900000 #m
    },

    "28654": {
        "name": "NOAA 18",
        "source": "APT",
        "earthObservationImagery": True,
        "resolution": 6000, #6km/px
        "swath": 2900000 #m
    },

    "32789": {
        "name": "DELFI-C3 (DO-64)",
        "source": "TELEMETRY"
    },

    "33591": {
        "name": "NOAA 19",
        "source": "APT",
        "earthObservationImagery": True,
        "resolution": 6000, #6km/px
        "swath": 2900000 #m
    },

    "39430": {
        "name": "GOMX-1",
        "source": "TELEMETRY"
    },

    "39444": {
        "name": "FUNCUBE-1 (AO-73)",
        "source": "TELEMETRY"
    },

    "40069": {
        "name": "METEOR-M 2",
        "source": "LRPT",
        "earthObservationImagery": True,
        "resolution": 1000, #1km/px
        "swath": 2800000 #m
    },

    "41460": {
        "name": "AAUSAT 4",
        "source": "TELEMETRY"
    },

    "42017": {
        "name": "NAYIF-1 (EO-88)",
        "source": "TELEMETRY"
    },

    "42784": {
        "name": "PEGASUS",
        "source": "TELEMETRY"
    },

    "42829": {
        "name": "TECHNOSAT",
        "source": "TELEMETRY"
    },

    "43186": {
        "name": "S-NET D",
        "source": "TELEMETRY"
    },

    "43187": {
        "name": "S-NET B",
        "source": "TELEMETRY"
    },

    "43188": {
        "name": "S-NET A",
        "source": "TELEMETRY"
    },

    "43189": {
        "name": "S-NET C",
        "source": "TELEMETRY"
    },

    "43743": {
        "name": "REAKTOR HELLO WORLD",
        "source": "TELEMETRY"
    },

    "43786": {
        "name": "ITASAT 1",
        "source": "TELEMETRY"
    },

    "43792": {
        "name": "ESEO",
        "source": "TELEMETRY"
    },

    "43798": {
        "name": "ASTROCAST 0.1",
        "source": "TELEMETRY"
    },

    "43803": {
        "name": "JY1SAT (JO-97)",
        "source": "TELEMETRY"
    },

    "43804": {
        "name": "SUOMI-100",
        "source": "TELEMETRY"
    },

    "43814": {
        "name": "PW-SAT2",
        "source": "TELEMETRY"
    },

    "43881": {
        "name": "D-STAR ONE (SPARROW)",
        "source": "TELEMETRY"
    },

    "43908": {
        "name": "LUME 1",
        "source": "TELEMETRY"
    },

    "44103": {
        "name": "AISTECHSAT-3",
        "source": "TELEMETRY"
    },

    "44406": {
        "name": "LUCKY-7",
        "source": "TELEMETRY"
    },

    "44878": {
        "name": "OPS-SAT",
        "source": "TELEMETRY"
    },

    "44885": {
        "name": "FLORIPASAT-1",
        "source": "TELEMETRY"
    },

    "45115": {
        "name": "SWAMPSAT-2",
        "source": "TELEMETRY"
    },

    "45263": {
        "name": "QARMAN",
        "source": "TELEMETRY"
    },

    "45598": {
        "name": "QUETZAL-1",
        "source": "TELEMETRY"
    },

    "44083": {
        "name": "ASTROCAST 0.2",
        "source": "TELEMETRY"
    },

    "43017": {
        "name": "RADFXSAT (FOX-1B)",
        "source": "TELEMETRY"
    },

    "43770": {
        "name": "FOX-1CLIFF (AO-95)",
        "source": "TELEMETRY"
    },

    "43137": {
        "name": "FOX-1D (AO-92)",
        "source": "TELEMETRY"
    },

    "45119": {
        "name": "HUSKYSAT-1",
        "source": "TELEMETRY"
    },

    "44365": {
        "name": "PAINANI 1",
        "source": "TELEMETRY"
    },

    "43855": {
        "name": "CHOMPTT",
        "source": "TELEMETRY"
    },

    "43880": {
        "name": "UWE-4",
        "source": "TELEMETRY"
    },

    "40012": {
        "name": "UNISAT-6",
        "source": "TELEMETRY"
    },

    "40042": {
        "name": "POLYITAN-1",
        "source": "TELEMETRY"
    },

    "42775": {
        "name": "AALTO-1",
        "source": "TELEMETRY"
    },

    "44352": {
        "name": "ARMADILLO",
        "source": "TELEMETRY"
    },

    "44355": {
        "name": "BRICSAT2 (NO-103)",
        "source": "FSK_AX25_G3RUH"
    },

    "40014": {
        "name": "BUGSAT-1 (TITA)",
        "source": "FSK_AX25_G3RUH"
    },

    "42761": {
        "name": "ZHUHAI-1 01 (CAS-4A)",
        "source": "FSK_AX25_G3RUH"
    },

    "42759": {
        "name": "ZHUHAI-1 02 (CAS-4B)",
        "source": "FSK_AX25_G3RUH"
    },

    "40379": {
        "name": "GRIFEX",
        "source": "FSK_AX25_G3RUH"
    },

    "43793": {
        "name": "CSIM-FD",
        "source": "FSK_AX25_G3RUH"
    },

    "43666": {
        "name": "CUBEBEL-1 (BSUSAT-1)",
        "source": "TELEMETRY"
    },

    "43617": {
        "name": "ELFIN-A",
        "source": "FSK_AX25_G3RUH"
    },

    "43616": {
        "name": "ELFIN-B",
        "source": "FSK_AX25_G3RUH"
    },

    "40377": {
        "name": "FIREBIRD 3",
        "source": "FSK_AX25_G3RUH"
    },

    "40378": {
        "name": "FIREBIRD 4",
        "source": "FSK_AX25_G3RUH"
    },

    "43693": {
        "name": "IRVINE01",
        "source": "FSK_AX25_G3RUH"
    },

    "44420": {
        "name": "LIGHTSAIL 2",
        "source": "TELEMETRY"
    },

    "42768": {
        "name": "LITUANICASAT-2",
        "source": "FSK_AX25_G3RUH"
    },

    "43758": {
        "name": "MINXSS-2",
        "source": "FSK_AX25_G3RUH"
    },

    "43937": {
        "name": "NEXUS (FO-99)",
        "source": "TELEMETRY"
    },

    "39440": {
        "name": "CUBEBUG-2 (LO-74)",
        "source": "FSK_AX25_G3RUH"
    },

    "42789": {
        "name": "SKCUBE",
        "source": "TELEMETRY"
    },

    "43784": {
        "name": "SNUGLITE",
        "source": "FSK_AX25_G3RUH"
    },

    "44356": {
        "name": "TBEX-A",
        "source": "FSK_AX25_G3RUH"
    },

    "40043": {
        "name": "TIGRISAT",
        "source": "FSK_AX25_G3RUH"
    },

    "30776": {
        "name": "FALCONSAT-3",
        "source": "TELEMETRY"
    },

    "44369": {
        "name": "ACRUX 1",
        "source": "FSK_AX25_G3RUH"
    },

    "43768": {
        "name": "AISTECHSAT 2",
        "source": "TELEMETRY"
    },

    "41789": {
        "name": "ALSAT 1N",
        "source": "TELEMETRY"
    },

    "40968": {
        "name": "BISONSAT",
        "source": "FSK_AX25_G3RUH"
    },

    "46494": {
        "name": "NORBI",
        "source": "TELEMETRY"
    },

    "39090": {
        "name": "STRAND-1",
        "source": "TELEMETRY"
    },

    "46495": {
        "name": "SALSAT",
        "source": "TELEMETRY"
    },

    "44030": {
        "name": "DELPHINI",
        "source": "TELEMETRY"
    },

    "43199": {
        "name": "SHAONIAN XING",
        "source": "TELEMETRY"
    },

    "40909": {
        "name": "XW-2E",
        "source": "FSK_AX25_G3RUH"
    },

    "40910": {
        "name": "XW-2F",
        "source": "FSK_AX25_G3RUH"
    },

    "40907": {
        "name": "XW-2D",
        "source": "FSK_AX25_G3RUH"
    },

    "46287": {
        "name": "AMICALSAT",
        "source": "TELEMETRY"
    },

    "44332": {
        "name": "SPOOQY-1",
        "source": "TELEMETRY"
    },

    "46489": {
        "name": "MEZNSAT",
        "source": "TELEMETRY"
    },

    "43738": {
        "name": "INNOSAT-2",
        "source": "TELEMETRY"
    },

    "43721": {
        "name": "FACSAT-1",
        "source": "TELEMETRY"
    },

    "40931": {
        "name": "LAPAN-A2",
        "source": "TELEMETRY"
    },

    "44426": {
        "name": "SWIATOWID",
        "source": "TELEMETRY"
    },

    "46923": {
        "name": "NEUTRON-1",
        "source": "TELEMETRY"
    },

    "42792": {
        "name": "ROBUSTA-1B",
        "source": "TELEMETRY"
    },

    "40912": {
        "name": "KAITUO 1B",
        "source": "TELEMETRY"  
    },

    "46922": {
        "name": "BOBCAT-1",
        "source": "TELEMETRY"  
    }
}
