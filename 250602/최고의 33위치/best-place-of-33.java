import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] matrix = new int[N][N];

        for (int i=0; i < N; i++){
            String[] tokens = br.readLine().split(" ");
            for (int j =0; j < N; j++){
                matrix[i][j] = Integer.parseInt(tokens[j]);
            }
        }

        int max = 0;

        for (int i =0; i<=N-3; i++){
            for (int j=0; j<=N-3;j++){
                int sum =0;

                for (int dx= 0; dx<3; dx++){
                    for (int dy=0; dy<3; dy++){
                        sum += matrix[i+dx][j+dy];
                    }
                }
                max = Math.max(max, sum);
            }
        }
        System.out.println(max);
    }
}