import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] token = br.readLine().split(" ");
        int n = Integer.parseInt(token[0]);
        int m = Integer.parseInt(token[1]);

        int[][] matrix = new int[2][n];

        for (int i =0; i<2; i++){
            String[] tokens = br.readLine().split(" ");
            for (int j=0; j<n; j++){
                matrix[i][j] = Integer.parseInt(tokens[j]);
            }
        }
        
        while (m-- >0){
            int temp = matrix[0][n-1];

            for (int i=n-1; i>=1; i--){
                matrix[0][i] = matrix[0][i-1];
            }

            matrix[0][0] = matrix[1][n-1];
            
            for(int i=n-1; i>=1; i--){
                matrix[1][i] = matrix[1][i-1];
            }
            matrix[1][0] = temp;
        }

        for (int i =0; i<2; i++){
            for (int j=0; j<n; j++){
                System.out.print(matrix[i][j] + " ");
            }
            System.out.println();
        }
        
    }
}