# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/468?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/468
- Title: Mel’s Law
- Congress: 119
- Bill type: HR
- Bill number: 468
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/468",
    "number": "468",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Mel\u2019s Law",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:02:15Z",
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NJ"
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
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr468ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 468\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Vel\u00e1zquez (for herself, Ms. Malliotakis , Mr. Espaillat , Mr. Tonko , Mrs. Cherfilus-McCormick , and Mrs. McIver ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to require institutions of higher education, as a condition of participation in programs under title IV of such Act, to establish a policy to award posthumous degrees to certain deceased students, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Mel\u2019s Law .\n#### 2. Requirement to award posthumous degrees\n##### (a) Posthumous degrees\nSection 487(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a) ) is amended by adding at the end the following:\n(30) The institution certifies that the institution has established a policy to award posthumous degrees to deceased students who\u2014 (A) had been enrolled in a degree program at the institution; (B) died prior to completing such program; and (C) at the time of death, were in academic standing consistent with the requirements for graduation from such program, as determined by the institution. .\n##### (b) Accreditation criteria\nSection 496(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1099b(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (6) through (8) as paragraphs (7) through (9), respectively; and\n**(2)**\nby inserting after paragraph (5) the following:\n(6) the standards for accreditation of the agency or association do not take into consideration the number of posthumous degrees awarded by the institution to deceased students; .\n##### (c) Effective date\nThe amendments made by this Act shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-01-15",
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
            "name": "Higher education",
            "updateDate": "2025-03-12T13:33:15Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-03-12T13:33:22Z"
          },
          {
            "name": "Student records",
            "updateDate": "2025-03-12T13:33:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-02-20T16:37:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr468",
          "measure-number": "468",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr468v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mel's Law</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student aid programs to establish policies for awarding posthumous degrees.</p><p>Specifically, the IHE must certify that it has a policy to award a posthumous degree to a deceased student who (1) was enrolled in a degree program at the IHE; (2) died prior to completing such program; and (3) at the time of death, was in academic standing consistent with the requirements for graduation from such program (as determined by the IHE).</p><p>The bill prohibits accrediting agencies from taking into consideration the number of posthumous degrees awarded to deceased students by the\u00a0IHE. (Under current law, an IHE must be accredited by an accrediting agency to participate in federal student aid programs.)</p>"
        },
        "title": "Mel\u2019s Law"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr468.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mel's Law</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student aid programs to establish policies for awarding posthumous degrees.</p><p>Specifically, the IHE must certify that it has a policy to award a posthumous degree to a deceased student who (1) was enrolled in a degree program at the IHE; (2) died prior to completing such program; and (3) at the time of death, was in academic standing consistent with the requirements for graduation from such program (as determined by the IHE).</p><p>The bill prohibits accrediting agencies from taking into consideration the number of posthumous degrees awarded to deceased students by the\u00a0IHE. (Under current law, an IHE must be accredited by an accrediting agency to participate in federal student aid programs.)</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr468"
    },
    "title": "Mel\u2019s Law"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mel's Law</strong></p><p>This bill requires institutions of higher education (IHEs) that participate in federal student aid programs to establish policies for awarding posthumous degrees.</p><p>Specifically, the IHE must certify that it has a policy to award a posthumous degree to a deceased student who (1) was enrolled in a degree program at the IHE; (2) died prior to completing such program; and (3) at the time of death, was in academic standing consistent with the requirements for graduation from such program (as determined by the IHE).</p><p>The bill prohibits accrediting agencies from taking into consideration the number of posthumous degrees awarded to deceased students by the\u00a0IHE. (Under current law, an IHE must be accredited by an accrediting agency to participate in federal student aid programs.)</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr468"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr468ih.xml"
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
      "title": "Mel\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T13:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mel\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T13:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to require institutions of higher education, as a condition of participation in programs under title IV of such Act, to establish a policy to award posthumous degrees to certain deceased students, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T13:33:22Z"
    }
  ]
}
```
