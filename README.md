# Goodreads-Quotes-Extractor
Simple python script that requests the name of a book/author and prints out the top 30 relevant quotes as found on Goodreads (www.goodreads.com)

## How to use this?

##### Get the python wrapper for Goodreads API
      First download the zip from https://github.com/sefakilic/goodreads 
      Extract it to your current directory
      Under the 'goodreads' subdirectory, look for the 'client.py' file
      Look for the search_books function and modify the return statement to the following:

              return [(work['id']['#text']) for work in works]
      
##### Get a developer key from the Goodreads website

##### Replace the CONSUMER_KEY and CONSUMER_SECRET strings with your developer key and key-secret

##### Run the python code from the terminal
  
