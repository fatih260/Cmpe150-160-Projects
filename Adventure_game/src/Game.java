import java.util.Scanner;

public class Game {
	Player player;
	Location location;
	Scanner scan = new Scanner(System.in);
	
	public void login() {
		Scanner scan = new Scanner(System.in);
		System.out.println("Hoþ geldiniz");
		System.out.print("Ýsminizi giriniz : ");
		
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
			System.out.println("Bir mekan seçiniz : ");
			System.out.println("1 --> Güvenli Ev : Düþman yok");
			System.out.println("2 --> Maðara : Zombi çýkabilir! ");
			System.out.println("3 --> Orman : Vampir çýkabilir! ");
			System.out.println("4 --> Nehir : Ayý çýkabilir! ");
			System.out.println("5 --> Maðaza : Silah veya zýrh alabilirsiniz! ");
			
			System.out.print("Gitmek istediðiniz yer : ");
			int selloc = scan.nextInt();
			while (selloc < 1 || selloc > 5) {
				System.out.print("Lütfen geçerli bir yer seçiniz : ");
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
			if (location.getName().equals("Güvenli Ev")) {
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

