#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct { int s, e, a; } Order;

// qsort 비교용 받는 마을(e) 기준 오름차순 정렬
int cmp(const void *a, const void *b) {
    Order *o1 = (Order *)a, *o2 = (Order *)b;
    if (o1->e != o2->e) return o1->e - o2->e;
    return o1->s - o2->s;
}

Order list[10005];
int truck_load[2005]; // 각 마을 구간별 트럭에 실린 박스 양

int main() {
    char buf[128];
    int n, c, m;
    
    if (!fgets(buf, 128, stdin)) return 0;
    sscanf(buf, "%d %d", &n, &c); // 마을 수 n, 트럭 용량 c
    
    if (!fgets(buf, 128, stdin)) return 0;
    m = atoi(buf); // 박스 정보 개수 m

    for (int i = 0; i < m; i++) {
        if (fgets(buf, 128, stdin)) {
            sscanf(buf, "%d %d %d", &list[i].s, &list[i].e, &list[i].a);
        }
    }

    // 받는 마을 기준 정렬
    qsort(list, m, sizeof(Order), cmp);

    int total = 0;
    for (int i = 0; i < m; i++) {
        int start = list[i].s;
        int end = list[i].e;
        int amount = list[i].a;

        // (start ~ end-1)에서 트럭에 실린 최대 박스 양 찾기
        int max_in_truck = 0;
        for (int j = start; j < end; j++) {
            if (truck_load[j] > max_in_truck) max_in_truck = truck_load[j];
        }

        // 여유 공간 계산
        int can_take = amount;
        if (can_take > c - max_in_truck) {
            can_take = c - max_in_truck;
        }

        if (can_take > 0) {
            total += can_take;
            // 실은 만큼 해당 구간의 용량 차감
            for (int j = start; j < end; j++) {
                truck_load[j] += can_take;
            }
        }
    }

    printf("%d\n", total);
    return 0;
}
