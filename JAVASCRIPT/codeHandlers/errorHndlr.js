

try {
    n = 7 / 0

    if (n == Infinity)
        throw 'Error: Division on zero'
    
} catch(error) {
    console.log(error);

} finally {
    console.log('Watch out for Errors!');
}



/**               ERROR TYPES
 *  EvalError      => Erreur dans la fonction eval()
 *  RangeError     => Nombre hors limite
 *  ReferenceError => Référence inconnue
 *  SyntaxError    => Erreur de syntaxe
 *  TypeError      => Une erreur de type s'est produite
 *  URIError       => URI incorrecte
 */