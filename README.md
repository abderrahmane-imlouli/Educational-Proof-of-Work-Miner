# Educational Proof-of-Work Miner

An educational Python project that demonstrates how **Proof-of-Work (PoW)** mining works by searching for a nonce that satisfies a configurable hash difficulty.

> **Disclaimer:** This project is **not** a Bitcoin miner and does **not** interact with any blockchain network. It is intended solely for learning and experimentation.

---

## Features

*  Simulates the Proof-of-Work mining process
*  Supports multiple worker processes for parallel searching (Multiprocessing workers)
*  Uses configurable hashing algorithms available in Python's `hashlib`
*  Demonstrates Proof-of-Work using leading zero bits
*  Adjustable mining difficulty
*  Command-line interface (CLI)
*  Reports elapsed time and approximate hash rate
*  Saves mining results in JSON format

---

## How It Works

The miner repeatedly computes:

```
hash = SHA256(nonce + message)
```

until it finds a hash that satisfies the configured difficulty target.

This demonstrates the same core concept used by Proof-of-Work blockchains: finding a valid nonce through repeated hashing.

---

## Example

Command:

```bash
python miner.py --message "Hello" --difficulty 20 --workers 4
```

Possible output:

```json
{
  "message": "Hello",
  "difficulty": 20,
  "algorithm": "sha256",
  "nonce": 490691,
  "hash": "00000cede446c9acba5acd73cd2fdfb0e77392f018ffc54806dbf4fbcac6ce39",
  "elapsed_seconds": 12.13,
  "approx_hash_rate": 41633.78
}
```

---

## Project Goals

* Understand cryptographic hash functions
* Explore nonce-based search
* Learn the fundamentals of Proof-of-Work
* Experiment with mining difficulty and performance

---

## Requirements

* Python 3.9+
* Standard Python libraries only

---

## License

Released under the MIT License — see the [LICENSE](LICENSE) file for details.
