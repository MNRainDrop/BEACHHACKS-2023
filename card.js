// Declaration
class Card {
    constructor(suit, rank) {
        this.suit = suit;
        this.rank = rank;
    }



    getValue() {
        switch(new rank){
            case 2:
                break;
            case 3:
                return 3;
            case 4: 
                return 4;
            case 5:
                break;
            case 6:
                break;
            case 7:
                return 7;
            case 8:
                return 8;
            case 9:
                return 9;
            case 10:
                break;
            case J:
                return 10;
            case Q:
                return 11;
            case K:
                return 12;
            case A:
                return 13
        }
    }

    cardDisplay() {
        if (suit == S){
            console.log(`${rank}♠`);
        }
        else if (suit == C){
            console.log(`${rank}♣`);
        }
        else if (suit == D){
            console.log(`${rank}♦`);
        }
        else if (suit == H){
            console.log(`${rank}♥`);
        }
    }
};

class Deck {
    constructor() {
        this.array = [];
    }

    refreshDeck() {
        rankArray = [2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A];
        suitArray = ['♠', '♣', '♦', '♥'];

        suitIndex = 0

        for (i = 0; i < 52; i ++) {

            if (i < 13 ){
                suitIndex = 0;
            }

            else if  (i < 26) {
                suitIndex = 1;
            }

            else if (i < 39) {
                suitIndex = 2;
            }
            else if (i >= 39) {
                suitIndex = 3;
            }
            array = Card(rankArray[i% 13], suit[suitIndex]);
        }
    }

};