import java.util.Scanner;
class ADifferentProblem{
	final static int SLEEP = 45;
	public static void main(String args[]){
		Scanner in = new Scanner(System.in);
		while(in.hasNext()){
			long v1 = in.nextLong();
			long v2 = in.nextLong();
			long result = v1 - v2;
			if(result<0){
				result *= -1;
			}
			System.out.printf("%d\n",result);
		}
	} 
}