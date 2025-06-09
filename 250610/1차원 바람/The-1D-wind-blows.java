import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] token = br.readLine().split(" ");
        int n = Integer.parseInt(token[0]);
        int m = Integer.parseInt(token[1]);
        int q = Integer.parseInt(token[2]);

        int[][] matrix = new int[n][m];
        for (int i =0; i<n; i++){
            String[] tokens = br.readLine().split(" ");
            for (int j=0; j<m; j++){
                matrix[i][j] = Integer.parseInt(tokens[j]);
            }
        }
        
        
        for (int t=0; t<q; t++){
            String[] tokenss = br.readLine().split(" ");
            int r = Integer.parseInt(tokenss[0]) - 1;
            char d = tokenss[1].charAt(0);

            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[]{r, d == 'L'? 1 : 0});
            boolean[] visited = new boolean[n];
            visited[r] = true;

            while(!queue.isEmpty()){
                int[] cur = queue.poll();
                int row = cur[0];
                int dir = cur[1];

                if(dir ==0){
                    int temp = matrix[row][0];
                    for (int i=0; i<m-1; i++){
                        matrix[row][i] = matrix[row][i+1];
                    }
                    matrix[row][m-1] = temp;
                }else{
                    int temp = matrix[row][m-1];
                    for (int i=m-1; i>0; i--){
                        matrix[row][i] = matrix[row][i-1];
                    }
                    matrix[row][0] = temp;
                }

                for (int dr = -1; dr<=1; dr+=2){
                    int nr = row + dr;
                    if (nr < 0 || nr >= n || visited[nr]) continue;

                    boolean hasSame = false;
                    for (int j =0; j<m; j++){
                        if(matrix[row][j] == matrix[nr][j]){
                            hasSame = true;
                            break;
                        }
                    }

                    if (hasSame){
                        visited[nr] = true;
                        queue.offer(new int[]{nr, 1-dir});
                    }
                }
            }
        }
        
        for (int i =0; i<n; i++){
            
            for(int j=0; j<m; j++){
                System.out.print(matrix[i][j]+" ");
                
            }
            System.out.println();
        }
    }
}