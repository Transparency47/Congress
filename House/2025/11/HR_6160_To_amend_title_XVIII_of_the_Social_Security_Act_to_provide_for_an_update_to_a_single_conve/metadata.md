# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6160?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6160
- Title: Strengthening Medicare for Patients and Providers Act
- Congress: 119
- Bill type: HR
- Bill number: 6160
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-05-01T08:08:29Z
- Update date including text: 2026-05-01T08:08:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-11-19 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6160",
    "number": "6160",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
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
    "title": "Strengthening Medicare for Patients and Providers Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:29Z",
    "updateDateIncludingText": "2026-05-01T08:08:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:01:50Z",
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
          "date": "2025-11-19T15:01:45Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "WA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "NJ"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "SC"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "FL"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6160ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6160\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Ruiz (for himself, Mr. Bilirakis , Mr. Panetta , Mr. Bera , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for an update to a single conversion factor under the Medicare physician fee schedule that is based on the Medicare economic index.\n#### 1. Short title\nThis Act may be cited as the Strengthening Medicare for Patients and Providers Act .\n#### 2. Transition to an update to a single conversion factor under the Medicare physician fee schedule based on the Medicare economic index\n##### (a) In general\nSection 1848(d)(2) of the Social Security Act ( 42 U.S.C. 1395w\u20134(d)(20) ) is amended to read as follows:\n(20) Update for 2026 and subsequent years The update to the single conversion factor established in paragraph (1)(C) for 2026 and each subsequent year shall be equal to the Secretary\u2019s estimate of the percentage increase in the MEI (as defined in section 1842(i)(3)) for the year. .\n##### (b) Conforming amendment To provide for a single conversion factor after 2025\nSection 1848(d)(1)(A) of the Social Security Act ( 42 U.S.C. 1395w\u20134(d)(1)(A) ) is amended\u2014\n**(1)**\nby striking and ending with 2025 ; and\n**(2)**\nby striking There shall be two separate conversion factors and all that follows through the end of the subparagraph.",
      "versionDate": "2025-11-19",
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
        "name": "Health",
        "updateDate": "2025-12-05T15:28:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-19",
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
          "measure-id": "id119hr6160",
          "measure-number": "6160",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-19",
          "originChamber": "HOUSE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6160v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-11-19",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Strengthening Medicare for Patients and Providers Act</strong></p><p>This bill modifies certain adjustments to payment amounts under the Medicare physician fee schedule.</p><p>Payment amounts under the Medicare physician fee schedule are based on a service's relative value, a conversion factor, and a geographic adjustment factor. Current law provides for separate conversion factors for physicians that are qualifying participants in advanced alternative payment models (also known as qualifying APM participants) and for other physicians beginning in 2026, with an annual update of 0.75% and 0.25%, respectively.</p><p>The bill replaces the separate conversion factors for qualifying APM participants and other physicians with a single conversion factor and provides for an update that is equal to the annual percentage increase in the Medicare Economic Index, beginning in 2026. (The Medicare Economic Index is a specialized index that is generally used to determine allowed charges for physician services based on annual price changes.)</p>"
        },
        "title": "Strengthening Medicare for Patients and Providers Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6160.xml",
    "summary": {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Medicare for Patients and Providers Act</strong></p><p>This bill modifies certain adjustments to payment amounts under the Medicare physician fee schedule.</p><p>Payment amounts under the Medicare physician fee schedule are based on a service's relative value, a conversion factor, and a geographic adjustment factor. Current law provides for separate conversion factors for physicians that are qualifying participants in advanced alternative payment models (also known as qualifying APM participants) and for other physicians beginning in 2026, with an annual update of 0.75% and 0.25%, respectively.</p><p>The bill replaces the separate conversion factors for qualifying APM participants and other physicians with a single conversion factor and provides for an update that is equal to the annual percentage increase in the Medicare Economic Index, beginning in 2026. (The Medicare Economic Index is a specialized index that is generally used to determine allowed charges for physician services based on annual price changes.)</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6160"
    },
    "title": "Strengthening Medicare for Patients and Providers Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-19",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Medicare for Patients and Providers Act</strong></p><p>This bill modifies certain adjustments to payment amounts under the Medicare physician fee schedule.</p><p>Payment amounts under the Medicare physician fee schedule are based on a service's relative value, a conversion factor, and a geographic adjustment factor. Current law provides for separate conversion factors for physicians that are qualifying participants in advanced alternative payment models (also known as qualifying APM participants) and for other physicians beginning in 2026, with an annual update of 0.75% and 0.25%, respectively.</p><p>The bill replaces the separate conversion factors for qualifying APM participants and other physicians with a single conversion factor and provides for an update that is equal to the annual percentage increase in the Medicare Economic Index, beginning in 2026. (The Medicare Economic Index is a specialized index that is generally used to determine allowed charges for physician services based on annual price changes.)</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119hr6160"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6160ih.xml"
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
      "title": "Strengthening Medicare for Patients and Providers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T13:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Medicare for Patients and Providers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T13:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for an update to a single conversion factor under the Medicare physician fee schedule that is based on the Medicare economic index.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T13:03:44Z"
    }
  ]
}
```
