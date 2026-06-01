# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5331?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5331
- Title: Auto Bailout Accident Victims Recovery Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5331
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-24T15:22:29Z
- Update date including text: 2025-09-24T15:22:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5331",
    "number": "5331",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Auto Bailout Accident Victims Recovery Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-24T15:22:29Z",
    "updateDateIncludingText": "2025-09-24T15:22:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5331ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5331\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Moore of Alabama (for himself and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo waive the statute of limitations for cases against the government related to the General Motors bailout that were filed on or before July 9, 2015, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Auto Bailout Accident Victims Recovery Act of 2025 .\n#### 2. Settlement of accident victim litigation related to the General Motors bailout; Waiver of statute of limitations\n##### (a)\nAny eligible civil action arising from the filing of an eligible complaint alleging a violation of the takings clause of amendment V to the United States Constitution is not subject to any statute of limitations.\n##### (b)\nThe United States shall pay just compensation to an eligible claimant, consistent with amendment V to the Constitution of the United States, to resolve an eligible claim. Just compensation payments to eligible claimants shall be made pursuant to section 1304 of title 31, United States Code.\n##### (c)\nIf a settlement agreement has not been submitted to the court presiding over an eligible complaint within 60 days after the date of enactment of this Act, the Attorney General shall submit a report to Congress describing the reasons why a settlement agreement was not reached with counsel of record to an eligible complaint.\n#### 3. Definitions\nFor purposes of this Act, the following definitions shall apply:\n**(1)**\nThe term eligible claim means a claim asserted in an eligible complaint on behalf of all eligible claimants.\n**(2)**\nThe term eligible claimant means a plaintiff, class member, or putative class member represented in an eligible complaint who holds an eligible claim and who filed a proof of claim in the bankruptcy case captioned In re Motors Liquidation Company, et al., No. 09\u201350026 (Bankr. S.D.N.Y), based on death or personal injuries that were caused by or attributable to alleged defects in motor vehicles designed for operation on public roadways, or by the component parts of such motor vehicles, and in each case, manufactured, sold, or delivered by General Motors Corporation or any of its subsidiaries on or before June 1, 2009.\n**(3)**\nThe term eligible complaint means the complaint filed with the United States Court of Federal Claims by or on behalf of eligible claimants on July 9, 2015, captioned Campbell, et al., v. United States, No. 15\u2013717, alleging violation by the United States of amendment V to the Constitution in connection with the acquisition on July 10, 2009, by NGMCO, Inc., a United States Treasury-sponsored entity, of substantially all the assets of General Motors Corporation.\n**(4)**\nThe term just compensation means payment of a lump-sum amount equal to the sum of\u2014\n**(A)**\n2.5 times the allowed amount listed on the final claims register filed on June 3, 2021, in the In re Motors Liquidation Company et al. bankruptcy case in respect of a proof of claim filed by or on behalf of an eligible claimant, plus\n**(B)**\ninterest thereon from July 10, 2009, to the effective date of settlement at a rate of three and one-half percent (3.5 percent) per annum, compounded quarterly, plus\n**(C)**\nreasonable court-approved fees and costs to counsel of record on the eligible complaint, all without offset of any kind.",
      "versionDate": "2025-09-11",
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
        "name": "Law",
        "updateDate": "2025-09-24T15:22:29Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5331ih.xml"
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
      "title": "Auto Bailout Accident Victims Recovery Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-23T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Auto Bailout Accident Victims Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-23T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To waive the statute of limitations for cases against the government related to the General Motors bailout that were filed on or before July 9, 2015, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:24Z"
    }
  ]
}
```
