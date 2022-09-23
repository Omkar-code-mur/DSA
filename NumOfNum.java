import java.util.Scanner;

public class NumOfNum{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a big number : ");
        long num = input.nextLong();
        byte count = 0;
        while (num > 0 ){
            if (num%10 == 7){
                count++;
            }
            num /=10;
        }
        System.out.println(count);
    }

}