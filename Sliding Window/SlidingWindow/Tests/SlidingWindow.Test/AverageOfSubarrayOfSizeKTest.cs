using SlidingWindow.Easy;
using Xunit;

namespace SlidingWindow.Test;

public class AverageOfSubarrayOfSizeKTest
{
    [Theory]
    [InlineData(new[] {1, 3, 2, 6, -1, 4, 1, 8, 2}, 5, new[] {2.2, 2.8, 2.4, 3.6, 2.8})]
    [InlineData(new[] {5},1,new[] {5.0})]
    public void ShouldPassAllTests(int[] array, int K, double[] expected)
    {
        var actual = AverageOfSubarrayOfSizeK.FindAverage(array, K);

        Assert.Equal(expected, actual);
    }
}