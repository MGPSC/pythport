# Software Requirements

## Vision

The vision of the product is to create a locally used password management CLI. The tool will be accessed using a single master login. It will provide users with a place to securely store and retrieve passwords without needing to rely on a third party web service to do so.

People should care about this because companies like Google and Mozilla are at risk of being hacked. With the recent rise in cyber-attacks, moving password management to the local machine level may be a solution to help keep secure information secure.

## Scope

* IN
  * Provide a place for users to store and retrieve login information for various websites or accounts
  * Encrypt passwords locally to keep them safe while stored
  * Restrict access to application and data based on single master password, created by user upon initial setup of app
  * Users will be able to add, retrieve, and modify login information after logging in with their master password
* OUT
  * App will not allow access to any stored information if user password is not provided
  * App will not support multiple accounts within the same instance. Limited to local operation.
  * App will not save user information to a cloud or server of any kind.

## Functional Requirements

* A user will have to provide a master password to access information stored in the application
* A user will be able to add, retrieve, and modify saved logins
* The application will store login information in a raw .txt file, with the password two-way encrypted for safety while stored
* The application will save the master password in a hashed form using one-way encryption.

## Non-Functional Requirements

* Security
  * Passwords will be securely encrypted and retrieved in a way that prevents bad actors from figuring out.
  * Python bcrypt may be a solution here, with utilization of hashing/salting
* Usability
  * Since this is a CLI app, interface will have to be well explained to the user.
  * Most navigation will be performed using number inputs that correspond to a "path" through the app that the user can take for actions.
