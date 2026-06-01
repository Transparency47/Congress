# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/203
- Title: Recognizing the roles and contributions of military animals and their valiant human handlers for bravery in both war and peace, and acknowledging the importance of honoring their valor and meritorious achievements.
- Congress: 119
- Bill type: HRES
- Bill number: 203
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-06-11T16:10:49Z
- Update date including text: 2025-06-11T16:10:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House
- Latest action: 2025-03-10: Submitted in House

## Actions

- 2025-03-10 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-03-10 - IntroReferral: Submitted in House
- 2025-03-10 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/203",
    "number": "203",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Recognizing the roles and contributions of military animals and their valiant human handlers for bravery in both war and peace, and acknowledging the importance of honoring their valor and meritorious achievements.",
    "type": "HRES",
    "updateDate": "2025-06-11T16:10:49Z",
    "updateDateIncludingText": "2025-06-11T16:10:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres203ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 203\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Ms. Brownley submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nRecognizing the roles and contributions of military animals and their valiant human handlers for bravery in both war and peace, and acknowledging the importance of honoring their valor and meritorious achievements.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes and thanks the brave American service animals and their dedicated and selfless handlers who serve the United States in both war and peace; and\n**(2)**\nsupports the creation of an annual process to nominate animals for the Medal of Bravery and Distinguished Service Medal.",
      "versionDate": "2025-03-10",
      "versionType": "IH"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-15T00:15:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hres203",
          "measure-number": "203",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres203v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes and thanks American service animals and their handlers who serve the United States in times of war and peace and supports the creation of an annual process to nominate animals for the Medal of Bravery and the Distinguished Service Medal.</p>"
        },
        "title": "Recognizing the roles and contributions of military animals and their valiant human handlers for bravery in both war and peace, and acknowledging the importance of honoring their valor and meritorious achievements."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres203.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes and thanks American service animals and their handlers who serve the United States in times of war and peace and supports the creation of an annual process to nominate animals for the Medal of Bravery and the Distinguished Service Medal.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hres203"
    },
    "title": "Recognizing the roles and contributions of military animals and their valiant human handlers for bravery in both war and peace, and acknowledging the importance of honoring their valor and meritorious achievements."
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes and thanks American service animals and their handlers who serve the United States in times of war and peace and supports the creation of an annual process to nominate animals for the Medal of Bravery and the Distinguished Service Medal.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hres203"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres203ih.xml"
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
      "title": "Recognizing the roles and contributions of military animals and their valiant human handlers for bravery in both war and peace, and acknowledging the importance of honoring their valor and meritorious achievements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T08:33:25Z"
    },
    {
      "title": "Recognizing the roles and contributions of military animals and their valiant human handlers for bravery in both war and peace, and acknowledging the importance of honoring their valor and meritorious achievements.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-11T08:05:40Z"
    }
  ]
}
```
