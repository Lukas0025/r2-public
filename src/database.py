import mysql.connector
import json

class database:
    
    def __init__(self, config):
        self.link = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['pass'],
            database=config['db']
        )
        
        self.cursor = self.link.cursor(buffered=True, dictionary=True)

    def __del__(self): 
        self.close()

    def insertObservation(self, ob):
        if ob.haveA:
            aUrl = ob.aURL
        else:
            aUrl = None

        if ob.haveData:
            dataUrl = ob.dataURL
        else:
            dataUrl = None

        if ob.haveSpect:
            spectUrl = ob.spectrogramURL
        else:
            spectUrl = None

        sql = """INSERT INTO observations (
                    id,
                    norad,
                    start,
                    end,
                    sampleRate, 
                    inputSampleRate,
                    frequency,
                    actualFrequency,
                    bandwidth,
                    tle,
                    numberOfDecodedPackets, 
                    gain,
                    aUrl,
                    dataUrl,
                    spectogramURL,
                    groundStation
              ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (
            ob.id,
            ob.satellite,
            ob.start,
            ob.end,
            ob.sampleRate,
            ob.inputSampleRate,
            ob.frequency,
            ob.actualFrequency,
            ob.bandwidth,
            ob.tle.getStr(),
            ob.numberOfDecodedPackets,
            ob.gain,
            aUrl,
            dataUrl,
            spectUrl,
            json.dumps(ob.groundStation),
        )

        self.cursor.execute(sql, val)

    def haveObservation(self, obid):
        sql = "SELECT id FROM observations WHERE id = %s"
        val = (obid,)
        self.cursor.execute(sql, val)
        return self.cursor.rowcount > 0

    def getGroundStations(self):
        sql = "SELECT groundStation FROM observations GROUP BY groundStation"
        self.cursor.execute(sql)
        grs = self.cursor.fetchall()
        out = []

        for gr in grs:
            out.append(json.loads(gr['groundStation']))

        return out

    def getObservationsWithData(self, limit):
        sql = "SELECT * FROM observations WHERE aUrl is not NULL OR dataUrl is not NULL ORDER BY start DESC LIMIT %s"
        val = (limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    def getLastWithA(self):
        sql = "SELECT * FROM observations WHERE aUrl is not NULL ORDER BY start DESC LIMIT 1"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0]


    def getObservation(self, id):
        sql = "SELECT * FROM observations WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()[0]

    def observationList(self, limit):
        sql = "SELECT * FROM observations ORDER BY start DESC LIMIT %s"
        val = (limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    def observationListOfSat(self, norad, limit):
        sql = "SELECT * FROM observations WHERE norad = %s ORDER BY start DESC LIMIT %s"
        val = (norad, limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    def observationListOfGroundStation(self, ground, limit):
        sql = "SELECT * FROM observations WHERE groundStation = %s ORDER BY start DESC LIMIT %s"
        val = (ground, limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    def observationListInTime(self, time):    
        self.cursor.execute('SELECT * FROM observations WHERE DATEDIFF(start, %s) = 0 ORDER BY start DESC', (time,))
        return self.cursor.fetchall()

    def expiredObservationList(self, ttl):
        self.cursor.execute('SELECT * FROM observations WHERE DATEDIFF(NOW(), start) > %s ORDER BY start DESC', (ttl,))
        return self.cursor.fetchall()

    def removeObservation(self, obid):
        self.cursor.execute('DELETE FROM observations WHERE id = %s', (obid,))

    def commit(self):
        self.link.commit()

    def close(self):
        self.cursor.close()
        self.link.close()