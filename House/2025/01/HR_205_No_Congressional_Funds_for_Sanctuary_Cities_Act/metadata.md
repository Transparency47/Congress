# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/205?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/205
- Title: No Congressional Funds for Sanctuary Cities Act
- Congress: 119
- Bill type: HR
- Bill number: 205
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-06-28T08:06:21Z
- Update date including text: 2025-06-28T08:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/205",
    "number": "205",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "No Congressional Funds for Sanctuary Cities Act",
    "type": "HR",
    "updateDate": "2025-06-28T08:06:21Z",
    "updateDateIncludingText": "2025-06-28T08:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:28:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:28:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MS"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "WI"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "OH"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr205ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 205\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Van Duyne (for herself and Mr. Ellzey ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the use of Federal funds for congressional earmarks targeted to a State or unit of local government that is a sanctuary jurisdiction.\n#### 1. Short title\nThis Act may be cited as the No Congressional Funds for Sanctuary Cities Act .\n#### 2. Prohibition on use of congressional earmarks targeted to sanctuary jurisdictions\n##### (a) Prohibition\nNo Federal funds may be used for a congressional earmark targeted to a State or unit of local government which is a sanctuary jurisdiction.\n##### (b) Congressional earmark defined\nIn subsection (a), the term congressional earmark has the meaning given such term under clause 9(e) of rule XXI of the Rules of the House of Representatives.\n#### 3. Sanctuary jurisdiction defined\n##### (a) In general\nExcept as provided under subsection (b), for purposes of this Act the term sanctuary jurisdiction means any State or political subdivision of a State that has in effect a statute, ordinance, policy, or practice that prohibits or restricts any government entity or official from\u2014\n**(1)**\nsending, receiving, maintaining, or exchanging with any Federal, State, or local government entity information regarding the citizenship or immigration status (lawful or unlawful) of any individual; or\n**(2)**\ncomplying with a request lawfully made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357) to comply with a detainer for, or notify about the release of, an individual.\n##### (b) Exception\nA State or political subdivision of a State shall not be deemed a sanctuary jurisdiction based solely on its having a policy whereby its officials will not share information regarding, or comply with a request made by the Department of Homeland Security under section 236 or 287 of the Immigration and Nationality Act (8 U.S.C. 1226 and 1357) to comply with a detainer regarding, an individual who comes forward as a victim or a witness to a criminal offense.\n#### 4. Effective date\nThis Act applies with respect to fiscal year 2026 and each succeeding fiscal year.",
      "versionDate": "2025-01-03",
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
        "name": "Immigration",
        "updateDate": "2025-02-04T12:59:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr205",
          "measure-number": "205",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr205v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Congressional Funds for Sanctuary Cities Act</strong></p><p>This bill prohibits federal funds from being used as congressionally directed spending (i.e., an\u00a0earmark) for jurisdictions that withhold information about citizenship or immigration status or do not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>This prohibition begins in FY2026.</p>"
        },
        "title": "No Congressional Funds for Sanctuary Cities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr205.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Congressional Funds for Sanctuary Cities Act</strong></p><p>This bill prohibits federal funds from being used as congressionally directed spending (i.e., an\u00a0earmark) for jurisdictions that withhold information about citizenship or immigration status or do not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>This prohibition begins in FY2026.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr205"
    },
    "title": "No Congressional Funds for Sanctuary Cities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Congressional Funds for Sanctuary Cities Act</strong></p><p>This bill prohibits federal funds from being used as congressionally directed spending (i.e., an\u00a0earmark) for jurisdictions that withhold information about citizenship or immigration status or do not cooperate with immigration detainers.</p><p>Specifically, such funds are denied to any jurisdiction that has a law, policy, or practice that prohibits or restricts any government entity from</p><ul><li>maintaining, sending, or receiving information regarding the citizenship or immigration status of any individual;</li><li>exchanging information regarding an individual's citizenship or immigration status with a federal, state, or local government entity;</li><li>complying with a valid immigration detainer from the Department of Homeland Security (DHS); or</li><li>notifying DHS about an individual's release from custody.</li></ul><p>The funding restriction does not apply to a law, policy, or practice that only applies to an individual who comes forward as a victim of or a witness to a criminal offense.</p><p>This prohibition begins in FY2026.</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119hr205"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr205ih.xml"
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
      "title": "No Congressional Funds for Sanctuary Cities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-04T07:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Congressional Funds for Sanctuary Cities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T07:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of Federal funds for congressional earmarks targeted to a State or unit of local government that is a sanctuary jurisdiction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T07:48:28Z"
    }
  ]
}
```
