from sqlalchemy import Column, Integer, Float, String, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, backref
from helloflask.init_db import Base

class Album(Base):
    __tablename__ = 'Album'
    albumid = Column(String, primary_key=True)
    createdt = Column(String)
    title = Column(String)
    company = Column(String)
    genre = Column(String)
    likecnt = Column(Integer)
    rate = Column(Float)
    crawldt = Column(String)
    songs = relationship('Song')

class Song(Base):
    __tablename__ = 'Song'
    songno = Column(String, primary_key=True)
    title = Column(String)
    genre = Column(String)
    likecnt = Column(Integer)
    albumid = Column(String, ForeignKey('Album.albumid'), nullable=False)
    # album = relationship('Album', backref=backref('Album'))
    album = relationship('Album')
    songartists = relationship('SongArtist')


class SongArtist(Base):
    __tablename__ = 'SongArtist'
    songno = Column(String, ForeignKey('Song.songno'), nullable=False)
    artistid = Column(String, ForeignKey('Artist.artistid'))
    atype = Column(Integer)
    song = relationship('Song')
    artist = relationship('Artist')
    __table_args__ = (PrimaryKeyConstraint('songno', 'artistid', 'atype'), {})


class Artist(Base):
    __tablename__ = 'Artist'
    artistid = Column(String, primary_key=True)
    name = Column(String)
    atype = Column(Integer)
    songartists = relationship('SongArtist')
    def atype_name(self):
        if self.atype == 1:
            return "작사"
        elif self.atype == 2:
            return "작곡"
        else:
            return "노래"

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    passwd = Column(String)
    nickname = Column(String)

    def __init__(self, email=None, nickname='손님'):
        self.email = email
        self.nickname = nickname

    def __repr__(self):
        return 'User %s, %r, %r' % (self.id, self.email, self.nickname)