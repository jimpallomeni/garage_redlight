#!/bin/bash

# Created by John Impallomeni
# April 3, 2015
# Version 1.0



NOW=$(date +"%R")

# Edit with your email
echo "Garage Door Open" | mail -s $NOW xxxxxxxxxx@vtext.com
