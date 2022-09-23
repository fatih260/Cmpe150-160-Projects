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
			setName("�ovalye");
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
		System.out.println("Karakter:"+getName()+"   Hasar:"+getDamage()+"   Sa�l�k"+getHealth()+"   Para:"+getMoney()+"   Max Sa�l�k:"+getRhealth());
	}
	
	public int chaMenu() {
		System.out.println("Karakter se�iniz");
		System.out.println("1- Samuray\t Hasar : 5\t Sa�l�k : 21\t Para : 15");
		System.out.println("2- Okcu   \t Hasar : 7\t Sa�l�k : 18\t Para : 20");
		System.out.println("3- �ovalye\t Hasar : 8\t Sa�l�k : 24\t Para : 5");
		System.out.print("Se�iminiz : ");
		int chaID = scan.nextInt();
		
		while (chaID < 1 || chaID > 3) {
			System.out.print("L�tfen ge�erli bir se�im yap�n�z : ");
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
