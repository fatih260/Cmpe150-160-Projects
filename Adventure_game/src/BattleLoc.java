
public abstract class BattleLoc extends Location{
	
	protected Obstacle obstacle;
	protected String nItem;
	
	BattleLoc(Player player, String name, Obstacle obstacle, String nItem) {
		super(player);
		this.obstacle = obstacle;
		this.name = name;
		this.nItem = nItem;
	}
	
	public boolean getLocation() {
		int obsCount = obstacle.count();
		System.out.println("Þuan buradasýnýz : " + this.getName());
		System.out.println("Burada " + obsCount + " adet " + obstacle.getName() + " bulunuyor.");
		System.out.print("<S>avaþ veya <K>aç : ");
		String selCase = scan.nextLine();
		selCase = selCase.toUpperCase();
		if (selCase.equals("S")) {
			if (combat(obsCount)) {
				System.out.println("\n" + this.getName() + " bölgesindeki tüm  düþmanlarý temizlediniz!!");
				if (this.nItem.equals("Food") && player.getInv().isFood() == false) {
					System.out.println(this.nItem + " kazandýnýz.");
					player.getInv().setFood(true);
					
				}else if (this.nItem.equals("Water") && player.getInv().isWater() == false) {
					System.out.println(this.nItem + " kazandýnýz.");
					player.getInv().setWater(true);
					
				}else if (this.nItem.equals("Firewood") && player.getInv().isFirewood() == false) {
					System.out.println(this.nItem + " kazandýnýz.");
					player.getInv().setFirewood(true);
				}
				return true;
			}
			if (player.getHealth() <= 0) {
				System.out.println("Öldünüz!");
				return false;
			}
		}
		return true;
	}
	public boolean combat(int obsCount) {
		for (int i = 0; i < obsCount; i++) {
			int defOfHealth = obstacle.getHealth();
			playerstats();
			enemystats();
			while (player.getHealth() > 0 && obstacle.getHealth() > 0) {
				System.out.print("\n<V>ur veya <K>aç : ");
				String selCase = scan.nextLine();
				selCase = selCase.toUpperCase();
				if (selCase.equals("V")) {
					System.out.println("Siz vurdunuz");
					obstacle.setHealth((obstacle.getHealth()-player.getTotalDamage()));
					afterHit();
					if (obstacle.getHealth() > 0) {
						System.out.println();
						System.out.println(obstacle.getName()+" size vurdu!");
						player.setHealth(player.getHealth() - (obstacle.getDamage()-player.getInv().getArmor()));
						afterHit();
					}
				}else {
					break;
				}
			}
			if (obstacle.getHealth() <= 0 && player.getHealth() > 0) {
				System.out.println("Düþmaný yendiniz.");
				player.setMoney(player.getMoney() + obstacle.getAward());
				System.out.println("Güncel paranýz : " + player.getMoney());
				obstacle.setHealth(defOfHealth);			
				
			}else {
				return false;
			}
			System.out.println("------------------------");
		}
		
		return true;
	}
	public void playerstats() {
		System.out.println("\nOyuncu deðerleri\n=======================");
		System.out.println("Can :   "+ player.getHealth());
		System.out.println("Hasar : "+ player.getDamage());
		System.out.println("Para :  "+ player.getMoney());
		if (player.getInv().getDamage()>0) {
			System.out.println("Silah : " + player.getInv().getwName());
		}
		if (player.getInv().getArmor() >0) {
		System.out.println("Zýrh :  " + player.getInv().getaName());
		}		
	}
	public void enemystats() {
		System.out.println("\n"+obstacle.getName() + " deðerleri\n=================");
		System.out.println("Can : "+obstacle.getHealth());
		System.out.println("Hasar : "+obstacle.getDamage());
		System.out.println("Ödül : "+obstacle.getAward());		
	}
	public void afterHit() {
		System.out.println("Oyuncu Caný : " + player.getHealth());
		System.out.println(obstacle.getName() + " Caný : " + obstacle.getHealth());
	}
}
