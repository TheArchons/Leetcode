#include <stdio.h>
#include <queue>

using namespace std;

void query() {
    int nodes, edges;
    scanf("%d %d", &nodes, &edges);

    vector<vector<int>> graph(nodes + 1);
    int dists[nodes + 1];
    for (int i = 0; i < nodes+1; i++) {
        dists[i] = -1;
    }

    for (int i = 0; i < edges; i++) {
        int a, b;
        scanf("%d %d", &a, &b);
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    int root;
    scanf("%d", &root);

    queue<int> q;
    q.push(root);

    dists[root] = 0;

    while(!q.empty()) {
        int node = q.front(); q.pop();

        for (int i = 0; i < graph[node].size(); i++) {
            int next = graph[node][i];
            if (dists[next] == -1 || dists[next] > dists[node] + 1) {
                dists[next] = dists[node] + 1;
                q.push(next);
            }
        }
    }

    for (int i = 1; i <= nodes; i++) {
        if (i != root) {
            printf("%d ", dists[i] == -1 ? -1 : dists[i] * 6);
        }
    }
    printf("\n");
}

int main() {
    int q;
    scanf("%d", &q);
    while (q--) {
        query();
    }
}