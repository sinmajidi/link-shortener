from database import URLShortener,app,db,generate_short_url,jsonify,request
db.create_all()
server_ip="http://127.0.0.1:8590/"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    if 'original_url' in request.get_json():
        original_url = request.get_json()['original_url']
        short_url=generate_short_url()
        url_entry = URLShortener.query.filter_by(short_url=short_url).first()
        while url_entry:
            short_url=generate_short_url()
            url_entry = URLShortener.query.filter_by(short_url=short_url).first()
        
        url_entry = URLShortener(original_url=original_url,short_url=short_url)
        db.session.add(url_entry)
        db.session.commit()
        return jsonify({'short_url': server_ip+short_url}),200
        
    return jsonify({'message': 'lost original_url in request'}),400

@app.route('/<short_url>')
def redirect_to_original(short_url):
    url_entry = URLShortener.query.filter_by(short_url=short_url).first()
    if url_entry:
        return jsonify({'original_url': url_entry.original_url}),200
    return jsonify({'message': 'url not found'}),404

app.run(host='0.0.0.0',port=8590)