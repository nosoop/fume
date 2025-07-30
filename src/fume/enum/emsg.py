#!/usr/bin/python3

import enum


class EMsg(enum.IntEnum):
    Invalid = 0
    Multi = 1

    ClientLogOff = 706
    ClientLogonResponse = 751

    ClientGetDepotDecryptionKey = 5438
    ClientGetDepotDecryptionKeyResponse = 5439

    ClientServersAvailable = 5501
    ClientLogon = 5514

    PICSBase = 8900
    ClientPICSChangesSinceRequest = 8901
    ClientPICSChangesSinceResponse = 8902
    ClientPICSProductInfoRequest = 8903
    ClientPICSProductInfoResponse = 8904
