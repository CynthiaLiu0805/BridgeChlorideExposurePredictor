class InputOutofOntarioError extends Error {
    constructor(message) {
        super(message);
        this.name = 'InputOutofOntarioError';
    }
}