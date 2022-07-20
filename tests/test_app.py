import unittest
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Vi-Linh</title>" in html

        # TODO Add more test relating to the home page
        assert "<meta charset=\"utf-8\" />" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    # tests relating to the /api/timeline_post GET and POST apis
    
    def test_timeline_first_post_get(self):
        # testing POST api
        response = self.client.post(
            "/api/timeline_post", 
            data={
                "name": "One", 
                "email": "test-one@test.com", 
                "content": "Test One Content"
                }
        )
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == "One"
        assert json["email"] == "test-one@test.com"
        assert json["content"] == "Test One Content"

        # testing GET api
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1

        # tests relating to the timeline page
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        assert "<title>Timeline</title>" in html
        assert 'name="name"' in html
        assert 'type="email"' in html
        assert 'name="content"' in html

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
    
    


