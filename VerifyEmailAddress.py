import re
import dns.resolver
from optparse import OptionParser

# parse incoming arguments
parser = OptionParser()
parser.add_option("-e", "--email", dest="email", help ="Email address to check")
(options, args) = parser.parse_args()

# Simple Regex for syntax checking
regex = '^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$'

# Email address to verify
inputAddress = options.email
addressToVerify = str(inputAddress)

# Syntax check
match = re.match(regex, addressToVerify)
if match == None:
	print 'Bad syntax'
    
else:
    # Get domain for DNS lookup
    splitAddress = addressToVerify.split('@')
    domain = str(splitAddress[1])
   
    #try to contact the domain 
    try:
        records = dns.resolver.query(domain, 'MX')
        mxRecord = records[0].exchange
        mxRecord = str(mxRecord)
        print "Good"
    except :
        print "Bad domain name"
