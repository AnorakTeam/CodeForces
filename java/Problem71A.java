package java;

import java.util.Scanner;

public class Problem71A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        String [] arr = new String[n];
        
        for(int i = 0; i < n; i++){
            arr[i] = scanner.next();
        }
        
        for(String word : arr){
            if(word.length() <= 10){
                System.out.println(word);
            } else {
                System.out.println(
                    word.charAt(0) + String.valueOf(word.length() - 2) + word.charAt(word.length() - 1)
                );
            }
        }

        scanner.close();
    }
}