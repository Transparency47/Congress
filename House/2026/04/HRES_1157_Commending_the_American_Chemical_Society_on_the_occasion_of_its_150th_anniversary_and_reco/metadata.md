# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1157
- Title: Commending the American Chemical Society on the occasion of its 150th anniversary and recognizing its many years of service to the United States.
- Congress: 119
- Bill type: HRES
- Bill number: 1157
- Origin chamber: House
- Introduced date: 2026-04-09
- Update date: 2026-05-04T17:00:57Z
- Update date including text: 2026-05-04T17:00:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-09: Introduced in House
- 2026-04-09 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-04-09 - IntroReferral: Submitted in House
- Latest action: 2026-04-09: Submitted in House

## Actions

- 2026-04-09 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2026-04-09 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-09",
    "latestAction": {
      "actionDate": "2026-04-09",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1157",
    "number": "1157",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B000490",
        "district": "2",
        "firstName": "Sanford",
        "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
        "lastName": "Bishop",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Commending the American Chemical Society on the occasion of its 150th anniversary and recognizing its many years of service to the United States.",
    "type": "HRES",
    "updateDate": "2026-05-04T17:00:57Z",
    "updateDateIncludingText": "2026-05-04T17:00:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-09",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
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
          "date": "2026-04-09T15:30:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1157ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1157\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2026 Mr. Bishop (for himself and Mr. Moolenaar ) submitted the following resolution; which was referred to the Committee on Science, Space, and Technology\nRESOLUTION\nCommending the American Chemical Society on the occasion of its 150th anniversary and recognizing its many years of service to the United States.\nThat the House of Representatives\u2014\n**(1)**\ncommends the American Chemical Society on the momentous occasion of its 150th anniversary;\n**(2)**\nrecognizes the American Chemical Society for its enduring contributions to the scientific, educational, and economic strength of the United States;\n**(3)**\naffirms the importance of promoting science, technology, engineering, and mathematics (STEM) education, expanding opportunities for students to pursue chemistry and related fields, and encouraging youth from all communities to pursue careers in these disciplines; and\n**(4)**\nrequests that the Clerk of the House of Representatives transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe President of the American Chemical Society, Rigoberto Hernandez;\n**(B)**\nthe Chief Executive Officer of the American Chemical Society, Albert Horvath; and\n**(C)**\nthe Chair of the Board of the American Chemical Society, Wayne Jones.",
      "versionDate": "2026-04-09",
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
        "actionDate": "2026-04-29",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2109; text: CR S2135)"
      },
      "number": "702",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution commending the American Chemical Society on the occasion of its 150th anniversary and recognizing its many years of service to the United States.",
      "type": "SRES"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-04-14T18:33:51Z"
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
      "date": "2026-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1157ih.xml"
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
      "title": "Commending the American Chemical Society on the occasion of its 150th anniversary and recognizing its many years of service to the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T08:18:28Z"
    },
    {
      "title": "Commending the American Chemical Society on the occasion of its 150th anniversary and recognizing its many years of service to the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T08:05:46Z"
    }
  ]
}
```
