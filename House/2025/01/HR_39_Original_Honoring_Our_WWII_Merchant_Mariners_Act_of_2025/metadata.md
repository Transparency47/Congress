# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/39?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/39
- Title: Original Honoring Our WWII Merchant Mariners Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 39
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-20T09:06:43Z
- Update date including text: 2025-12-20T09:06:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/39",
    "number": "39",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Original Honoring Our WWII Merchant Mariners Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-20T09:06:43Z",
    "updateDateIncludingText": "2025-12-20T09:06:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:18:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T18:58:34Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr39ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 39\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Green of Texas introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish the Merchant Mariner Equity Compensation Fund to provide benefits to certain individuals who served in the United States merchant marine (including the Army Transport Service and the Naval Transport Service) during World War II.\n#### 1. Short Title\nThis Act may be cited as the Original Honoring Our WWII Merchant Mariners Act of 2025 .\n#### 2. Payments to individuals who served during World War II in the United States Merchant Marine\n##### (a) Establishment of Compensation Fund\nSubchapter II of chapter 5 of title 38, United States Code, is amended by adding at the end the following new section:\n533. Merchant Mariner Equity Compensation Fund (a) Compensation Fund (1) There is in the general fund of the Treasury a fund to be known as the Merchant Mariner Equity Compensation Fund (in this section referred to as the compensation fund ). (2) Subject to the availability of appropriations for such purpose, amounts in the compensation fund shall be available to the Secretary without fiscal year limitation to make payments to eligible individuals in accordance with this section. (b) Eligible Individuals (1) An eligible individual is an individual who\u2014 (A) during the one-year period beginning on the date of the enactment of this section, submits to the Secretary an application containing such information and assurances as the Secretary may require; (B) has not received benefits under the Servicemen's Readjustment Act of 1944 ( Public Law 78\u2013346 ); and (C) has engaged in qualified service. (2) For purposes of paragraph (1), a person has engaged in qualified service if, between December 7, 1941, and December 31, 1946, the person\u2014 (A) was a member of the United States merchant marine (including the Army Transport Service and the Naval Transport Service) serving as a crewmember of a vessel that was\u2014 (i) operated by the War Shipping Administration or the Office of Defense Transportation (or an agent of the Administration or Office); (ii) operated in waters other than inland waters, the Great Lakes, and other lakes, bays, and harbors of the United States; (iii) under contract or charter to, or property of, the Government of the United States; and (iv) serving the Armed Forces; and (B) while so serving, was licensed or otherwise documented for service as a crewmember of such a vessel by an officer or employee of the United States authorized to license or document the person for such service. (3) In determining the information and assurances required in the application pursuant to paragraph (1)(A), the Secretary shall accept a DD\u2013214 form as proof of qualified service. (c) Amount of Payment The Secretary shall make one payment out of the compensation fund in the amount of $25,000 to an eligible individual. The Secretary shall make such a payment to eligible individuals in the order in which the Secretary receives the applications of the eligible individuals. (d) Authorization of Appropriations There is authorized to be appropriated for fiscal year 2026 $125,000,000 for the compensation fund. Such amount shall remain available until expended. (e) Reports The Secretary shall include, in documents submitted to Congress by the Secretary in support of the President's budget for each fiscal year, detailed information on the operation of the compensation fund, including the number of applicants, the number of eligible individuals receiving benefits, the amounts paid out of the compensation fund, the administration of the compensation fund, and an estimate of the amounts necessary to fully fund the compensation fund for that fiscal year and each of the three subsequent fiscal years. (f) Regulations The Secretary shall prescribe regulations to carry out this section. .\n##### (b) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Secretary shall prescribe the regulations required under section 532(f) of title 38, United States Code, as added by subsection (a).\n##### (c) Clerical Amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item related to section 532 the following new item:\n533. Merchant Mariner Equity Compensation Fund. .",
      "versionDate": "2025-01-03",
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
            "name": "Conflicts and wars",
            "updateDate": "2025-03-05T15:24:31Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-03-05T15:24:31Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2025-03-05T15:24:31Z"
          },
          {
            "name": "Transportation employees",
            "updateDate": "2025-03-05T15:24:31Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-03-05T15:24:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T15:34:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr39",
          "measure-number": "39",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr39v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Original Honoring Our WWII Merchant Mariners Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs to distribute a payment of $25,000 to U.S. merchant marines who engaged in qualified service during World War II. To be eligible, an individual must apply for the benefit and must not have received benefits under the Servicemen's Readjustment Act of 1944. The bill sets forth what constitutes qualified service, including time frame of service and licensing requirements.</p>"
        },
        "title": "Original Honoring Our WWII Merchant Mariners Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr39.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Original Honoring Our WWII Merchant Mariners Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs to distribute a payment of $25,000 to U.S. merchant marines who engaged in qualified service during World War II. To be eligible, an individual must apply for the benefit and must not have received benefits under the Servicemen's Readjustment Act of 1944. The bill sets forth what constitutes qualified service, including time frame of service and licensing requirements.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr39"
    },
    "title": "Original Honoring Our WWII Merchant Mariners Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Original Honoring Our WWII Merchant Mariners Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs to distribute a payment of $25,000 to U.S. merchant marines who engaged in qualified service during World War II. To be eligible, an individual must apply for the benefit and must not have received benefits under the Servicemen's Readjustment Act of 1944. The bill sets forth what constitutes qualified service, including time frame of service and licensing requirements.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr39"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr39ih.xml"
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
      "title": "Original Honoring Our WWII Merchant Mariners Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Original Honoring Our WWII Merchant Mariners Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to establish the Merchant Mariner Equity Compensation Fund to provide benefits to certain individuals who served in the United States merchant marine (including the Army Transport Service and the Naval Transport Service) during World War II.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T04:18:19Z"
    }
  ]
}
```
