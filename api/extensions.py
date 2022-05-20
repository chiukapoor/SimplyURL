from hashids import Hashids
from api.config import SECRET_KEY

hashidsObj = Hashids(min_length=5, salt=SECRET_KEY)