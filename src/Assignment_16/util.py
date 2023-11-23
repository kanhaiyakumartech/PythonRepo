import re

def valid_email_or_not(s):
    return bool(re.match(r'^([a-z0-9_\-]+)@([a-z0-9]+)\.([a-z]{1,3})$', s))

def filtered_emails(emails):
    return sorted(filter(valid_email_or_not, emails))
