# Splunk_whoismonkey
whois app for Splunk by Jack Rasgaitis

Splunk add-on to perform whois requests and returns a JSON response. Extract IP addresses from your index data into a field name ip. This field is used as the input for external lookups.


Installation

Copy the add-on whoismonkey and its contents into $SPLUNK_HOME/etc/apps/ directory. Restart Splunk.

Search example

*|lookup whoisLookup ip OUTPUT whois

This creates a whois field for the events of the extracted ip field. The whois field contain the whois response in JSON format.  

Other example

* | lookup whoisLookup ip| search ip="x.x.x.x"
