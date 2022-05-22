try:
    from hashids import Hashids
    from api.config import SECRET_KEY
    from api.commons.apispec import APISpecExt
    from flask_marshmallow import Marshmallow
except Exception as e:
    print("Error: {} ".format(e))

ma = Marshmallow()
apispec = APISpecExt()
hashidsObj = Hashids(min_length=5, salt=SECRET_KEY)
