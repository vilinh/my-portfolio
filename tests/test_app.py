from app import app
import unittest
import os
os.environ['TESTING'] = 'true'


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Vi-Linh</title>" in html
        assert "<h1>vi-linh vu</h1>" in html
        assert "<div class=\"home\">" in html

    def test_timeline_page_form(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert 'name="name"' in html
        assert 'name="email"' in html
        assert 'name="content"' in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

    def test_timeline_post(self):
        info = {"name": "vi", "email": "test2@gmail.com",
                "content": "hello world!"}
        response = self.client.post("/api/timeline_post", data=info)
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert json["name"] == "vi"
        assert json["email"] == "test2@gmail.com"
        assert json["content"] == "hello world!"

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1

        self.client.post("/api/timeline_post", data=info)

        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 2

    def test_timeline_post_html(self):
        info = {"name": "vi", "email": "test2@gmail.com",
                "content": "hello world!"}
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert "vi" in html
        assert "test2@gmail.com" in html
        assert "hello world!" in html
