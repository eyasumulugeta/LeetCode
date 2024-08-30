class Solution {
    public double[] convertTemperature(double celsius) {
        double[] temp = new double[2];
        double kelvin = 0.0, fahrenheit = 0.0f;

        kelvin = celsius + 273.15;
        fahrenheit = (celsius * 1.80) + 32.00;

        temp[0] = kelvin;
        temp[1] = fahrenheit;

        return temp;
    }
}