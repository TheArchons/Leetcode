#include <stdio.h>
#include <vector>
#include <tuple>
#include <queue>

using namespace std;

int main() {
    freopen("input07.txt", "r", stdin);
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        int nodes, edges;
        scanf("%d %d", &nodes, &edges);

        vector<vector<tuple<int, int>>> graph(nodes + 1);
        int dists[nodes + 1];

        for (int j = 0; j < nodes+1; j++) {
            dists[j] = -1;
        }
        
        for (int j = 0; j < edges; j++) {
            int a, b, w;
            scanf("%d %d %d", &a, &b, &w);

            graph[a].push_back(make_tuple(b, w));
            graph[b].push_back(make_tuple(a, w));
        }

        int start;
        scanf("%d", &start);

        dists[start] = 0;

        queue<int> q;
        q.push(start);
        while (!q.empty()) {
            int node = q.front(); q.pop();
            
            for (int j = 0; j < graph[node].size(); j++) {
                int next = get<0>(graph[node][j]);
                int dist = get<1>(graph[node][j]);

                if (dists[next] == -1 || dists[node] + dist < dists[next]) {
                    dists[next] = dists[node] + dist;
                    q.push(next);
                }
            }
        }

        for (int j = 1; j <= nodes; j++) {
            if (j != start) {
                printf("%d ", dists[j]);
            }
        }
        printf("\n");
    }
}