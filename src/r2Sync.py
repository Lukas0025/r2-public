import r2server.api
import r2server.tools.common
import setting
from database import database

network = r2server.api(setting.apiServer)
db      = database(setting.db)


for satellite in setting.satellites:
    
    info = setting.satellites[satellite]
    print("syncing {} source {}".format(info["name"], info["source"]))
    # observations sync
    for ob in network.observation(satellite):
        if not(db.haveObservation(ob.id)) and (ob.haveSpect or ob.haveA or ob.haveData):
            if setting.mirror:
                if ob.haveA:
                    image = ob.a()
                    if not(isinstance(image, int)): #can download
                        r2server.tools.common.bin2file(image, setting.mirrorPATH + "/a/" + str(ob.id) + ".jpg")
                        ob.aURL = setting.mirrorURL + "/a/" + str(ob.id) + ".jpg"
                    else:
                        print("fail to mirror skiping")
                        continue
            
                if ob.haveData:
                    data = ob.data()
                    if not(isinstance(data, int)): #can download
                        r2server.tools.common.bin2file(data, setting.mirrorPATH + "/data/" + str(ob.id) + ".bin")
                        ob.dataURL = setting.mirrorURL + "/data/" + str(ob.id) + ".bin"
                    else:
                        print("fail to mirror skiping")
                        continue

                if ob.haveSpect:
                    spect = ob.spectrogram()
                    if not(isinstance(spect, int)): #can download
                        r2server.tools.common.bin2file(spect, setting.mirrorPATH + "/spects/" + str(ob.id) + ".png")
                        ob.spectrogramURL = setting.mirrorURL + "/spects/" + str(ob.id) + ".png"
                    else:
                        print("fail to mirror skiping")
                        continue
            
            # insert OB to DB
            db.insertObservation(ob)

    #save all changes to DB
    db.commit()
