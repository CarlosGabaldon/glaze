#!/usr/bin/env python
# encoding: utf-8
"""
test_couchdb.py

Created by Carlos Gabaldon on 2010-09-23.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

from couchdb import Couch

def test():
    foo = Couch('localhost', '5984')

    print "\nCreate database 'glaze':"
    foo.createDb('glaze')

    print "\nList databases on server:"
    foo.listDb()

    print "\nCreate a document 'mydoc' in database 'glaze':"
    doc = """
    {
        "value":
        {
            "Subject":"I like Planktion",
            "Author":"Rusty",
            "PostedDate":"2006-08-15T17:30:12-04:00",
            "Tags":["plankton", "baseball", "decisions"],
            "Body":"I decided today that I don't like baseball. I like plankton."
        }
    }
    """
    foo.saveDoc('glaze', doc, 'mydoc')

    print "\nCreate a document, using an assigned docId:"
    foo.saveDoc('glaze', doc)

    print "\nList all documents in database 'glaze'"
    foo.listDoc('glaze')

    print "\nRetrieve document 'mydoc' in database 'glaze':"
    foo.openDoc('glaze', 'mydoc')

    print "\nDelete document 'mydoc' in database 'glaze':"
    foo.deleteDoc('glaze', 'mydoc')

    print "\nList all documents in database 'glaze'"
    foo.listDoc('glaze')

    print "\nList info about database 'glaze':"
    foo.infoDb('glaze')

    #print "\nDelete database 'glaze':"
    #foo.deleteDb('glaze')

    print "\nList databases on server:"
    foo.listDb()

if __name__ == "__main__":
    test()