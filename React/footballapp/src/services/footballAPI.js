import axios from 'axios';

//Public football data no AUTH needed

const api = axios.create({
    baseURL:"https://www.thesportsdb.com/api/v1/json/3",
    timeout: 10000,
});

//ASYNC AWAIT with try/catch
export async function getSoccerLeagues() {
    try {
        const {data} = await api.get("/search_all_leagues.php", {
            params: { s: "Soccer" },
        });
        return data?.countries || {};
    } catch (err) {
        console.error("getSoccerLeagues failed:", err?.message || err);
        return [];
    }
} 

export async function getTeamsByLeague(leagueID) {
    try {
        const { data } = await api.get("/lookup_all_teams.php", {
            params: { id: leagueID},
        });
        return data?.teams || [];
    } catch(err) {
        console.error("getTeamsByLeague Failed:", err?.message || err);
        return [];
    }
}

export async function searchTeamsByName(name) {
    try{
        const { data } = await api.get("/searchteams.php", {
            params: { t:name },
        });
        return data?.teams || [];
    } catch(err) {
        console.error("searchTeamsByName failed:", err?.message || err);
        return [];
    }
}

//Promise request with no await/async

export function getLeaguesPromise() {
    return api
    .get("/search_all_leagues.php", { params: { s: "Soccer" } })
    .then((res) => res.data?.countries || [])
    .catch((err) => {
        console.error("getLeaguesPromise failed:", err?.message || err);
        return [];
    });
}