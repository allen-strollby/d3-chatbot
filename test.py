import unittest
import requests


class TestLocationTypeMapping(unittest.TestCase):
    BASE_URL = "http://localhost:8098/chat/ollama"

    def send_get_request(self, query):
        response = requests.get(self.BASE_URL, params={"question": query})
        return response

    def compare_responses(self, actual, expected):
        """
        Compare two dictionaries while ignoring keys in 'args' that have None values
        or are missing in one of them.
        """
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
                # If both are None or equal, continue; else return False
                if actual_value != expected_value and not (
                    actual_value is None and expected_value is None
                ):
                    return False
            elif expected_value is not None:
                # If key is missing in actual and expected value is not None, return False
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

    def test_account_questions(self):
        queries = [
            (
                "Are there any job openings for Python developers?",
                {"location_type": "ACCOUNT", "args": {"job_vacancy": "Python"}},
            ),
            (
                "What are the available job vacancies?",
                {"location_type": "ACCOUNT", "args": {"job_vacancy": None}},
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
                "What food options are available in the cafeteria?",
                {"location_type": "CAFETERIA", "args": {"food_type": None}},
            ),
            (
                "Where can I get something to eat?",
                {"location_type": "CAFETERIA", "args": {"food_type": None}},
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
        query = "Where is the washroom on the second floor?"
        expected_response = {"location_type": "AMENITY", "args": {"type": "washroom"}}
        response = self.send_get_request(query)
        self.assertEqual(response.status_code, 200)
        actual_response = response.json()
        self.assertTrue(self.compare_responses(actual_response, expected_response))

    def test_bank_questions(self):
        queries = [
            (
                "Can I get the contact for ICICI bank?",
                {"location_type": "BANK", "args": {"type": "ICICI"}},
            ),
            (
                "Is there a Federal Bank here?",
                {"location_type": "BANK", "args": {"type": "FEDERAL"}},
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
        query = "Where is the nearest ATM?"
        expected_response = {"location_type": "ATM"}
        response = self.send_get_request(query)
        self.assertEqual(response.status_code, 200)
        actual_response = response.json()
        self.assertTrue(self.compare_responses(actual_response, expected_response))

    def test_store_questions(self):
        queries = [
            (
                "Where can I buy a notebook?",
                {"location_type": "STORE", "args": {"item": "notebook"}},
            ),
            (
                "Is there a store where I can buy items?",
                {"location_type": "STORE", "args": {"item": None}},
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

    def test_tech_bar_questions(self):
        query = "I need help with my laptop."
        expected_response = {"location_type": "TECH_BAR"}
        response = self.send_get_request(query)
        self.assertEqual(response.status_code, 200)
        actual_response = response.json()
        self.assertTrue(self.compare_responses(actual_response, expected_response))

    def test_security_questions(self):
        queries = [
            (
                "I lost my keys, where can I check?",
                {"location_type": "SECURITY", "args": {"item": "keys"}},
            ),
            (
                "Where is the lost and found office?",
                {"location_type": "SECURITY", "args": {"item": None}},
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

    def test_recreation_questions(self):
        query = "I want to play foosball, where can I go?"
        expected_response = {"location_type": "RECREATION"}
        response = self.send_get_request(query)
        self.assertEqual(response.status_code, 200)
        actual_response = response.json()
        self.assertTrue(self.compare_responses(actual_response, expected_response))

    def test_gym_questions(self):
        queries = [
            (
                "What is the fee for the gym?",
                {
                    "location_type": "GYM",
                    "args": {
                        "contact_details": "no",
                        "maintenance_status": "no",
                        "fee_structure": "yes",
                        "application_process": "no",
                        "documents_needed": "no",
                    },
                },
            ),
            (
                "Is the gym under maintenance right now?",
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

    def test_insurance_questions(self):
        query = "How do I get my insurance renewed?"
        expected_response = {"location_type": "INSURANCE"}
        response = self.send_get_request(query)
        self.assertEqual(response.status_code, 200)
        actual_response = response.json()
        self.assertTrue(self.compare_responses(actual_response, expected_response))

    def test_people_questions(self):
        queries = [
            (
                "Who is my manager?",
                {"location_type": "PEOPLE", "args": {"type": "MANAGER"}},
            ),
            (
                "Who is the CEO of the company?",
                {"location_type": "PEOPLE", "args": {"type": "CEO"}},
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
                "Where can I see a doctor?",
                {
                    "location_type": "HEALTH",
                    "args": {"type": "doctor", "booking": False, "availability": False},
                },
            ),
            (
                "Can I book an appointment with the doctor?",
                {
                    "location_type": "HEALTH",
                    "args": {"type": "doctor", "booking": True, "availability": False},
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
                {"location_type": "PLACE", "args": {"name": "Founders Hall"}},
            ),
            (
                "Where is the Main Lobby?",
                {"location_type": "PLACE", "args": {"name": "Main Lobby"}},
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
