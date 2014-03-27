gwi-client
==========

Git With It Client

## Intent
Provide a chat client that allows collaberation by adding
context via "plugged-in" third-party tools, systems, etc.

Github will be one example of this.

### Components
* The leader: Flask server (manufacturedba/gwi-server)
* The scout: RabbitMQ
* The soldiers: Ngrok & [Github...
* The demoman: MongoDB (pymongo)
* The lady in the red dress: Kivy

### Usage
    from gwi import Client
    from hooks import Github

    client = Client.login("username", "password")
    github = Github.auth(client.github)
    commit = github.get_commit("manufacturedba/gwi-client", 789456123)

    contact = client.get_contact("mybestfriend123")
    group = client.get_group("bestbuddies")

    client.send_message("Hello bestfriend", contact.username)
    client.send_message("Hey, can you guys look at " + commit, group.groupname)
**and it should be as simple/easy as this!**
