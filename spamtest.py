""" spamtest.py
Send EICAR file and GTUBE string to target mail server to check spam rules.
Usage:
    spamtest.py [options] -r <recipient> -s <sender> -d <destmta> [options]

Options:
    -v, --verbose       Print verbose messages on cli
    -c, --relaycheck    Check if server accepts a relay to test@test.com

"""
__author__ = 'olivier'

# import statements
from docopt import docopt
from email.message import Message
from smtplib import SMTPConnectError
from smtplib import SMTPRecipientsRefused
import logging as log
import smtplib


def send_mail(sender,
              recipient,
              dstmta,
              subject,
              body,
              verbose):
    """
    Sends e-mail to specific server.
    """
    msg = Message()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_payload(body)

    try:
        server = smtplib.SMTP(dstmta)
        if verbose:
            log.info("smtp debug level was set to 1")
            server.set_debuglevel(1)
        server.sendmail(sender, recipient, msg.as_string())
        print "Successfully sent email"
    # if no success code an
    except SMTPConnectError as smtpconnerr:
        log.error("unable to send mail")
        log.error(smtpconnerr)


def main():
    """
    Main function
    """
    # generic virus test string
    EICARSTR = ('X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*]')
    # generic spam test string
    GTUBESTR = ('XJS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X')
    # subjects for mails
    subjectvirus = "Virus Testmail"
    subjectspam = "Spam Testmail"

    # gets arguments from docopt
    arguments = docopt(__doc__)
    # assigns docopt arguments
    sender = arguments['<sender>']
    recipient = arguments['<recipient>']
    destmta = arguments['<destmta>']
    verbose = arguments['--verbose']
    relaycheck = arguments['--relaycheck']

    # set log level to verbose if user has chosen -v, --verbose
    if verbose:
        log.basicConfig(format="%(levelname)s: %(message)s", level=log.DEBUG)
        log.info("Verbose output activated.")
    else:
        log.basicConfig(format="%(levelname)s: %(message)s")

    # print arguments to console
    log.info("arguments are: ")
    log.info(arguments)

    # send spam testmail
    log.info("Sending Eicar Mail")
    send_mail(sender, recipient, destmta, subjectvirus, EICARSTR, verbose)
    log.info("Sending Gtubestring Mail")
    send_mail(sender, recipient, destmta, subjectspam, GTUBESTR, verbose)
    # if user has specified --relaycheck
    if relaycheck:
        log.info("Trying Relay:")
        recipient = "test@test.com"
        # should fail with SMTPREcipientsRefused
        try:
            send_mail(sender, recipient, destmta,
                      subjectspam, GTUBESTR, verbose)
        # test is OK if server refuses relay
        except SMTPRecipientsRefused as rcptrefused:
            log.info("Relaying not accepted: OK")
            log.info(rcptrefused)


if __name__ == "__main__":
    main()
