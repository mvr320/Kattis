import java.util.Scanner;
class Spavanac{
	final static int SLEEP = 45;
	public static void main(String args[]){
		Scanner in = new Scanner(System.in);
		int h = in.nextInt();
		int m = in.nextInt();
		if(m-SLEEP<0){
			m = 15+m;
			if(h-1<0){
				h=23;
			} else {
				h--;
			}
		} else {
			m -= SLEEP;
		}
		System.out.printf("%d %d",h,m);
	} 
}
