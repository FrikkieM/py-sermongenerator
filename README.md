# py-sermongenerator
A simple HTML generator for Taberna Dei. 

It accepts a date in YYYYMMDD and then looks in the 'WebsitePreke' subfolder (relative to the script's path) for all sermons preached on that date.
These are then ordered by campus. 

It then generates the HTML for the Campus, Pastor, Title, MP3 link and PDF link for our church's website in format.

<b>Usage:</b>
py main.py YYYYMMDD

<em>Example:</em>
py main.py 20190725


Sermon files are in the following format:<br>
YYYYMMDD_CAMPUS_PASTOR_TITLE.mp3 and YYYYMMDD_CAMPUS_PASTOR_TITLE.pdf in the 'WebsitePreke' folder.

Example:
20190725_TDO_DO_My_sermon_title.mp3 and 20190725_TDO_DO_My_sermon_notes.pdf


