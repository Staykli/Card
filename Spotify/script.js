/** @jsx dom */

let indexSong = 0;
let isLocked = false;
let songsLength = null;
let selectedSong = null;
let loadingProgress = 0;
let songIsPlayed = false;
let progress_elmnt = null;
let songName_elmnt = null;
let sliderImgs_elmnt = null;
let singerName_elmnt = null;
let progressBar_elmnt = null;
let playlistSongs_elmnt = [];
let loadingProgress_elmnt = null;
let musicPlayerInfo_elmnt = null;
let progressBarIsUpdating = false;
let broadcastGuarantor_elmnt = null;
const root = querySelector("#root");

const songs = [
  {
    "bg": "#c9bea28f",
    "artist": "sickick",
    "songName": "talking to the moon (bruno mars remix)",
    "files": {
      "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/1/song.mp3",
      "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/1/img.jpg"
    }
  },
  {
    "bg": "#0896eba1",
    "artist": "bless you",
    "songName": "driving",
    "files": {
      "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/2/song.mp3",
      "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/2/img.jpg"
    }
  },
  {
    "bg": "#ebbe03",
    "artist": "lil uzi vert",
    "songName": "demon high",
    "files": {
     "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/3/song.mp3",
     "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/3/img.jpg"
    }
  },
  {
    "bg": "#ffc382",
    "artist": "travis scott",
    "songName": "a man",
    "files": {
    "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/4/song.mp3",
    "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/4/img.jpg"
    }
  },
  {
    "bg": "#ffcbdc",
    "artist": "randall",
    "songName": "waharan",
    "files": {
    "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/5/song.mp3",
    "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/5/img.jpg"
    }
  },
  {
    "bg": "#44c16fb5",
    "artist": "tritonal",
    "songName": "diamonds (feat. rose darling)",
    "files": {
    "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/6/song.mp3",
    "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/6/img.jpg"
    }
  },
  {
    "bg": "#ff4545",
    "artist": "the weeknd",
    "songName": "blinding lights",
    "files": {
    "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/7/song.mp3",
    "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/7/img.jpg"
    }
  },
  {
    "bg": "#e5e7e9",
    "artist": "arizona zervas",
    "songName": "no i in team",
    "files": {
    "song": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/8/song.mp3",
    "cover": "https://raw.githubusercontent.com/abxlfazl/music-player-widget/main/src/assets/media/songs/8/img.jpg"
    }
  }
];

songsLength = songs.length - 1;
selectedSong = new Audio(songs[0].files.song);
selectedSong.addEventListener('timeupdate', () => {
  if (!progressBarIsUpdating) return;
  const progress = (selectedSong.currentTime / selectedSong.duration) * 100;
  setProperty(progressBar_elmnt, '--width', `${progress}%`);
});

root.appendChild(App({ songs }));

function App({ songs }) {
  function handleChangeMusic({ isPrev = false, playListIndex = null }) {
    if (isLocked || indexSong === playListIndex) return;

    if (playListIndex || playListIndex === 0) {
      indexSong = playListIndex;
    } else {
      indexSong = isPrev ? indexSong - 1 : indexSong + 1;
    }

    if (indexSong < 0) {
      indexSong = 0;
      return;
    } else if (indexSong > songsLength) {
      indexSong = songsLength;
      return;
    }

    selectedSong.pause();
    selectedSong.currentTime = 0;
    progressBarIsUpdating = false;
    selectedSong = new Audio(songs[indexSong].files.song);

    if (songIsPlayed) selectedSong.play();

    setBodyBg(songs[indexSong].bg);
    setProperty(sliderImgs_elmnt, "--index", -indexSong);
    updateInfo(singerName_elmnt, songs[indexSong].artist);
    updateInfo(songName_elmnt, songs[indexSong].songName);
  }

  setBodyBg(songs[0].bg);

  return (
    dom("div", { class: "music-player flex-column" },
      dom(Slider, { slides: songs, handleChangeMusic: handleChangeMusic }),
      dom(Playlist, { list: songs, handleChangeMusic: handleChangeMusic })
    )
  );
}

function Slider({ slides, handleChangeMusic }) {
  function handleResizeSlider({ target }) {
    if (isLocked) {
      return;
    } else if (target.classList.contains("music-player__info")) {
      this.classList.add("resize");
      setProperty(this, "--controls-animate", "down running");
      return;
    } else if (target.classList.contains("music-player__playlist-button")) {
      this.classList.remove("resize");
      setProperty(this, "--controls-animate", "up running");
      return;
    }
  }

  function handlePlayMusic() {
    if (selectedSong.currentTime === selectedSong.duration) {
      handleChangeMusic({});
    }

    this.classList.toggle("click");
    songIsPlayed = !songIsPlayed;
    selectedSong.paused ? selectedSong.play() : selectedSong.pause();
  }

  return (
    dom("div", { class: "slider center", onClick: handleResizeSlider },
      dom("div", { class: "slider__content center" },
        dom("button", { class: "music-player__playlist-button center button" },
          dom("i", { class: "icon-playlist" })
        ),
        dom("button", {
          onClick: handlePlayMusic,
          class: "music-player__broadcast-guarantor center button"
        },
          dom("i", { class: "icon-play" }),
          dom("i", { class: "icon-pause" })
        ),
        dom("div", { class: "slider__imgs flex-row" },
          slides.map(({ songName, files: { cover } }) =>
            dom("img", { src: cover, class: "img", alt: songName })
          )
        )
      ),
      dom("div", { class: "slider__controls center" },
        dom("button", {
          class: "slider__switch-button flex-row button",
          onClick: () => handleChangeMusic({ isPrev: true })
        },
          dom("i", { class: "icon-back" })
        ),
        dom("div", { class: "music-player__info text_trsf-cap" },
          dom("div", null,
            dom("div", { class: "music-player__singer-name" },
              dom("div", null, slides[0].artist)
            ),
            dom("div", null,
              dom("div", { class: "music-player__subtitle" },
                dom("div", null, slides[0].songName)
              )
            )
          )
        ),
        dom("button", {
          class: "slider__switch-button flex-row button",
          onClick: () => handleChangeMusic({ isPrev: false })
        },
          dom("i", { class: "icon-next" })
        ),
        dom("div", {
          class: "progress center",
          onPointerdown: e => {
            handleScrub(e);
            progressBarIsUpdating = true;
          }
        },
          dom("div", { class: "progress__wrapper" },
            dom("div", { class: "progress__bar center" })
          )
        )
      )
    )
  );
}

function Playlist({ list, handleChangeMusic }) {
  function loadedAudio() {
    const duration = this.duration;
    const target = this.parentElement.querySelector(".music-player__song-duration");
    target.textContent = formatTime(duration);
  }

  function handleSelectSong(index) {
    handleChangeMusic({ playListIndex: index });
  }

  return (
    dom("div", { class: "music-player__playlist flex-column" },
      list.map((song, index) =>
        dom("div", {
          class: "music-player__song flex-row",
          onClick: () => handleSelectSong(index)
        },
          dom("img", {
            src: song.files.cover,
            class: "music-player__song-img",
            alt: song.songName
          }),
          dom("div", { class: "music-player__playlist-info flex-column" },
            dom("div", { class: "text_overflow" }, song.songName),
            dom("div", { class: "music-player__song-duration" })
          ),
          dom("audio", {
            src: song.files.song,
            onLoadedMetadata: loadedAudio,
            ref: el => playlistSongs_elmnt[index] = el
          })
        )
      )
    )
  );
}

function formatTime(seconds) {
  const minutes = Math.floor(seconds / 60);
  const remainingSeconds = Math.floor(seconds % 60);
  return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}

function setBodyBg(color) {
  document.body.style.backgroundColor = color;
}

function setProperty(element, property, value) {
  element.style.setProperty(property, value);
}

function updateInfo(element, value) {
  element.textContent = value;
}

function handleScrub(event) {
  const { offsetX, target } = event;
  const { clientWidth } = target;
  const scrubTime = (offsetX / clientWidth) * selectedSong.duration;
  selectedSong.currentTime = scrubTime;
}

function querySelector(selector) {
  return document.querySelector(selector);
}

document.addEventListener('DOMContentLoaded', () => {
  root.appendChild(App({ songs }));
});