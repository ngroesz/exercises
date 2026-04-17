/* Just your standard binary-tree implementation
 * I mostly saved this off because it was a demonstration of the regex library (in the read_file() function)
*/

#include <regex>
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <cerrno>
#include <map>
#include <queue>

using namespace std;

struct Node
{
    long int node_id;
    long int left_id;
    Node *left_child;
    long int right_id;
    Node *right_child;
    string description;
};

typedef map<long int, Node*> NodeMap;

class Tree
{
    public:
        Tree()
        {
            head = NULL;
        }

        ~Tree()
        {
            if (head != NULL) {
                delete_node(head);
            }
        }

        bool read_file(const char *filename)
        {
            ifstream input_file(filename);

            if (!input_file.is_open()) {
                cerr << "Cannot open input file " << filename << endl;
                return false;
            }

            regex match_node_with_children("([[:digit:]]+)[[:space:]]+([[:digit:]]+)[[:space:]]+([[:digit:]]+)[[:space:]]+(.*)", regex_constants::extended);
            regex match_node_without_children("([[:digit:]]+)[[:space:]]+(.*)", regex_constants::extended);
            cmatch capture;

            string line;
            NodeMap node_map;
            while (getline(input_file, line)) {
                if (regex_match(line.c_str(), capture, match_node_with_children)) {
                    long int node_id = parse_node_id(capture[1]);
                    long int left_node_id = parse_node_id(capture[2]);
                    long int right_node_id = parse_node_id(capture[3]);
                    Node *new_node = construct_node(node_id, left_node_id, right_node_id, capture[4]);

                    node_map[new_node->node_id] = new_node;
                } else if(regex_match(line.c_str(), capture, match_node_without_children)) {
                    long int node_id = parse_node_id(capture[1]);
                    Node *new_node = construct_node(node_id, -1, -1, capture[2]);

                    node_map[new_node->node_id] = new_node;
                } else {
                    cerr << "Error: Could not parse line \"" << line << "\"" << endl;
                }
            }
            this->link_nodes(node_map);

            return true;
        }

        const void print_depth_first()
        {
            this->traverse_and_print_depth_first(head);
            cout << endl;
        }

        const void print_breadth_first()
        {
            if (head == NULL) {
                return;
            }

            queue<Node *> breadth_first_queue;
            breadth_first_queue.push(head);

            Node *current_ptr;

            while (!breadth_first_queue.empty()) {
                current_ptr = breadth_first_queue.front();
                breadth_first_queue.pop();
                cout << "'" << current_ptr->description << "'" << " ";

                if (current_ptr->left_child) {
                    breadth_first_queue.push(current_ptr->left_child);
                }

                if (current_ptr->right_child) {
                    breadth_first_queue.push(current_ptr->right_child);
                }
            }
            cout << endl;
        }

    private:
        void link_nodes(const map<long int, Node *> node_map)
        {
            for (NodeMap::const_iterator loop_itr = node_map.begin(); loop_itr != node_map.end(); ++loop_itr) {
                NodeMap::const_iterator search_itr = node_map.find(loop_itr->second->left_id);
                if (search_itr != node_map.end()) {
                    loop_itr->second->left_child = search_itr->second;
                }
                search_itr = node_map.find(loop_itr->second->right_id);
                if (search_itr != node_map.end()) {
                    loop_itr->second->right_child = search_itr->second;
                }
            }

            // find the head node
            for (NodeMap::const_iterator loop_itr = node_map.begin(); loop_itr != node_map.end(); ++loop_itr) {
                bool has_parents = false;
                for (NodeMap::const_iterator search_itr = node_map.begin(); search_itr != node_map.end(); ++search_itr) {
                    if (search_itr == loop_itr) continue;
                    if (search_itr->second->left_id == loop_itr->second->node_id || search_itr->second->right_id == loop_itr->second->node_id) {
                        has_parents = true;
                        break;
                    }
                }
                if (has_parents == false) {
                    if (head) {
                        cout << "Error: Found multiple nodes with no parents (" << head->node_id << ", " << loop_itr->second->node_id << ")" << endl;
                    }
                    head = loop_itr->second;
                }
            }
            if (head == NULL) {
                cout << "Error: Cannot find my head" << endl;
            }
        }

        void delete_node(Node *starting_ptr)
        {
            if (starting_ptr->left_child) {
                delete_node(starting_ptr->left_child);
            }
            if (starting_ptr->right_child) {
                delete_node(starting_ptr->right_child);
            }
            delete starting_ptr;
        }

        const void traverse_and_print_depth_first(Node *node_ptr)
        {
            if (node_ptr == NULL) {
                return;
            }
            cout << "'" << node_ptr->description << "'" << " ";
            traverse_and_print_depth_first(node_ptr->left_child);
            traverse_and_print_depth_first(node_ptr->right_child);
        }

        Node *construct_node(const long int node_id, const long int left_id, const long int right_id, const string &description)
        {
            Node *new_node = new Node;
            new_node->node_id = node_id;
            new_node->left_id = left_id;
            new_node->left_child = NULL;
            new_node->right_id = right_id;
            new_node->right_child = NULL;
            new_node->description = description;

            return new_node;
        }

        const long int parse_node_id(const string &node_id_str)
        {
            long int node_id = 0;
            node_id = strtol(node_id_str.c_str(), NULL, 0);
            if (errno != 0) {
                cerr << "Error parsing node_id \"" << node_id_str << "\"" << endl;
            }
            return node_id;
        }

        Node *head;
};

int main(int argc, char **argv)
{
    if (argc != 2) {
        cout << "Usage: tree <input_file>" << endl;
        return 1;
    }

    Tree *tree = new Tree();
    tree->read_file(argv[1]);
    tree->print_depth_first();
    tree->print_breadth_first();

    delete tree;
}
