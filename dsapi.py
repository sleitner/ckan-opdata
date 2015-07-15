#!/usr/bin/env python
import urllib2
import urllib
import json
import pprint

SITE_API='http://127.0.0.1:8080/api/3/action/'
API_KEY='394a4af7-0ff5-40a4-bc24-95c164f0a349'
import sys
def make_http_request(api, data_string):
    request= urllib2.Request(api)
    request.add_header('Authorization', API_KEY)
    urllib2.urlopen
    urllib2.urlopen
    response=''
    try:
        response = urllib2.urlopen(request, data_string)
    except urllib2.HTTPError, e:
        print 'HTTPError = ' + str(e.code)
        print json.loads(e.read())
    except urllib2.URLError, e:
        print 'URLError = ' + str(e.reason)
        print json.loads(e.read())
    except httplib.HTTPException, e:
        print 'HTTPException'
        print json.loads(e.read())
    except Exception:
        import traceback
        print 'generic exception: ' + traceback.format_exc()
    # now fail if you hit an exception
    if response:
        assert response.code == 200
        # Use the json module to load CKAN's response into a dictionary.
        response_dict = json.loads(response.read())
        assert response_dict['success'] is True
        # package_create returns the created package as its result.
        return response_dict
    return None
def create(data, columns):
    data.update({'force':'true',
                   'fields':columns,
                   'records': [],
               })
    # Use the json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(data))
    response_dict  = make_http_request(SITE_API+'datastore_create', data_string)
    created_package = response_dict['result']
    print '----------------creating'
    pprint.pprint(created_package)
    print '----------------'
def insert_record(data, record):
    data.update({'force':'true',
                 'filters': record_filter, 
                 'records': record,
    })
    data_string = urllib.quote(json.dumps(data))
    response_dict = make_http_request(SITE_API+'datastore_create', data_string) #or upsert
    print '----------------inserting'
    pprint.pprint(response_dict)
    print '----------------'
def delete(data, record_filter):
    data.update({'force':'true',
                 'filters': record_filter, 
    })
    data_string = urllib.quote(json.dumps(data))
    response_dict = make_http_request(SITE_API+'datastore_delete', data_string)
    print '----------------delete'
    pprint.pprint(response_dict)
    print '----------------'
def search(data, columns):
    # Use the json module to dump the dictionary to a string for posting.
    data_string = urllib.quote(json.dumps(data))
    response_dict = make_http_request(SITE_API+'datastore_search?resource_id='+resource_id, data_string)
    print '----------------search'
    pprint.pprint(response_dict)
    print '----------------'

    
resource_id='09487ca6-3859-4787-95ad-e8b6cd52fab6'
pkey_name='name'
# Put the options of the dataset we're going to create into a dict.
data = {'resource_id':resource_id,}


record_filter = {'name':'otherdata'},
record_filter = {}
delete(data, record_filter)

# Name the fields for creation
columns = [{'id':'name', 'type':'text'},
          {'id':'subname', 'type':'text'},
          {'id':'jtable', 'type':'json'},
          {'id':'datetime', 'type':'timestamp'},
          {'id':'response', 'type':'bool'},
          {'id':'response_time', 'type':'int'}]
create(data, columns)
record = [
    {
    'name':'op_data',
    'subname':'historical',
    'datetime':'2012-10-01T02:43Z',
    'response':True,
    'response_time':100,
    },
    {
    'name':'op_data',
    'subname':'historical',
    'datetime':'2012-10-01T03:43Z',
    'response':True,
    'response_time':200,
    },
    {
    'name':'op_data',
    'subname':'historical',
    'datetime':'2012-10-01T04:43Z',
    'response':True,
    'response_time':300,
    },
    {
    'name':'op_data',
    'subname':'historical',
    'datetime':'2012-10-01T06:43Z',
    'response':True,
    'response_time':250,
    },
]
          
insert_record(data, record)
# search(data, columns)

