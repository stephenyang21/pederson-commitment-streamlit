from ecdsa import SECP256k1, SigningKey
import hashlib


def generate_key():
    # Generate a private key
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return private_key, public_key


def check_point_on_curve(point, curve=SECP256k1):
    x = point.x()
    y = point.y()
    p = curve.curve.p()
    
    # Check if the point satisfies y^2 = x^3 + 7 (mod p)
    return (y * y) % p == (x * x * x + 7) % p


def commitment(m_hex, r_hex, curve=SECP256k1):
    # Ensure m and r are integers
    m = int(m_hex, 16)
    r = int(r_hex, 16)

    G = curve.generator
    order = G.order()
    
    hash_of_zero = hashlib.sha256(b'0').digest()
    scalar = int.from_bytes(hash_of_zero, byteorder="big") % order
    H = scalar * G


    C = m * G + r * H

    return C, C.x(), C.y()

def generate_key():
    # Generate a private key
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    return  public_key