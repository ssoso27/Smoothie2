package baekjoon;

import java.io.*;
import java.util.Arrays;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Hacking {
    private BufferedReader br;
    private BufferedWriter bw;
    private StringTokenizer tokenizer;
    private HashMap<String, Entity> graph;

    public Hacking() {
        br = new BufferedReader(new InputStreamReader(System.in));
        bw = new BufferedWriter(new OutputStreamWriter(System.out));
    }

    private void execute() throws IOException {
        int testcases = Integer.parseInt(br.readLine());
        for(int i = 0; i < testcases; i++) {
            dijkstra();
        }
    }

    private void dijkstra() throws IOException {
        tokenizer = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(tokenizer.nextToken());
        int d = Integer.parseInt(tokenizer.nextToken());
        int c = Integer.parseInt(tokenizer.nextToken());

        Boolean[] checked = makeChecked(n, c);
        HashMap<String, String> parents = makeParents(c);
        HashMap<String, Integer> costs = makeCosts(c);

        String current = getCheapestComputer(costs);

    }

    private HashMap<String, Integer> makeCosts(int c) {
        HashMap<String, Integer> costs = new HashMap<>();
        costs.put(c+"", 0);

        return costs;
    }

    private HashMap<String, String> makeParents(int c) {
        HashMap<String, String> parents = new HashMap<>();
        parents.put(c+"", null);
        graph.get(c+"");

        return parents;
    }

    private Boolean[] makeChecked(int n, int c) {
        Boolean[] checked = new Boolean[n+1];
        Arrays.fill(checked, false);
        checked[c] = true;

        return checked;
    }

    private HashMap<String, Entity> makeGraph(int d) throws IOException {
        HashMap<String, Entity> graph = new HashMap<>();
        for(int i = 0; i < d; i++) {
            tokenizer = new StringTokenizer(br.readLine());

            String a = tokenizer.nextToken();
            String b = tokenizer.nextToken();
            int s = Integer.parseInt(tokenizer.nextToken());

            graph.put(b, new Entity(a, s));
        }
        return graph;
    }

    public static void main(String[] args) throws IOException {
        Hacking hacking = new Hacking();
        hacking.execute();
    }

    class Entity {
        private String computer;
        private Integer time;

        public String getComputer() {
            return computer;
        }

        public void setComputer(String computer) {
            this.computer = computer;
        }

        public Integer getTime() {
            return time;
        }

        public void setTime(Integer time) {
            this.time = time;
        }

        public Entity() {
        }

        public Entity(String computer, Integer time) {
            this.computer = computer;
            this.time = time;
        }
    }
}
