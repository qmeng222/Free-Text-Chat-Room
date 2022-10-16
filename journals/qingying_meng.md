# Developer's Journal_Qingying

## Template:

- The date of the entry
- A list of features/issues that you worked on and who you worked with, if applicable
- A reflection on any design conversations that you had
- At least one ah-ha! moment that you had during your coding, however small

---

## Friday, 10/14/2022

- Debugged the ValidationError of creating a new user with Andrew's help

  ![API-DB communication: create a user](/images/API-DB-commu1.png)

  ![API-DB communication: create another user](/images/API-DB-commu2.png)

- Finished signup/login/logout/get_token/get_protected endpoints
- Ah-ha! moment:
  - [x] use **_get_current_account_data_** to look for a bearer token in the Authorization header
  - [x] use **_try_get_current_account_data_** to get OPTIONAL current account data
  - [x] use **_try_get_current_account_data_** and **_authenticator.cookie_name_** to send back a payload that contains the JWT for use in fetch calls to non-authenticating services

## Thursday, 10/13/2022

- continue working on JWTdown for FastAPI:
  - [x] create a user
  - [x] easy login (assign a token) & logout (kill the token)
  - [x] get the token after login
  - [x] is api protected (return boolean)
- blocker: received error (pydantic.error_wrappers.ValidationError: 1 validation error for AccountOutWithPw) when creating a new user, tried to debug, but doesn't work, will seek help from my team members.

## Wednesday, 10/12/2022

- edited docker-compose.yaml
- learnt JWTdown for FastAPI:
  - [] FastAPI - Swagger UI: http://localhost:8000/docs

## Tuesday, 10/11/2022

- wrote the userEntity function and listOfUserEntity function
- enabled MongoDB CRUD operations in user_service
- Ah-ha! moment:

## Monday, 10/10/2022

- Edited the Dockerfile & defined services in the compose file
- Experimented MongoDB CRUD operations
- Ah-ha! moment: MongoDB enforces no schemas. Documents don't have to use the same schema inside of one collection.

<br>

## Friday off, 10/7/2022

- Self-learning: developing CRUD application using FastAPI & MongoDB

<br>

## Thursday, 10/6/2022

- updatd ReadMe with responsibilities assigned for each team member, plus MongoDB CRUD operations
- worked on data schemas and data modelling
- Ah-ha! moment: in MongoDB, we can build one-to-many relationsuse using references (e.g. \_id) or using embedded structure

## Wednesday, 10/5/2022

- Created _issues list_ for the work that we want to implement with group agreements.
- Wrote _user story_, _feature_, and _description_ for issue **_Chat_** and issue **_Chats history_**
- Ah-ha! moment: acceptance testing provides a clear and unambiguous “contract” between developers, complementing the unit tests.

<br>

## Tuesday, 10/4/2022

- Added a merge flowchat as well as detailed instructions to ReadMe.
- Disscussed project architecture to coordinate team work. I was assigned to implement the **_chat_** model and related features.
- Finished project setup
- Ah-ha! moment - PostgreSQL vs. MongoDB:
  - Postgres uses SQL; MongoDB uses BSON (NoSQL)
  - Postgres is a relational database management system; MongoDB is a document database.
  - A row in a table has to comply with the data types of the columns. A document can hold any data as key-value pairs.
  - PostgreSQL has a monolithic architecture; MongoDB has a distributed architecture.

<br>

## Monday, 10/3/2022

- Embedded wirefram.png into ReadMe.md (under _Overview_)
- Finished sample service deployment with the help from team member Chris
- Updated ReadMe.md with detailed deployment instructions
- Ah-ha! moment: GitLab project visualbitliy must be set to "public" to allow deployment

<br>

## Sunday, 10/2/2022

- Updated api-design.md to v.2. with corrected data types
- Labelled uncertain data types for further discussion with team members
- Updated project wireframe to v.2. with rearranged layouts

<br>

## Friday, 9/30/2022

- Discussed project topic & details with team members
- Created a live collaboration on Excalidraw at https://excalidraw.com/#room=39a092e7d8562776c544,Hv4ProKb7q01V6opLyDHqg
- Setup a dev-branch called **_qingying_**
- Finished project wirefram v.1.
- Created and finished api-design.md v.1.
- Ah-ha! moment:
  - failed to push to dev-branch (pipeline: failed)
  - solution: git push worked once GitLab account verification is finished