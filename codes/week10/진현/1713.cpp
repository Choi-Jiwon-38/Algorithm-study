#include <bits/stdc++.h>

using namespace std;

struct candidate {
    int id;
    int like;
    int tick;

    void init(int _id, int _tick) {
        id = _id;
        tick = _tick;
        like = 1;
    }
};

struct cmp {
    bool operator()(const candidate& a, const candidate& b) const {
        if (a.like == b.like)
            return a.tick < b.tick;
        else
            return a.like < b.like;
    }
};
bool valid[101];
set<candidate, cmp>::iterator iters[101];

int main(void)
{
    cin.tie(NULL);
    cout.tie(NULL);
    iostream::sync_with_stdio(false);

    set<candidate, cmp> photos;
    priority_queue<int> pq;
    int N, T;
    cin >> N >> T;
    for (int tick=1; tick<=T; tick++) {
        int id;
        cin >> id;

        if (valid[id]) {
            auto tg = *iters[id];
            photos.erase(iters[id]);

            tg.like++;
            iters[id] = photos.insert(tg).first;
        }
        else {
            candidate n_tg;
            if (photos.size() >= N) {
                auto it = photos.begin();
                valid[it->id] = false;
                photos.erase(it);
            }

            n_tg.init(id, tick);
            iters[id] = photos.insert(n_tg).first;
            valid[id] = true;
        }
    }

    for (auto tg: photos)
        pq.push(-tg.id);
    while (pq.size()) {
        cout << (-pq.top()) << ' ';
        pq.pop();
    }
}