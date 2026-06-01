# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2662?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2662
- Title: Staged Accident Fraud Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2662
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2026-05-14T08:08:12Z
- Update date including text: 2026-05-14T08:08:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2662",
    "number": "2662",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001129",
        "district": "10",
        "firstName": "Mike",
        "fullName": "Rep. Collins, Mike [R-GA-10]",
        "lastName": "Collins",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Staged Accident Fraud Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:12Z",
    "updateDateIncludingText": "2026-05-14T08:08:12Z"
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
          "date": "2025-04-07T16:02:05Z",
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
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "FL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "KS"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "WI"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2662ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2662\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Mr. Collins (for himself and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 49, United States Code, to prohibit staged collisions with commercial motor vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Staged Accident Fraud Prevention Act of 2025 .\n#### 2. Staging of motor vehicle collisions with commercial motor vehicles\n##### (a) In general\nChapter 805 of title 49, United States Code, is amended by adding at the end the following:\n80505. Staging of motor vehicle collisions with commercial motor vehicles (a) Penalty for staging collision A person operating a motor vehicle who intentionally causes a collision with a commercial motor vehicle, as defined in section 31101, or arranges for another person to cause such a collision, shall be fined under title 18, imprisoned for not more than 20 years, or both. (b) Penalty for staging collision causing serious bodily injury A person operating a motor vehicle who intentionally causes a collision with a commercial motor vehicle, as defined in section 31101, that results in serious bodily injury or death to another person, or arranges for another person to cause such a collision, shall be fined under title 18, imprisoned for not less than 20 years, or both. (c) Limitation on prosecution A person may not be prosecuted for an act under this section if the person has been convicted or acquitted on the merits for the same act under the laws of a State, the District of Columbia, or a territory or possession of the United States. .\n##### (b) Clerical amendment\nThe analysis for chapter 805 of title 49, United States Code, is amended by adding at the end the following:\n80505. Staging of motor vehicle collisions with commercial motor vehicles. .",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-02T12:25:07Z"
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
          "measure-id": "id119hr2662",
          "measure-number": "2662",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-07",
          "originChamber": "HOUSE",
          "update-date": "2025-09-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2662v00",
            "update-date": "2025-09-26"
          },
          "action-date": "2025-04-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Staged Accident Fraud Prevention Act of 2025 </strong></p><p>This bill makes staging a collision with a commercial motor vehicle a federal crime.</p><p>Specifically, a person who is operating a motor vehicle and intentionally causes a collision\u00a0with a commercial motor vehicle (or arranges for another person to cause such a collision) is subject to a fine, a prison term of up to 20 years, or both. If the collision results in serious bodily injury or death, the prison term may not be less than 20 years.</p>"
        },
        "title": "Staged Accident Fraud Prevention Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2662.xml",
    "summary": {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Staged Accident Fraud Prevention Act of 2025 </strong></p><p>This bill makes staging a collision with a commercial motor vehicle a federal crime.</p><p>Specifically, a person who is operating a motor vehicle and intentionally causes a collision\u00a0with a commercial motor vehicle (or arranges for another person to cause such a collision) is subject to a fine, a prison term of up to 20 years, or both. If the collision results in serious bodily injury or death, the prison term may not be less than 20 years.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr2662"
    },
    "title": "Staged Accident Fraud Prevention Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Staged Accident Fraud Prevention Act of 2025 </strong></p><p>This bill makes staging a collision with a commercial motor vehicle a federal crime.</p><p>Specifically, a person who is operating a motor vehicle and intentionally causes a collision\u00a0with a commercial motor vehicle (or arranges for another person to cause such a collision) is subject to a fine, a prison term of up to 20 years, or both. If the collision results in serious bodily injury or death, the prison term may not be less than 20 years.</p>",
      "updateDate": "2025-09-26",
      "versionCode": "id119hr2662"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2662ih.xml"
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
      "title": "Staged Accident Fraud Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Staged Accident Fraud Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to prohibit staged collisions with commercial motor vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T02:48:21Z"
    }
  ]
}
```
