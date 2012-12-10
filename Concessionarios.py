import pymongo
import ast

class QueryDB(object):

	def __init__(self,db):
		self.db = db
	def Query(self,collection):

		pipeline = "[{'$project':{'montadora':1,'lbsid':1}},{'$project':{'montadora':1,'lbsid':1}}]"
		print pipeline
		
		command = "{'aggregate' :" +str(collection) + ", 'pipeline': " + pipeline + "} "
		command = ast.literal_eval(command)
		cursor = self.db.runCommand(command)
		

if __name__ == "__main__":

	connLocal = pymongo.Connection()
	connSpa = pymongo.Connection('192.168.3.1')

	dbLocal = connLocal.test
	dbSpa = connLocal.apontador

	qLocal = QueryDB(dbLocal)
	qSpa = QueryDB(dbSpa)
	lbsids = q.Query('routesAll')

	states = {}

	for lbsid in lbsids:
		qSpa.Query(lbsid)


