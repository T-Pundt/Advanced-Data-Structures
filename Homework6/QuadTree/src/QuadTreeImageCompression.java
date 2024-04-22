import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

class QuadTreeNode {
    private int color;
    private QuadTreeNode[] children;

    public QuadTreeNode(int color) {
        this.color = color;
        this.children = null;
    }

    public QuadTreeNode(QuadTreeNode[] children) {
        this.color = -1;
        this.children = children;
    }

    public boolean isLeaf() {
        return children == null;
    }

    public int getColor() {
        return color;
    }

    public QuadTreeNode[] getChildren() {
        return children;
    }
}

public class QuadTreeImageCompression {
    private static final int THRESHOLD = 10;

    public static QuadTreeNode compress(BufferedImage image) {
        int width = image.getWidth();
        int height = image.getHeight();

        if (width == 1 && height == 1) {
            int color = image.getRGB(0, 0);
            return new QuadTreeNode(color);
        }

        int halfWidth = width / 2;
        int halfHeight = height / 2;

        BufferedImage[] subImages = new BufferedImage[4];
        subImages[0] = image.getSubimage(0, 0, halfWidth, halfHeight);
        subImages[1] = image.getSubimage(halfWidth, 0, halfWidth, halfHeight);
        subImages[2] = image.getSubimage(0, halfHeight, halfWidth, halfHeight);
        subImages[3] = image.getSubimage(halfWidth, halfHeight, halfWidth, halfHeight);

        QuadTreeNode[] children = new QuadTreeNode[4];
        for (int i = 0; i < 4; i++) {
            children[i] = compress(subImages[i]);
        }

        if (canMerge(children)) {
            int color = children[0].getColor();
            return new QuadTreeNode(color);
        } else {
            return new QuadTreeNode(children);
        }
    }

    private static boolean canMerge(QuadTreeNode[] nodes) {
        int color = nodes[0].getColor();
        for (int i = 1; i < 4; i++) {
            if (!nodes[i].isLeaf() || nodes[i].getColor() != color) {
                return false;
            }
        }
        return true;
    }

    public static BufferedImage decompress(QuadTreeNode root, int width, int height) {
        BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);

        decompress(root, image, 0, 0, width, height);

        return image;
    }

    private static void decompress(QuadTreeNode node, BufferedImage image, int x, int y, int width, int height) {
        if (node.isLeaf()) {
            int color = node.getColor();
            for (int i = x; i < x + width; i++) {
                for (int j = y; j < y + height; j++) {
                    image.setRGB(i, j, color);
                }
            }
        } else {
            int halfWidth = width / 2;
            int halfHeight = height / 2;
            QuadTreeNode[] children = node.getChildren();
            decompress(children[0], image, x, y, halfWidth, halfHeight);
            decompress(children[1], image, x + halfWidth, y, halfWidth, halfHeight);
            decompress(children[2], image, x, y + halfHeight, halfWidth, halfHeight);
            decompress(children[3], image, x + halfWidth, y + halfHeight, halfWidth, halfHeight);
        }
    }

    public static void main(String[] args) {
        File imageFile = new File("Raccoon.jpg");
        if (imageFile.exists() && imageFile.canRead()) {
            System.out.println("The program has read access to the file.");
        } else {
            System.out.println("The program does not have read access to the file or the file does not exist.");
        }

        try {
            BufferedImage originalImage = ImageIO.read(new File("Raccoon.jpg"));
            QuadTreeNode compressedImage = compress(originalImage);
            BufferedImage decompressedImage = decompress(compressedImage, originalImage.getWidth(), originalImage.getHeight());
            ImageIO.write(decompressedImage, "png", new File("decompressed_image.png"));
            System.out.println("Image compression and decompression completed.");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}