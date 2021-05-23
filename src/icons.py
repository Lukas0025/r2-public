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
    }.get(int(satId), "default.png")