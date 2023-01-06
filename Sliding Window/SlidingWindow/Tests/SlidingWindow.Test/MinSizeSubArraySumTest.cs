using SlidingWindow.Easy;
using Xunit;

namespace SlidingWindow.Test;

public class MinSizeSubArraySumTest
{
    [Theory]
    [InlineData(new[]{2, 1, 5, 2, 3, 2}, 7, 2)]
    [InlineData(new[] {2, 1, 5, 2, 8}, 7, 1)]
    [InlineData(new[]{3, 4, 1, 1, 6},8,3)]
    public void ShouldPassAllTests(int[] array, int S, int expected)
    {
        var actual = MinSizeSubArraySum.FindMinSubArray(array, S);
        Assert.Equal(expected, actual);
    }
}