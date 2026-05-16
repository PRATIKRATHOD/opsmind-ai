import unittest

from app.agents import incident_memory_agent


class FakeModel:

    def encode(self, query):
        return [0.1, 0.2, 0.3]


class FakeCollection:

    def __init__(self, documents):
        self.documents = documents

    def query(self, query_embeddings, n_results):
        return {
            "documents": [
                self.documents
            ]
        }


class IncidentMemoryTests(unittest.TestCase):

    def setUp(self):
        self.original_model = incident_memory_agent._model
        self.original_collection = incident_memory_agent._collection
        incident_memory_agent._model = FakeModel()

    def tearDown(self):
        incident_memory_agent._model = self.original_model
        incident_memory_agent._collection = self.original_collection

    def test_search_similar_incidents_returns_matches(self):
        incident_memory_agent._collection = FakeCollection(
            [
                "previous payment failure incident"
            ]
        )

        result = incident_memory_agent.search_similar_incidents(
            "payment failures"
        )

        self.assertEqual(
            result["status"],
            "SIMILAR_INCIDENTS_FOUND"
        )
        self.assertEqual(
            result["matches"],
            [
                "previous payment failure incident"
            ]
        )

    def test_search_similar_incidents_handles_empty_results(self):
        incident_memory_agent._collection = FakeCollection([])

        result = incident_memory_agent.search_similar_incidents(
            "payment failures"
        )

        self.assertEqual(
            result,
            {
                "status": "NO_SIMILAR_INCIDENTS"
            }
        )


if __name__ == "__main__":
    unittest.main()
