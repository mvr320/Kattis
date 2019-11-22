import java.util.Scanner;
class Pot
{
	public static void main(String args[]){
        	Scanner in = new Scanner(System.in);
	   	int sum = 0;
		int numCase = in.nextInt();
	   	for(int i=0; i<numCase; i++){
			int read = in.nextInt();
	   		int grou = read/10;
	   		int pow = read-(grou*10);
			sum+=Math.pow(grou,pow);
	   	}
		System.out.printf("%d",sum);
        }
}
