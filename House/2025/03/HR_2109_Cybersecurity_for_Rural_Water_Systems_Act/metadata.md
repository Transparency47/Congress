# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2109
- Title: Cybersecurity for Rural Water Systems Act
- Congress: 119
- Bill type: HR
- Bill number: 2109
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-05-21T08:08:36Z
- Update date including text: 2026-05-21T08:08:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2109",
    "number": "2109",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000230",
        "district": "1",
        "firstName": "Donald",
        "fullName": "Rep. Davis, Donald G. [D-NC-1]",
        "lastName": "Davis",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Cybersecurity for Rural Water Systems Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:36Z",
    "updateDateIncludingText": "2026-05-21T08:08:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:13:05Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "IA"
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
      "sponsorshipDate": "2025-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2109ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2109\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Davis of North Carolina (for himself and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo include cybersecurity technical assistance in the national rural water and wastewater circuit rider program of Department of Agriculture.\n#### 1. Short title\nThis Act may be cited as the Cybersecurity for Rural Water Systems Act .\n#### 2. Inclusion of cybersecurity technical assistance in the national rural water and wastewater circuit rider program\n##### (a) In general\nSection 306(a)(22)(A) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a)(22)(A) ) is amended\u2014\n**(1)**\nby striking and at the end of clause (i); and\n**(2)**\nby redesignating clause (ii) as clause (iii) and inserting after clause (i) the following:\n(ii) shall include cybersecurity technical assistance for rural water systems serving fewer than 10,000 persons, to\u2014 (I) assess system efficacy in protecting against cyber threats; and (II) implement cybersecurity plans, procedures, and technologies to protect against cyber threats; and .\n##### (b) Extension of program\nSection 306(a)(22)(B) of such Act ( 7 U.S.C. 1926(a)(22)(B) ) is amended by striking $25,000,000 for each of fiscal years 2019 through 2023 and inserting $32,500,000 for each of fiscal years 2026 through 2030, of which $7,500,000 for each of the fiscal years shall be used to provide cybersecurity technical assistance in accordance with subparagraph (A)(ii) .",
      "versionDate": "2025-03-14",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-14T13:07:05Z"
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
          "measure-id": "id119hr2109",
          "measure-number": "2109",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2109v00",
            "update-date": "2025-06-09"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Cybersecurity for Rural Water Systems Act</strong></p><p>This bill amends the Department of Agriculture (USDA) Circuit Rider Program to include cybersecurity technical assistance for rural water systems serving fewer than 10,000 people. Under the program, USDA provides technical assistance to rural water systems that are experiencing day-to-day operational, financial, or managerial issues.</p><p>Specifically, the program's cybersecurity technical assistance must (1) assess system efficacy in protecting against cyber threats; and (2) implement cybersecurity plans, procedures, and technologies to protect against cyber threats.</p><p>The bill also reauthorizes the Circuit Rider Program through FY2030.</p>"
        },
        "title": "Cybersecurity for Rural Water Systems Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2109.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cybersecurity for Rural Water Systems Act</strong></p><p>This bill amends the Department of Agriculture (USDA) Circuit Rider Program to include cybersecurity technical assistance for rural water systems serving fewer than 10,000 people. Under the program, USDA provides technical assistance to rural water systems that are experiencing day-to-day operational, financial, or managerial issues.</p><p>Specifically, the program's cybersecurity technical assistance must (1) assess system efficacy in protecting against cyber threats; and (2) implement cybersecurity plans, procedures, and technologies to protect against cyber threats.</p><p>The bill also reauthorizes the Circuit Rider Program through FY2030.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr2109"
    },
    "title": "Cybersecurity for Rural Water Systems Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Cybersecurity for Rural Water Systems Act</strong></p><p>This bill amends the Department of Agriculture (USDA) Circuit Rider Program to include cybersecurity technical assistance for rural water systems serving fewer than 10,000 people. Under the program, USDA provides technical assistance to rural water systems that are experiencing day-to-day operational, financial, or managerial issues.</p><p>Specifically, the program's cybersecurity technical assistance must (1) assess system efficacy in protecting against cyber threats; and (2) implement cybersecurity plans, procedures, and technologies to protect against cyber threats.</p><p>The bill also reauthorizes the Circuit Rider Program through FY2030.</p>",
      "updateDate": "2025-06-09",
      "versionCode": "id119hr2109"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2109ih.xml"
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
      "title": "Cybersecurity for Rural Water Systems Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cybersecurity for Rural Water Systems Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To include cybersecurity technical assistance in the national rural water and wastewater circuit rider program of Department of Agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T04:18:28Z"
    }
  ]
}
```
