import sys
import json

from BigDataProject.bfr.ClusterDB import ClusterDB
from BigDataProject.bfr.Cluster import Cluster

clusterDb = ClusterDB()

def readAllClusters():

    for line in sys.stdin:
		try:
			data_json = json.loads(line)  	# convert the str to json format

			cluster = Cluster()
			cluster.N = data_json[0]
			cluster.SUM = data_json[1]
			cluster.SUMSQ = data_json[2]

			clusterDb.addCluster(cluster)

			checkAllClustersForCombining()
		except ValueError:
			continue

def checkAllClustersForCombining():
    for cluster in clusterDb.clusters:
        for otherCluster in clusterDb.clusters:
            if cluster == otherCluster:
                continue
            else:
                if cluster.checkCombineClusters(otherCluster):
                    print 'Combined cluster: ' + cluster.toString() + ' and ' + otherCluster.toString()
                    cluster.combineClusters(otherCluster)
                    clusterDb.removeCluster(otherCluster)
                    print 'Combined cluster to: ' + cluster.toString()

def printFoundClusters():
    for cluster in clusterDb.clusters:
        print cluster.toString()



readAllClusters()
printFoundClusters()