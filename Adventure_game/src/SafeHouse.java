
public class SafeHouse extends Normalloc{
	

	SafeHouse(Player player) {
		super(player, "G�venli Ev");
	}
	public boolean getLocation() {
		player.setHealth(player.getRhealth());
		System.out.println("�yile�tiniz");
		System.out.println("�uan G�venli Evdesiniz.");

		return true;
	}

	
}
