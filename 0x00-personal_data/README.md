# Personal Data Protection Project

## Table of Contents
* [Description](#description)
* [Resources](#resources)
* [Learning Objectives](#learning-objectives)
* [Requirements](#requirements)
* [Tasks](#tasks)
  * [1. Regex-ing](#1-regex-ing)
  * [2. Log formatter](#2-log-formatter)
  * [3. Create logger](#3-create-logger)
  * [4. Connect to secure database](#4-connect-to-secure-database)
  * [5. Read and filter data](#5-read-and-filter-data)
  * [6. Encrypting passwords](#6-encrypting-passwords)
  * [7. Check valid password](#7-check-valid-password)
* [Copyright](#copyright)

## Description
This project focuses on implementing measures to protect personal data in a back-end application. It covers topics such as logging, encryption of passwords, database authentication, and filtering sensitive information.

## Resources
Read or watch:
* [What Is PII, non-PII, and Personal Data?](#)
* [Logging Documentation](#)
* [Bcrypt Package](#)
* [Logging to Files, Setting Levels, and Formatting](#)

## Learning Objectives
After completing this project, you should be able to explain to anyone, without the help of Google:
* Examples of Personally Identifiable Information (PII)
* Implementation of a log filter to obfuscate PII fields
* Encryption of passwords and validation of input passwords
* Authentication to a database using environment variables

## Requirements
* All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python3 (version 3.7).
* All files should end with a newline character.
* The first line of all files should be exactly `#!/usr/bin/env python3`.
* Your code should follow the PEP 8 style guide (version 2.5).
* All files must be executable.
* The length of your files will be tested.
* All modules, classes, and functions should have documentation.
* All functions should be type annotated.

## Tasks

### 1. Regex-ing
Write a function called `filter_datum` that returns the log message obfuscated:

```python
filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))

