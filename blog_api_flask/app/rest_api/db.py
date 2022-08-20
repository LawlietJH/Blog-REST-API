from lib2to3.pgen2 import token
import bson

from flask import current_app, g
from werkzeug.local import LocalProxy
from pymongo import MongoClient, DESCENDING



def get_db():
    
    URI = current_app.config['MONGO_URI']
    client = MongoClient(URI)

    return client.RestApi


# Use LocalProxy to read the global db instance with just `db`
db = LocalProxy(get_db)

#==================================================================

def get_token():

    collTokens = db.Tokens

    try:
        token = collTokens.find({'username': 'Deleon'}).next()
        return token
    except:
        return

#==================================================================

def get_views():

    collViews = db.Views
    
    results = (
        list(collViews.find()),
        collViews.count_documents({})
    )

    return results

def get_view(id):

    collViews = db.Views
    
    try:
        data = collViews.find({'_id': id}).next()
        return data
    except:
        return

def add_views(views):

    collViews = db.Views
    # last_element = collViews.find().sort([('$natural', -1)]).limit(1).next()
    
    insert_after = []
    ignoreds = []
    inserts = []
    results = None

    # try:
    
    if views.__class__ == list:

        for view in views:
            id = view.get('_id')
            if not id:
                insert_after.append(view)
            else:
                existent = collViews.find_one({'_id': id})
                if not existent:
                    inserts.append(view)
                else:
                    ignoreds.append(view)
        
        if inserts:
            collViews.insert_many(inserts)
        
        if insert_after:
            
            last_id = collViews.find_one({}, sort=[('_id', DESCENDING)]).get('_id')
            # last_id = sorted([insert['_id'] for insert in inserts])[-1]
            
            for insert in insert_after:
                last_id += 1
                insert['_id'] = last_id
            
            collViews.insert_many(insert_after)

        return inserts + insert_after, ignoreds

    elif views.__class__ == dict:
        print(3, views)
        # results = collViews.insert_one(views)
    return results
    # except:
    #     return

def update_view(id):

    collViews = db.Views

    try:
        view = collViews.find({'_id': id}).next()
        qty_views = view.get('views')
        response = collViews.update_one(
            {'_id': id},
            {'$set': {'views': qty_views+1}}
        )
        return response
    except:
        return

def reset_view(id):

    collViews = db.Views

    try:
        response = collViews.update_one(
            {'_id': id},
            {'$set': {'views': 0}}
        )
        return response
    except:
        return

#==================================================================
