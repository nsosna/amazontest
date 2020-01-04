Feature: search Amazon
 
Background:
Given Open http://www.amazon.com
Scenario: search the term
Given enter term "Software Development"
When the customer submits the search
Then the results of that search are displayed
And the number of results is displayed as a positive integer
When the customer doesn't enter the search term
Then the related items get displayed