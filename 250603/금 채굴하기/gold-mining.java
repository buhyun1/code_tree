import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        String[] token = br.readLine().split(" ");
        int n = Integer.parseInt(token[0]);
        int m = Integer.parseInt(token[1]);

        int[][] matrix = new int[n][n];

        for (int i=0; i<n; i++){
            String[] tokens = br.readLine().split(" ");
            for (int j=0; j<n; j++){
                matrix[i][j] = Integer.parseInt(tokens[j]);
            }
        }

        int maxgold = 0;
        for (int cx = 0; cx<n; cx++){
            for (int cy = 0; cy<n; cy++){
                for (int k =0; k<=2*(n-1); k++){
                    int gold =0;

                     for (int x = 0; x < n; x++) {
                        for (int y = 0; y < n; y++) {
                            if(Math.abs(x-cx) + Math.abs(y-cy)<=k){
                                if(matrix[x][y] ==1) gold++;
                            }
                        }
                     }
                     int cost = k*k+(k+1)*(k+1);
                     if (gold*m >= cost){
                        maxgold = Math.max(gold,maxgold);
                     }
                }
            }
        }
        System.out.println(maxgold);
    }
}