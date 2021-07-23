package sample.java.project;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNull;
import org.junit.Before;
import org.junit.Test;

public class SampleJavaProjectTest {
    private SampleJavaProject sjp;
    @Before
    public final void setUp() {
        sjp = new SampleJavaProject();
    }
    @Test
    public final void testGetSet() {
        sjp.setName("foo");
        assertEquals("foo", sjp.getName());
    }
    @Test(expected=NullPointerException.class)
    public final void nullTest() {
        sjp.setName(null);
    }
}
