class ThreadExp extends Thread{
	public native static void sleep(long miliseconds)throws InterruptedException; 
	static { 
		System.loadLibrary("SleepInC");
	}
	public void run(){
		for (int i = 0; i < 4; i++) {
			try{
				System.out.println("Thread iteration " + i);
				sleep(1);
			}catch(Exception e){
				System.out.println(e);
			}
		}
	}
}

class Execution{
	public static void main(String[] args) throws Exception{
		ThreadExp x = new ThreadExp();
		x.start();
	}
}