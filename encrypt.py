import uuid
import hashlib

# sh256 - password hashing
def encrypt_pass(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

# salting 
def salting_pass(sha_signature):
    salt = uuid.uuid4().hex
    salted_signature = sha_signature+':'+salt
    return salted_signature
