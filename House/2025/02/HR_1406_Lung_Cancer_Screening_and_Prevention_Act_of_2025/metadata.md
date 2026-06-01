# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1406?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1406
- Title: Lung Cancer Screening and Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1406
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-02-27T21:41:19Z
- Update date including text: 2026-02-27T21:41:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1406",
    "number": "1406",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Lung Cancer Screening and Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-27T21:41:19Z",
    "updateDateIncludingText": "2026-02-27T21:41:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-18T18:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "NY"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "VA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "IL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "FL"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CO"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1406ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1406\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Buchanan (for himself, Mr. Kennedy of New York , Mr. Griffith , Mr. LaHood , Mr. Soto , and Ms. Wasserman Schultz ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to authorize the coverage of additional lung cancer screening tests under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Lung Cancer Screening and Prevention Act of 2025 .\n#### 2. Authority to expand coverage of tests for lung cancer screening under the medicare program\n##### (a) In general\nSection 1834(n) of the Social Security Act ( 42 U.S.C. 1395m(n) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) of paragraph (1) as clauses (i) and (ii), respectively, with appropriate indentation;\n**(2)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, with appropriate indentation;\n**(3)**\nby striking Notwithstanding any other provision of this title and inserting:\n(1) In general Notwithstanding any other provision of this title and subject to paragraph (2) ; and\n**(4)**\nby adding at the end the following new paragraph:\n(2) Authority to cover new lung cancer screening tests as preventive services (A) In general Notwithstanding paragraph (1), in addition to preventive services consisting of screening tests for the early detection of lung cancer covered under this part pursuant to national coverage determination 210.14, the Secretary may provide for coverage under this part of other lung cancer screening tests that are cleared or approved by the Food and Drug Administration as preventive services when furnished to appropriate individuals (as determined by the Secretary), with such frequency and payment limits as the Secretary determines appropriate in consultation with appropriate organizations. (B) Use of national coverage determination process (i) In general Coverage of other lung cancer screening tests under subparagraph (A) shall be determined using the process for making national coverage determinations (as defined in section 1869(f)(1)(B)), except that there shall be no requirement for a determination under section 1861(ddd)(3)(B) with respect to such test under such process. (ii) Rule of construction Nothing in clause (i) shall be construed as preventing the Secretary from considering recommendations made by entities with expertise in preventive services, including entities convened by the Secretary or the Director of the Agency for Healthcare Research and Quality, with respect to other lung cancer screening tests described in subparagraph (A). .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date of the enactment of this Act, and apply with respect to coverage of preventive services under Part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395j et seq. ) on or after such date.",
      "versionDate": "2025-02-18",
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
            "updateDate": "2025-07-09T14:01:10Z"
          },
          {
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-07-09T14:01:10Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-07-09T14:01:10Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-09T14:01:10Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-07-09T14:01:10Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-07-09T14:01:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T14:45:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119hr1406",
          "measure-number": "1406",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1406v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Lung Cancer Screening and Prevention Act of 2025</strong></p><p>This bill authorizes Medicare coverage of additional types of lung cancer screening tests that are approved by the Food and Drug Administration, regardless of whether they are recommended by the United States Preventive Services Task Force. The Centers for Medicare & Medicaid Services must set coverage and payment limits for such tests. (Currently, Medicare covers screening tests for the early detection of lung cancer if they are recommended by the task force.)</p>"
        },
        "title": "Lung Cancer Screening and Prevention Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1406.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lung Cancer Screening and Prevention Act of 2025</strong></p><p>This bill authorizes Medicare coverage of additional types of lung cancer screening tests that are approved by the Food and Drug Administration, regardless of whether they are recommended by the United States Preventive Services Task Force. The Centers for Medicare & Medicaid Services must set coverage and payment limits for such tests. (Currently, Medicare covers screening tests for the early detection of lung cancer if they are recommended by the task force.)</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1406"
    },
    "title": "Lung Cancer Screening and Prevention Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lung Cancer Screening and Prevention Act of 2025</strong></p><p>This bill authorizes Medicare coverage of additional types of lung cancer screening tests that are approved by the Food and Drug Administration, regardless of whether they are recommended by the United States Preventive Services Task Force. The Centers for Medicare & Medicaid Services must set coverage and payment limits for such tests. (Currently, Medicare covers screening tests for the early detection of lung cancer if they are recommended by the task force.)</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1406"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1406ih.xml"
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
      "title": "Lung Cancer Screening and Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lung Cancer Screening and Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to authorize the coverage of additional lung cancer screening tests under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T09:18:23Z"
    }
  ]
}
```
