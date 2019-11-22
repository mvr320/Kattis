import java.util.Scanner;
class TwoStones
{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        if(in.nextInt()%2==0){
            System.out.printf("Bob");
        } else {
            System.out.printf("Alice");
        }
    }
}
