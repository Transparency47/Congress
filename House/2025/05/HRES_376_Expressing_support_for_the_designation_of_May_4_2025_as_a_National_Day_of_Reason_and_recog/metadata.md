# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/376?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/376
- Title: Expressing support for the designation of May 4, 2025, as a "National Day of Reason" and recognizing the central importance of reason in the betterment of humanity.
- Congress: 119
- Bill type: HRES
- Bill number: 376
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-05-27T15:03:00Z
- Update date including text: 2026-05-27T15:03:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House
- Latest action: 2025-05-01: Submitted in House

## Actions

- 2025-05-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/376",
    "number": "376",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000606",
        "district": "8",
        "firstName": "Jamie",
        "fullName": "Rep. Raskin, Jamie [D-MD-8]",
        "lastName": "Raskin",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Expressing support for the designation of May 4, 2025, as a \"National Day of Reason\" and recognizing the central importance of reason in the betterment of humanity.",
    "type": "HRES",
    "updateDate": "2026-05-27T15:03:00Z",
    "updateDateIncludingText": "2026-05-27T15:03:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-01T13:07:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "CA"
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
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "DC"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "WI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres376ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 376\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Raskin (for himself, Mr. Huffman , Ms. Brownley , Mr. Johnson of Georgia , Ms. Tlaib , and Ms. Norton ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of May 4, 2025, as a National Day of Reason and recognizing the central importance of reason in the betterment of humanity.\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of a National Day of Reason ; and\n**(2)**\nencourages all persons in the United States to observe this day and uplift the central importance of reason, critical thought, the scientific method, and free inquiry to resolving social problems and promoting the welfare of humankind.",
      "versionDate": "2025-05-01",
      "versionType": "IH"
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
        "actionDate": "2026-05-07",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1266",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of May 4, 2026, as a \"National Day of Reason\" and recognizing the central importance of reason in the betterment of humanity.",
      "type": "HRES"
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
        "updateDate": "2025-06-04T13:16:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119hres376",
          "measure-number": "376",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2025-08-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres376v00",
            "update-date": "2025-08-04"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of a National Day of Reason and encourages everyone in the United States to uplift the central importance of reason, critical thought, the scientific method, and free inquiry to resolving social problems and promoting human welfare.</p>"
        },
        "title": "Expressing support for the designation of May 4, 2025, as a \"National Day of Reason\" and recognizing the central importance of reason in the betterment of humanity."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres376.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of a National Day of Reason and encourages everyone in the United States to uplift the central importance of reason, critical thought, the scientific method, and free inquiry to resolving social problems and promoting human welfare.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hres376"
    },
    "title": "Expressing support for the designation of May 4, 2025, as a \"National Day of Reason\" and recognizing the central importance of reason in the betterment of humanity."
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of a National Day of Reason and encourages everyone in the United States to uplift the central importance of reason, critical thought, the scientific method, and free inquiry to resolving social problems and promoting human welfare.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hres376"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres376ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expressing support for the designation of May 4, 2025, as a \"National Day of Reason\" and recognizing the central importance of reason in the betterment of humanity.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T08:48:22Z"
    },
    {
      "title": "Expressing support for the designation of May 4, 2025, as a \"National Day of Reason\" and recognizing the central importance of reason in the betterment of humanity.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T08:06:46Z"
    }
  ]
}
```
