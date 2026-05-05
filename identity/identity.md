# SOVEREIGN Identity System

## DID Schema
did:sov:<network>:<agent-id>

## Key Hierarchy
- Master Key (TPM)
- Operational Key (rotated quarterly)
- Recovery Key (Shamir 3-of-5)

## Verification Flow
1. Present DID + nonce
2. Sign with operational key
3. Verify on-chain
4. Check revocation
