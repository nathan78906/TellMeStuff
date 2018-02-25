# TellMeStuff

## Rapheal Ambegia, Nathan Seebarran, Kareem Hage-Ali

### Description

TellMeStuff is a subscription based notification system. It allows the user to subscribe to various topics they are interested in (news, sports, word of the day, etc). It notifies the user via text or email about their subscribed topics. The frequency of the notifications depend on the users preference (realtime, hourly, daily, etc).

### Key Features for the Beta Version 

- Sign up page for the user
- Saving account information into a database
- Secure storage of login, phone number, email
- Allow the user to subscript to 5-7 topics of their choice
	- OAUTH logins for external services
- Text / Email notification
- Monitoring the topic APIs (weather API, sports API, etc)
- Basic UI

### Key Features for the Final Version 

- Home page that displays the user's subscribed topics
- Better UI
- History of notifications per user
- Allow the user to subscribe to 10-15 topics of their choice
- If we have time ...
	- Realtime notifications for specific topics on the web page
	- General statistics for topics (most subscribed, users that have the most subsriptions, etc)
	- Sub-topics for more general topics (specific sport teams, specific topics on news, specific artists in entertainment)
	- Packaging as a desktop app to receive notifications on your computer

### Description of Technology 

- Backend: Python (Django or Flask)
- OAUTH logins for external services
- Various APIs for different topics
- Database: MongoDB or other NoSQL database
- Frontend: React (or TBD)

### 5 Technical Challenges

- Integrating multiple APIs into the web application (SMS, APIs for each subscription topic)
- Learning new frontend and backend development frameworks (see above)
- Realtime notifications on the website
- Managing incoming webooks for different APIs
- Making the UI work for various screen sizes (fully responsive)