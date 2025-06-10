import java.util.*;
import java.io.*;

public class Main {

    public static int getLength(List<String> list){
            int count = 1;
            int length = 0;
            for(int i=1; i<list.size();i++){
                
                if(list.get(i).equals(list.get(i-1))){
                    count++;
                }else{
                    
                    length += 1 + Integer.toString(count).length();
                    count = 1;
                }
            }
            length += 1 + Integer.toString(count).length();
            return length;
        } 

    public static void shift(List<String> list){
        String temp = list.get(list.size()-1);

        for (int i=list.size()-1; i>0; i--){
            list.set(i, list.get(i-1));
        }
        list.set(0, temp);
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String token = br.readLine();
        List<String> result = new ArrayList<>();

        for (int i=0; i<token.length(); i++){
            result.add(Character.toString(token.charAt(i)));
        }

        int minlength = Integer.MAX_VALUE;

        for (int i=0; i<token.length(); i++){
            int length = getLength(result);
            minlength = Math.min(length, minlength);
            shift(result);

        }

        System.out.println(minlength);

    }
}