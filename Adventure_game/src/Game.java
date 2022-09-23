import java.util.Scanner;

public class Game {
	Player player;
	Location location;
	Scanner scan = new Scanner(System.in);
	
	public void login() {
		Scanner scan = new Scanner(System.in);
		System.out.println("Ho� geldiniz");
		System.out.print("�sminizi giriniz : ");
		
		String playername = scan.nextLine();
		player = new Player(playername);
		player.selectCha();
		
		start();
		
	}
	public void start() {
		while(true) {
			System.out.println();
			System.out.println("=============================");
			System.out.println();
			System.out.println("Bir mekan se�iniz : ");
			System.out.println("1 --> G�venli Ev : D��man yok");
			System.out.println("2 --> Ma�ara : Zombi ��kabilir! ");
			System.out.println("3 --> Orman : Vampir ��kabilir! ");
			System.out.println("4 --> Nehir : Ay� ��kabilir! ");
			System.out.println("5 --> Ma�aza : Silah veya z�rh alabilirsiniz! ");
			
			System.out.print("Gitmek istedi�iniz yer : ");
			int selloc = scan.nextInt();
			while (selloc < 1 || selloc > 5) {
				System.out.print("L�tfen ge�erli bir yer se�iniz : ");
				selloc = scan.nextInt();
			}
			switch(selloc) {
			case 1:
				location = new SafeHouse(player);
				break;
			case 2:
				location = new Cave(player);
				break;
			case 3:
				location = new Forest(player);
				break;
			case 4:
				location = new River(player);
				break;
			case 5:
				location = new ToolStore(player);
				break;
				
			default :
				location = new SafeHouse(player);
				break;		
			
			
			}
			if (location.getName().equals("G�venli Ev")) {
				if (player.getInv().isFood() && player.getInv().isFirewood() && player.getInv().isWater()) {
					System.out.println("Tebrikler");
					System.out.println("Oyun Bitti");
					break;
				}
			}
			if (!location.getLocation()) {
				System.out.println("Oyun Bitti");
				break;
			}
			
		}
	}

}	

