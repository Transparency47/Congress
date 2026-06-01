# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/133?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/133
- Title: A resolution expressing support for the local public K-12 schools of the United States and condemning any actions that would defund public education or weaken or dismantle the Department of Education.
- Congress: 119
- Bill type: SRES
- Bill number: 133
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2025-09-03T19:47:28Z
- Update date including text: 2025-09-03T19:47:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1805-1806)
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1805-1806)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/133",
    "number": "133",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A resolution expressing support for the local public K-12 schools of the United States and condemning any actions that would defund public education or weaken or dismantle the Department of Education.",
    "type": "SRES",
    "updateDate": "2025-09-03T19:47:28Z",
    "updateDateIncludingText": "2025-09-03T19:47:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1805-1806)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-24T20:28:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-24",
      "state": "VT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "HI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NV"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "VT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NH"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CT"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "IL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "OR"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "DE"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NM"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MN"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres133is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 133\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Mr. Schiff (for himself, Mr. Sanders , Ms. Hirono , Mr. Merkley , Mr. Padilla , Mr. Peters , Ms. Rosen , Ms. Slotkin , Mr. Van Hollen , Mr. Welch , Mrs. Shaheen , Mr. Blumenthal , Mr. Markey , Mr. Durbin , Mr. Warnock , Mr. Wyden , Ms. Blunt Rochester , Mr. Heinrich , and Ms. Klobuchar ) submitted the following resolution; which was referred to the Committee on Health, Education, Labor, and Pensions\nRESOLUTION\nExpressing support for the local public K\u201312 schools of the United States and condemning any actions that would defund public education or weaken or dismantle the Department of Education.\nThat the Senate\u2014\n**(1)**\nstrongly supports Federal investment in public K\u201312 schools and the students and families served by such schools;\n**(2)**\naffirms that the Department of Education plays a vital role in the public education system of the United States;\n**(3)**\naffirms that the Federal Government\u2019s investment is important to the success of public schools, and investment in public education should not be diverted, including through the use of vouchers, to privately-run K\u201312 schools; and\n**(4)**\ncondemns any executive or legislative action that would\u2014\n**(A)**\ndismantle or relocate major offices within the Department of Education;\n**(B)**\ndismantle or relocate the Department of Education; or\n**(C)**\nreduce Federal funding for public education, block major Federal grant programs for education, or transfer funding burdens for education to State and local governments.",
      "versionDate": "2025-03-24",
      "versionType": "IS"
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
            "name": "Department of Education",
            "updateDate": "2025-04-14T17:55:02Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-04-14T17:55:02Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2025-04-14T17:55:02Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-04-14T17:55:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-28T13:25:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
    "originChamber": "Senate",
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
          "measure-id": "id119sres133",
          "measure-number": "133",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres133v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution supports federal investment in public K-12 schools, affirms that the Department of Education (ED) plays a vital role in the public education system, and states that public education funding should not be diverted (e.g., through the use of vouchers) to privately run K-12 schools.\u00a0</p><p>The resolution also condemns any executive or legislative action to (1) dismantle or relocate ED or any of its major offices; or (2) reduce federal funding for public education, block federal grants for education, or transfer funding burdens for education to state and local governments.</p>"
        },
        "title": "A resolution expressing support for the local public K-12 schools of the United States and condemning any actions that would defund public education or weaken or dismantle the Department of Education."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres133.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports federal investment in public K-12 schools, affirms that the Department of Education (ED) plays a vital role in the public education system, and states that public education funding should not be diverted (e.g., through the use of vouchers) to privately run K-12 schools.\u00a0</p><p>The resolution also condemns any executive or legislative action to (1) dismantle or relocate ED or any of its major offices; or (2) reduce federal funding for public education, block federal grants for education, or transfer funding burdens for education to state and local governments.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119sres133"
    },
    "title": "A resolution expressing support for the local public K-12 schools of the United States and condemning any actions that would defund public education or weaken or dismantle the Department of Education."
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports federal investment in public K-12 schools, affirms that the Department of Education (ED) plays a vital role in the public education system, and states that public education funding should not be diverted (e.g., through the use of vouchers) to privately run K-12 schools.\u00a0</p><p>The resolution also condemns any executive or legislative action to (1) dismantle or relocate ED or any of its major offices; or (2) reduce federal funding for public education, block federal grants for education, or transfer funding burdens for education to state and local governments.</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119sres133"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres133is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing support for the local public K-12 schools of the United States and condemning any actions that would defund public education or weaken or dismantle the Department of Education.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T04:18:21Z"
    },
    {
      "title": "A resolution expressing support for the local public K-12 schools of the United States and condemning any actions that would defund public education or weaken or dismantle the Department of Education.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T10:56:21Z"
    }
  ]
}
```
