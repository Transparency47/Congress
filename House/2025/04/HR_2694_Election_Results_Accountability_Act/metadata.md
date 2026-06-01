# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2694?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2694
- Title: Election Results Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 2694
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-05-18T13:09:48Z
- Update date including text: 2026-05-18T13:09:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2694",
    "number": "2694",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Election Results Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-18T13:09:48Z",
    "updateDateIncludingText": "2026-05-18T13:09:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "M001177",
      "district": "5",
      "firstName": "Tom",
      "fullName": "Rep. McClintock, Tom [R-CA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McClintock",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2694ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2694\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Obernolte (for himself, Mr. Calvert , Mr. Kiley of California , Mr. Fong , Mr. Valadao , Mr. Issa , and Mr. McClintock ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to establish deadlines for States to count the ballots cast in elections for Federal office and to certify the results of elections for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Election Results Accountability Act .\n#### 2. Establishment of deadlines for counting ballots and certifying results of Federal elections\n##### (a) Deadlines\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 20181 et seq. ), as amended by section 2(a) of the COCOA Act of 2024, is amended\u2014\n**(1)**\nby redesignating sections 305 and 306 as sections 306 and 307; and\n**(2)**\nby inserting after section 304 the following new section:\n305. Deadlines for counting ballots and certifying results (a) Deadlines (1) Counting ballots Not later than 72 hours after the closing of the polls for an election for Federal office held in a State, the State shall count not less than 90 percent of the ballots cast in the election and make the result of the count publicly available. (2) Certifying results Not later than 2 weeks after the closing of the polls for an election for Federal office held in a State, the State shall\u2014 (A) complete the counting of all of the ballots cast in the election; and (B) officially certify the result of the election and make the result publicly available. (b) Exceptions A State shall not be considered to be out of compliance with the requirements of subsection (a) if the Commission and the Attorney General certify that the State\u2019s failure to meet such requirements is due to any of the following: (1) A bona fide emergency, including\u2014 (A) a major disaster (as defined in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 )); (B) a significant public health emergency, such as a pandemic or widespread outbreak; or (C) a cyberattack, data breach, or other significant security threat to the election infrastructure. (2) Technical difficulties, including\u2014 (A) malfunctioning election equipment or software; or (B) errors in the tabulation of ballots or the transmission of results that could not have been reasonably anticipated or mitigated in advance. (3) The implementation of new election procedures or reforms and the State certifies that it is in the process of complying with all such requirements, except that this paragraph applies only with respect to the first election held after the implementation of the new procedures or reforms. (4) The conducting of a recount of the results of the election. (c) Withholding of election administration funds for failure To comply with deadlines If the Commission and the Attorney General each certify that a State is not in compliance with the requirements of subsection (a) with respect to an election, the State may not receive any funds from the Commission to support the administration of subsequent elections unless\u2014 (1) the State submits to the Commission and the Attorney General a plan to ensure that the State will comply with such requirements with respect to such subsequent elections; and (2) the Commission and the Attorney General each certify that the State has taken actions to comply with such plan. .\n##### (b) Conforming amendment relating to existing enforcement provisions\nSection 401 of such Act ( 52 U.S.C. 21111 ), as amended by section 2(b) of the COCOA Act of 2024, is amended by striking and 304 and inserting 304, and 305 .\n##### (c) Clerical amendment\nThe table of contents of such Act, as amended by section 2(c) of the COCOA Act of 2024, is amended\u2014\n**(1)**\nby redesignating the items relating to sections 305 and 306 as relating to section 306 and 307; and\n**(2)**\nby inserting after the item relating to section 304 the following:\nSec. 305. Deadlines for counting ballots and certifying results. .\n##### (d) Effective date\nThis Act and the amendments made by this Act shall apply with respect to elections held after the expiration of the 90-day period which begins on the date of the enactment of this Act.",
      "versionDate": "2025-04-07",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-23T14:17:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-07",
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
          "measure-id": "id119hr2694",
          "measure-number": "2694",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2026-05-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2694v00",
            "update-date": "2026-05-18"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Election Results Accountability Act</strong></p><p>This bill establishes deadlines for states to count ballots and certify results in federal elections.\u00a0</p><p>Specifically, the bill requires a state to count not less than 90% of the ballots cast in a federal election held in the state not later than 72 hours after polls close and make the result of the count publicly available. Further, the state must certify and make publicly available the complete election results not later than two weeks after the election.\u00a0</p><p>The bill provides exceptions to these deadlines, including for bona fide emergencies (e.g., major disasters) or technical difficulties (e.g., malfunctioning election equipment or software).</p><p>The bill prohibits a state from receiving federal election administration funds for subsequent elections if the state does not comply with the deadlines established by the bill. However, a state may regain eligibility for these funds if (1) the state submits a compliance plan to the Election Assistance Commission (EAC) and the Department of Justice (DOJ), and (2) the EAC and DOJ each certify that the state has taken actions to comply with the plan.</p>"
        },
        "title": "Election Results Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2694.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Election Results Accountability Act</strong></p><p>This bill establishes deadlines for states to count ballots and certify results in federal elections.\u00a0</p><p>Specifically, the bill requires a state to count not less than 90% of the ballots cast in a federal election held in the state not later than 72 hours after polls close and make the result of the count publicly available. Further, the state must certify and make publicly available the complete election results not later than two weeks after the election.\u00a0</p><p>The bill provides exceptions to these deadlines, including for bona fide emergencies (e.g., major disasters) or technical difficulties (e.g., malfunctioning election equipment or software).</p><p>The bill prohibits a state from receiving federal election administration funds for subsequent elections if the state does not comply with the deadlines established by the bill. However, a state may regain eligibility for these funds if (1) the state submits a compliance plan to the Election Assistance Commission (EAC) and the Department of Justice (DOJ), and (2) the EAC and DOJ each certify that the state has taken actions to comply with the plan.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr2694"
    },
    "title": "Election Results Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Election Results Accountability Act</strong></p><p>This bill establishes deadlines for states to count ballots and certify results in federal elections.\u00a0</p><p>Specifically, the bill requires a state to count not less than 90% of the ballots cast in a federal election held in the state not later than 72 hours after polls close and make the result of the count publicly available. Further, the state must certify and make publicly available the complete election results not later than two weeks after the election.\u00a0</p><p>The bill provides exceptions to these deadlines, including for bona fide emergencies (e.g., major disasters) or technical difficulties (e.g., malfunctioning election equipment or software).</p><p>The bill prohibits a state from receiving federal election administration funds for subsequent elections if the state does not comply with the deadlines established by the bill. However, a state may regain eligibility for these funds if (1) the state submits a compliance plan to the Election Assistance Commission (EAC) and the Department of Justice (DOJ), and (2) the EAC and DOJ each certify that the state has taken actions to comply with the plan.</p>",
      "updateDate": "2026-05-18",
      "versionCode": "id119hr2694"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2694ih.xml"
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
      "title": "Election Results Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T09:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Election Results Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T09:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Help America Vote Act of 2002 to establish deadlines for States to count the ballots cast in elections for Federal office and to certify the results of elections for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T09:48:18Z"
    }
  ]
}
```
