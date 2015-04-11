__author__ = 'Milan'

class ClusterDB(object):
    def __init__(self):
        self.id = 0
        self.clusters = []

    def addCluster(self, cluster):
        self.clusters.append(cluster)

    def removeCluster(self, cluster):
        self.clusters.remove(cluster)

