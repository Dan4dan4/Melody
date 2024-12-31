import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import { useSelector } from "react-redux";
import { FaSearch } from 'react-icons/fa';
import palm from '../../../../../images/palm.png'
import "./Navigation.css";
import LoginFormModal from "../LoginFormModal";


function Navigation() {
  const sessionUser = useSelector(state => state.session.user);


  return (
    <>
    <nav className="nav-container">
      <div className="nav-left">
      <NavLink to="/" className="site-name">
          <img src={palm} alt="Logo" className="Logo"/>
        </NavLink>
        <NavLink to="/" className='site-name'>
          Melody
        </NavLink>
      </div>
      
      <div className="nav-center">
        <div className="search-container">
          <FaSearch className="search-icon" />
          <input 
            type="search" 
            className="search-bar" 
            placeholder="Search for songs..."
            />
      </div>
      </div>
      <div className="nav-right">
        {sessionUser && (
          <NavLink to="/songs/new" className="nav-link">
            Add Song
          </NavLink>
        )}
        <ProfileButton />
      </div>
    </nav>
    {sessionUser && (
      <div className="side-bar">
        <NavLink to="/playlists" className="side-nav">
        Playlists
        </NavLink>
      </div>
    )}
        </>
  );
}


export default Navigation;
