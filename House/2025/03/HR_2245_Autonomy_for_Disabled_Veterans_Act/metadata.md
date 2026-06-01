# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2245?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2245
- Title: Autonomy for Disabled Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 2245
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-12-19T09:07:40Z
- Update date including text: 2025-12-19T09:07:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-04-04 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2245",
    "number": "2245",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Autonomy for Disabled Veterans Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:40Z",
    "updateDateIncludingText": "2025-12-19T09:07:40Z"
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
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T18:10:02Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-05-09",
      "state": "NM"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NJ"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "NJ"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "FL"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "IL"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CO"
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
      "sponsorshipDate": "2025-06-20",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NV"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "FL"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2245ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2245\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Bacon introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to increase the amount paid by the Secretary of Veterans Affairs to veterans for improvements and structural alterations furnished as part of home health services.\n#### 1. Short title\nThis Act may be cited as the Autonomy for Disabled Veterans Act .\n#### 2. Increase in amount available to disabled veterans for improvements and structural alterations furnished as part of home health services\n##### (a) Increase\nSection 1717 of title 38, United States Code, is amended, in paragraph (2) of subsection (a)\u2014\n**(1)**\nin subparagraph (A)(ii), by striking $6,800 and inserting $10,000 ; and\n**(2)**\nin subparagraph (B)(ii), by striking $2,000 and inserting $5,000 .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply to a veteran who first applies for benefits under such paragraph on or after the date of the enactment of this Act.\n##### (c) Clarification\nA veteran who exhausted the eligibility of such veteran for benefits under such paragraph before the date of the enactment of this Act is not entitled to additional benefits under such section by reason of the amendments made by subsection (a).\n#### 3. Adjustment for inflation\nSuch subsection is further amended by adding at the end the following new paragraph:\n(4) On an annual basis, the Secretary shall increase the dollar amount in effect under subsection (a)(2) by a percentage equal to the percentage by which the Consumer Price Index for all urban consumers (United States city average) increased during the 12-month period ending with the last month for which Consumer Price Index data is available. In the event that such Consumer Price Index does not increase during such period, the Secretary shall maintain the dollar amount in effect under subsection (a)(2) during the previous fiscal year. .",
      "versionDate": "2025-03-21",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T17:25:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hr2245",
          "measure-number": "2245",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2245v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Autonomy for Disabled Veterans Act</strong></p><p>This bill increases the maximum amount authorized under the Home Improvements and Structural Alterations (HISA) grant program to $10,000 for veterans with a service-connected disability and $5,000 for those with disabilities that are not service-connected. The HISA grant program provides medically necessary improvements and structural alterations to a veteran's (or service member's) primary residence for specified purposes (e.g., allowing for entrance to their home).</p><p>The bill requires the Department of Veterans Affairs to increase the maximum dollar amount of the grant in accordance with inflation as determined by the Consumer Price Index.</p>"
        },
        "title": "Autonomy for Disabled Veterans Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2245.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Autonomy for Disabled Veterans Act</strong></p><p>This bill increases the maximum amount authorized under the Home Improvements and Structural Alterations (HISA) grant program to $10,000 for veterans with a service-connected disability and $5,000 for those with disabilities that are not service-connected. The HISA grant program provides medically necessary improvements and structural alterations to a veteran's (or service member's) primary residence for specified purposes (e.g., allowing for entrance to their home).</p><p>The bill requires the Department of Veterans Affairs to increase the maximum dollar amount of the grant in accordance with inflation as determined by the Consumer Price Index.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2245"
    },
    "title": "Autonomy for Disabled Veterans Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Autonomy for Disabled Veterans Act</strong></p><p>This bill increases the maximum amount authorized under the Home Improvements and Structural Alterations (HISA) grant program to $10,000 for veterans with a service-connected disability and $5,000 for those with disabilities that are not service-connected. The HISA grant program provides medically necessary improvements and structural alterations to a veteran's (or service member's) primary residence for specified purposes (e.g., allowing for entrance to their home).</p><p>The bill requires the Department of Veterans Affairs to increase the maximum dollar amount of the grant in accordance with inflation as determined by the Consumer Price Index.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2245"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2245ih.xml"
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
      "title": "Autonomy for Disabled Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Autonomy for Disabled Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to increase the amount paid by the Secretary of Veterans Affairs to veterans for improvements and structural alterations furnished as part of home health services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:03:32Z"
    }
  ]
}
```
