import validators
import shortuuid
from app import db
from app.models.main import Url


def helloWorld():
    return 'Hello World!'


# Check if url is on good standards e.g. https://foo.bar
def validateUrl(url):
    result = validators.url(url)

    return result

# Generate a random ID of n characters (6)


def generateID():
    result = shortuuid.ShortUUID().random(length=6)

    return result


def addUrlDB(url):
    response = {}

    if validateUrl(url):
        shorten_url = generateID()

        response['short_url'] = shorten_url
        response['original_url'] = url

        # TODO: Better db handling e.g. 'check for errors dude!'
        new_url = Url(shorten_url=shorten_url, original_url=url)
        db.session.add(new_url)
        db.session.commit()

    else:
        response['error'] = 'Not a valid URL'

    return response


def getUrlDB(shorten_url):

    query = Url.query.filter_by(shorten_url=shorten_url).first()
    if query:
        return query.original_url
    else:
        return None
