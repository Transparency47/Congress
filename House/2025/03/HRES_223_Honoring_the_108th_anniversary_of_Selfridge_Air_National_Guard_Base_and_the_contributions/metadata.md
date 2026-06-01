# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/223?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/223
- Title: Honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States.
- Congress: 119
- Bill type: HRES
- Bill number: 223
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2025-12-05T22:01:27Z
- Update date including text: 2025-12-05T22:01:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-03-14 - IntroReferral: Submitted in House
- 2025-03-14 - IntroReferral: Submitted in House
- Latest action: 2025-03-14: Submitted in House

## Actions

- 2025-03-14 - IntroReferral: Referred to the House Committee on Armed Services.
- 2025-03-14 - IntroReferral: Submitted in House
- 2025-03-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/223",
    "number": "223",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "J000307",
        "district": "10",
        "firstName": "John",
        "fullName": "Rep. James, John [R-MI-10]",
        "lastName": "James",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States.",
    "type": "HRES",
    "updateDate": "2025-12-05T22:01:27Z",
    "updateDateIncludingText": "2025-12-05T22:01:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:02:15Z",
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MI"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres223ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 223\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. James (for himself, Mr. Barrett , Mrs. Dingell , Mr. Bergman , Ms. Scholten , Mr. Huizenga , Mr. Thanedar , Mrs. McClain , Mr. Moolenaar , Ms. McDonald Rivet , Ms. Stevens , and Mr. Walberg ) submitted the following resolution; which was referred to the Committee on Armed Services\nRESOLUTION\nHonoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States.\nThat the House of Representatives\u2014\n**(1)**\nhonors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary;\n**(2)**\ncommends the thousands of men and women who have worked and trained at Selfridge Air National Guard Base;\n**(3)**\nreinforces the commitment of the Armed Forces to Selfridge Air National Guard Base as a facility that is key to the national security of United States;\n**(4)**\nencourages continued cooperation and dialogue with the Department of Defense in support of Selfridge Air National Guard Base; and\n**(5)**\nacknowledges the ongoing investments of the State of Michigan in its defense assets and workforce and continued contributions to the defense of the United States.",
      "versionDate": "2025-03-14",
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
        "actionDate": "2025-03-14",
        "text": "Referred to the Committee on Armed Services. (text: CR S1781)"
      },
      "number": "127",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the Armed Forces and national security of the United States.",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-21T00:07:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hres223",
          "measure-number": "223",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres223v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution honors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary, commends the thousands of men and women who have worked and trained at the base, and reinforces the commitment of the Armed Forces to the base as a facility that is key to national security. The resolution also encourages continued cooperation and dialogue with the Department of Defense in support of the base and acknowledges Michigan's ongoing investments in its defense assets and workforce.</p>"
        },
        "title": "Honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres223.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary, commends the thousands of men and women who have worked and trained at the base, and reinforces the commitment of the Armed Forces to the base as a facility that is key to national security. The resolution also encourages continued cooperation and dialogue with the Department of Defense in support of the base and acknowledges Michigan's ongoing investments in its defense assets and workforce.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hres223"
    },
    "title": "Honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors Selfridge Air National Guard Base in Harrison Township, Michigan, on its 108th anniversary, commends the thousands of men and women who have worked and trained at the base, and reinforces the commitment of the Armed Forces to the base as a facility that is key to national security. The resolution also encourages continued cooperation and dialogue with the Department of Defense in support of the base and acknowledges Michigan's ongoing investments in its defense assets and workforce.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hres223"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres223ih.xml"
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
      "title": "Honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T08:18:34Z"
    },
    {
      "title": "Honoring the 108th anniversary of Selfridge Air National Guard Base and the contributions of Selfridge Air National Guard Base to the military and national security of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T08:06:25Z"
    }
  ]
}
```
