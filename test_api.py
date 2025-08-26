#!/usr/bin/env python3
"""
Simple test script for the TODO API
Run this after starting the API to test basic functionality
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_api():
    print("🧪 Testing TODO API...")
    
    # Test health check
    print("\n1. Testing health check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"   ✅ Health check: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"   ❌ Health check failed: {e}")
        return
    
    # Test root endpoint
    print("\n2. Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"   ✅ Root endpoint: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"   ❌ Root endpoint failed: {e}")
    
    # Test creating a todo
    print("\n3. Testing create todo...")
    todo_data = {
        "title": "Test TODO",
        "description": "This is a test todo item"
    }
    try:
        response = requests.post(f"{BASE_URL}/todos", json=todo_data)
        if response.status_code == 201:
            created_todo = response.json()
            todo_id = created_todo["id"]
            print(f"   ✅ Created todo: {response.status_code} - ID: {todo_id}")
            print(f"      Title: {created_todo['title']}")
            print(f"      Description: {created_todo['description']}")
            print(f"      Completed: {created_todo['completed']}")
        else:
            print(f"   ❌ Create todo failed: {response.status_code}")
            return
    except Exception as e:
        print(f"   ❌ Create todo failed: {e}")
        return
    
    # Test getting all todos
    print("\n4. Testing get all todos...")
    try:
        response = requests.get(f"{BASE_URL}/todos")
        if response.status_code == 200:
            todos = response.json()
            print(f"   ✅ Get all todos: {response.status_code} - Found {len(todos)} todos")
        else:
            print(f"   ❌ Get all todos failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Get all todos failed: {e}")
    
    # Test getting specific todo
    print("\n5. Testing get specific todo...")
    try:
        response = requests.get(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            todo = response.json()
            print(f"   ✅ Get specific todo: {response.status_code} - {todo['title']}")
        else:
            print(f"   ❌ Get specific todo failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Get specific todo failed: {e}")
    
    # Test updating todo
    print("\n6. Testing update todo...")
    update_data = {"completed": True}
    try:
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=update_data)
        if response.status_code == 200:
            updated_todo = response.json()
            print(f"   ✅ Update todo: {response.status_code} - Completed: {updated_todo['completed']}")
        else:
            print(f"   ❌ Update todo failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Update todo failed: {e}")
    
    # Test toggle todo
    print("\n7. Testing toggle todo...")
    try:
        response = requests.patch(f"{BASE_URL}/todos/{todo_id}/toggle")
        if response.status_code == 200:
            toggled_todo = response.json()
            print(f"   ✅ Toggle todo: {response.status_code} - Completed: {toggled_todo['completed']}")
        else:
            print(f"   ❌ Toggle todo failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Toggle todo failed: {e}")
    
    # Test deleting todo
    print("\n8. Testing delete todo...")
    try:
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            print(f"   ✅ Delete todo: {response.status_code} - {response.json()}")
        else:
            print(f"   ❌ Delete todo failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Delete todo failed: {e}")
    
    # Verify deletion
    print("\n9. Verifying deletion...")
    try:
        response = requests.get(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 404:
            print(f"   ✅ Todo deletion verified: {response.status_code} - Todo not found")
        else:
            print(f"   ❌ Todo deletion verification failed: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Todo deletion verification failed: {e}")
    
    print("\n🎉 API testing completed!")

if __name__ == "__main__":
    print("Waiting for API to start...")
    time.sleep(2)  # Give the API time to start
    test_api()
