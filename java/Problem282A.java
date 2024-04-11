package java;

import java.util.Scanner;

public class Problem282A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.nextLine();
        String [] arr = new String[n];

        for(int i=0; i < n; i++){
            arr[i] = scanner.next().replace("X", "");
        }

        int x = 0;

        for (String operation : arr) {
            if(operation.equals("++")){
                x++;
            } 
            if(operation.equals("--")){
                x--;
            }
        }
        
        System.out.println(x);

        scanner.close();
    }
}