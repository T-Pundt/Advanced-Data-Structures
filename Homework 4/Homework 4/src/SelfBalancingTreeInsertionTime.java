import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Random;
import java.util.TreeMap;

public class SelfBalancingTreeInsertionTime {
    public static void main(String[] args) {
        int n = 50000000; // Number of iterations
        int maxValue = 1000000; // Maximum value for random integers
        int printInterval = 300000; // Print every 10000th item
        String outputFile = "insertion_times.csv"; // Output file name

        TreeMap<Integer, Integer> tree = new TreeMap<>();
        Random random = new Random();

        try (PrintWriter writer = new PrintWriter(new FileWriter(outputFile))) {
            writer.println("Index,InsertionTime(ns)");

            for (int i = 1; i <= n; i++) {
                int value = random.nextInt(maxValue);

                long startTime = System.nanoTime();
                tree.put(value, value);
                long endTime = System.nanoTime();

                long insertionTime = endTime - startTime;

                if (i % printInterval == 0) {
                    writer.println(i + "," + insertionTime);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}