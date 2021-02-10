# scraper-imslp-composer-dates
A simple web scraper to get composers' birth and death dates from IMSLP. 

The script creates the function composerDates(). The function takes a list of composer names taken from IMSLP and scrapes their IMSLP webpages to collect their birth and death year. It returns a pandas df wherein each row has a composer name birth and death years (if available and retrieved), the length of each year (e.g., 1984 -> 4), and a column showing whether the composers' info could be retrieved (yes/no). Additionally, the function writes the df to a .csv file.

Args are:
* composer_names: a pandas series with composers names as they appear in IMSLP (*)
* wd: the working directory
* output_file: a filename wherein to write results (e.g., 'file.csv')
    
  (*) Note not just any name will work. The scraper feeds on composer names as they appear in the IMSLP database. E.g., 'Mozart, Wolfgang Amadeus' and not just 'Mozart'. I also provide a .csv with ~3500 composer names taken from IMSLP.
  
This is part of a much larger MIR (i.e., music information retrieval) project that combines symbolic music notation and composer metadata. You can check out a part of it [here](https://sites.google.com/view/mgigena/misc).
