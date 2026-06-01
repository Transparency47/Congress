# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5021
- Title: American Decade of Sports Act
- Congress: 119
- Bill type: HR
- Bill number: 5021
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2026-05-07T14:38:23Z
- Update date including text: 2026-05-07T14:38:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 46 - 3.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-12-03 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-03 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 46 - 3.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5021",
    "number": "5021",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "American Decade of Sports Act",
    "type": "HR",
    "updateDate": "2026-05-07T14:38:23Z",
    "updateDateIncludingText": "2026-05-07T14:38:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-03",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 46 - 3.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-08-22",
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
        "item": [
          {
            "date": "2025-12-03T16:10:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-08-22T13:00:15Z",
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "MI"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NY"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "GU"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NV"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "RI"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "FL"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "DE"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "IL"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "GA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "GA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "NE"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "WA"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "AS"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "GA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "GA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "MA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "AZ"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "TX"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "MP"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5021ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5021\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Ms. Kamlager-Dove (for herself, Mr. Huizenga , Mr. Meeks , Mr. McCaul , Mr. Moylan , Ms. Salazar , Mr. Lawler , Mrs. Cherfilus-McCormick , Mr. Lieu , Ms. Titus , Mr. Amo , Ms. Castor of Florida , Ms. McBride , Mr. Jackson of Illinois , Ms. Williams of Georgia , Mr. Johnson of Georgia , Mr. Bacon , Mr. Baumgartner , Mrs. Radewagen , Mr. Carter of Georgia , Mrs. Kim , Mr. McCormick , Mr. Keating , and Mr. Stanton ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require a sports diplomacy strategy to strategically leverage the major sporting events being hosted in the United States in the next decade to enhance United States soft power, diplomatic relationships, and global leadership, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Decade of Sports Act .\n#### 2. Mega-Decade Sports Diplomacy Strategy\n##### (a) Submission\n**(1) Initial strategy**\nNot later than 120 days after the date of the enactment of this Act, the Assistant Secretary for Educational and Cultural Affairs of the Department of State shall submit to the Committee on Foreign Affairs of the House of Representatives and Committee on Foreign Relations of the Senate a 5-year sports diplomacy strategy to strategically leverage the major sporting events being hosted in the United States to enhance United States soft power, diplomatic relationships, and global leadership.\n**(2) Subsequent strategy**\nNot later than 5 years after the date on which the initial strategy is submitted pursuant to paragraph (1), the Assistant Secretary for Educational and Cultural Affairs shall submit to the Committee on Foreign Affairs of the House of Representatives and Committee on Foreign Relations of the Senate a subsequent 5-year sports diplomacy strategy in accordance with the requirements of this section.\n##### (b) Elements\nThe elements of each strategy required by subsection (a) shall include the following:\n**(1)**\nA description of the Department of State\u2019s diplomatic objectives and metrics of success related to the mega-decade of sports.\n**(2)**\nA plan to partner with local host cities, diaspora communities, creatives, athletes, the sports industry, private sector entities, human rights organizations, and civil society stakeholders surrounding the competitions for the purpose of showcasing United States national strengths and forging new diplomatic connections.\n**(3)**\nA plan to coordinate internally within the Department of State to leverage sporting events to advance various diplomatic lines of effort, including by\u2014\n**(A)**\nintegrating sports diplomacy into regional bureaus\u2019 bilateral engagements and efforts to pursue new areas of cooperation with foreign partners;\n**(B)**\nintegrating sports into public diplomacy to reach new foreign audiences that might not otherwise engage with United States embassies abroad; and\n**(C)**\nleveraging sports diplomacy to advance commercial diplomacy.\n**(4)**\nA plan to ensure an expeditious and secure visa process for athletes and their families and support staff and eligible international visitors planning to travel to the United States to attend the games, including reducing visa appointment wait times.\n**(5)**\nA description of the financial and personnel support needed to implement the 5-year sports diplomacy strategy.\n**(6)**\nAny plans to deploy domestic public diplomacy resources, such as the Cultural Unit and Foreign Press Center established during the 1984 Olympic Games, to enable foreign visitors to engage with American culture and values.\n##### (c) Public availability\nEach strategy required by subsection (a) shall be made publicly available on an internet website of the Department of State not later than 180 days after the date of the enactment of this Act, and again 5 years later.\n##### (d) Consultation\nPrior to the submission of each strategy required by subsection (a), the Assistant Secretary for Educational and Cultural Affairs shall consult with the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate on the elements of the strategy and every 180 days thereafter provide information on the implementation of each strategy until December 31, 2034.\n#### 3. Requirement for the Office of Sports Diplomacy to carry out the Mega-Decade of Sports Diplomacy Strategy\n##### (a) In general\nNo later than 90 days after the enactment of this Act, the Secretary of State shall rename the sports diplomacy division of the Department of State as the Office of Sports Diplomacy. The Office shall report directly to the Deputy Assistant Secretary for Professional and Cultural Exchanges in the Bureau of Educational and Cultural Affairs. The Office shall be responsible for managing sports diplomacy exchange programs and implementing each strategy required by section 2(a), including by carrying out the following:\n**(1)**\nCoordinating implementation of the strategy across relevant bureaus, directorates, and offices of the Department of State.\n**(2)**\nWorking with host cities and their social, political, and economic partners to identify new avenues for engagement with foreign entities.\n**(3)**\nEngaging local diaspora communities to deepen people-to-people connections with foreign visitors and officials.\n**(4)**\nPartnering with the United States sports industry, major sports leagues, and individual athletes to promote new international sports partnerships and sports diplomacy programs.\n**(5)**\nCollaborating with host cities\u2019 international trade and tourism offices to deepen economic and commercial ties with foreign nations.\n**(6)**\nElevating American arts, film, and music creators to promote cultural exchange and connection with foreign visitors.\n**(7)**\nCoordinating with internal Department and interagency stakeholders to ensure efficient and expeditious processing of visas for eligible international visitors, broadcasters, athletes, and support staff interested in attending the games.\n##### (b) Full-Time equivalent employees\nThe Secretary of State shall, not later than 180 days after the date of the enactment of this Act, and until December 31, 2034, assign to the Office of Sports Diplomacy established under subsection (a) not less than 3 additional full-time equivalent staff dedicated to implementing each strategy required by section 2(a). Such staff shall not be dual-hatted, and shall be assigned to the Office by considering mechanisms, including\u2014\n**(1)**\nthe use of existing flexible hiring authorities, including Domestic Employees Teleworking Overseas (DETOs); and\n**(2)**\nthe realignment of existing personnel.\n#### 4. Implementation report\nNot later than 1 year after the submission of the strategy required in section 2(a), and annually thereafter until December 31, 2034, the Secretary of State shall submit to the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate a report on the progress toward achieving the objectives of this Act.\n#### 5. Definition\nIn this Act, the terms mega-decade of sports and American decade of sports mean the major international sporting competitions hosted in the United States between 2024 and 2034, including the 2024 Copa America, 2025 Club World Cup, 2026 FIFA World Cup, 2028 Summer Olympics and Paralympics, the 2031 Men\u2019s and 2033 Women\u2019s Rugby World Cup, and the 2034 Winter Olympics and Paralympics.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cultural exchanges and relations",
            "updateDate": "2026-05-07T14:33:24Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-05-07T14:33:52Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-07T14:38:23Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-07T14:38:17Z"
          },
          {
            "name": "Sports and recreation facilities",
            "updateDate": "2026-05-07T14:33:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2025-09-05T16:16:48Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5021ih.xml"
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
      "title": "American Decade of Sports Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Decade of Sports Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a sports diplomacy strategy to strategically leverage the major sporting events being hosted in the United States in the next decade to enhance United States soft power, diplomatic relationships, and global leadership, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-23T08:18:24Z"
    }
  ]
}
```
