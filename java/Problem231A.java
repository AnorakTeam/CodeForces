package java;

import java.util.Scanner;

public class Problem231A {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        scanner.nextLine();
        int solvedProblems = 0;

        for (int i = 0; i < n; i++) {
            String line = scanner.nextLine();
            String[] options = line.split(" ");

            int sum = 0;
            for (String option : options) {
                sum += Integer.parseInt(option);
            }

            if (sum >= 2) {
                solvedProblems++;
            }
        }

        System.out.println(solvedProblems);

        scanner.close();
    }
}