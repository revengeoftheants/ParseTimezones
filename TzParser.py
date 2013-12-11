#Quick script to tzdata region files. See http://www.iana.org/time-zones.

import sys

infile, outfile = sys.argv[1], sys.argv[2]

inf = open(infile, "r")
outf = open(outfile, "w")
zoneInd = False
zoneNm = ""
zoneLn = ""
prevZoneLn = ""

for line in inf:

    if line.startswith("Zone"):
        if len(prevZoneLn) > 0:
            zoneLn = prevZoneLn.split("\t")
            utc = zoneLn[3]

            tmFndInd = False

            while tmFndInd == False:
                if (utc.endswith(" ") or not utc[len(utc) - 1:].isdigit()):
                    utc = utc[0:-1]
                else:
                    tmFndInd = True
            
            outf.write(zoneNm.strip() + "," + utc.strip() + "\n")

        zoneNm = line.replace("Zone", "")
        zoneNm = zoneNm.strip()
        zoneNm = zoneNm.split(":",1)[0]
        zoneNm = zoneNm.split("0",1)[0]
        
        nmFndInd = False

        while nmFndInd == False:
            if (zoneNm.endswith(" ") or zoneNm[len(zoneNm) - 1:].isdigit() or
                zoneNm.endswith("-")):
                zoneNm = zoneNm[0:-1]
            else:
                nmFndInd = True
    elif (line.startswith("\t")):
        prevZoneLn = line


#Process the last zone.
if len(prevZoneLn) > 0:
    zoneLn = prevZoneLn.split("\t")
    utc = zoneLn[3]
    outf.write(zoneNm.strip() + "," + utc.strip())
