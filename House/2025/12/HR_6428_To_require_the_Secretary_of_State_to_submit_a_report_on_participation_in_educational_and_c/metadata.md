# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6428
- Title: To require the Secretary of State to submit a report on participation in educational and cultural exchange programs.
- Congress: 119
- Bill type: HR
- Bill number: 6428
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-04T19:21:20Z
- Update date including text: 2026-05-04T19:21:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 3.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 3.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6428",
    "number": "6428",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001287",
        "district": "6",
        "firstName": "Ami",
        "fullName": "Rep. Bera, Ami [D-CA-6]",
        "lastName": "Bera",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "To require the Secretary of State to submit a report on participation in educational and cultural exchange programs.",
    "type": "HR",
    "updateDate": "2026-05-04T19:21:20Z",
    "updateDateIncludingText": "2026-05-04T19:21:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 42 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
        "item": [
          {
            "date": "2026-03-26T16:38:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-04T14:03:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "SC"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "MD"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "DE"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6428ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6428\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Bera (for himself and Mr. Wilson of South Carolina ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Secretary of State to submit a report on participation in educational and cultural exchange programs.\n#### 1. Promoting United States educational and cultural exchange programs\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nCongress recognizes the critical role of international exchange and study abroad programs in advancing United States national security interests, strengthening diplomatic ties, and fostering global leadership skills among emerging leaders, particularly in regions vital to United States strategic interests;\n**(2)**\neducational and cultural exchange programs are critical soft power tools for building influence with the next generation of leaders in partner nations;\n**(3)**\nthe People\u2019s Republic of China is actively deploying such programs to expand its influence; and\n**(4)**\nthe United States must expand and strengthen its own exchange programs to maintain and advance United States strategic interests globally.\n##### (b) Reporting requirements\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and every 5 years thereafter, the Secretary of State shall submit to the appropriate congressional committees a report that includes\u2014\n**(A)**\na list, disaggregated by country, of the number of individuals who participated in educational or cultural exchange programs sponsored or funded by the People\u2019s Republic of China in the previous year;\n**(B)**\na list, disaggregated by country, of the number of individuals who participated in a program described in paragraph (2) in the previous year;\n**(C)**\nin coordination with the Monitoring, Evaluation, Learning, and Innovation Unit, for each program described in paragraph (2)\u2014\n**(i)**\nthe amount of funds provided by the United States for the program;\n**(ii)**\nthe number of participants in the program;\n**(iii)**\nthe number of cohorts in the program;\n**(iv)**\nthe countries of origin of the participants in the program;\n**(v)**\nthe ages of the participants in the program;\n**(vi)**\nthe percent of participants in the program who reported a more favorable opinion of the United States Government following participation in the program;\n**(vii)**\nthe percent of foreign participants who traveled to the United States for the first time during the program;\n**(viii)**\nthe percent of foreign participants who reported that they are more likely to recommend the United States as a good place to study following participation in the program;\n**(ix)**\nthe percent of foreign participants who reported a more favorable opinion of United States citizens following participation in the program;\n**(x)**\nthe percent of foreign participants who reported an increased understanding of United States culture and values as a result of participation in the program;\n**(xi)**\nthe percent of participants who agreed with statements in support of democratic values following participation in the program;\n**(xii)**\nthe percent of foreign participants who reported an increased network of United States citizens as a result of participation in the program; and\n**(xiii)**\nthe percent of participants who reported that they understand that the program they participated in is a Department of State program;\n**(D)**\nan assessment of trends of participation in the programs described in subparagraph (A) and paragraph (2) and an analysis of the implications of such trends for United States diplomatic and strategic interests; and\n**(E)**\nan analysis of the impact of such programs on the diplomatic standing and strategic influence of the United States and the People\u2019s Republic of China in each respective country.\n**(2) Programs described**\nThe programs described in this paragraph are the following:\n**(A)**\nThe Fulbright Program.\n**(B)**\nThe Young African Leaders Initiative, including the Mandela Washington Fellowship.\n**(C)**\nThe Young Southeast Asian Leaders Initiative.\n**(D)**\nThe Kennedy-Lugar Youth Exchange and Study Program.\n**(E)**\nThe Future Leaders Exchange Program.\n**(F)**\nAny educational or cultural exchange program sponsored or funded by the United States that was previously included in a report required by paragraph (1).\n**(G)**\nIn the case of any report required by paragraph (1) submitted after the first such report, not fewer than 10 educational or cultural exchange programs sponsored or funded by the United States that have not been included in a previous such report.\n**(3) Form**\nThe reports required in this subsection shall be submitted in an unclassified form, but may include a classified annex.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations of the Senate.",
      "versionDate": "2025-12-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Area studies and international education",
            "updateDate": "2026-05-04T19:21:04Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-04T19:21:20Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-05-04T19:21:12Z"
          },
          {
            "name": "International exchange and broadcasting",
            "updateDate": "2026-05-04T19:20:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-01-06T19:55:23Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6428ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State to submit a report on participation in educational and cultural exchange programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:33Z"
    },
    {
      "title": "To require the Secretary of State to submit a report on participation in educational and cultural exchange programs.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T09:06:32Z"
    }
  ]
}
```
