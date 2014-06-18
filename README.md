# Spam Test Script
Sends a EICAR file and a GTUBE string to recipient to test functionality of the spam filter. 

## Background Information
* For information about EICAR file, see: http://www.eicar.org/86-0-Intended-use.html
* For information about GTUBE string, see: http://spamassassin.apache.org/gtube/

Note: 
    The GTUBE string may not be implemented in your spam filter software. Implement
    pattern recognition to test your appliance. 

## Usage

    $ spamtest.py -h 
    spamtest.py
    Send EICAR file and GTUBE string to target mail server to check spam rules.
    Usage:
        spamtest.py [options] -r <recipient> -s <sender> -d <destmta>
    
    Options:
        -v, --verbose       Print verbose messages on cli
