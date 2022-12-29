namespace SlidingWindow.Easy;

public class AverageOfSubarrayOfSizeK
{
    public static double[] FindAverage(int[] array, int K)
    {
        var result = new double[array.Length-K + 1];
        var start = 0;
        var sum = 0;
        for (int i = 0; i < array.Length; i++)
        {
            sum += array[i];
            if (i >= K - 1)
            {
                result[start]= (double)sum / K;
                sum -= array[start];
                start++;
            }
        }
        
        return result;
    }
}