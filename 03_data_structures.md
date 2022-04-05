# Chapter 3 Data Structures

## Exercise 1
> If you had a spreadsheet with data, which pandas data structure would you use to hold the data? Why?

Given the two dimensional nature of most of the data that I work with in spreadsheets, I'd select to use a DataFrame to hold these data. For me, there are rarely times where I'd elect to use a series to hold data other than temporarily (usually as part of a data pipeline prior to that series being stored in its proper context as part of a DataFrame).

## Exercise 2
> If you had a database with data, which pandas data structure would you use to hold the data? Why?

My answer here is quite similar to that above. I'd select a DataFrame in most instances becuase the majority of the data with which I work is two dimensional. There are also added perks associated with data base style manipulations (joins, unions, etc.) that I feel are best replicated with a DataFrame as the operative mental model.