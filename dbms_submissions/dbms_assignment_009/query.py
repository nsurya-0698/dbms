Q1 = '''SELECT AVG(age) FROM player'''

Q2 = '''SELECT match_no, play_date FROM match where audience > 50000 ORDER BY match_no'''

Q3 = '''select team_id, count(win_lose) as no_of_match_own
        from matchteamdetails 
        where win_lose ="W" 
        group by team_id 
        order by no_of_match_own DESC,team_id ASC;'''
        
Q4 = '''SELECT match_no, play_date 
        FROM match 
        where stop1_sec >(select avg(stop1_sec) from match) 
        order by match_no desc;'''
        
Q5 = '''select match_no, 
        (select name from team where team_id = mc.team_id) as team_name, 
        (select name from player where player_id = mc.captain) as captain_name 
        from matchcaptain as mc  order by match_no ASC, team_name ASC;'''


Q6 = '''SELECT match.match_no, player.name, jersey_no 
        FROM match inner join player on match.player_of_match = player.player_id 
        order by match.match_no ASC;'''
 
Q7 = '''SELECT team.name, avg(age) 
        from player inner join team on player.team_id = team.team_id 
        group by team.name having avg(age) > 26 
        order  by team.name ASC;'''
        
        
Q8 = '''SELECT player.name,  player.jersey_no, player.age, 
       (select count(goal_id)  from goaldetails where goaldetails.player_id = player.player_id) as goal_count 
        from  player where player.age <= 27 and goal_count <> 0 
        order by goal_count DESC, player.name ASC;'''

Q9 = '''select team_id, ((count(goal_id) *100.0)/(select count(goal_id) from goaldetails)) as percentage_of_goal 
        from goaldetails group by team_id having count(goal_id) <> 0;'''



Q10 = '''SELECT avg(cnt) from (select count(goal_id) as cnt from goaldetails group by team_id);'''

Q11 = '''select player_id, name, date_of_birth  from player as p
         where NOT EXISTS( select * from goaldetails where goaldetails.player_id = p.player_id) order by player_id'''

Q12 = '''select `t`.name,	`match`.match_no,audience,audience-(select AVG(m1.audience) FROM team t1 inner join matchteamdetails on `t1`.team_id=`matchteamdetails`.team_id inner join match m1 on `matchteamdetails`.match_no=`m1`.match_no WHERE `t1`.team_id=`t`.team_id ) from team t inner join matchteamdetails on `t`.team_id=`matchteamdetails`.team_id inner join match on `matchteamdetails`.match_no=`match`.match_no order by `match`.match_no ASC;'''
