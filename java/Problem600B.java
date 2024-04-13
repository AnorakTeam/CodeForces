import java.util.Scanner;
import java.util.*;

public class Problem600B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int [] array1 = new int[n];
        int [] array2 = new int[m];
        
        scanner.nextLine();

        for(int i=0; i < n; i++){
            array1[i] = scanner.nextInt();
        }
        
        scanner.nextLine();
        
        for(int i=0; i < m; i++){
            array2[i] = scanner.nextInt();
        }
        
        //--------------------------

        /*
        input:
        5 4
        1 3 5 7 9
        6 4 2 8
        */
        Arrays.sort(array1);
        
        for(int i = 0; i < m; i++){
            int l = 0, r = n, mid = n;
            int target = array2[i];

            while(l < r && l != n){
                mid = l + (r - l) / 2;
                if(target >= array1[mid]){
                    l = mid + 1;
                } else {
                    r = mid;
                }
            }
            
            System.out.print(l);
            if(i != m-1){
                System.out.print(" ");
            }
        }
        scanner.close();
    }
}
