import java.util.Scanner;
class SpeedLimit
{
	public static void main(String args[]){
        Scanner in = new Scanner(System.in);
	   	while(in.hasNext()){
	   		int cases = in.nextInt();
	   		if(cases==-1){
	   			break;
	   		}
	   		int t = 0;
	   		int sum = 0;
	   		int speed;
	   		int tp;
	   		for(int i=0; i<cases; i++){
	   			speed = in.nextInt();
	   			tp = in.nextInt();
	   			sum += speed*(tp-t);
	   			t = tp;
	   		}
	   		System.out.printf("%d miles\n", sum);
	   	}
	}
}
