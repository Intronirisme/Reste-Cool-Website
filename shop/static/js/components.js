clamp = (value, min, max) => {return value <= min ? min : value >= max ? max : value};
map = (value, inMin, inMax, outMin, outMax) => {return clamp((value-inMin)/(inMax-inMin), 0, 1)*(outMax-outMin)+outMin};


class ScrollElem extends HTMLElement {
    constructor() {
        super();
        this.update = this.update.bind(this);
    }

    connectedCallback() {
        //DEFAULT VALUE
        if(!this.hasAttribute('start')) {
            this.setAttribute('start', this.offsetTop);
        }
        if(!this.hasAttribute('stop')) {
            this.setAttribute('stop', this.offsetTop+window.innerHeight);
        }
        if(!this.hasAttribute('from')) {
            this.setAttribute('from', '100');
        }
        if(!this.hasAttribute('to')) {
            this.setAttribute('to', '-10');
        }
        if(!this.hasAttribute('unit')) {
            this.setAttribute('unit', '%');
        }

        this.update(); //SETUP

        //EVENT LISTENER
        window.addEventListener('scroll', this.update);
    }
    
    disconnectedCallback() {
        //REMOVE EVENT LISTENER WHEN REMOVED FROM DOM
        window.removeEventListener('scroll', this.update);
    }
    
    update() {
        let y = window.scrollY;
        if(this.hasAttribute('global')) {
            document.body.style.setProperty(this.getAttribute('global'), map(y, +this.start, +this.stop, +this.from, +this.to)+this.unit);
        } else {
            this.style.setProperty('--s', map(y, +this.start, +this.stop, +this.from, +this.to)+this.unit);
        }
    }
    
    static get observedAttributes() {
        return ['start', 'stop', 'from', 'to'];
    }

    attributeChangedCallback() {
        this.update();
    }
    
    get start() {
        return this.getAttribute('start');
    }
    get stop() {
        return this.getAttribute('stop');
    }
    get from() {
        return this.getAttribute('from');
    }
    get to() {
        return this.getAttribute('to');
    }
    get unit() {
        return this.getAttribute('unit');
    }
    
    set start(newValue) {
        this.setAttribute('start', newValue);
    }
    set stop(newValue) {
        this.setAttribute('stop', newValue);
    }
    set from(newValue) {
        this.setAttribute('from', newValue);
    }
    set to(newValue) {
        this.setAttribute('to', newValue);
    }
    set unit(newValue) {
        this.setAttribute('unit', newValue);
    }
}
window.customElements.define('s-scroll', ScrollElem);