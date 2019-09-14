# WorkingSeniorProject
Storage of my senior project, recreated because of fatal errors

Stage1 contains scripts for running a SQL injection on the DVWA VM

Stage2 contains scripts to determine if pages of a domain are vulnerable to SQL Injection
	
	Usage: Run main.py and enter a domain name. Sit back and watch

	Current Steps:
		1. Get the domain name from the user (if needed add the "http://")
		2. Checks for sitemap
			2a. If finds sitemap, retrieves url's from the xml file
			2b. If no sitemap/bad sitemap retirieves all url's in href tags
		3. Modify url's into usable forms
			3a. Iterate through list of url's and change "#" to domain index
			3b. Iterate through list and add domain name to "url's" that start with "/"
		4. Creates new list that only contains links belonging to the domain
		5. Remove duplicates from list of domain url's
		6. Attempt to reach url's from list of non-duplicate domain url's and create list/file of valid domain links
		   Prints each url and whether it was reached, also prints progress
			6a. If reachable, add url to list of valid links and add to text file with valid links 
			6b. If not reachable print "url" is bad, and do nothing with it
