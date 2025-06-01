import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] token = br.readLine().split(" ");
        int N = Integer.parseInt(token[0]);
        int M = Integer.parseInt(token[1]);

        int[][] matrix = new int[N][N];

        for (int i=0; i<N; i++){
            String[] tokens = br.readLine().split(" ");
            for (int j=0; j<N; j++){
                matrix[i][j] = Integer.parseInt(tokens[j]);
            }
        }

        
        int happycount = 0;
        // M = 1이면 무조건 모든 행, 열이 행복
        if (M == 1) {
            System.out.println(2 * N);
            return;  // ✅ 여기서 main 함수 내부를 빠져나갑니다
        }
        
        for (int i=0; i < N; i++){
            int count = 1;
            boolean ishappy = false;
            for (int j= 1; j < N; j++){
                if (matrix[i][j] == matrix[i][j-1]){
                    count += 1;
                    if (count >= M) {
                        ishappy = true;
                        break;
                    }
                }else{
                    count = 1;
                }
            }
            if (ishappy) happycount++;
        }
        
        for (int j=0; j < N; j++){
            int count = 1;
            boolean ishappy = false;
            for (int i= 1; i < N; i++){
                if (matrix[i][j] == matrix[i-1][j]){
                    count += 1;
                    if (count >= M) {
                        ishappy = true;
                        break;
                    }
                }else{
                    count = 1;
                }
            }
            if (ishappy) happycount++;
        }
        System.out.println(happycount);
    }
}