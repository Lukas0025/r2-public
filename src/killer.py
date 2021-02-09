from database import database
import setting
import os

db      = database(setting.db)

for ob in db.expiredObservationList(setting.observationTTL):   
    print("deleting Observation %s" % ob['id'])
    if setting.mirror:
        if ob['aUrl']:
            print("deleting A")
            os.remove(setting.mirrorPATH + "/a/" + str(ob['id']) + ".jpg")

        if ob['dataUrl']:
            print("deleting DATA")
            os.remove(setting.mirrorPATH + "/data/" + str(ob['id']) + ".bin")

        if ob['spectogramURL']:
            print("deleting Spectogram")
            os.remove(setting.mirrorPATH + "/spect/" + str(ob['id']) + ".png")

    db.removeObservation(ob['id'])

#save all changes to DB
db.commit()
