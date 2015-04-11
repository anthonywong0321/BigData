__author__ = 'Milan'

import json

from DataPoint import DataPoint
from ClusterDB import ClusterDB
from Cluster import Cluster


file = open("../dataset/test.json")
clusterDb = ClusterDB()


def readAllDataPoints():
    for line in file:
        data_json = json.loads(line)  	# convert the str to json format

        dataPoint = DataPoint(data_json["latitude"], data_json["longitude"],data_json["stars"])

        checkDataPoint(dataPoint)

        checkAllClustersForCombining()


def checkDataPoint(dataPoint):
    for cluster in clusterDb.clusters:
        if cluster.checkDataPoint(dataPoint):
            print 'Add point to: ' + cluster.toString()
            cluster.addDataPoint(dataPoint)
            print 'and gives: ' + cluster.toString()
            return

    newCluster = Cluster()
    newCluster.addDataPoint(dataPoint)
    clusterDb.addCluster(newCluster)
    print 'Made new cluser: ' + newCluster.toString()

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



readAllDataPoints()
printFoundClusters()
