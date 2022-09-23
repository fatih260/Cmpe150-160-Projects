import java.util.Scanner;

public class Player {
	private int damage, health, money, rhealth;
	private String name,cName;	
	Inventory inv;
	
	
	Scanner scan = new Scanner(System.in);
	
	
	public Player(String name) {
		this.name = name;
		this.inv = new Inventory();
	}
	
	public void selectCha() {
		switch (chaMenu()) {
		case 1 : 
			setName("Samuray");
			setDamage(5);
			setHealth(21);
			setMoney(15);
			setRhealth(21);
			break;
			
		case 2:
			setName("Okcu");
			setDamage(7);
			setHealth(18);
			setMoney(20);
			setRhealth(18);

			break;
			
		case 3:
			setName("Þovalye");
			setDamage(8);
			setHealth(24);
			setMoney(5);
			setRhealth(24);

			break;
		default :
			setName("Samuray");
			setDamage(5);
			setHealth(21);
			setMoney(15);
			setRhealth(21);

			break;
		}
		System.out.println("Karakter:"+getName()+"   Hasar:"+getDamage()+"   Saðlýk"+getHealth()+"   Para:"+getMoney()+"   Max Saðlýk:"+getRhealth());
	}
	
	public int chaMenu() {
		System.out.println("Karakter seçiniz");
		System.out.println("1- Samuray\t Hasar : 5\t Saðlýk : 21\t Para : 15");
		System.out.println("2- Okcu   \t Hasar : 7\t Saðlýk : 18\t Para : 20");
		System.out.println("3- Þovalye\t Hasar : 8\t Saðlýk : 24\t Para : 5");
		System.out.print("Seçiminiz : ");
		int chaID = scan.nextInt();
		
		while (chaID < 1 || chaID > 3) {
			System.out.print("Lütfen geçerli bir seçim yapýnýz : ");
			chaID = scan.nextInt();
		}
				
		return chaID;

	}
	
	public int getTotalDamage() {
		return (this.getDamage() + this.getInv().getDamage());
	}
	
	// getter and setters
	public int getDamage() {
		return damage;
	}
	public void setDamage(int damage) {
		this.damage = damage;
	}
	public int getHealth() {
		return health;
	}
	public void setHealth(int health) {
		this.health = health;
	}
	public int getMoney() {
		return money;
	}
	public void setMoney(int money) {
		this.money = money;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getcName() {
		return cName;
	}
	public void setcName(String cName) {
		this.cName = cName;
	}
	public Inventory getInv() {
		return inv;
	}
	public void setInv(Inventory inv) {
		this.inv = inv;
	}
	public int getRhealth() {
		return rhealth;
	}
	public void setRhealth(int rhealth) {
		this.rhealth = rhealth;
	}
	
	
}
