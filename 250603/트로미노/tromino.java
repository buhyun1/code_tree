import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] tokens = br.readLine().split(" ");
        int n = Integer.parseInt(tokens[0]);
        int m = Integer.parseInt(tokens[1]);

        int[][] matrix = new int[n][m];

        for (int i =0; i<n; i++){
            String[] token = br.readLine().split(" ");
            for (int j=0; j<m; j++){
                matrix[i][j] = Integer.parseInt(token[j]);
            }
        }
        int max = 0;
        for (int i=0; i<n; i++){
            for (int j=0; j<m-2; j++){
                int temp_max = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2];
                max = Math.max(max,temp_max);
            }
        }

        for (int i=0; i<n-2; i++){
            for (int j=0; j<m; j++){
                int temp_max = matrix[i][j] + matrix[i+1][j] + matrix[i+2][j];
                max = Math.max(max,temp_max);
            }
        }

        int[][][] block = {
            {{0,0}, {0,1}, {1,0}},  // ┌
            {{0,0}, {1,0}, {1,1}},  // └
            {{0,1}, {1,0}, {1,1}},  // ┘
            {{0,0}, {0,1}, {1,1}}   // ┐
        };
        
        for (int i=0; i<n; i++){
            for (int j=0; j<m; j++){
                for (int[][] shape : block){
                    int sum =0;
                    boolean valid = true;
                    for (int[] pos : shape){
                        int ni = i + pos[0];
                        int nj = j + pos[1];
                        
                        if (ni>=n || nj>=m ){
                        valid = false;
                        break;
                        }
                        sum += matrix[ni][nj];
                    } 
                    if (valid) max = Math.max(max, sum);
                }
            }
        }

        System.out.println(max);
    }
}