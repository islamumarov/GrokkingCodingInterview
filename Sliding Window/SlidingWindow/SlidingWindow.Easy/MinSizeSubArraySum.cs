namespace SlidingWindow.Easy;

public class MinSizeSubArraySum
{
    public static int FindMinSubArray(int[] array, int S)
    {
        int min = array.Length;
        int sum = 0;
        int start = 0;
        for (int end = 0; end < array.Length; end++)
        {
            sum += array[end];
            while (sum >= S)
            {
                min = Math.Min(end - start + 1, min);
                sum -= array[start];
                start++;
            }
        }
        return min == array.Length ? 0 : min;
    }
}