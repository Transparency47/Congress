# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2356?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2356
- Title: Dual Loyalty Disclosure Act
- Congress: 119
- Bill type: HR
- Bill number: 2356
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-08-30T08:05:31Z
- Update date including text: 2025-08-30T08:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2356",
    "number": "2356",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Dual Loyalty Disclosure Act",
    "type": "HR",
    "updateDate": "2025-08-30T08:05:31Z",
    "updateDateIncludingText": "2025-08-30T08:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:04:50Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AZ"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "LA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "GA"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "AK"
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
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "PA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2356ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2356\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Massie (for himself, Mr. Biggs of Arizona , Mr. Higgins of Louisiana , and Ms. Greene of Georgia ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo require that the statement required under the Federal Election Campaign Act of 1971 for a candidate to designate a principal campaign committee include information with respect to whether the candidate is a citizen of any country other than the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Dual Loyalty Disclosure Act .\n#### 2. Contents of statement of candidacy\n##### (a) In general\nSection 302(e)(1) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30102(e)(1) ) is amended by inserting , and shall include, in the case the candidate is a citizen of any country other than the United States, a disclosure with respect to such citizenship that includes an identification of the other country of which the candidate is a citizen after principal campaign committee of such candidate .\n##### (b) Effective date\nThe amendment made by this section shall take effect on the date of the enactment of this Act.",
      "versionDate": "2025-03-26",
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
        "updateDate": "2025-05-09T16:04:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-26",
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
          "measure-id": "id119hr2356",
          "measure-number": "2356",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-26",
          "originChamber": "HOUSE",
          "update-date": "2025-06-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2356v00",
            "update-date": "2025-06-30"
          },
          "action-date": "2025-03-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Dual Loyalty Disclosure Act</strong></p><p>This bill requires a candidate for federal office (other than a nominee for Vice President) who is a citizen of any country other than the United States to disclose such citizenship (including the other country of citizenship)\u00a0in the candidate's statement of candidacy. A statement of candidacy collects basic information about the candidate and is where the candidate designates their principal campaign committee.</p>"
        },
        "title": "Dual Loyalty Disclosure Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2356.xml",
    "summary": {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dual Loyalty Disclosure Act</strong></p><p>This bill requires a candidate for federal office (other than a nominee for Vice President) who is a citizen of any country other than the United States to disclose such citizenship (including the other country of citizenship)\u00a0in the candidate's statement of candidacy. A statement of candidacy collects basic information about the candidate and is where the candidate designates their principal campaign committee.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2356"
    },
    "title": "Dual Loyalty Disclosure Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Dual Loyalty Disclosure Act</strong></p><p>This bill requires a candidate for federal office (other than a nominee for Vice President) who is a citizen of any country other than the United States to disclose such citizenship (including the other country of citizenship)\u00a0in the candidate's statement of candidacy. A statement of candidacy collects basic information about the candidate and is where the candidate designates their principal campaign committee.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2356"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2356ih.xml"
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
      "title": "Dual Loyalty Disclosure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dual Loyalty Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that the statement required under the Federal Election Campaign Act of 1971 for a candidate to designate a principal campaign committee include information with respect to whether the candidate is a citizen of any country other than the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:22Z"
    }
  ]
}
```
