#!/usr/bin/env python3
# Simple Challenge-Response Authentication with Replay Attack Detection

import hashlib
import random
import time

# ----- User database (username: password) -----
USER_DB = {
    "alice": "password123",
    "bob": "mypassword"
}

# Store used nonces to detect replay attacks
USED_NONCES = set()

# ----- Helper functions -----
def generate_nonce():
    """Generate a random number as challenge"""
    return str(random.randint(100000, 999999))

def hash_response(password, nonce):
    """Compute hash of password + nonce"""
    data = password + nonce
    return hashlib.sha256(data.encode()).hexdigest()

def authenticate(username):
    """Simulate challenge-response authentication"""
    if username not in USER_DB:
        print("Invalid username!")
        return False

    password = USER_DB[username]

    # Server generates challenge
    nonce = generate_nonce()
    print("\nServer: Your challenge is:", nonce)

    # Client computes response
    response = hash_response(password, nonce)
    print("Client: Sending response hash:", response)

    # Replay attack detection
    if response in USED_NONCES:
        print("Server: Replay attack detected! Authentication failed.")
        return False

    # Server verifies response
    expected = hash_response(password, nonce)
    if response == expected:
        print("Server: Authentication successful!")
        USED_NONCES.add(response)
        return True
    else:
        print("Server: Authentication failed!")
        return False

# ----- Main Program -----
print("=== Challenge-Response Authentication Simulation ===")
username = input("Enter username: ")

# First authentication attempt
authenticate(username)

# Simulate replay attack
print("\n--- Simulating Replay Attack ---")
print("Client tries to resend same response...")
# Using last used response
if USED_NONCES:
    replay_response = list(USED_NONCES)[-1]
    print("Replaying hash:", replay_response)
    if replay_response in USED_NONCES:
        print("Server: Replay attack detected! Authentication failed.")
