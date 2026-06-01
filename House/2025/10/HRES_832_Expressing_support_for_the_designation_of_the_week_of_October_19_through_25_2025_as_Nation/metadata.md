# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/832?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/832
- Title: Expressing support for the designation of the week of October 19 through 25, 2025, as "National Chemistry Week".
- Congress: 119
- Bill type: HRES
- Bill number: 832
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-04-02T19:31:40Z
- Update date including text: 2026-04-02T19:31:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-10-24 - IntroReferral: Submitted in House
- 2025-10-24 - IntroReferral: Submitted in House
- Latest action: 2025-10-24: Submitted in House

## Actions

- 2025-10-24 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-10-24 - IntroReferral: Submitted in House
- 2025-10-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/832",
    "number": "832",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001194",
        "district": "2",
        "firstName": "John",
        "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
        "lastName": "Moolenaar",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Expressing support for the designation of the week of October 19 through 25, 2025, as \"National Chemistry Week\".",
    "type": "HRES",
    "updateDate": "2026-04-02T19:31:40Z",
    "updateDateIncludingText": "2026-04-02T19:31:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
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
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:02:30Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "IN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "GA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres832ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 832\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mr. Moolenaar (for himself, Mr. Bishop , Mr. Carson , and Mr. Carter of Georgia ) submitted the following resolution; which was referred to the Committee on Science, Space, and Technology\nRESOLUTION\nExpressing support for the designation of the week of October 19 through 25, 2025, as National Chemistry Week .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of National Chemistry Week ;\n**(2)**\nsupports the goals and welcomes the participants of the 36th annual National Chemistry Week;\n**(3)**\nrecognizes the need to promote the fields of science, including chemistry, technology, engineering, and mathematics, and to encourage youth, including from underrepresented groups, to pursue careers in these fields; and\n**(4)**\ncommends the American Chemical Society and the partners of that society for seeking opportunities to engage with the public and for organizing and convening events and activities surrounding National Chemistry Week each year.",
      "versionDate": "2025-10-24",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-03T17:46:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-24",
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
          "measure-id": "id119hres832",
          "measure-number": "832",
          "measure-type": "hres",
          "orig-publish-date": "2025-10-24",
          "originChamber": "HOUSE",
          "update-date": "2026-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres832v00",
            "update-date": "2026-04-02"
          },
          "action-date": "2025-10-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of National Chemistry Week. </p> <p>The resolution also recognizes the need to promote the fields of science, including chemistry, technology, engineering, and mathematics, and to encourage youth, including from underrepresented groups, to pursue careers in these fields. </p> <ul> </ul>"
        },
        "title": "Expressing support for the designation of the week of October 19 through 25, 2025, as \"National Chemistry Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres832.xml",
    "summary": {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Chemistry Week. </p> <p>The resolution also recognizes the need to promote the fields of science, including chemistry, technology, engineering, and mathematics, and to encourage youth, including from underrepresented groups, to pursue careers in these fields. </p> <ul> </ul>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hres832"
    },
    "title": "Expressing support for the designation of the week of October 19 through 25, 2025, as \"National Chemistry Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Chemistry Week. </p> <p>The resolution also recognizes the need to promote the fields of science, including chemistry, technology, engineering, and mathematics, and to encourage youth, including from underrepresented groups, to pursue careers in these fields. </p> <ul> </ul>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hres832"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres832ih.xml"
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
      "title": "Expressing support for the designation of the week of October 19 through 25, 2025, as \"National Chemistry Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T04:18:14Z"
    },
    {
      "title": "Expressing support for the designation of the week of October 19 through 25, 2025, as \"National Chemistry Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-25T08:05:42Z"
    }
  ]
}
```
