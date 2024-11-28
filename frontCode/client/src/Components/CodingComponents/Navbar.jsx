import PropTypes from 'prop-types';
import Select from 'react-select';
import './Navbar.css';

const Navbar = ({ userLang, setUserLang, userTheme, setUserTheme, fontSize, setFontSize }) => {
    const languages = [
        { value: "c", label: "C" },
        { value: "cpp", label: "C++" },
        { value: "python", label: "Python" },
        { value: "java", label: "Java" },
    ];
    const themes = [
        { value: "vs-dark", label: "Dark" },
        { value: "light", label: "Light" },
    ];
    
    return (
        <div className="navbar">
            <h1 className="text-3xl font-bold text-center">Skill Studio Compiler</h1>
            <Select
                options={languages}
                value={languages.find(lang => lang.value === userLang)}
                onChange={(e) => setUserLang(e.value)}
                placeholder="Select Language"
                className='language-select'
            />
            <Select
                options={themes}
                value={themes.find(theme => theme.value === userTheme)}
                onChange={(e) => setUserTheme(e.value)}
                placeholder="Select Theme"
                className='theme-select'
            />
            <label>Font Size</label>
            <input
                className='font-size-input'
                type="range"
                min="12"
                max="30"
                value={fontSize}
                step="2"
                onChange={(e) => setFontSize(Number(e.target.value))}
            />
        </div>
    );
};

// Define PropTypes for the component
Navbar.propTypes = {
    userLang: PropTypes.string.isRequired,
    setUserLang: PropTypes.func.isRequired,
    userTheme: PropTypes.string.isRequired,
    setUserTheme: PropTypes.func.isRequired,
    fontSize: PropTypes.number.isRequired,
    setFontSize: PropTypes.func.isRequired,
};

export default Navbar;
