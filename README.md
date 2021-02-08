# ECSE3038_Lab2
## Aim
This lab is meant to get students more accustomed to the technologies used in designing and implementing a RESTful API server.
## Requirements
The task design a RESTful API that allows each IoT enabled water tank to interface with your server so that the measure values can be represented visually on a web page. The web page will be designed by another member of your team.

The API should also support the maintenance of a simple user profile.

The server should be able to perform the actions of a simple HTTP web server. The server should be able to perform actions on a resource such as Create, Read, Update and Delete.

The server was designed to host 7 specific HTTP routes: 
- GET /profile
- POST /profile
 - PATCH /profile
- GET /data
- POST /data
- PATCH /data/:id
- DELETE /data/:id

## Required Attributes
### Profile
- Username
- Favourite color
- Role
### Tank
- Tank id
- Tank location
- Percent full
- Latitude
- Longitude
