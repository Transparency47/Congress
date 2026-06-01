# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2441
- Title: Build Now Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2441
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-01-10T07:23:01Z
- Update date including text: 2026-01-10T07:23:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2441",
    "number": "2441",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Build Now Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T07:23:01Z",
    "updateDateIncludingText": "2026-01-10T07:23:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-07-24T17:17:04Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2441is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2441\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Kennedy (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo provide for adjustments to community development block grant allocations based on improvements in housing growth rates.\n#### 1. Short title\nThis Act may be cited as the Build Now Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Covered recipient**\nThe term covered recipient means a metropolitan city or urban county, as those terms are defined in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ), that receives funds under section 106.\n**(2) Current annual growth rate**\nThe term current annual growth rate , with respect to an eligible recipient and a fiscal year, means the average annual percentage increase in the number of housing units in the jurisdiction of the eligible recipient, as calculated by the Secretary, during the period\u2014\n**(A)**\nbeginning with the third quarter of the sixth preceding fiscal year; and\n**(B)**\nending with the third quarter of the preceding fiscal year.\n**(3) Eligible recipient**\nThe term eligible recipient means any covered recipient unless\u2014\n**(A)**\n**(i)**\nthe median Small Area Fair Market Rent in the jurisdiction of the covered recipient is at or below the 60th percentile of median Small Area Fair Market Rents in the jurisdictions of all covered recipients; and\n**(ii)**\nthe median home value in the jurisdiction of the covered recipient is below the median home value for the United States;\n**(B)**\nthe annual natural rental vacancy rate in the jurisdiction of the covered recipient is greater than the national annual natural rental vacancy rate for the most recent year available, as published by the Bureau of the Census;\n**(C)**\nduring the 1-year period preceding the date on which the Secretary allocates funds under section 106, the jurisdiction of the covered recipient has been the subject of a major disaster or emergency declaration under section 401 or 501, respectively, of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 , 5191); or\n**(D)**\nthe covered recipient lacks the legal authority to enact or update zoning and permitting ordinances.\n**(4) Extremely high-growth recipient**\nThe term extremely high-growth recipient means an eligible recipient for which the current annual growth rate is at or above 4 percent.\n**(5) Housing growth improvement rate**\nThe term housing growth improvement rate , with respect to an eligible recipient and a fiscal year, means the quotient of\u2014\n**(A)**\nthe current annual growth rate of the eligible recipient; and\n**(B)**\nthe prior annual growth rate of the eligible recipient.\n**(6) Prior annual growth rate**\nThe term prior annual growth rate , with respect to an eligible recipient and a fiscal year, means the average annual percentage increase in the number of housing units in the jurisdiction of the eligible recipient, as calculated by the Secretary, during the period\u2014\n**(A)**\nbeginning with the third quarter of the 11th preceding fiscal year; and\n**(B)**\nending with the third quarter of the sixth preceding fiscal year.\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(8) Section 106**\nThe term section 106 means section 106 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5306 ).\n#### 3. Adjustments to community development block grant allocations\n##### (a) In general\nIn allocating amounts to an eligible recipient under section 106 for a fiscal year, the Secretary shall adjust the allocation based on the housing growth improvement rate of the eligible recipient, in accordance with subsection (b) of this section.\n##### (b) Adjustments\n**(1) Housing growth improvement rate at or above median; extremely high-growth recipients**\n**(A) In general**\nIf, with respect to a fiscal year for which the allocation under section 106 is being determined, the housing growth improvement rate for an eligible recipient is at or above the median housing growth improvement rate for all eligible recipients other than extremely high-growth recipients, or if an eligible recipient is an extremely high-growth recipient, the Secretary shall allocate to the eligible recipient for that fiscal year, in addition to the amount that would otherwise be allocated to the eligible recipient under section 106, a bonus amount, as determined under subparagraph (B) of this paragraph.\n**(B) Bonus amount**\nFor purposes of subparagraph (A), the bonus amount for an eligible recipient for a fiscal year shall be equal to the product of\u2014\n**(i)**\nthe aggregate amount by which allocations to eligible recipients are decreased under paragraph (2) for that fiscal year; and\n**(ii)**\nthe quotient of\u2014\n**(I)**\nthe number of housing units, as of the third quarter of the preceding fiscal year, in the jurisdiction of the eligible recipient, as calculated by the Secretary; and\n**(II)**\nthe number of housing units, as of the third quarter of the preceding fiscal year, in the jurisdictions of all eligible recipients that receive a bonus amount under this paragraph, as calculated by the Secretary.\n**(2) Housing growth improvement rate below median**\nIf, with respect to a fiscal year for which the allocation under section 106 is being determined, the housing growth improvement rate for an eligible recipient is below the median housing growth improvement rate for all eligible recipients other than high-growth outliers, the Secretary shall decrease the amount that would otherwise be allocated to the eligible recipient under section 106 for that fiscal year by 10 percent.\n#### 4. Calculation of housing units\n##### (a) H UD requirements\nIn calculating the number of housing units in the jurisdiction of an eligible recipient under any provision of this Act, the Secretary shall\u2014\n**(1)**\nuse the Current Address Count Listing Files and other data products, as needed, of the Bureau of the Census tabulated from the Master Address File; and\n**(2)**\nmake calculations at the block level, using boundaries that reflect the most current boundaries.\n##### (b) Census Bureau and Postal Service Requirements\nThe Bureau of the Census and the United States Postal Service shall provide any relevant data to the Secretary upon request to assist the Secretary in making a calculation described in subsection (a).\n##### (c) Adjustment of calculation periods\nThe Secretary may adjust the calculation periods under subparagraphs (A) and (B) of section 2(2), subparagraphs (A) and (B) of section 2(6), and subclauses (I) and (II) of section 3(b)(1)(B)(ii) by not more than 2 months to achieve alignment with the data provided by the Bureau of the Census.\n#### 5. Annual report on housing growth improvement rate\nBefore allocating funds under section 106 for a fiscal year, the Secretary shall publish a report that\u2014\n**(1)**\nincludes the housing growth improvement rate for each eligible recipient; and\n**(2)**\nlists, for the most recent fiscal year for which allocations were made under section 106\u2014\n**(A)**\nthe eligible recipients that received a bonus amount under section 3(b)(1); and\n**(B)**\nthe eligible recipients for which the allocation under section 106 was decreased under section 3(b)(2) of this Act.\n#### 6. Notification; implementation dates\n##### (a) Notification\n**(1) In general**\nNot later than 60 days after the date of enactment of this Act, the Secretary shall notify each eligible recipient of the recipient's housing growth improvement rate and whether that housing growth improvement rate is above, at, or below the median housing growth improvement rate for all eligible recipients other than extremely high-growth recipients.\n**(2) Guidance**\nAs part of the notification under paragraph (1), the Secretary shall share guidance, including resources developed by the Department of Housing and Urban Development, on best practices and recommendations on policies to reduce regulatory barriers to housing and increase housing supply.\n##### (b) Implementation dates\nSection 3 shall take effect beginning with the second full fiscal year after the date of enactment of this Act and remain in effect through fiscal year 2042.",
      "versionDate": "2025-07-24",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-02",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6363",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Build Now Act of 2025",
      "type": "HR"
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-17T16:39:27Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2441is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Build Now Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-07T05:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Build Now Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-07T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for adjustments to community development block grant allocations based on improvements in housing growth rates.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-07T05:18:30Z"
    }
  ]
}
```
