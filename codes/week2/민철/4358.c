#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 메모리 제한이 256MB로 매우 널널해서 그냥 정적할당
char all_trees[1000000][32];

// qsort 비교용 함수
int compare(const void *a, const void *b) {
    return strcmp((char *)a, (char *)b);
}

int main() {
    int total = 0;
    
    while (fgets(all_trees[total], 32, stdin) != NULL) { //total에다 넣고, 최대 32글자(30글자인데 여유분), 
        all_trees[total][strcspn(all_trees[total], "\n")] = '\0';
        if (all_trees[total][0] != '\0') total++;
    }

    qsort(all_trees, total, sizeof(all_trees[0]), compare); // 사전순 정렬

    for (int i = 0; i < total; i++) {
        int count = 1;
        while (i + 1 < total && strcmp(all_trees[i], all_trees[i + 1]) == 0) { // 앞에서 봤던 놈이면 카운트 증가 시키고 차례 넘김
            count++;
            i++;
        }
        
        float res = ((float)count / total) * 100;
        printf("%s %.4f\n", all_trees[i], res); // 소수점 4째자리까지만
    }

    return 0;
}
