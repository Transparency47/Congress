# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/914?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/914
- Title: American CANS Act
- Congress: 119
- Bill type: HR
- Bill number: 914
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-07-11T08:06:06Z
- Update date including text: 2025-07-11T08:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/914",
    "number": "914",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "American CANS Act",
    "type": "HR",
    "updateDate": "2025-07-11T08:06:06Z",
    "updateDateIncludingText": "2025-07-11T08:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "WI"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WI"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "OR"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "ME"
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
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "WI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MI"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr914ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 914\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Harder of California (for himself and Mr. Van Orden ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Tariff Act of 1930 to provide that required country-of-origin labeling for any agricultural product packaged in a can shall be on the front label or top of such can, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Consumer Awareness of National Source Act or the American CANS Act .\n#### 2. Method of notification of country of origin of an agricultural product packaged in a can\n##### (a) In general\nSection 304(b) of the Tariff Act of 1930 ( 19 U.S.C. 1304(b) ) is amended by inserting after the first sentence the following: In the case of such an article that is an agricultural product (as defined in section 207 of the Agricultural Marketing Act of 1946) packaged in a can, the marking required under this subsection shall appear on the front label of the can or be stamped, embossed, or printed on the top of the can. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall only apply to agricultural products imported on or after the date that is 18 months after the date of enactment of this Act.",
      "versionDate": "2025-02-04",
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
            "name": "Agricultural marketing and promotion",
            "updateDate": "2025-06-09T16:50:59Z"
          },
          {
            "name": "Agricultural trade",
            "updateDate": "2025-06-09T16:51:08Z"
          },
          {
            "name": "Food supply, safety, and labeling",
            "updateDate": "2025-06-09T16:50:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-01T19:53:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr914",
          "measure-number": "914",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-06-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr914v00",
            "update-date": "2025-06-26"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>American Consumer Awareness of National Source Act or the American CANS Act</strong></p><p>This bill revises country-of-origin labeling requirements for canned goods.</p><p>Under current country-of-origin labeling requirements, every article of foreign origin entering the United States must be legibly marked with the English name of the country of origin of the article (with certain exemptions). This bill requires country-of-origin labeling for any agricultural product packaged in a can to (1) appear on the front label of the can; or (2) be stamped, embossed, or printed on the top of the can.</p>"
        },
        "title": "American CANS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr914.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Consumer Awareness of National Source Act or the American CANS Act</strong></p><p>This bill revises country-of-origin labeling requirements for canned goods.</p><p>Under current country-of-origin labeling requirements, every article of foreign origin entering the United States must be legibly marked with the English name of the country of origin of the article (with certain exemptions). This bill requires country-of-origin labeling for any agricultural product packaged in a can to (1) appear on the front label of the can; or (2) be stamped, embossed, or printed on the top of the can.</p>",
      "updateDate": "2025-06-26",
      "versionCode": "id119hr914"
    },
    "title": "American CANS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>American Consumer Awareness of National Source Act or the American CANS Act</strong></p><p>This bill revises country-of-origin labeling requirements for canned goods.</p><p>Under current country-of-origin labeling requirements, every article of foreign origin entering the United States must be legibly marked with the English name of the country of origin of the article (with certain exemptions). This bill requires country-of-origin labeling for any agricultural product packaged in a can to (1) appear on the front label of the can; or (2) be stamped, embossed, or printed on the top of the can.</p>",
      "updateDate": "2025-06-26",
      "versionCode": "id119hr914"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr914ih.xml"
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
      "title": "American CANS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American CANS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Consumer Awareness of National Source Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Tariff Act of 1930 to provide that required country-of-origin labeling for any agricultural product packaged in a can shall be on the front label or top of such can, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:51Z"
    }
  ]
}
```
