#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

class TreeNode {
public:

    int peso = 1;
    string palabraroot = "";
    TreeNode *left = new TreeNode();
    TreeNode *right = new TreeNode();
    TreeNode *opcion = new TreeNode();

    TreeNode(){

    }

void setup(int pesoParam, string palabrarootParam) : peso(pesoParam), palabraroot(palabrarootParam) {
    if(left->palabraroot == ""){
        left->palabraroot = palabrarootParam;
    }else if(left->palabraroot <= palabrarootParam && right->palabraroot == ""){
        right->palabraroot = palabraroot;
    }else if(left->palabraroot > palabrarootParam){
        if(left->left == nullptr) {
            left->left = new TreeNode();
        }
        left->left->palabraroot = palabrarootParam;
    }else if(right->palabraroot < palabrarootParam){
        if(right->right == nullptr) {
            right->right = new TreeNode();
        }
        right->right->palabraroot = palabrarootParam;
    }else{
        if(right->left == nullptr) {
            right->left = new TreeNode();
        }
        right->left->palabraroot = palabrarootParam;
    }
}

void Init(int pesoParam, string palabrarootParam) {

    if(opcion == nullptr){
        opcion->peso = pesoParam;
        opcion->palabraroot = palabrarootParam;
        right->left->opcion->palabraroot = palabrarootParam;
    }else if(opcion->peso <= pesoParam && right->opcion == nullptr){
        right->opcion->palabraroot = palabrarootParam;
    }else if(opcion->peso > pesoParam){
        if(left->opcion == nullptr){
            left->opcion->palabraroot = palabrarootParam;
            right->left->opcion->peso = pesoParam;
        }else{
            left->left->opcion->palabraroot = palabrarootParam;
            right->left->opcion->peso = pesoParam;
        }
    }else if(right->opcion->peso < pesoParam){
        if(right->right->opcion == nullptr){
            right->right->opcion->peso = pesoParam;
            right->left->opcion->peso = pesoParam;
        }else{
            right->right->right->opcion->palabraroot = palabrarootParam;
            right->left->opcion->peso = pesoParam;
        }
    }else{
        if(right->left->opcion == nullptr){
            right->left->opcion->palabraroot = palabrarootParam;
            right->left->opcion->peso = pesoParam;
        }else{
            right->left->left->opcion->palabraroot = palabrarootParam;
            right->left->left->opcion->peso = pesoParam;
        }
    }
}




void LTM(){
  
}

};

/*
class Cerebro {
public:
    TreeNode arbol1;
    void setup(string palabra) {
        // Aquí puedes agregar el código para configurar el cerebro
    }
};
*/
int main() {

    cout << "procesando" << endl;

    ifstream file("0_palabras_todas.txt");
    if (!file.is_open()) {
        cout << "No se pudo abrir el archivo palabras.txt\n";
        return 1;
    }

    TreeNode* Cerebro = nullptr;
    string line;
    int peso = 1;

    string palabra;
    for (int i = 0; i < 10 && getline(file, line); i++) { 
        if (Cerebro == nullptr) {
                Cerebro->setup(peso, line);
                //Cerebro->Init(peso, line);
            } else {
                // Aquí va el código para agregar la palabra al árbol Cerebro
            }
            peso++;
    }
    cout << "proceso terminado, se leyeron todas las palabras" << endl;
    return 0;
}
