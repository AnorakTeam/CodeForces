import java.util.Scanner;
import java.util.*;


// TODO: terminar el problema, buscar upper bound

public class Problema600B {
    static int upper_bound(int arr[], int key) 
    { 
        int upperBound = 0; 
  
        while (upperBound < arr.length) { 
            // If current value is lesser than or equal to 
            // key 
            if (arr[upperBound] <= key) 
                upperBound++; 
  
            // This value is just greater than key 
            else{ 
                System.out.print("The upper bound of " + key + " is " + arr[upperBound] + " at index " + upperBound); 
                return arr[upperBound]; 
            }     
        } 
        System.out.print("The upper bound of " + key + " does not exist."); 
    } 
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        //--------------------------
        /*
        5 4
        1 3 5 7 9
        6 4 2 8
        */
        
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        int [] array1 = new int[n];
        int [] array2 = new int[m];
        int [] answer = new int[m];
        
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
        5 4
        1 3 5 7 9
        6 4 2 8
        */
        Arrays.sort(array1);
        
        for(int i = 0; i < m; i++){
            
            int l = 0, r = n, mid = 0;
            int target = array2[i];
            
            while(l <= r){
                mid = (r+l)/2;
                if(array1[mid] > target){
                    r = mid - 1;  
                } 
                else {
                    l = mid + 1;
                }
            }
            answer[i] = mid;
        }
        
        String msg = "";
        for(int i = 0; i < answer.length; i++){
            msg += answer[i];
            if(i != answer.length-1){
                msg += " ";
            }
        }
        
        System.out.println(msg);
        
        scanner.close();
    }
}
