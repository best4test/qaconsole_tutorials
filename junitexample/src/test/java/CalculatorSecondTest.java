import org.junit.Test;

public class CalculatorSecondTest {

    @Test
    public void addingTest_LOMA0006(){
        Calculator calc =  new Calculator();
        assert calc.add(1,1) == 2;
    }
}
