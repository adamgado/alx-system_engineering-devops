0x19. Postmortem

Issue Summary:

The duration of the access issue spanned approximately two days, specifically from August 14th at 6 AM (EEST) to August 16th at 7 PM (EEST). During this challenging period, users encountered significant difficulties in accessing the web servers, with many unable to log in due to an error message indicating "permission denied (public key)." While an exact count of affected users was not documented, discussions held within the Discord channel revealed that a considerable number of individuals were facing the same problem. Estimates suggest that between 40% to 60% of users experienced this login issue, highlighting the widespread impact of the situation across our user base. The underlying root cause of this access problem was found to be the failure to detect the RSA key properly, which left many users frustrated and unable to access essential tools for the projects.


Timeline:

The issue was initially identified by an engineer attempting to access one of the web servers. Upon realizing the problem, the engineer verified the existence of the RSA key and attempted to refresh the servers in hopes of resolving the issue. Unfortunately, these measures did not yield any positive results or improvements. In an effort to find a solution, the engineer reached out to cohort mentors and fellow peers for assistance, seeking collaboration to take care of the problem effectively. Ultimately, this was resolved by generating a new RSA key and replacing the existing one on the server, restoring access for users and alleviating their concerns.


Root Cause and Resolution:

The primary issue stemmed from the server's inability to detect the RSA key pair correctly. This failure was traced back to a mismatch between the key stored in the sandbox environment and the one held in the intranet profile. The problem was effectively resolved through the generation of a new key pair, which was then updated in both the sandbox and intranet profile, ensuring proper functionality and restoring user access without further complications.


Corrective and Preventative Measures:

To mitigate similar issues in the future, several improvements are necessary. First and foremost, enhancing communication with cohort mentors is crucial. The resolution process could have been expedited significantly if users had direct access to expert advice and guidance. Additionally, it is essential to check the key pair thoroughly when launching a new sandbox environment. Regularly logging into the servers will help identify potential issues early on, and updating the RSA key pair at regular intervals will ensure that all access permissions remain valid and functional. By implementing these corrective and preventative measures, we hope to improve the accessibility of our web servers, ultimately providing a more seamless experience for all users.

