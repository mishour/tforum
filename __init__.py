# -*- coding: utf-8 -*-
import pymongo

if __name__ == "__main__":

    db = pymongo.MongoClient().test
    db.tag.drop()

    db.tag.save({"tag": "top", "tag_name": "最热"})
    db.tag.save({"tag": "programmer", "tag_name": "程序员"})
    db.tag.save({"tag": "Python", "tag_name": "Python"})
    db.tag.save({"tag": "Linux", "tag_name": "Linux"})
    db.tag.save({"tag": "node.js", "tag_name": "node.js"})
    db.tag.save({"tag": "cloud", "tag_name": "云计算"})
    db.tag.save({"tag": "ideas", "tag_name": "奇思妙想"})