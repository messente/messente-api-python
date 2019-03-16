# Messente API Library: 0.0.1

[Messente](https://messente.com) is a global provider of messaging and user verification services. Use Messente API library to send and receive SMS, Viber and WhatsApp messages, blacklist phone numbers to make sure you&#39;re not sending any unwanted messages, manage contacts and groups.  Messente builds [tools](https://messente.com/documentation) to help organizations connect their services to people anywhere in the world.

## Installation guide

Install Messente API library with `pip install messente-api`.

## Features

Messente API has the following features:

- Omnichannel ([external docs](https://messente.com/omnichannel-api)),
- Phonebook ([external docs](https://messente.com/phonebook-api)).

Messente API Library provides the operations described below to access the features.


### BlacklistApi

Method | Summary | HTTP Action
------------- | ------------- | -------------
[add_to_blacklist](docs/BlacklistApi.md#add_to_blacklist) | Adds a phone number to the blacklist. | POST
[delete_from_blacklist](docs/BlacklistApi.md#delete_from_blacklist) | Deletes a phone number from the blacklist. | DELETE
[fetch_blacklist](docs/BlacklistApi.md#fetch_blacklist) | Returns all blacklisted phone numbers. | GET
[is_blacklisted](docs/BlacklistApi.md#is_blacklisted) | Checks if a phone number is blacklisted. | GET

### ContactsApi

Method | Summary | HTTP Action
------------- | ------------- | -------------
[add_contact_to_group](docs/ContactsApi.md#add_contact_to_group) | Adds a contact to a group. | POST
[create_contact](docs/ContactsApi.md#create_contact) | Creates a new contact. | POST
[delete_contact](docs/ContactsApi.md#delete_contact) | Deletes a contact. | DELETE
[fetch_contact](docs/ContactsApi.md#fetch_contact) | Lists a contact. | GET
[fetch_contact_groups](docs/ContactsApi.md#fetch_contact_groups) | Lists groups of a contact. | GET
[fetch_contacts](docs/ContactsApi.md#fetch_contacts) | Returns all contacts. | GET
[remove_contact_from_group](docs/ContactsApi.md#remove_contact_from_group) | Remove a contact from a group. | DELETE
[update_contact](docs/ContactsApi.md#update_contact) | Updates a contact. | PATCH

### DeliveryReportApi

Method | Summary | HTTP Action
------------- | ------------- | -------------
[retrieve_delivery_report](docs/DeliveryReportApi.md#retrieve_delivery_report) | Retrieves the delivery report for the Omnimessage | GET

### GroupsApi

Method | Summary | HTTP Action
------------- | ------------- | -------------
[create_group](docs/GroupsApi.md#create_group) | Creates a new group with the provided name. | POST
[delete_group](docs/GroupsApi.md#delete_group) | Deletes a group. | DELETE
[fetch_group](docs/GroupsApi.md#fetch_group) | Lists a group. | GET
[fetch_groups](docs/GroupsApi.md#fetch_groups) | Returns all groups. | GET
[update_group](docs/GroupsApi.md#update_group) | Updates a group with the provided name. | PUT

### OmnimessageApi

Method | Summary | HTTP Action
------------- | ------------- | -------------
[cancel_scheduled_message](docs/OmnimessageApi.md#cancel_scheduled_message) | Cancels a scheduled Omnimessage. | DELETE
[send_omnimessage](docs/OmnimessageApi.md#send_omnimessage) | Sends an Omnimessage. | POST

## Auth

**Type**: HTTP basic authentication

Read the [external getting-started article](https://messente.com/documentation/getting-started) which explains API keys and Sender ID logic.

## Getting started: Messente API Library

TODO: how to send Omnimessage

## License

[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)

## Terms

[https://messente.com/terms-and-conditions](https://messente.com/terms-and-conditions)
