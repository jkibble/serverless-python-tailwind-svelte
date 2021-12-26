import { register, init, getLocaleFromNavigator, locale, _, dictionary } from 'svelte-i18n';

let page = document.querySelector('#page').getAttribute('data-page');
let chosenLanguage = document.querySelector('#language').getAttribute('data-language') ?? getLocaleFromNavigator();

dictionary.set(window.lang)
// register('en', () => fetch(`/language/${page}/en.json`).then(res => res.json()));
// register('fr', () => fetch(`/language/${page}/fr.json`).then(res => res.json()));
// register('es', () => fetch(`/language/${page}/es.json`).then(res => res.json()));
// register('de', () => fetch(`/language/${page}/de.json`).then(res => res.json()));

init({
  fallbackLocale: 'en',
  initialLocale: chosenLanguage,
});


export { locale, _, dictionary };