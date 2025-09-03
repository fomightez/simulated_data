# Scripts and resources for generating simulated data for general computation endeavors / Tidy data vs. messy data, etc.

My code
-------

**DESCRIPTIONS**


### ????.py


> ???




Related software by others I have encountered
--------------------------------------------

### Python

* [Silly - A python library for producing fanciful test data.](https://github.com/classam/silly?utm_content=buffera8f2d&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)

* [Faker is a Python package that generates fake data for you](https://github.com/joke2k/faker)


### R

* [Charlatan](https://github.com/ropensci/charlatan) looks to be an R version of Python's 'Faker'
* If you need to generate a more realistic, i.e., 'dirty' data to test on, see https://twitter.com/matthewdlincoln/status/1042364406796038146
>"Teaching data cleaning this semester? My new #rstats package salty for making slightly dirty datasets is now on CRAN: https://cran.r-project.org/package=salty "


* [wakefield](https://github.com/trinker/wakefield) - generates random R data sets and has some tools for visualization

>"Whoa, the wakefield package in #rstats is incredibly helpful for manufacturing example data. Look at the effect of this fake math camp on fake grad school GPAs! 
(full reproducible code here: https://gist.github.com/andrewheiss/51f60fc2a410ca0d321d942153b955e7)
(package link: https://github.com/trinker/wakefield)" SOURCE:[Andrew Heiss](https://twitter.com/andrewheiss/status/1179566764335730688)

* [fabricatr](https://declaredesign.org/r/fabricatr/)
>"See also the fabricatr package, which lets you do this with panel data and other nested structures:"SOURCE:[Andrew Heiss](https://twitter.com/andrewheiss/status/1179566764335730688)

* >"Need to mock or fake something in #Rstats? Check out these packages of @sckottie's at @rOpenSci
📦 https://github.com/ropensci/charlatan … for creating fake data
📦 https://github.com/ropensci/webmockrfor … for stubbing and setting expectations on HTTP requests" - https://twitter.com/ma_salmon/status/993736067022053377

* [messy](https://github.com/nrennie/messy)
>"When teaching examples using R, instructors often using nice datasets - but these aren't very realistic, and aren't what students will later encounter in the real world. Real datasets have typos, missing values encoded in strange ways, and weird spaces. The {messy} R package takes a clean dataset, and randomly adds these things in - giving students the opportunity to practice their data cleaning and wrangling skills without having to change all of your examples."

* ['Creating messy datasets for teaching purposes with {truffle}'](https://mmmdata.io/posts/2025/08/creating-messy-datasets-for-teaching-purposes-with-truffle/):
>"{truffle} is an R package for teaching users to process data.  
It allows you to create datasets with various known effects to be rediscovered (truffles, via truffle_ functions), and then create data processing headaches that have to be solved (dirt, via dirt_ functions). Users must then search for truffles among the dirt.  
Generated datasets can include demographics variables and item-level Likert responses. Known effects (truffles) can be buried in the data including differences in sum-score means between conditions, known correlations between the different outcomes’ sum-scores, known Cronbach’s alpha values for each scale, etc.  
Data can then be made dirty in several different ways to create common data processing challenges, such as poorly named columns that disagree with R, duplicate rows, missingness with irregular codings, mixed date formats, untidy demographics data with misspellings and erroneous entries, number columns with comma seperators and units, impossible values beyond the scale range, header rows that disrupt reading data into R, and untidy columns that contain more than one variable."


Related resources
----------------

*?
