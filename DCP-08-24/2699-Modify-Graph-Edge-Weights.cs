using System;
using System.Collections.Generic;

public class Solution {
    public int[][] ModifiedGraphEdges(int n, int[][] edges, int source, int destination, int target) {
        var adjList = CreateAdjacencyList(n, edges);
        var distances = InitializeDistances(n, source);
        
        ModifiedDijkstra(adjList, edges, distances, source, 0, 0);
        
        int difference = target - distances[destination][0];
        if (difference < 0) {
            return new int[0][];
        }
        
        ModifiedDijkstra(adjList, edges, distances, source, difference, 1);
        
        if (distances[destination][1] < target) {
            return new int[0][];
        }
        
        return UpdateEdges(edges);
    }
    
    private List<(int, int)>[] CreateAdjacencyList(int n, int[][] edges) {
        var adjList = new List<(int, int)>[n];
        for (int i = 0; i < n; i++) {
            adjList[i] = new List<(int, int)>();
        }
        
        for (int i = 0; i < edges.Length; i++) {
            int u = edges[i][0], v = edges[i][1];
            adjList[u].Add((v, i));
            adjList[v].Add((u, i));
        }
        
        return adjList;
    }
    
    private int[][] InitializeDistances(int n, int source) {
        var distances = new int[n][];
        for (int i = 0; i < n; i++) {
            distances[i] = new int[2];
            Array.Fill(distances[i], int.MaxValue);
        }
        distances[source][0] = distances[source][1] = 0;
        return distances;
    }
    
    private void ModifiedDijkstra(List<(int, int)>[] adjList, int[][] edges, int[][] distances, int source, int difference, int run) {
        var pq = new PriorityQueue<(int, int), int>();
        pq.Enqueue((source, 0), 0);
        
        while (pq.Count > 0) {
            var (currentNode, currentDistance) = pq.Dequeue();
            
            if (currentDistance > distances[currentNode][run]) {
                continue;
            }
            
            foreach (var (nextNode, edgeIndex) in adjList[currentNode]) {
                int weight = edges[edgeIndex][2];
                if (weight == -1) {
                    weight = 1;
                }
                
                if (run == 1 && edges[edgeIndex][2] == -1) {
                    int newWeight = difference + distances[nextNode][0] - distances[currentNode][1];
                    if (newWeight > weight) {
                        edges[edgeIndex][2] = weight = newWeight;
                    }
                }
                
                if (distances[nextNode][run] > distances[currentNode][run] + weight) {
                    distances[nextNode][run] = distances[currentNode][run] + weight;
                    pq.Enqueue((nextNode, distances[nextNode][run]), distances[nextNode][run]);
                }
            }
        }
    }
    
    private int[][] UpdateEdges(int[][] edges) {
        foreach (var edge in edges) {
            if (edge[2] == -1) {
                edge[2] = 1;
            }
        }
        return edges;
    }
}
