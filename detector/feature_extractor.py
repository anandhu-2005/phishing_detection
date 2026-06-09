import re
from urllib.parse import urlparse
import tldextract

def extract_features(url: str) -> list:
    parsed = urlparse(url)
    ext = tldextract.extract(url)

    features = [
        len(url),                                                                # url_length
        1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed.netloc) else 0,           # has_ip
        1 if '@' in url else 0,                                                 # has_at_symbol
        1 if '//' in url[7:] else 0,                                            # has_double_slash
        len(ext.subdomain.split('.')) if ext.subdomain else 0,                  # subdomain_count
        1 if parsed.scheme == 'https' else 0,                                   # has_https
        len(ext.domain),                                                         # domain_length
        len(parsed.path),                                                        # path_length
        1 if '-' in ext.domain else 0,                                          # hyphen_in_domain
        sum(c.isdigit() for c in url) / len(url),                               # digit_ratio
        sum(url.count(c) for c in ['%', '=', '?', '&']),                       # special_char_count
        1 if any(t in parsed.path for t in ['.com', '.net', '.org']) else 0,   # tld_in_path
    ]
    return features