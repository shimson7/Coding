def larger_sport_facility(lt, wt, le, we):
    larger_facility = "Tie"
    
    eurecom = lt * wt
    telecomparistech = le * we
    
    if eurecom > telecomparistech:
        larger_facility = "TelecomParisTech"
    elif eurecom < telecomparistech:
        larger_facility = "Eurecom"
        
    return larger_facility


if __name__ == "__main__":
    for _ in range(int(input())):
        lt, wt, le, we = map(int, input().split())
        
        print(larger_sport_facility(lt=lt, wt=wt, le=le, we=we))