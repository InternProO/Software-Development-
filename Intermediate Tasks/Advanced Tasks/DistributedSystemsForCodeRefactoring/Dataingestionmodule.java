import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class DataIngestionModule {
    public static void main(String[] args) {
        File folder = new File("path/to/legacy/code");
        File[] listOfFiles = folder.listFiles();

        for (File file : listOfFiles) {
            if (file.isFile()) {
                try (Stream<String> lines = Files.lines(Paths.get(file.getAbsolutePath()))) {
                    lines.forEach(line -> {
                        // Process the line of code
                        // Extract relevant features
                        // Store the data in a database
                    });
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
