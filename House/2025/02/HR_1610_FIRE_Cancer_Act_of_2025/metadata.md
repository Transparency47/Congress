# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1610?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1610
- Title: FIRE Cancer Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1610
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-03-21T08:05:53Z
- Update date including text: 2026-03-21T08:05:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1610",
    "number": "1610",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "FIRE Cancer Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-21T08:05:53Z",
    "updateDateIncludingText": "2026-03-21T08:05:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:03:40Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NE"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1610ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1610\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Gottheimer (for himself, Mr. Bacon , Ms. Gillen , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Federal Fire Prevention and Control Act of 1974 to make available under the assistance to firefighters grant program the establishment of cancer prevention programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Firefighter Investments to Recognize Exposure to Cancer Act of 2025 or the FIRE Cancer Act of 2025 .\n#### 2. Cancer prevention programs for firefighters\n##### (a) In general\nSection 33 of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2229 ) is amended\u2014\n**(1)**\nin subsection (c)(3)\u2014\n**(A)**\nby redesignating subparagraphs (F) through (N) as subparagraphs (G) through (O), respectively; and\n**(B)**\nby inserting after subparagraph (E) the following new subparagraph:\n(F) To establish cancer prevention programs for firefighting personnel, including providing multi-cancer early detection testing or other forms of preventative tests. ;\n**(2)**\nin subsection (i), by adding at the end the following new paragraph:\n(4) Maximum amount for certain cancer tests Not more than $1,750 from available grant funds under subsection (c)(3)(F) may be obligated and expended for each multi-cancer early detection test or other form of preventative test. ;\n**(3)**\nin subsection (q), by adding at the end the following new paragraph:\n(4) Cancer prevention programs There is authorized to be appropriated $700,000,000 for grants under subsection (c)(3)(F). ;\n**(4)**\nby redesignating subsection (r) as subsection (s); and\n**(5)**\nby inserting after subsection (q) the following new subsection:\n(r) Cancer research The Administrator of FEMA and the Director of the Centers for Disease Control and Prevention shall jointly establish a voluntary program through which firefighting personnel may share with the Centers results of multi-cancer early detection testing or other forms of preventative tests in order to identify any trends or causes of cancer in such personnel. Any such results shall be shared in an anonymized, de-identified manner that safeguards the personally identifiable information of such personnel in order to prevent attribution to any such personnel of any such shared results. .\n##### (b) Technical and conforming amendment\nParagraph (1) of section 33(i) of the Federal Fire Prevention and Control Act of 1974 ( 15 U.S.C. 2229(i) ) is amended by striking described in subsection (c)(3)(F) and inserting described in subsection (c)(3)(G) .",
      "versionDate": "2025-02-26",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cancer",
            "updateDate": "2025-07-24T14:38:14Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-07-24T14:38:24Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2025-07-24T14:38:28Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-07-24T14:38:33Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-24T14:38:20Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-07-24T14:38:38Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-07-24T14:38:43Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T17:33:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1610",
          "measure-number": "1610",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-08-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1610v00",
            "update-date": "2025-08-14"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Firefighter Investments to Recognize Exposure to Cancer Act of 2025 or the FIRE Cancer Act of 2025</strong></p><p>This bill expands the Federal Emergency Management Agency's (FEMA's) Assistance to Firefighters Grant program for fire departments and emergency medical services organizations to include cancer prevention programs (e.g., multi-cancer early detection testing)\u00a0for firefighting personnel. It also establishes a joint cancer research program between FEMA and the Centers for Disease Control and Prevention (CDC)\u00a0through which firefighting personnel may voluntarily share the anonymized results of preventative cancer testing so the CDC can study trends or causes of cancer in such personnel.</p>"
        },
        "title": "FIRE Cancer Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1610.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Firefighter Investments to Recognize Exposure to Cancer Act of 2025 or the FIRE Cancer Act of 2025</strong></p><p>This bill expands the Federal Emergency Management Agency's (FEMA's) Assistance to Firefighters Grant program for fire departments and emergency medical services organizations to include cancer prevention programs (e.g., multi-cancer early detection testing)\u00a0for firefighting personnel. It also establishes a joint cancer research program between FEMA and the Centers for Disease Control and Prevention (CDC)\u00a0through which firefighting personnel may voluntarily share the anonymized results of preventative cancer testing so the CDC can study trends or causes of cancer in such personnel.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr1610"
    },
    "title": "FIRE Cancer Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Firefighter Investments to Recognize Exposure to Cancer Act of 2025 or the FIRE Cancer Act of 2025</strong></p><p>This bill expands the Federal Emergency Management Agency's (FEMA's) Assistance to Firefighters Grant program for fire departments and emergency medical services organizations to include cancer prevention programs (e.g., multi-cancer early detection testing)\u00a0for firefighting personnel. It also establishes a joint cancer research program between FEMA and the Centers for Disease Control and Prevention (CDC)\u00a0through which firefighting personnel may voluntarily share the anonymized results of preventative cancer testing so the CDC can study trends or causes of cancer in such personnel.</p>",
      "updateDate": "2025-08-14",
      "versionCode": "id119hr1610"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1610ih.xml"
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
      "title": "FIRE Cancer Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FIRE Cancer Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Firefighter Investments to Recognize Exposure to Cancer Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Fire Prevention and Control Act of 1974 to make available under the assistance to firefighters grant program the establishment of cancer prevention programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:01Z"
    }
  ]
}
```
