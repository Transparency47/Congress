# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1846?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1846
- Title: Federal Reserve Board Abolition Act
- Congress: 119
- Bill type: HR
- Bill number: 1846
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-12-05T21:51:06Z
- Update date including text: 2025-12-05T21:51:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Financial Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1846",
    "number": "1846",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Federal Reserve Board Abolition Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:51:06Z",
    "updateDateIncludingText": "2025-12-05T21:51:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
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
          "date": "2025-03-05T15:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MO"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "WY"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1846ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1846\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Massie (for himself, Mr. Biggs of Arizona , Ms. Boebert , Mr. Burlison , Mrs. Cammack , Mr. Cloud , Mr. Crane , Ms. Greene of Georgia , Ms. Hageman , Mr. Perry , and Mr. Roy ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo abolish the Board of Governors of the Federal Reserve System and the Federal reserve banks, to repeal the Federal Reserve Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Reserve Board Abolition Act .\n#### 2. Federal Reserve Board abolished\n##### (a) In General\nEffective at the end of the 1-year period beginning on the date of the enactment of this Act, the Board of Governors of the Federal Reserve System and each Federal reserve bank are hereby abolished.\n##### (b) Repeal of Federal Reserve Act\nEffective at the end of the 1-year period beginning on the date of the enactment of this Act, the Federal Reserve Act is hereby repealed.\n##### (c) Disposition of Affairs\n**(1) Management during dissolution period**\nDuring the 1-year period referred to in subsection (a), the Chairman of the Board of Governors of the Federal Reserve System\u2014\n**(A)**\nshall, for the sole purpose of winding up the affairs of the Board of Governors of the Federal Reserve System and the Federal reserve banks\u2014\n**(i)**\nmanage the employees of the Board and each such bank and provide for the payment of compensation and benefits of any such employee which accrue before the position of such employee is abolished; and\n**(ii)**\nmanage the assets and liabilities of the Board and each such bank until such assets and liabilities are liquidated or assumed by the Secretary of the Treasury in accordance with this subsection; and\n**(B)**\nmay take such other action as may be necessary, subject to the approval of the Secretary of the Treasury, to wind up the affairs of the Board and the Federal reserve banks.\n**(2) Liquidation of assets**\n**(A) In general**\nThe Director of the Office of Management and Budget shall liquidate all assets of the Board and the Federal reserve banks in an orderly manner so as to achieve as expeditious a liquidation as may be practical while maximizing the return to the Treasury.\n**(B) Transfer to treasury**\nAfter satisfying all claims against the Board and any Federal reserve bank which are accepted by the Director of the Office of Management and Budget and redeeming the stock of such banks, the net proceeds of the liquidation under subparagraph (A) shall be transferred to the Secretary of the Treasury and deposited in the General Fund of the Treasury.\n**(3) Assumption of liabilities**\nAll outstanding liabilities of the Board of Governors of the Federal Reserve System and the Federal reserve banks at the time such entities are abolished, including any liability for retirement and other benefits for former officers and employees of the Board or any such bank in accordance with employee retirement and benefit programs of the Board and any such bank, shall become the liability of the Secretary of the Treasury and shall be paid from amounts deposited in the general fund pursuant to paragraph (2) which are hereby appropriated for such purpose until all such liabilities are satisfied.\n##### (d) Report\nAt the end of the 18-month period beginning on the date of the enactment of this Act, the Secretary of the Treasury and the Director of the Office of Management and Budget shall submit a joint report to the Congress containing a detailed description of the actions taken to implement this Act and any actions or issues relating to such implementation that remain uncompleted or unresolved as of the date of the report.",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "869",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Federal Reserve Board Abolition Act",
      "type": "S"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-21T18:42:46Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1846ih.xml"
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
      "title": "Federal Reserve Board Abolition Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Reserve Board Abolition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To abolish the Board of Governors of the Federal Reserve System and the Federal reserve banks, to repeal the Federal Reserve Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:07Z"
    }
  ]
}
```
