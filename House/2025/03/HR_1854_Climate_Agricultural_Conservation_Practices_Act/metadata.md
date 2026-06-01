# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1854?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1854
- Title: Climate Agricultural Conservation Practices Act
- Congress: 119
- Bill type: HR
- Bill number: 1854
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-04-23T08:07:05Z
- Update date including text: 2026-04-23T08:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1854",
    "number": "1854",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Climate Agricultural Conservation Practices Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:05Z",
    "updateDateIncludingText": "2026-04-23T08:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:49:45Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
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
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NM"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "HI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "IN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "DC"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1854ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1854\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Ms. Brownley (for herself, Ms. Castor of Florida , Ms. Salinas , and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Natural Resources Conservation Service to review the national conservation practice standards, taking into consideration climate benefits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Climate Agricultural Conservation Practices Act .\n#### 2. Consideration of climate benefits in conservation practice standards\nSection 1242(h) of the Food Security Act of 1985 ( 16 U.S.C. 3842(h) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), by striking 1 year after the date of enactment of the Agriculture Improvement Act of 2018 and inserting 5 years after the date of enactment of the Climate Agricultural Conservation Practices Act ;\n**(B)**\nin subparagraph (C), by striking ; and and inserting a semicolon;\n**(C)**\nin subparagraph (D), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following:\n(E) evaluate the climate benefits of the standards. ;\n**(2)**\nin paragraph (3)(B), by striking conservation innovations and and inserting climate benefits, conservation innovations, and ; and\n**(3)**\nby adding at the end the following:\n(5) Climate benefit defined In this subsection, the term climate benefit means\u2014 (A) a reduction in agricultural greenhouse gas emissions; (B) an increase in carbon sequestration; or (C) mitigation against, or adaptation to, increased weather volatility. .",
      "versionDate": "2025-03-05",
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
        "updateDate": "2025-05-13T18:49:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1854",
          "measure-number": "1854",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-06-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1854v00",
            "update-date": "2025-06-16"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Climate Agricultural Conservation Practices Act</strong></p><p>This bill requires the Natural Resources Conservation Service (NRCS) to consider climate benefits in reviews or revisions of its conservation practice standards. Climate benefits include\u00a0a reduction in agricultural greenhouse gas emissions, an increase in carbon sequestration, or\u00a0mitigation against (or adaptation to) increased weather volatility.</p><p>As background, NRCS\u00a0administers most of the Department of Agriculture conservation programs, which assist producers and landowners who wish to practice conservation on agricultural lands. The NRCS conservation practice standards\u00a0provide guidance and set out minimum quality criteria for implementing federally funded conservation practices.</p>"
        },
        "title": "Climate Agricultural Conservation Practices Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1854.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Climate Agricultural Conservation Practices Act</strong></p><p>This bill requires the Natural Resources Conservation Service (NRCS) to consider climate benefits in reviews or revisions of its conservation practice standards. Climate benefits include\u00a0a reduction in agricultural greenhouse gas emissions, an increase in carbon sequestration, or\u00a0mitigation against (or adaptation to) increased weather volatility.</p><p>As background, NRCS\u00a0administers most of the Department of Agriculture conservation programs, which assist producers and landowners who wish to practice conservation on agricultural lands. The NRCS conservation practice standards\u00a0provide guidance and set out minimum quality criteria for implementing federally funded conservation practices.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1854"
    },
    "title": "Climate Agricultural Conservation Practices Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Climate Agricultural Conservation Practices Act</strong></p><p>This bill requires the Natural Resources Conservation Service (NRCS) to consider climate benefits in reviews or revisions of its conservation practice standards. Climate benefits include\u00a0a reduction in agricultural greenhouse gas emissions, an increase in carbon sequestration, or\u00a0mitigation against (or adaptation to) increased weather volatility.</p><p>As background, NRCS\u00a0administers most of the Department of Agriculture conservation programs, which assist producers and landowners who wish to practice conservation on agricultural lands. The NRCS conservation practice standards\u00a0provide guidance and set out minimum quality criteria for implementing federally funded conservation practices.</p>",
      "updateDate": "2025-06-16",
      "versionCode": "id119hr1854"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1854ih.xml"
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
      "title": "Climate Agricultural Conservation Practices Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:57:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Climate Agricultural Conservation Practices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Natural Resources Conservation Service to review the national conservation practice standards, taking into consideration climate benefits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:25Z"
    }
  ]
}
```
