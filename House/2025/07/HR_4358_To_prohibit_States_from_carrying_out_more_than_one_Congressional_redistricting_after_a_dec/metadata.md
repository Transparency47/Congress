# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4358?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4358
- Title: Anti-Rigging Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4358
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-03-31T11:07:25Z
- Update date including text: 2026-03-31T11:07:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4358",
    "number": "4358",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000131",
        "district": "33",
        "firstName": "Marc",
        "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
        "lastName": "Veasey",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Anti-Rigging Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-31T11:07:25Z",
    "updateDateIncludingText": "2026-03-31T11:07:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:08:50Z",
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
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "TX"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4358ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4358\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Veasey (for himself, Ms. Johnson of Texas , Mr. Doggett , Mr. Green of Texas , Mrs. Fletcher , Ms. Escobar , and Ms. Crockett ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit States from carrying out more than one Congressional redistricting after a decennial census and apportionment.\n#### 1. Short title; finding of constitutional authority\n##### (a) Short title\nThis Act may be cited as the Anti-Rigging Act of 2025 .\n##### (b) Finding\nCongress finds that it has the authority to establish the terms and conditions States must follow in carrying out Congressional redistricting after an apportionment of Members of the House of Representatives because\u2014\n**(1)**\nthe authority granted to Congress under article I, section 4 of the Constitution of the United States gives Congress the power to enact laws governing the time, place, and manner of elections for Members of the House of Representatives; and\n**(2)**\nthe authority granted to Congress under section 5 of the fourteenth amendment to the Constitution gives Congress the power to enact laws to enforce section 2 of such amendment, which requires Representatives to be apportioned among the several States according to their number.\n#### 2. Limit on congressional redistricting after an apportionment\nThe Act entitled An Act for the relief of Doctor Ricardo Vallejo Samala and to provide for congressional redistricting , approved December 14, 1967 ( 2 U.S.C. 2c ), is amended by adding at the end the following: A State which has been redistricted in the manner provided by law after an apportionment under section 22(a) of the Act entitled An Act to provide for the fifteenth and subsequent decennial censuses and to provide for an apportionment of Representatives in Congress , approved June 18, 1929 ( 2 U.S.C. 2a ), may not be redistricted again until after the next apportionment of Representatives under such section, unless a court requires the State to conduct such subsequent redistricting to comply with the Constitution or to enforce the Voting Rights Act of 1965 (42 U.S.C. 5 1973 et seq.). .\n#### 3. No effect on elections for State and local office\nNothing in this Act or in any amendment made by this Act may be construed to affect the manner in which a State carries out elections for State or local office, including the process by which a State establishes the districts used in such elections.\n#### 4. Effective date\nThis Act and the amendment made by this Act shall apply with respect to any Congressional redistricting which occurs after the regular decennial census conducted during 2020.",
      "versionDate": "2025-07-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-09-17",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5426",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "John Tanner and Jim Cooper Fairness and Independence in Redistricting Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-05",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4889",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To prohibit States from carrying out more than one Congressional redistricting after a decennial census and apportionment.",
      "type": "HR"
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
        "updateDate": "2025-09-16T17:44:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-10",
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
          "measure-id": "id119hr4358",
          "measure-number": "4358",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-10",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4358v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong></strong><strong>Anti-Rigging Act of 2025</strong></p><p>This bill prohibits a state where the congressional districts have been redistricted after a decennial census from carrying out another redistricting until after the next apportionment of Representatives following a decennial census, unless a court requires the state to conduct a subsequent redistricting to comply with the Constitution or enforce the Voting Rights Act of 1965.</p><p>The bill is applicable to any congressional redistricting which occurs after the regular decennial census conducted during 2020.</p>"
        },
        "title": "Anti-Rigging Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4358.xml",
    "summary": {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong><strong>Anti-Rigging Act of 2025</strong></p><p>This bill prohibits a state where the congressional districts have been redistricted after a decennial census from carrying out another redistricting until after the next apportionment of Representatives following a decennial census, unless a court requires the state to conduct a subsequent redistricting to comply with the Constitution or enforce the Voting Rights Act of 1965.</p><p>The bill is applicable to any congressional redistricting which occurs after the regular decennial census conducted during 2020.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4358"
    },
    "title": "Anti-Rigging Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong><strong>Anti-Rigging Act of 2025</strong></p><p>This bill prohibits a state where the congressional districts have been redistricted after a decennial census from carrying out another redistricting until after the next apportionment of Representatives following a decennial census, unless a court requires the state to conduct a subsequent redistricting to comply with the Constitution or enforce the Voting Rights Act of 1965.</p><p>The bill is applicable to any congressional redistricting which occurs after the regular decennial census conducted during 2020.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hr4358"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4358ih.xml"
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
      "title": "Anti-Rigging Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Anti-Rigging Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T03:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit States from carrying out more than one Congressional redistricting after a decennial census and apportionment.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T03:33:32Z"
    }
  ]
}
```
