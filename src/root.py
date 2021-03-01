import setting
import os
import time
from multiprocessing import Process
from signal import *
import json
from hexdump import hexdump
from datetime import datetime
from database import database
import requests
from flask import Flask, render_template, redirect, url_for, request


#crons
def sync_cron():
    while True:
        print("[INFO] Starting sync cron")
        os.system("python3 r2Sync.py")  
        print("[INFO] sync cron finished")
        time.sleep(setting.syncCronInterval)


def killer_cron():
    while True:
        print("[INFO] Starting killer cron")
        os.system("python3 killer.py")  
        print("[INFO] killer cron finished")
        time.sleep(setting.killerCronInterval)


def startCrons():
    crons = [
        Process(target=sync_cron),
        Process(target=killer_cron)
    ]
    
    for cron in crons:
        cron.start()

    return crons

print("Wait 60s for DB init")
time.sleep(60)

db = database(setting.db)

if not(db.isInited()):
    db.initDb()

db.close()

app      = Flask(__name__)
crons    = startCrons()


@app.route('/')
def root():
    db     = database(setting.db)

    return render_template(
        'home.html',
        siteName         = setting.siteName,
        custom           = setting.customMain,
        customHead       = setting.customHead,
        grs              = db.getGroundStations(),
        obs              = db.getObservationsWithData(setting.mainObsCount),
        json             = json,
        lastImage        = db.getLastWithLotPacketsA(),
        sats             = setting.satellites,
        subSiteTitle     = ""
    )


##
## IMAGE API
##
@app.route('/api/img/last')
def apiImgLast():
    db     = database(setting.db)

    sat    = request.args.get('sat')
    if sat != None:
        img = db.getLastSatWithA(sat)['aUrl']
    else:
        img = db.getLastWithA()['aUrl']

    return redirect(img)

@app.route('/api/img/lastbest')
def apiImgLastBest():
    db     = database(setting.db)

    sat    = request.args.get('sat')
    if sat != None:
        img = db.getLastSatWithLotPacketsA(sat)['aUrl']
    else:
        img = db.getLastWithLotPacketsA()['aUrl']

    return redirect(img)

@app.route('/api/img/besttoday')
def apiImgBestToday():
    db     = database(setting.db)

    sat    = request.args.get('sat')
    if sat != None:
        img = db.getBestSatPacketsToday(sat)['aUrl']
    else:
        img = db.getBestPacketsToday()['aUrl']

    return redirect(img)
##
## API end
##


@app.route('/observation')
def observation():
    obId        = request.args.get('ob')
    db          = database(setting.db)
    ob          = db.getObservation(obId)
    
    tle         = json.loads(ob['tle'])

    return render_template(
        'observation.html',
        ob = ob,
        customHead  = setting.customHead,
        siteName = setting.siteName,
        setting = setting,
        tle = tle,
        groundStation = json.loads(ob['groundStation']),
        hexdump = hexdump,
        requests = requests,
        hexdumpLimit = setting.hexdumpLimit,
        subSiteTitle = " - observation %s of %s" % (ob['id'], tle[0])
    )

@app.route('/decodedobservationlist')
def decodedObservationList():
    db     = database(setting.db)

    main_title   = "All decoded observations (limit: %s)" % (setting.observationsLimit)

    observations = db.getObservationsWithData(setting.observationsLimit)

    return render_template(
        'observationList.html',
        obs         = observations,
        customHead  = setting.customHead,
        siteName    = setting.siteName,
        datetime    = datetime,
        main_title  = main_title,
        json        = json,
        subSiteTitle = " - decoded observations list"
    )

@app.route('/observationlist')
def observationList():
    sat    = request.args.get('sat')
    time   = request.args.get('time')
    ground = request.args.get('ground')
    
    db     = database(setting.db)

    
    if sat != None:
        main_title   = "All observations of satellite %s (limit: %s)" % (setting.satellites[sat]['name'], setting.observationsLimit)
        observations = db.observationListOfSat(sat, setting.observationsLimit)
    elif time != None:
        main_title   = "All observations %s" % time

        date = datetime.strptime(time, "%Y-%m-%d")

        observations = db.observationListInTime(date)
    elif ground != None:
        main_title   = "All observations by GroundStation (limit: %s)" % (setting.observationsLimit)

        observations = db.observationListOfGroundStation(ground, setting.observationsLimit)
    else:
        main_title   = "All observations (limit: %s)" % (setting.observationsLimit)

        observations = db.observationList(setting.observationsLimit)

    return render_template(
        'observationList.html',
        customHead    = setting.customHead,
        obs           = observations,
        siteName      = setting.siteName,
        datetime      = datetime,
        main_title    = main_title,
        json          = json,
        subSiteTitle  = " - observations list"
    )
