This project consists of basic implementation of keylogger. 

It logs in these 3 ways within the time interval of 60 seconds - 
1) It logs any sequence of events by mouse or keyboard of less than 300 in a variable. 
2) If sequence of events greater than 300 but less than 500, it takes screenshot of the whole screen as it is better stored as png file.
3) If events are greater than 500, it logs all into a text file.

After every interval, it sends the variable data/ png file/ text file to the host using smtplib library and necessary email credentials.
