#include <iostream>
#include <fstream>
#include <functional>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <vector>
#include <random>
using namespace std;

#include "generate_preferences.cpp"
#include "deferred_acceptance.cpp"
#include "visualization.cpp"

const bool randomness = false;

int main()
{
  vvi prefMen, prefWomen;
  vvi preffirm =
      {{3, 7, 9, 11, 5, 4, 10, 8, 6, 1, 2},
       {5, 7, 10, 6, 8, 2, 3, 11},
       {11, 6, 8, 3, 2, 4, 7, 1, 10},
       {10, 1, 2, 11, 4, 9, 5, 3, 6, 8},
       {2, 4, 10, 7, 6, 1, 8, 3, 11, 9}};
  vvi prefworker =
      {{3, 1, 5, 4},
       {1, 3, 4, 2, 5},
       {4, 5, 3, 1, 2},
       {3, 4, 1, 5},
       {1, 4, 2},
       {4, 3, 2, 1, 5},
       {2, 5, 1, 3},
       {1, 3, 2, 5, 4},
       {4, 1, 5},
       {3, 1, 5, 2, 4},
       {5, 4, 1, 3, 2}};
  vi capacity = {4, 3, 3, 2, 1};
  for (int f = 0; f < (int)preffirm.size(); f++)
  {
    for (int i = 0; i < (int)preffirm[f].size(); i++)
    {
      preffirm[f][i]--;
    }
  }
  for (int w = 0; w < (int)prefworker.size(); w++)
  {
    for (int i = 0; i < (int)prefworker[w].size(); i++)
    {
      prefworker[w][i]--;
    }
  }
  tie(prefMen, prefWomen) = canonical_convert(preffirm, prefworker, capacity);
  cerr << "Computing rotations" << endl;

  GaleShapley gs(prefMen, prefWomen);
  gs.computeSolution();

  cerr << "Output results" << endl;

  vector<string> nameMen, nameWomen;
  //* men = number, women = letters
  for (int i = 1; i <= (int)preffirm.size(); i++)
  {
    for (int cap = 1; cap <= capacity[i - 1]; cap++)
    {
      nameMen.push_back("f" + to_string(i) + "_" + to_string(cap));
    }
  }
  for (int i = 1; i <= (int)prefWomen.size(); i++) // works when nbWomen <= 26
    nameWomen.push_back("w" + to_string(i));
  //*/
  /* experimental: html formula
  for (int i=1; i<=nbMen; i++)
    nameMen.push_back("m<sub>" + to_string(i) + "</sub>");
  for (int i=1; i<=nbWomen; i++)
    nameWomen.push_back("w<sub>" + to_string(i) + "</sub>");
  //*/

  Visualization vis(nameMen, nameWomen, prefMen, prefWomen, gs.rotation, gs.edges, capacity);
  vis.enumerate();
  vis.print_data(ofstream("data.js"));
  vis.print_rotations(ofstream("rotations.dot"));
  vis.print_matchings(ofstream("matchings.dot"));
  vis.print_preferences(ofstream("preferences.html"));
}
