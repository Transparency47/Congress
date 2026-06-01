# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5017?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5017
- Title: Greyhound Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5017
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2026-05-16T08:07:02Z
- Update date including text: 2026-05-16T08:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Livestock, Dairy, and Poultry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-22",
    "latestAction": {
      "actionDate": "2025-08-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5017",
    "number": "5017",
    "originChamber": "House",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Greyhound Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:02Z",
    "updateDateIncludingText": "2026-05-16T08:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-08-22T13:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:51:20Z",
              "name": "Referred to"
            }
          },
          "name": "Livestock, Dairy, and Poultry Subcommittee",
          "systemCode": "hsag29"
        }
      },
      "systemCode": "hsag00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "IA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "GA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NJ"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "KS"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "TN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NJ"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "TX"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "IL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-10-06",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "NH"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NY"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "HI"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MN"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "ME"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "SC"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2026-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "MN"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "FL"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5017ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5017\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Mr. Carbajal (for himself, Mr. Fine , Mr. Davis of North Carolina , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Animal Welfare Act to prohibit commercial greyhound racing, live lure training, and open field coursing, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Greyhound Protection Act of 2025 .\n#### 2. Congressional findings and policy\nThe Congress finds the following:\n**(1)**\nGreyhounds have existed for thousands of years and are the only canines mentioned by name in the Bible.\n**(2)**\nCommercial greyhound racing was first legalized in Florida in 1931.\n**(3)**\nModern racetracks require internet-based wire communications to process bets and wagers, calculate odds, broadcast races, announce results, and pay winnings to gamblers. The majority of gambling on dog racing now occurs via simulcast and online.\n**(4)**\nPublic records reveal that some greyhounds used for live commercial racing suffer serious injuries including broken backs, broken necks, head trauma, paralysis, seizures, and electrocution.\n**(5)**\nRegulatory records show that some racing greyhounds test positive for drugs including cocaine, amphetamines, barbituates, opiods, and steroids.\n**(6)**\nState investigatory files document that racing greyhounds are kept confined for 20 to 23 hours a day in stacked, metal cages, typically with little opportunity to socialize with other dogs.\n**(7)**\nMany small animals, including jack rabbits and hares, are bought, sold, delivered, transported, and received in interstate and foreign commerce for use as live bait in the training of racing greyhounds and in open field coursing.\n**(8)**\nTypically, animals used in live lure training of greyhounds may be dragged on ropes, hung from a horizontal pole which rotates around a training track, or simply set loose to be chased and mauled. Alive or dead, helpless bait animals may be used repeatedly until they are torn apart.\n**(9)**\nLive lure training is prohibited in more than a dozen States, but there is no Federal statute prohibiting such practice. In the late 1970s, the National Greyhound Association, a membership organization representing breeders, trainers, and other industry participants, announced a policy against live lure training in order to convince the late Senators Birch Bayh and Robert Dole to withdraw their proposed legislation.\n**(10)**\nOpen field coursing preceded commercial dog racing and is an activity in which greyhounds or other sighthounds are released to pursue and kill bait animals, including jack rabbits and hares, often in a fenced area. Greyhounds may collide and suffer injuries in the chase.\n**(11)**\nDog owners travel from multiple States and countries to compete and win prizes and sometimes gamble on open field coursing events.\n**(12)**\nAs with commercial greyhound racing, internet sites are used to promote coursing tournaments and post results to a worldwide audience.\n**(13)**\nThe National Field Coursing Association is the umbrella group for coursing clubs nationwide and maintained 12 clubs in California as of 2006.\n**(14)**\nOpen field coursing is illegal in as many as 12 States.\n**(15)**\nOpen field coursing was prohibited as a blood sport in Scotland in 2002, and in the United Kingdom in 2004.\n**(16)**\n25 years ago, there were 60 greyhound tracks in the United States. With the voter-mandated closure of 12 dog tracks in Florida and the voluntary shut down of Southland Park in Arkansas and Iowa Greyhound Park in 2022, only 2 tracks, both in West Virginia, will remain nationwide.\n**(17)**\nAccording to the State of Florida, track owners had been collectively losing more than $30,000,000 annually because of sagging attendance and decreased wagering. According to a State-commissioned report, the State spent more money regulating the industry in its national hub than it generated in tax revenue. Similarly, nearly $20,000,000 is diverted annually to subsidize the 2 West Virginia tracks.\n**(18)**\nAccording to State records, more than 10,000 greyhound injuries have been reported at West Virginia racetracks since 2008. More than 3,500 dogs suffered broken bones during this period, and at least 437 dogs died after suffering serious injuries.\n**(19)**\nLive commercial dog racing is illegal in 42 States. As of December 2022, this dying industry will remain legal and operational in no more than 1 State.\n#### 3. Protection of greyhounds\n##### (a) In general\nThe Animal Welfare Act ( 7 U.S.C. 2131 et seq. ) is amended by adding at the end the following:\n30. Protection of greyhounds (a) In general It shall be unlawful\u2014 (1) for any person to knowingly engage in commercial greyhound racing, live lure training, or open field coursing events in which any greyhound is moved in interstate or foreign commerce; (2) to conduct commercial greyhound racing or racing meeting where any form of betting or wagering on the speed or ability of greyhounds occurs; (3) to conduct open field coursing or live lure training with the use of any bait that is not an inanimate object; (4) to engage in or facilitate simulcast betting or wagering on greyhound races in interstate or foreign commerce; and (5) for any person to knowingly sell, buy, possess, train, transport, deliver, or receive any greyhound for purposes of having the greyhound participate in commercial greyhound racing, live lure training, or open field coursing events. (b) Investigations The Secretary, or any other person authorized by the Secretary, shall make such investigations as the Secretary determines necessary to determine whether any person has violated or is violating any provision of this section. The Secretary may obtain the assistance of the Federal Bureau of Investigation, the Department of the Treasury, or other law enforcement agencies of the United States, and State and local governmental agencies, in the conduct of such investigations, under cooperative agreements with such agencies. (c) Penalties Any person who violates any of paragraphs (1) through (5) of subsection (a) shall be fined under this Act, imprisoned for not more than 7 years, or both, for each such violation. Each instance of a violation of any such paragraph shall be considered a single violation. (d) Definitions In this section: (1) Commercial greyhound racing The term commercial greyhound racing means any event involving the participation of greyhounds in which betting or wagering on the speed or ability of such greyhounds occurs. (2) Simulcast The term simulcast means the simultaneous audio or visual transmission from one location of foreign or domestic greyhound races taking place at a different location and gambling on the results of such races. .\n##### (b) Definition of animal\nSection 2(g) of the Animal Welfare Act ( 7 U.S.C. 2132(g) ) is amended by inserting hare, after rabbit, .\n##### (c) Applicability\nThe amendments made by this section shall apply with respect to conduct occurring on or after October 1, 2027.\n##### (d) Rule of construction\nNothing in this section, or the amendments made by this section, shall be construed\u2014\n**(1)**\nto preempt any State law prohibiting gambling or protecting the welfare of animals, including greyhounds, jackrabbits, and hares; or\n**(2)**\nto alter, limit, or extend the relationship between the Interstate Horseracing Act of 1978 ( 15 U.S.C. 3001 et seq. ) as it relates to horse racing and other Federal laws in effect on the date of enactment of this Act.",
      "versionDate": "2025-08-22",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Animals",
        "updateDate": "2026-03-24T15:16:08Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5017ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Greyhound Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Greyhound Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Animal Welfare Act to prohibit commercial greyhound racing, live lure training, and open field coursing, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-23T08:18:22Z"
    }
  ]
}
```
