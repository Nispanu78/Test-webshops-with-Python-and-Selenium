
Feature: I want to search for products

 Scenario Outline: Search
    Given I am on home page
    when I search for <term>
    then I should see results <search_count> in search results

 Examples: By category
    | term    | search_count |
    | cardigan | 2            |

 Examples: By product name
    | term      	  | search_count |
    |  earbuds        | 0            |