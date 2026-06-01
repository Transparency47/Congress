# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/163?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/163
- Title: Expressing the sense of the House of Representatives that the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life.
- Congress: 119
- Bill type: HRES
- Bill number: 163
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2025-09-05T08:05:59Z
- Update date including text: 2025-09-05T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-02-25 - Committee: Submitted in House
- Latest action: 2025-02-25: Submitted in House

## Actions

- 2025-02-25 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-02-25 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/163",
    "number": "163",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Expressing the sense of the House of Representatives that the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life.",
    "type": "HRES",
    "updateDate": "2025-09-05T08:05:59Z",
    "updateDateIncludingText": "2025-09-05T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-25T15:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sponsorshipDate": "2025-02-25",
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
      "sponsorshipDate": "2025-02-25",
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
      "sponsorshipDate": "2025-02-25",
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
      "sponsorshipDate": "2025-02-25",
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
      "sponsorshipDate": "2025-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MI"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres163ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 163\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Huizenga (for himself, Mr. Moolenaar , Mr. Thanedar , Mrs. Dingell , Ms. McDonald Rivet , Ms. Scholten , and Mr. James ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing the sense of the House of Representatives that the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life;\n**(2)**\nencourages the development and use of literacy programs that include 1-on-1 tutoring for each student diagnosed with a literacy gap of 1 year or more, 5 days per week until the student is reading at grade level;\n**(3)**\nencourages State and local governments, including educational agencies, to collaborate with private organizations offering proven literacy programs to identify and implement effective solutions to address illiteracy; and\n**(4)**\nencourages State and local governments, including educational agencies, to collaborate with private organizations that offer proven literacy programs to create adult literacy initiatives aimed at helping adults with reading skills below an eighth-grade level.",
      "versionDate": "2025-02-25",
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
        "name": "Education",
        "updateDate": "2025-03-01T16:37:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119hres163",
          "measure-number": "163",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-25",
          "originChamber": "HOUSE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres163v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the goal of education in U.S. schools as that of ensuring that\u00a0virtually every student achieves grade-level reading proficiency. It also encourages state and local governments, including educational agencies, to collaborate with private organizations that offer proven literacy programs to (1) identify and implement effective solutions to address illiteracy, and (2) create adult literacy initiatives for adults with reading skills below an 8th grade level.</p>"
        },
        "title": "Expressing the sense of the House of Representatives that the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres163.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the goal of education in U.S. schools as that of ensuring that\u00a0virtually every student achieves grade-level reading proficiency. It also encourages state and local governments, including educational agencies, to collaborate with private organizations that offer proven literacy programs to (1) identify and implement effective solutions to address illiteracy, and (2) create adult literacy initiatives for adults with reading skills below an 8th grade level.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hres163"
    },
    "title": "Expressing the sense of the House of Representatives that the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life."
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the goal of education in U.S. schools as that of ensuring that\u00a0virtually every student achieves grade-level reading proficiency. It also encourages state and local governments, including educational agencies, to collaborate with private organizations that offer proven literacy programs to (1) identify and implement effective solutions to address illiteracy, and (2) create adult literacy initiatives for adults with reading skills below an 8th grade level.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hres163"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres163ih.xml"
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
      "title": "Expressing the sense of the House of Representatives that the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:23Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives that the goal of education in schools across America shall be that virtually every student in the United States achieves grade-level reading proficiency, providing them with the foundation to develop the skills and knowledge needed for success in school, work, and life.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T09:06:03Z"
    }
  ]
}
```
