import mysql.connector
import json

class database:
    
    ## database object conscructor
    # create conection to database
    # @param self
    # @param config - named array with config [host, port, user, pass, db]
    # @return DB obj
    def __init__(self, config):
        self.link = mysql.connector.connect(
            host=config['host'],
            port=config['port'],
            user=config['user'],
            password=config['pass'],
            database=config['db']
        )
        
        self.cursor = self.link.cursor(buffered=True, dictionary=True)
            
    
    ## database object descructor
    # close conection to database
    # @param self
    # @return none
    def __del__(self): 
        self.close()
    
    ## check is databse inited
    # @param self
    # @return bool
    def isInited(self):
        self.cursor.execute("SHOW TABLES LIKE 'observations'")
        
        return self.cursor.fetchone()
    
    ## init database schema
    # @param self
    # @return none
    def initDb(self):
        self.cursor.execute("""DROP TABLE IF EXISTS `observations`;
                                                CREATE TABLE `observations` (
                                                        `id` int(11) NOT NULL,
                                                        `norad` int(11) NOT NULL,
                                                        `start` datetime NOT NULL,
                                                        `end` datetime NOT NULL,
                                                        `sampleRate` int(11) NOT NULL,
                                                        `inputSampleRate` int(11) NOT NULL,
                                                        `frequency` int(11) NOT NULL,
                                                        `actualFrequency` int(11) NOT NULL,
                                                        `bandwidth` int(11) NOT NULL,
                                                        `tle` text NOT NULL,
                                                        `numberOfDecodedPackets` int(11) NOT NULL,
                                                        `gain` float NOT NULL,
                                                        `aUrl` text DEFAULT NULL,
                                                        `dataUrl` text DEFAULT NULL,
                                                        `spectogramURL` text DEFAULT NULL,
                                                        `groundStation` text DEFAULT NULL,
                                                         PRIMARY KEY(`id`)
                                                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;""")

    ## insert observation to database
    # @param self
    # @param ob observation object - from r2server.observation
    # @return none
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

    ## check is observation with ID exist
    # @param self
    # @param obid int - id of oesrvation - r2server.observation.id
    # @return bool
    def haveObservation(self, obid):
        sql = "SELECT id FROM observations WHERE id = %s"
        val = (obid,)
        self.cursor.execute(sql, val)
        return self.cursor.rowcount > 0

    ## load list of ground stations
    # @param self
    # @return list of json.loads ground station
    def getGroundStations(self):
        sql = "SELECT groundStation FROM observations GROUP BY groundStation"
        self.cursor.execute(sql)
        grs = self.cursor.fetchall()
        out = []

        for gr in grs:
            out.append(json.loads(gr['groundStation']))

        return out

    ## load list of observations with data
    # @param self
    # @param limit int - limit of observations
    # @return list of json.loads ground station
    def getObservationsWithData(self, limit):
        sql = "SELECT * FROM observations WHERE aUrl is not NULL OR dataUrl is not NULL ORDER BY start DESC LIMIT %s"
        val = (limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    ## get last observation with A channel
    # @param self
    # @return named array of observation
    def getLastWithA(self):
        sql = "SELECT * FROM observations WHERE aUrl is not NULL ORDER BY start DESC LIMIT 1"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0]

    ## get last observation with lot of packets and A channel
    # @param self
    # @return named array of observation
    def getLastWithLotPacketsA(self):
        sql = "SELECT * FROM observations WHERE aUrl is not NULL ORDER BY (TIMESTAMPDIFF(SECOND, NOW(), start) - numberOfDecodedPackets)  ASC LIMIT 1"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0]

    ## get best observation today with lot of packets and A channel
    # @param self
    # @return named array of observation
    def getBestPacketsToday(self):
        sql = "SELECT * FROM observations WHERE aUrl is not NULL and start >= CURDATE() ORDER BY numberOfDecodedPackets DESC LIMIT 1"
        self.cursor.execute(sql)
        return self.cursor.fetchall()[0]

    ## get observation with id
    # @param self
    # @param id int - r2server.observation.id
    # @return named array of observation
    def getObservation(self, id):
        sql = "SELECT * FROM observations WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()[0]

    ## get list of observations ORDER BY start time
    # @param self
    # @param id int - r2server.observation.id
    # @return named array of observation
    def observationList(self, limit):
        sql = "SELECT * FROM observations ORDER BY start DESC LIMIT %s"
        val = (limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    ## get list of observations by satellite with norad
    # @param self
    # @param norad int - narad id of satellite
    # @param limit int - max len of array
    # @return named array of observation
    def observationListOfSat(self, norad, limit):
        sql = "SELECT * FROM observations WHERE norad = %s ORDER BY start DESC LIMIT %s"
        val = (norad, limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    ## get list of observations by ground station
    # @param self
    # @param ground string - json.dumps of groundstation
    # @param limit int - max len of array
    # @return named array of observation
    def observationListOfGroundStation(self, ground, limit):
        sql = "SELECT * FROM observations WHERE groundStation = %s ORDER BY start DESC LIMIT %s"
        val = (ground, limit,)
        self.cursor.execute(sql, val)
        return self.cursor.fetchall()

    ## get list of observations in specific date
    # @param self
    # @param time string - string of date
    # @return named array of observation
    def observationListInTime(self, time):    
        self.cursor.execute('SELECT * FROM observations WHERE DATEDIFF(start, %s) = 0 ORDER BY start DESC', (time,))
        return self.cursor.fetchall()

    ## get list of expired observations (to delete over TTL)
    # @param self
    # @param ttl int - number of days to live
    # @return named array of observation
    def expiredObservationList(self, ttl):
        self.cursor.execute('SELECT * FROM observations WHERE DATEDIFF(NOW(), start) > %s ORDER BY start DESC', (ttl,))
        return self.cursor.fetchall()

    ## remove observation from database
    # @param self
    # @param obid int - observation id - r2server.observation.id
    # @return none
    def removeObservation(self, obid):
        self.cursor.execute('DELETE FROM observations WHERE id = %s', (obid,))

    ## commit changes in DB
    # @param self
    # @return none
    def commit(self):
        self.link.commit()

    ## close connection to DB
    # @param self
    # @return none
    def close(self):
        self.cursor.close()
        self.link.close()
