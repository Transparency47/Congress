# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/698
- Title: Asylum Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 698
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-04-24T15:59:12Z
- Update date including text: 2025-04-24T15:59:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/698",
    "number": "698",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Asylum Accountability Act",
    "type": "HR",
    "updateDate": "2025-04-24T15:59:12Z",
    "updateDateIncludingText": "2025-04-24T15:59:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:07:30Z",
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
      "bioguideId": "F000450",
      "district": "5",
      "firstName": "Virginia",
      "fullName": "Rep. Foxx, Virginia [R-NC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Foxx",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OH"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr698ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 698\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Rouzer (for himself, Ms. Foxx , Mr. Balderson , and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to permanently bar aliens who are ordered removed after failing to appear at a removal proceeding, absent exceptional circumstances, from becoming permanent residents of the United States.\n#### 1. Short title\nThis Act may be cited as the Asylum Accountability Act .\n#### 2. Permanent ineligibility for adjustment of status after failure to appear at removal proceeding\nSection 240(b)(7) of the Immigration and Nationality Act ( 8 U.S.C. 1229a(b)(7) ) is amended by striking for a period of 10 years after the date of the entry of the final order of removal .",
      "versionDate": "2025-01-23",
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
        "updateDate": "2025-02-24T15:47:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr698",
          "measure-number": "698",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr698v00",
            "update-date": "2025-04-24"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Asylum Accountability Act</strong></p> <p>This bill permanently bars a non-U.S. national (<em>alien</em> under federal law) from receiving certain immigration-related relief if that individual is ordered removed from the United States after failing to appear at a removal proceeding, unless that failure to appear is due to exceptional circumstances. (Currently, this bar from relief is for 10 years.) </p> <p>Under this bill, such an individual shall be permanently barred from receiving discretionary relief under specified immigration provisions, such as (1) cancellation of removal and adjustment to lawful permanent resident status, (2) being allowed to voluntarily depart from the United States, or (3) being allowed to change from one nonimmigrant classification to another. </p>"
        },
        "title": "Asylum Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr698.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Asylum Accountability Act</strong></p> <p>This bill permanently bars a non-U.S. national (<em>alien</em> under federal law) from receiving certain immigration-related relief if that individual is ordered removed from the United States after failing to appear at a removal proceeding, unless that failure to appear is due to exceptional circumstances. (Currently, this bar from relief is for 10 years.) </p> <p>Under this bill, such an individual shall be permanently barred from receiving discretionary relief under specified immigration provisions, such as (1) cancellation of removal and adjustment to lawful permanent resident status, (2) being allowed to voluntarily depart from the United States, or (3) being allowed to change from one nonimmigrant classification to another. </p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr698"
    },
    "title": "Asylum Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Asylum Accountability Act</strong></p> <p>This bill permanently bars a non-U.S. national (<em>alien</em> under federal law) from receiving certain immigration-related relief if that individual is ordered removed from the United States after failing to appear at a removal proceeding, unless that failure to appear is due to exceptional circumstances. (Currently, this bar from relief is for 10 years.) </p> <p>Under this bill, such an individual shall be permanently barred from receiving discretionary relief under specified immigration provisions, such as (1) cancellation of removal and adjustment to lawful permanent resident status, (2) being allowed to voluntarily depart from the United States, or (3) being allowed to change from one nonimmigrant classification to another. </p>",
      "updateDate": "2025-04-24",
      "versionCode": "id119hr698"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr698ih.xml"
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
      "title": "Asylum Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T08:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Asylum Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T08:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to permanently bar aliens who are ordered removed after failing to appear at a removal proceeding, absent exceptional circumstances, from becoming permanent residents of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T08:03:46Z"
    }
  ]
}
```
