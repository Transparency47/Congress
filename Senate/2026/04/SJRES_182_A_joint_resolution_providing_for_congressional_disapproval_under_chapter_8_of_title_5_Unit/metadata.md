# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/182?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/182
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Education relating to "William D. Ford Federal Direct Loan (Direct Loan) Program".
- Congress: 119
- Bill type: SJRES
- Bill number: 182
- Origin chamber: Senate
- Introduced date: 2026-04-13
- Update date: 2026-05-26T17:47:17Z
- Update date including text: 2026-05-26T17:47:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-13: Introduced in Senate
- 2026-04-13 - IntroReferral: Introduced in Senate
- 2026-04-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-04-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 402.
- 2026-04-30 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2026-04-30 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2026-05-20 - Floor: Motion to proceed to consideration of measure rejected in Senate by Voice Vote. (CR S2407)
- Latest action: 2026-04-13: Introduced in Senate

## Actions

- 2026-04-13 - IntroReferral: Introduced in Senate
- 2026-04-13 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-04-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 402.
- 2026-04-30 - Discharge: Senate Committee on Health, Education, Labor, and Pensions discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2026-04-30 - Committee: Senate Committee on Health, Education, Labor, and Pensions discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2026-05-20 - Floor: Motion to proceed to consideration of measure rejected in Senate by Voice Vote. (CR S2407)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/182",
    "number": "182",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Education relating to \"William D. Ford Federal Direct Loan (Direct Loan) Program\".",
    "type": "SJRES",
    "updateDate": "2026-05-26T17:47:17Z",
    "updateDateIncludingText": "2026-05-26T17:47:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Motion to proceed to consideration of measure rejected in Senate by Voice Vote. (CR S2407)",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 402.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged, by petition, pursuant to 5 U.S.C. 802(c).",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Health, Education, Labor, and Pensions discharged, by petition, pursuant to 5 U.S.C. 802(c).",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-13",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2026-04-30T18:42:16Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-04-13T21:36:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MD"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "DE"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "DE"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "IL"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NH"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CO"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-13",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-04-13",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "OR"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NY"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "RI"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "WI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MN"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "HI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres182is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 182\nIN THE SENATE OF THE UNITED STATES\nApril 13, 2026 Mr. Kaine (for himself, Mrs. Gillibrand , Mr. Booker , Ms. Alsobrooks , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Coons , Mr. Durbin , Ms. Hassan , Mr. Hickenlooper , Mr. Kim , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Merkley , Mrs. Murray , Mr. Padilla , Mr. Reed , Mr. Sanders , Mr. Schiff , Mr. Van Hollen , Ms. Warren , Mr. Welch , Mr. Wyden , Mr. Schumer , and Mr. Whitehouse ) introduced the following joint resolution; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Education relating to William D. Ford Federal Direct Loan (Direct Loan) Program .\nThat Congress disapproves the rule submitted by the Department of Education relating to William D. Ford Federal Direct Loan (Direct Loan) Program (90 Fed. Reg. 48966 (October 31, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-04-13",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres182pcs.xml",
      "text": "IIA\nCalendar No. 402\n119th CONGRESS\n2d Session\nS. J. RES. 182\nIN THE SENATE OF THE UNITED STATES\nApril 13, 2026 Mr. Kaine (for himself, Mrs. Gillibrand , Mr. Booker , Ms. Alsobrooks , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Coons , Mr. Durbin , Ms. Hassan , Mr. Hickenlooper , Mr. Kim , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Merkley , Mrs. Murray , Mr. Padilla , Mr. Reed , Mr. Sanders , Mr. Schiff , Mr. Van Hollen , Ms. Warren , Mr. Welch , Mr. Wyden , Mr. Schumer , Mr. Whitehouse , Ms. Baldwin , Ms. Duckworth , Ms. Smith , Mr. Warnock , Mr. Murphy , and Ms. Hirono ) introduced the following joint resolution; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nApril 30, 2026 Committee discharged, by petition, pursuant to 5 U.S.C. 802(c) , and placed on the calendar\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Education relating to William D. Ford Federal Direct Loan (Direct Loan) Program .\nThat Congress disapproves the rule submitted by the Department of Education relating to William D. Ford Federal Direct Loan (Direct Loan) Program (90 Fed. Reg. 48966 (October 31, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-04-30",
      "versionType": "PCS"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-09",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "155",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Education relating to \"William D. Ford Federal Direct Loan (Direct Loan) Program\".",
      "type": "HJRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-05-26T17:47:01Z"
          },
          {
            "name": "Department of Education",
            "updateDate": "2026-05-26T17:47:06Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-05-26T17:47:17Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-05-26T17:47:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-04-17T19:53:24Z"
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
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres182is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres182pcs.xml"
        }
      ],
      "type": "PCS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Education relating to \"William D. Ford Federal Direct Loan (Direct Loan) Program\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-15T06:03:25Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Department of Education relating to \"William D. Ford Federal Direct Loan (Direct Loan) Program\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T10:56:24Z"
    }
  ]
}
```
