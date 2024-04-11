package java;

import java.util.Scanner;

public class Problem158A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int k = scanner.nextInt();
        int answer = 0;

        int [] arr = new int[n];
        
        for(int i = 0; i < n; i++){
            arr[i] = scanner.nextInt();
        }

        int kth_score = arr[k-1];

        for(int i = 0; i < n; i++){
            if (arr[i] != 0 && arr[i] >= kth_score){
                answer += 1;
            } else {
                break;
            }
        }
        
        System.out.println(answer);

        scanner.close();
    }
}