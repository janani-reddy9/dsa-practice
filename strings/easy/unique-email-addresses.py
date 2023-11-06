"""
https://leetcode.com/problems/unique-email-addresses/description/
"""


def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    output = []
    for email in emails:
        localname, domainname = email.split("@")[0], email.split("@")[1]
        localname = localname.replace(".", "")
        changed_localname = localname.split("+")[0]
        output.append(changed_localname+"@"+domainname)
    return len(set(output))


print(numUniqueEmails(["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]))
