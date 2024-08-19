Property for sale Consultation


Technologies Used

Lenguage: Python

Database: MySQL

Testing: Unittest

Development: Test-Driven Development (TDD)

Style Guide: PEP8


Development

Phase 1: Development of the Query Service

- Write unit tests that cover the basic functionalities of the service using TDD
- Implement an API that allows users to query properties with different filters
- Improve quality code
- Create a JSON file  with data and run tests


Phase 2: Conceptual Development of the Like Service

- Design an Entity-Relationship (ER) diagram
- Generate the SQL code to extend the database model
- Explain the design decisions in this README


Execution Instructions

Clone the repository

pip install -r requirements.txt

Run the program: go run main.go

python main.py


How to Test the Application

curl -X GET "http://localhost:8000/properties?year=2020&city=bogota&status=en_venta"


Like table

The like table was designed with efficiency and flexibility in mind. By including the is_active field, users can "deactivate" a "Like" without needing to delete the record, which helps maintain a complete history of interactions. Additionally, this approach ensures data integrity through foreign keys, so that every "Like" is always linked to a valid user and property. This is crucial not only for maintaining consistency in the database but also for facilitating future user behavior analysis.
