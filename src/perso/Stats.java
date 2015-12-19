package perso;

public class Stats {

	//str for strength, dex for dexterity, vit for vitality,
	//intel for intelligence, wis for wisdom, luk for luck
	int str, dex, vit, intel, wis, luk;
	//c for current, this is the value that can be changed by status
	int cstr, cdex, cvit, cintel, cwis, cluk;

	public Stats() {
		//TODO add default constructor
		//add with arguments constructor
		str = 10;
		dex = 10;
		vit = 10;
		intel = 10;
		wis = 10;
		luk = 10;
		this.reloadTempStats();
	}
	
	public Stats(int str, int dex, int vit, int intel, int wis, int luk){
		this.str = str;
		this.dex = dex;
		this.vit = vit;
		this.intel = intel;
		this.wis = wis;
		this.luk = luk;
		this.reloadTempStats();
	}
	
	public void reloadTempStats(){
		cstr = str;
		cdex = dex;
		cvit = vit;
		cintel = intel;
		cwis = wis;
		cluk = luk;
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
	public int getInt() {
		return intel;
	}
	public int getWis() {
		return wis;
	}
	public int getLuk() {
		return luk;
	}
	//setters
	public void tempSetStr(int value){
		this.cstr = value;
	}

}
