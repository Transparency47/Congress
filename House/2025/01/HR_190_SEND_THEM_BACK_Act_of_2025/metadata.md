# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/190?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/190
- Title: SEND THEM BACK Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 190
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-19T20:30:57Z
- Update date including text: 2025-02-19T20:30:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/190",
    "number": "190",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "SEND THEM BACK Act of 2025",
    "type": "HR",
    "updateDate": "2025-02-19T20:30:57Z",
    "updateDateIncludingText": "2025-02-19T20:30:57Z"
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
          "date": "2025-01-03T16:27:05Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AZ"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "GA"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "OK"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "SC"
    },
    {
      "bioguideId": "M001212",
      "district": "2",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr190ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 190\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Ogles (for himself, Mr. Biggs of Arizona , Mr. Clyde , Mr. Brecheen , Ms. Mace , and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide for expedited removal of certain illegal aliens.\n#### 1. Short title\nThis Act may be cited as the Sending Evading Non-Documented Threats Home Especially Migrants Biden Accepted Carelessly and Knowingly Act of 2025 or the SEND THEM BACK Act of 2025 .\n#### 2. Expedited removal of certain illegal aliens\n##### (a) In general\nNotwithstanding any other provision of law, an alien who entered the United States illegally on or since January 20, 2021, shall be subject to expedited removal, even if such alien indicated an intention to apply for asylum or a fear of persecution.\n##### (b) Exception\nSubsection (a) shall not apply to any alien who is currently a member of the Armed Forces of the United States as of January 1, 2025.",
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
        "updateDate": "2025-02-03T14:56:32Z"
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
          "measure-id": "id119hr190",
          "measure-number": "190",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr190v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sending Evading Non-Documented Threats Home Especially Migrants Biden Accepted Carelessly and Knowingly Act of 2025 or the SEND THEM BACK Act of 2025</strong></p><p>This bill subjects non-U.S. nationals (<em>aliens</em> under federal law) who illegally entered the United States on or after January 20, 2021, to expedited removal (i.e., removal without further hearing or review). This applies even if such an individual indicated an intention to apply for asylum or expressed a fear of persecution. The bill does not apply to an individual serving in the Armed Forces as of January 1, 2025.</p>"
        },
        "title": "SEND THEM BACK Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr190.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sending Evading Non-Documented Threats Home Especially Migrants Biden Accepted Carelessly and Knowingly Act of 2025 or the SEND THEM BACK Act of 2025</strong></p><p>This bill subjects non-U.S. nationals (<em>aliens</em> under federal law) who illegally entered the United States on or after January 20, 2021, to expedited removal (i.e., removal without further hearing or review). This applies even if such an individual indicated an intention to apply for asylum or expressed a fear of persecution. The bill does not apply to an individual serving in the Armed Forces as of January 1, 2025.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr190"
    },
    "title": "SEND THEM BACK Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sending Evading Non-Documented Threats Home Especially Migrants Biden Accepted Carelessly and Knowingly Act of 2025 or the SEND THEM BACK Act of 2025</strong></p><p>This bill subjects non-U.S. nationals (<em>aliens</em> under federal law) who illegally entered the United States on or after January 20, 2021, to expedited removal (i.e., removal without further hearing or review). This applies even if such an individual indicated an intention to apply for asylum or expressed a fear of persecution. The bill does not apply to an individual serving in the Armed Forces as of January 1, 2025.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr190"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr190ih.xml"
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
      "title": "SEND THEM BACK Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEND THEM BACK Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sending Evading Non-Documented Threats Home Especially Migrants Biden Accepted Carelessly and Knowingly Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-01T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for expedited removal of certain illegal aliens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T04:48:23Z"
    }
  ]
}
```
