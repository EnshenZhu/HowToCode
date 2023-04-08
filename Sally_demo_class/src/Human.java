public class Human {
    private String name;
    private int age;
    private String gender;

    public Human(String newName, int newAge, String newGender) {
        this.age = newAge;
        this.name = newName;
        this.gender = newGender;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
