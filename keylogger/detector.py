import re

class PatternDetector:
    PATTERNS = [
        r"(bc1|1[a-km-zA-HJ-NP-Z1-9]{25,34})",  # Bitcoin
        r"0x[a-fA-F0-9]{40}",                  # Ethereum
        r"(seed phrase|mnemonic|wallet)",      # Frases comunes
        r"(metamask|binance|trustwallet)"      # Plataformas
    ]

    def matches(self, text):
        return any(re.search(p, text.lower()) for p in self.PATTERNS)