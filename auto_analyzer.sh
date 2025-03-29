#!/bin/bash
LOGFILE="sample.log"
OUTPUTFILE="incident_report.txt"

python analyzer.py "$LOGFILE" >> "$OUTPUTFILE"
echo "Log analyzed at $(date)" >> "$OUTPUTFILE"
