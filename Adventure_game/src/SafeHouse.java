
public class SafeHouse extends Normalloc{
	

	SafeHouse(Player player) {
		super(player, "Güvenli Ev");
	}
	public boolean getLocation() {
		player.setHealth(player.getRhealth());
		System.out.println("Ýyileþtiniz");
		System.out.println("Þuan Güvenli Evdesiniz.");

		return true;
	}

	
}
