import unittest
import requests


class TestLocationTypeMapping(unittest.TestCase):
    BASE_URL = "http://0.0.0.0:8000/chat/ollama"

    def send_get_request(self, query):
        response = requests.get(self.BASE_URL, params={"question": query})
        return response

    def compare_responses(self, actual, expected):
        print("Actual: ", actual)
        print("Expected: ", expected)
        print()
        if actual["location_type"] != expected["location_type"]:
            return False

        actual_args = actual.get("args", {})
        expected_args = expected.get("args", {})

        for key, expected_value in expected_args.items():
            if key in actual_args:
                actual_value = actual_args[key]
                if actual_value != expected_value and not (
                    actual_value is None and expected_value is None
                ):
                    return False
            elif expected_value is not None:
                return False

        return True

    def test_conference_questions(self):
        queries = [
            (
                "I need a meeting room for 7 people.",
                {
                    "location_type": "CONFERENCE",
                    "args": {"number_of_people": 7, "floor_number": None},
                },
            ),
            (
                "Get me a meeting room for 3 people on the 2nd floor.",
                {
                    "location_type": "CONFERENCE",
                    "args": {"number_of_people": 3, "floor_number": 2},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_job_vacancy_questions(self):
        queries = [
            (
                "Are there any job vacancies for Python developers?",
                {
                    "location_type": "ACCOUNT",
                    "args": {"job_vacancy": "python"},
                },
            ),
            (
                "What job vacancies do you have?",
                {
                    "location_type": "ACCOUNT",
                    "args": {"job_vacancy": None},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_cafeteria_questions(self):
        queries = [
            (
                "What food is available in the cafeteria?",
                {
                    "location_type": "CAFETERIA",
                    "args": {"food_type": None},
                },
            ),
            (
                "I want to have a sandwich for lunch.",
                {
                    "location_type": "CAFETERIA",
                    "args": {"food_type": "sandwich"},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_amenity_questions(self):
        queries = [
            (
                "Where is the washroom on the first floor?",
                {
                    "location_type": "AMENITY",
                    "args": {"type": "washroom"},
                },
            ),
            (
                "Where can I find a washroom?",
                {
                    "location_type": "AMENITY",
                    "args": {"type": "washroom"},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_bank_questions(self):
        queries = [
            (
                "I want to open an account in ICICI.",
                {
                    "location_type": "BANK",
                    "args": {"type": "ICICI"},
                },
            ),
            (
                "Tell me about FEDERAL bank services.",
                {
                    "location_type": "BANK",
                    "args": {"type": "FEDERAL"},
                },
            ),
            (
                "What about HDFC bank?",
                {
                    "location_type": "BANK",
                    "args": {"type": None},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_atm_questions(self):
        queries = [
            (
                "Where is the nearest ATM?",
                {
                    "location_type": "ATM",
                },
            ),
            (
                "Can you tell me about ATMs on campus?",
                {
                    "location_type": "ATM",
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_technical_support_questions(self):
        queries = [
            (
                "I need help with my laptop.",
                {
                    "location_type": "TECH_BAR",
                },
            ),
            (
                "How do I troubleshoot my software issues?",
                {
                    "location_type": "TECH_BAR",
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_security_questions(self):
        queries = [
            (
                "I lost my umbrella.",
                {
                    "location_type": "SECURITY",
                    "args": {"item": "umbrella"},
                },
            ),
            (
                "Where can I report lost items?",
                {
                    "location_type": "SECURITY",
                    "args": {"item": None},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_gym_questions(self):
        queries = [
            (
                "What are the fees for the gym?",
                {
                    "location_type": "GYM",
                    "args": {
                        "contact_details": "yes",
                        "maintenance_status": "no",
                        "fee_structure": "yes",
                        "application_process": "yes",
                        "documents_needed": "no",
                    },
                },
            ),
            (
                "Is the gym open for maintenance?",
                {
                    "location_type": "GYM",
                    "args": {
                        "contact_details": "no",
                        "maintenance_status": "yes",
                        "fee_structure": "no",
                        "application_process": "no",
                        "documents_needed": "no",
                    },
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_health_questions(self):
        queries = [
            (
                "Where can I get my cold checked?",
                {
                    "location_type": "HEALTH",
                    "args": {
                        "type": "doctor",
                        "booking": "True",
                        "availability": "True",
                    },
                },
            ),
            (
                "I have a headache and need to see a doctor.",
                {
                    "location_type": "HEALTH",
                    "args": {
                        "type": "doctor",
                        "booking": "True",
                        "availability": "True",
                    },
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_place_questions(self):
        queries = [
            (
                "Where is Founders Hall?",
                {
                    "location_type": "PLACE",
                    "args": {"name": "Founders Hall"},
                },
            ),
            (
                "How do I get to the Main Lobby?",
                {
                    "location_type": "PLACE",
                    "args": {"name": "Main Lobby"},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_people_questions(self):
        queries = [
            (
                "Who is my manager?",
                {
                    "location_type": "PEOPLE",
                    "args": {"entity_type": "MANAGER"},
                },
            ),
            (
                "Who is my HR?",
                {
                    "location_type": "PEOPLE",
                    "args": {"entity_type": "HR"},
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )

    def test_insurance_questions(self):
        queries = [
            (
                "I want to get my insurance renewed.",
                {
                    "location_type": "INSURANCE",
                },
            ),
            (
                "Who should I contact for insurance queries?",
                {
                    "location_type": "INSURANCE",
                },
            ),
        ]
        for query, expected_response in queries:
            with self.subTest(query=query):
                response = self.send_get_request(query)
                self.assertEqual(response.status_code, 200)
                actual_response = response.json()
                self.assertTrue(
                    self.compare_responses(actual_response, expected_response)
                )


if __name__ == "__main__":
    unittest.main()
