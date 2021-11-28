# Newegg Price Scrapper

Hi all,

This is a price scrapper for newegg.com writteh in Python.
Using beautiful soup, the scrapper takes the title 
and price from the HTML, trims off the excess HTMl 
to make it readable, and prints the product and prices.

I found that using the sleep function when running the 
for loop helps with the performance when running a larger list.

To expand off of this, one could wrap this price scrapper into a method,
and then make another method for another website, and adjust the 
trimming methods since the HTML will be different per website. 
You may also have to use a different command for beautiful soup
when pulling the HTML. I found that it was easiest to pull
as a class, but other websites like amazon did not use classes.

A special thanks to Youtuber @Dev Ed, for the inspiration and 
general outline. He has a video that I will link on how to do 
this with amazon.com.

https://www.youtube.com/watch?v=Bg9r_yLk7VY&t=579s

