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
}

class Deck {
    constructor() {
        this.array = [];
        //topCard = 0;
    }

    refresh() {
        const rankArray = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'];
        const suitArray = ['♠', '♣', '♦', '♥'];

        let suitIndex = 0

        for (let i = 0; i < 52; i ++) {

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
            this.array = new Card(rankArray[i% 13], suitArray[suitIndex]);
        }
    }

    shuffle(){
        for (let i = 0; i < 100000; i++){
            x = Math.random() % 52;
            y = Math.random() % 52;
            temp = array[x];
            items[x] = items[y];
            items[y] = temp;
        }
    }

    deckDisplay() {
        for (let i = 1; i < 53; i++) {
            this.array[i - 1].cardDisplay();
            console.log(" ");
            if (i % 13 == 0) {
                console.log("\n");
            }
        }
    }

    deal() {
        dealing = array[topCard];
        topCard ++;
        return dealing
    }

    isEmpty(){
        if (topCard >= 52) {
            return true;
        }
        
        else{
            return false;
        }
    }

}

deck = new Deck;
deck.refresh();
deck.deckDisplay();

