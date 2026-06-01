# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1622?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1622
- Title: Uranium for Energy Independence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1622
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-01-16T16:05:30Z
- Update date including text: 2026-01-16T16:05:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Natural Resources.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1622",
    "number": "1622",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Uranium for Energy Independence Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-16T16:05:30Z",
    "updateDateIncludingText": "2026-01-16T16:05:30Z"
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
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
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
          "date": "2025-02-26T15:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "UT"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "AZ"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "AZ"
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
      "sponsorshipDate": "2025-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1622ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1622\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. McGuire (for himself, Ms. Maloy , Mr. Buchanan , Mr. McCormick , Mr. Haridopolos , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide for the inclusion of uranium on the list of critical minerals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Uranium for Energy Independence Act of 2025 .\n#### 2. Uranium critical mineral status\nNotwithstanding the exclusion of fuel minerals from the definition of the term critical mineral under any Federal law, regulation, or Executive order, uranium\u2014\n**(1)**\nis deemed to be included on the 2022 final list of critical minerals in the notice entitled 2022 Final List of Critical Minerals published by the United States Geological Survey (87 Fed. Reg. 10381; February 24, 2022), and shall be treated as if included on that list at the time of publication; and\n**(2)**\nshall be included on each subsequent list of critical minerals published pursuant to section 7002 of the Energy Act of 2020 ( 30 U.S.C. 1606 ).",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-18T16:19:31Z"
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
          "measure-id": "id119hr1622",
          "measure-number": "1622",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2026-01-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1622v00",
            "update-date": "2026-01-16"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Uranium for Energy Independence Act of 2025</strong></p><p>This bill includes uranium on the critical minerals list. In 2018, the U.S. Geological Survey (USGS) published a list of critical minerals, including uranium, in response to an executive order that called for a federal strategy to ensure secure and reliable supplies of critical minerals. The USGS updates the list every three years and includes certain minerals that are essential to economic or national security and have a supply chain vulnerable to disruption. In 2022, USGS removed uranium from the list. The bill reinstates uranium as a critical mineral and requires uranium to be treated\u00a0as if it were included on that list at the time of publication.</p>"
        },
        "title": "Uranium for Energy Independence Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1622.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Uranium for Energy Independence Act of 2025</strong></p><p>This bill includes uranium on the critical minerals list. In 2018, the U.S. Geological Survey (USGS) published a list of critical minerals, including uranium, in response to an executive order that called for a federal strategy to ensure secure and reliable supplies of critical minerals. The USGS updates the list every three years and includes certain minerals that are essential to economic or national security and have a supply chain vulnerable to disruption. In 2022, USGS removed uranium from the list. The bill reinstates uranium as a critical mineral and requires uranium to be treated\u00a0as if it were included on that list at the time of publication.</p>",
      "updateDate": "2026-01-16",
      "versionCode": "id119hr1622"
    },
    "title": "Uranium for Energy Independence Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Uranium for Energy Independence Act of 2025</strong></p><p>This bill includes uranium on the critical minerals list. In 2018, the U.S. Geological Survey (USGS) published a list of critical minerals, including uranium, in response to an executive order that called for a federal strategy to ensure secure and reliable supplies of critical minerals. The USGS updates the list every three years and includes certain minerals that are essential to economic or national security and have a supply chain vulnerable to disruption. In 2022, USGS removed uranium from the list. The bill reinstates uranium as a critical mineral and requires uranium to be treated\u00a0as if it were included on that list at the time of publication.</p>",
      "updateDate": "2026-01-16",
      "versionCode": "id119hr1622"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1622ih.xml"
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
      "title": "Uranium for Energy Independence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T04:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Uranium for Energy Independence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the inclusion of uranium on the list of critical minerals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T04:33:28Z"
    }
  ]
}
```
