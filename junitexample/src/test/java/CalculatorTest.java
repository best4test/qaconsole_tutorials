import org.junit.Test;

public class CalculatorTest {

    @Test
    public void addingTest(){
        Calculator calc =  new Calculator();
        assert calc.add(1,1) == 2;
    }
}
