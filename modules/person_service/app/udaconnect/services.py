import logging
from typing import Dict, List

from app import db
from app.udaconnect.models import Person


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("udaconnect-api-person-service")


class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        try:
            db.session.add(new_person)
            db.session.commit()
            logger.info("Person created successfully.")
        except Exception as e:
            logger.error(e)
            db.session.rollback()

        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        logger.info("Person retrieved successfully by id.")
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        logger.info("Persons retrieved successfully.")
        return db.session.query(Person).all()
