from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-server', port=6379)

@app.route('/')
def site_visit():
    redis.incr('visit_count')
    read_visit = str(redis.get('visit_count'), encoding='utf-8')
    return 'Till now the site has '+read_visit+' visits.'

if __name__ == '__main__':
    app.run(debug=True)
