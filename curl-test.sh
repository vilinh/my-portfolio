#!/bin/bash

curl -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=testing&email=testing@gmail.com&content=testing posting to db!'

curl http://127.0.0.1:5000/api/timeline_post
