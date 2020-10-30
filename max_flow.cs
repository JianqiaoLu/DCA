using System;
using System.Collections.Generic;
using System.Linq;

namespace GraphAlgorithmTesting
{
  class Program
  {
    static void Main(string[] args)
    {
      Graph g = new Graph(6);
      g.AddEdge(0, 1, 16);
      g.AddEdge(0, 2, 13);
      g.AddEdge(1, 2, 10);
      g.AddEdge(1, 3, 12);
      g.AddEdge(2, 1, 4);
      g.AddEdge(2, 4, 14);
      g.AddEdge(3, 2, 9);
      g.AddEdge(3, 5, 20);
      g.AddEdge(4, 3, 7);
      g.AddEdge(4, 5, 4);

      Console.WriteLine();
      Console.WriteLine("Graph Vertex Count : {0}", g.VertexCount);
      Console.WriteLine("Graph Edge Count : {0}", g.EdgeCount);
      Console.WriteLine();

      int maxFlow = g.FordFulkerson(0, 5);
      Console.WriteLine("The Max Flow is : {0}", maxFlow);

      Console.ReadKey();
    }

    class Edge
    {
      public Edge(int begin, int end, int weight)
      {
        this.Begin = begin;
        this.End = end;
        this.Weight = weight;
      }

      public int Begin { get; private set; }
      public int End { get; private set; }
      public int Weight { get; private set; }

      public override string ToString()
      {
        return string.Format(
          "Begin[{0}], End[{1}], Weight[{2}]",
          Begin, End, Weight);
      }
    }

    class Graph
    {
      private Dictionary<int, List<Edge>> _adjacentEdges
        = new Dictionary<int, List<Edge>>();

      public Graph(int vertexCount)
      {
        this.VertexCount = vertexCount;
      }

      public int VertexCount { get; private set; }

      public IEnumerable<int> Vertices
      {
        get
        {
          return _adjacentEdges.Keys;
        }
      }

      public IEnumerable<Edge> Edges
      {
        get
        {
          return _adjacentEdges.Values.SelectMany(e => e);
        }
      }

      public int EdgeCount
      {
        get
        {
          return this.Edges.Count();
        }
      }

      public void AddEdge(int begin, int end, int weight)
      {
        if (!_adjacentEdges.ContainsKey(begin))
        {
          var edges = new List<Edge>();
          _adjacentEdges.Add(begin, edges);
        }

        _adjacentEdges[begin].Add(new Edge(begin, end, weight));
      }

      public int FordFulkerson(int s, int t)
      {
        int u, v;

        // Create a residual graph and fill the residual graph with
        // given capacities in the original graph as residual capacities
        // in residual graph
        int[,] residual = new int[VertexCount, VertexCount];

        // Residual graph where rGraph[i,j] indicates
        // residual capacity of edge from i to j (if there
        // is an edge. If rGraph[i,j] is 0, then there is not)
        for (u = 0; u < VertexCount; u++)
          for (v = 0; v < VertexCount; v++)
            residual[u, v] = 0;
        foreach (var edge in this.Edges)
        {
          residual[edge.Begin, edge.End] = edge.Weight;
        }

        // This array is filled by BFS and to store path
        int[] parent = new int[VertexCount];

        // There is no flow initially
        int maxFlow = 0;

        // Augment the flow while there is path from source to sink
        while (BFS(residual, s, t, parent))
        {
          // Find minimum residual capacity of the edhes along the
          // path filled by BFS. Or we can say find the maximum flow
          // through the path found.
          int pathFlow = int.MaxValue;
          for (v = t; v != s; v = parent[v])
          {
            u = parent[v];
            pathFlow = pathFlow < residual[u, v]
              ? pathFlow : residual[u, v];
          }

          // update residual capacities of the edges and reverse edges
          // along the path
          for (v = t; v != s; v = parent[v])
          {
            u = parent[v];
            residual[u, v] -= pathFlow;
            residual[v, u] += pathFlow;
          }

          // Add path flow to overall flow
          maxFlow += pathFlow;
        }

        // Return the overall flow
        return maxFlow;
      }

      // Returns true if there is a path from source 's' to sink 't' in
      // residual graph. Also fills parent[] to store the path.
      private bool BFS(int[,] residual, int s, int t, int[] parent)
      {
        bool[] visited = new bool[VertexCount];
        for (int i = 0; i < visited.Length; i++)
        {
          visited[i] = false;
        }

        Queue<int> q = new Queue<int>();

        visited[s] = true;
        q.Enqueue(s);
        parent[s] = -1;

        // standard BFS loop
        while (q.Count > 0)
        {
          int u = q.Dequeue();

          for (int v = 0; v < VertexCount; v++)
          {
            if (!visited[v]
              && residual[u, v] > 0)
            {
              q.Enqueue(v);
              visited[v] = true;
              parent[v] = u;
            }
          }
        }

        // If we reached sink in BFS starting from source,
        // then return true, else false
        return visited[t] == true;
      }
    }
  }
}