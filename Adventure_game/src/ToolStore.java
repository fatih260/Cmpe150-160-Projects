
public class ToolStore extends Normalloc{

	ToolStore(Player player) {
		super(player, "Maðaza");
	}
	
	public boolean getLocation() {
		System.out.println("Para : " + player.getMoney());
		System.out.println("1. Silahlar");
		System.out.println("2. Zýrhlar");
		System.out.println("3. Çýkýþ");
		System.out.print("Seçiminiz : ");
		
		int selTool = scan.nextInt();
		int selItemID;
		
		switch(selTool) {
		case 1 : 
			selItemID = weaponMenu();
			buyWeapon(selItemID);			
			break;
		case 2 :
			selItemID = armorMenu();
			buyArmor(selItemID);			
			break;
		default :
			System.out.println("Çýkýþ yapýlýyor...");			
			break;
		}		
		
		return true;
	}
	
	public int armorMenu() {
		System.out.println("1. Hafif      Para : 15     Kaçýnma : 1");
		System.out.println("2. Orta       Para : 25     Kaçýnma : 3");
		System.out.println("3. Aðýr       Para : 40     Kaçýnma : 5");
		System.out.println("4. Çýkýþ ");

		System.out.print("Seçiminiz : ");
		int selarmorID = scan.nextInt();
		return selarmorID;
	}
	
	public void buyArmor(int itemID) {
		int avoid = 0;
		int cost = 0;
		String wName = null;
		switch(itemID) {
		case 1 :
			avoid = 1;
			wName = "Hafif Zýrh";
			cost = 15;
			break;
		case 2 :
			avoid = 3;
			wName = "Orta Zýrh";
			cost = 25;
			break;
		case 3 :
			avoid = 5;
			wName = "Aðýr Zýrh";
			cost = 35;
			break;
		case 4 : 
			System.out.println("Çýkýþ yapýlýyor...");
			break;
		default : 
			System.out.println("Geçersiz iþlem");
			break;
		}
		
		if (cost > 0) {
			if (player.getMoney() >= cost) {
				player.getInv().setaName(wName);
				player.getInv().setArmor(avoid);
				player.setMoney(player.getMoney()-cost);
				System.out.println(wName + " satýn aldýnýz. Engellenen hasar : " + player.getInv().getArmor());
				System.out.println("Kalan para : " + player.getMoney());

			}
			else {
				System.out.println("Para yetersiz!");
			}
		}
		
	}
		
		
	public int weaponMenu() {
		System.out.println("1. Tabanca     Para : 25    Hasar : 2");
		System.out.println("2. Kýlýç       Para : 35    Hasar : 3");
		System.out.println("3. Tüfek       Para : 45    Hasar : 7");
		System.out.println("4. Çýkýþ ");

		System.out.print("Seçiminiz : ");
		int selweaponID = scan.nextInt();
		return selweaponID;
	}
	
	public void buyWeapon(int itemID) {
		int damage = 0;
		int cost = 0;
		String wName = null;
		switch(itemID) {
		case 1 :
			damage = 2;
			wName = "Tabanca";
			cost = 25;
			break;
		case 2 :
			damage = 3;
			wName = "Kýlýç";
			cost = 35;
			break;
		case 3 :
			damage = 7;
			wName = "Tüfek";
			cost = 45;
			break;
		case 4 : 
			System.out.println("Çýkýþ yapýlýyor...");
			break;
		default : 
			System.out.println("Geçersiz iþlem");
			break;
		}
		
		if (cost > 0) {
			if (player.getMoney() >= cost) {
				player.getInv().setwName(wName);
				player.getInv().setDamage(damage);
				player.setMoney(player.getMoney()-cost);
				System.out.println(wName +" satýn aldýnýz. Önceki hasar : "+player.getDamage()+" Yeni hasar : "+player.getTotalDamage());
				System.out.println("Kalan para : " + player.getMoney());
			}
			else {
				System.out.println("Para yetersiz!");
			}
		}
		
	}
}
