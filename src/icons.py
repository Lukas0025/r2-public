#!/usr/bin/env python3
##
# Project: r2public
# File with icon factory
# @author Lukáš Plevač <lukas@plevac.eu>
# @date 23.5.2021

## Get icon of satellite by id
# @param satId id of satellite
# @return str path to icon
def getSatelliteIcon(satId):
    
    return "/static/images/satellites/" + {
        40069: "meteor-m2.png",
        33591: "noaa19.png", #noaa19
        28654: "noaa19.png", #noaa18
        25338: "noaa19.png", #noaa15
        32789: "generic_cube.png", #DELFI-C3 (DO-64)
        39430: "generic_cube.png", #GOMX-1
        39444: "generic_cube.png", #FUNCUBE-1 (AO-73)
        41460: "generic_cube.png", #AAUSAT 4
        42017: "generic_cube.png", #NAYIF-1
        42784: "generic_cube.png", #PEGASUS
        43743: "generic_cube.png", #REAKTOR HELLO WORLD
        43803: "generic_cube.png", #JY1SAT (JO-97)
        44406: "generic_cube.png", #Lucky7
        44332: "generic_cube.png", #SPOOQY-1
    }.get(int(satId), "default.png")