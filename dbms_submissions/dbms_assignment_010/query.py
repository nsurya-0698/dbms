Q1 = '''select player.player_id, matchcaptain.team_id, jersey_no, name, date_of_birth, age  from (player inner join matchcaptain on player.player_id = matchcaptain.captain) as pmc  left join goaldetails on goaldetails.player_id = pmc.player_id where goal_id is null;'''
Q2 = '''select team_id, count(match_no) 
        from matchteamdetails
        group by team_id;'''
Q3 = '''select `team`.team_id, count(goal_id)/23.0 
        from team inner join goaldetails on team.team_id = goaldetails.team_id group by team.team_id;'''
Q4 = '''select captain,count(match_no) as no_of_times_captain from matchcaptain group by captain'''

Q5 = '''select count(distinct m.player_of_match) as no_players
        from match as m inner join matchcaptain as mc on m.match_no = mc.match_no 
        where m.match_no = mc.match_no and m.player_of_match = mc.captain;'''
        
Q6 = '''select distinct p.player_id as playerids from player as p
        where EXISTS (select mc.captain from matchcaptain as mc where p.player_id == mc.captain) AND 
        NOT EXISTS (select m.player_of_match from match as m where m.player_of_match ==  p.player_id)'''
        
Q7 = '''Select strftime('%m', m.play_date) as Month, count(match_no) as no_of_match 
        from match as m  group by Month order by no_of_match DESC'''
        
Q8 = '''select p.jersey_no, count(mc.captain) as no_captain
        from player as p inner join matchcaptain as mc 
        on p.player_id = mc.captain  group by jersey_no order by 
        no_captain DESC, jersey_no DESC;'''
        
Q9 = '''select  player_id, avg(audience) as avg_audience from player inner join matchteamdetails on `player`.team_id = `matchteamdetails`.team_id inner join  match on `match`.match_no = `matchteamdetails`.match_no group by player_id order by avg_audience DESC, player_id DESC;
'''

Q10 = '''select team_id, avg(age) from player group by team_id;'''

Q11 = '''select avg(p.age) from matchcaptain as mc inner join player as p on p.player_id = mc.captain;'''

Q12 = '''select  strftime('%m', date_of_birth) as month, count(player_id) as no_of_players from player group by month order by no_of_players DESC, month DESC;'''

Q13 = '''select captain, count() as no_of_wins
        from matchteamdetails as mtd inner join  matchcaptain as mc on mc.team_id = mtd.team_id
        where win_lose == "W" and mc.match_no == mtd.match_no group by captain order by no_of_wins DESC'''