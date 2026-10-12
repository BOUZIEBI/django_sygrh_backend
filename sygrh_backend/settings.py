# ---------------------------------------------------------
# Domaines autorisés
# ---------------------------------------------------------

def get_env_list(name: str, default: str = "") -> list[str]:
    return [
        value.strip().rstrip("/")
        for value in os.getenv(name, default).split(",")
        if value.strip()
    ]


ALLOWED_HOSTS = get_env_list(
    "ALLOWED_HOSTS",
    "sygrhbackend-production.up.railway.app,localhost,127.0.0.1",
)

# ---------------------------------------------------------
# CORS
# ---------------------------------------------------------

CORS_ALLOWED_ORIGINS = get_env_list(
    "CORS_ALLOWED_ORIGINS",
    (
        "https://mesrssitevitrine-production.up.railway.app,"
        "http://localhost:5173,"
        "http://localhost:5174"
    ),
)

CORS_ALLOW_CREDENTIALS = True

from corsheaders.defaults import default_headers

CORS_ALLOW_HEADERS = (
    *default_headers,
    "x-crypto-session-id",
    "x-csrf-token",
)

# ---------------------------------------------------------
# CSRF
# ---------------------------------------------------------

CSRF_TRUSTED_ORIGINS = get_env_list(
    "CSRF_TRUSTED_ORIGINS",
    (
        "https://mesrssitevitrine-production.up.railway.app,"
        "http://localhost:5173,"
        "http://localhost:5174"
    ),
)