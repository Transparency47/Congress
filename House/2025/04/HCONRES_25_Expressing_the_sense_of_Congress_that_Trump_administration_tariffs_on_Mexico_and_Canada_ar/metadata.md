# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/25?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/25
- Title: Expressing the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement.
- Congress: 119
- Bill type: HCONRES
- Bill number: 25
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2025-12-10T09:05:41Z
- Update date including text: 2025-12-10T09:05:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-04-01 - IntroReferral: Submitted in House
- 2025-04-01 - IntroReferral: Submitted in House
- Latest action: 2025-04-01: Submitted in House

## Actions

- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-04-01 - IntroReferral: Submitted in House
- 2025-04-01 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/25",
    "number": "25",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement.",
    "type": "HCONRES",
    "updateDate": "2025-12-10T09:05:41Z",
    "updateDateIncludingText": "2025-12-10T09:05:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-04-01T14:09:10Z",
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
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NY"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "IL"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NV"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MD"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "IL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "TX"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "VA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NJ"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "KS"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres25ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 25\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Costa (for himself, Mr. Stanton , Mr. Kennedy of New York , Mr. Quigley , Mr. Liccardo , Mr. Carbajal , Mr. Vicente Gonzalez of Texas , Mr. Gray , Ms. Lofgren , Mr. McGovern , and Ms. McCollum ) submitted the following concurrent resolution; which was referred to the Committee on Ways and Means\nCONCURRENT RESOLUTION\nExpressing the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement.\nThat\u2014\n**(1)**\nit is the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement (USMCA); and\n**(2)**\nCongress recognizes strong support\u2014\n**(A)**\namongst the various sectors who recognize the vital importance of the USMCA;\n**(B)**\nfor the elimination of longstanding unwarranted nontariff trade barriers through an effective and efficient dispute settlement process; and\n**(C)**\nfor the 2026 review process to move forward.",
      "versionDate": "2025-04-01",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-13T19:51:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119hconres25",
          "measure-number": "25",
          "measure-type": "hconres",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2025-07-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hconres25v00",
            "update-date": "2025-07-11"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This concurrent resolution expresses the sense of Congress that 25% tariffs on imports from Canada and Mexico are in violation of the U.S.-Mexico-Canada Agreement\u00a0(USMCA). (President Donald J. Trump issued executive orders on February 1, 2025, to\u00a0impose an additional 25% tariff on most imports from Canada and Mexico.)</p>"
        },
        "title": "Expressing the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hconres/BILLSUM-119hconres25.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution expresses the sense of Congress that 25% tariffs on imports from Canada and Mexico are in violation of the U.S.-Mexico-Canada Agreement\u00a0(USMCA). (President Donald J. Trump issued executive orders on February 1, 2025, to\u00a0impose an additional 25% tariff on most imports from Canada and Mexico.)</p>",
      "updateDate": "2025-07-11",
      "versionCode": "id119hconres25"
    },
    "title": "Expressing the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement."
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This concurrent resolution expresses the sense of Congress that 25% tariffs on imports from Canada and Mexico are in violation of the U.S.-Mexico-Canada Agreement\u00a0(USMCA). (President Donald J. Trump issued executive orders on February 1, 2025, to\u00a0impose an additional 25% tariff on most imports from Canada and Mexico.)</p>",
      "updateDate": "2025-07-11",
      "versionCode": "id119hconres25"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres25ih.xml"
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
      "title": "Expressing the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing the sense of Congress that Trump administration tariffs on Mexico and Canada are in violation of the United States of America-Mexico-Canada Agreement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:58:25Z"
    }
  ]
}
```
