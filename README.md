## Requirements.

Python 3.11+ with pip for host or docker

## Installation & Usage

```sh
git clone https://github.com/dv4mp1r3/spacebot.git
cd spacebot
cp residents.csv.example residents.csv
cp .env.example .env
```

## Getting Started (docker)

First of all, edit files .env and residents.csv (fill in the correct data).

Then build and run docker container: ```docker build -t your/tag:1.0 . && docker run your/tag:1.0```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ResidentsApi* | [**list_residents**](docs/ResidentsApi.md#list_residents) | **GET** /api/tg-accounting/residents/debt | Get residents list
*TransactionsApi* | [**transaction_log**](docs/TransactionsApi.md#transaction_log) | **GET** /api/tg-accounting/transactions/{userId} | Transaction log for resident


## Documentation For Models

 - [Error](docs/Error.md)
 - [Resident](docs/Resident.md)
 - [Transaction](docs/Transaction.md)


## Documentation For Authorization

## bearerAuth

- **Type**: Bearer authentication

