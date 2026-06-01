# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5756?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5756
- Title: HEATS Act
- Congress: 119
- Bill type: HR
- Bill number: 5756
- Origin chamber: House
- Introduced date: 2025-10-14
- Update date: 2025-11-18T09:05:42Z
- Update date including text: 2025-11-18T09:05:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-14: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-10-14: Introduced in House

## Actions

- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5756",
    "number": "5756",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "R000599",
        "district": "25",
        "firstName": "Raul",
        "fullName": "Rep. Ruiz, Raul [D-CA-25]",
        "lastName": "Ruiz",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "HEATS Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:42Z",
    "updateDateIncludingText": "2025-11-18T09:05:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-14",
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
          "date": "2025-10-14T18:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "VA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "PA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NC"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "AZ"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5756ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5756\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Mr. Ruiz introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo provide funding for LIHEAP during a Federal Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Home Energy Assistance in Times of Shutdown Act or the HEATS Act .\n#### 2. Funding for LIHEAP during a Federal Government shutdown\nOut of any money in the Treasury not otherwise appropriated, there is appropriated such sums as are necessary to pay, during any period of a lapse in discretionary appropriations during any fiscal year, for making payments under section 2602(b) of the Low-Income Home Energy Assistance Act of 1981 ( 42 U.S.C. 8621(b) ) during such lapse.",
      "versionDate": "2025-10-14",
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
        "updateDate": "2025-10-16T13:35:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-14",
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
          "measure-id": "id119hr5756",
          "measure-number": "5756",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-14",
          "originChamber": "HOUSE",
          "update-date": "2025-10-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5756v00",
            "update-date": "2025-10-16"
          },
          "action-date": "2025-10-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Home Energy Assistance in Times of Shutdown Act or the HEATS Act</strong></p><p>This bill provides appropriations for the Low Income Home Energy Assistance Program (LIHEAP) during any period in which there is a lapse in discretionary appropriations for any fiscal year (i.e., a government shutdown). Under\u00a0LIHEAP, the federal government makes annual grants to states, tribes, and territories to operate home energy assistance programs for low-income households. The bill provides appropriations for LIHEAP payments to continue during a government shutdown.\u00a0</p>"
        },
        "title": "HEATS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5756.xml",
    "summary": {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Home Energy Assistance in Times of Shutdown Act or the HEATS Act</strong></p><p>This bill provides appropriations for the Low Income Home Energy Assistance Program (LIHEAP) during any period in which there is a lapse in discretionary appropriations for any fiscal year (i.e., a government shutdown). Under\u00a0LIHEAP, the federal government makes annual grants to states, tribes, and territories to operate home energy assistance programs for low-income households. The bill provides appropriations for LIHEAP payments to continue during a government shutdown.\u00a0</p>",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5756"
    },
    "title": "HEATS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Home Energy Assistance in Times of Shutdown Act or the HEATS Act</strong></p><p>This bill provides appropriations for the Low Income Home Energy Assistance Program (LIHEAP) during any period in which there is a lapse in discretionary appropriations for any fiscal year (i.e., a government shutdown). Under\u00a0LIHEAP, the federal government makes annual grants to states, tribes, and territories to operate home energy assistance programs for low-income households. The bill provides appropriations for LIHEAP payments to continue during a government shutdown.\u00a0</p>",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5756"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5756ih.xml"
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
      "title": "HEATS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-15T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEATS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-15T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Home Energy Assistance in Times of Shutdown Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-15T08:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide funding for LIHEAP during a Federal Government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-15T08:18:15Z"
    }
  ]
}
```
