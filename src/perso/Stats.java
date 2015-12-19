package perso;

public class Stats {

	//str for strength, dex for dexterity, vit for vitality,
	//intel for intelligence, wis for wisdom, luk for luck
	int str, dex, vit, intel, wis, luk;
	

	public Stats() {
		//TODO add default constructor
		//add with arguments constructor
		str = 10;
		dex = 10;
		vit = 10;
		intel = 10;
		wis = 10;
		luk = 10;
	}
	
	public Stats(int str, int dex, int vit, int intel, int wis, int luk){
		this.str = str;
		this.dex = dex;
		this.vit = vit;
		this.intel = intel;
		this.wis = wis;
		this.luk = luk;
	}
	
	
	//getters
	public int getStr() {
		return str;
	}
	public int getDex() {
		return dex;
	}
	public int getVit() {
		return vit;
	}
	public int getIntel() {
		return intel;
	}
	public int getWis() {
		return wis;
	}
	public int getLuk() {
		return luk;
	}

}
