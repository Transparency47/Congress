# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4226
- Title: STOP Corrupt Bets Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4226
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-13T18:39:22Z
- Update date including text: 2026-04-23T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4226",
    "number": "4226",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "STOP Corrupt Bets Act of 2026",
    "type": "S",
    "updateDate": "2026-04-13T18:39:22Z",
    "updateDateIncludingText": "2026-04-23T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T17:42:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "sponsorshipDate": "2026-03-26",
      "state": "MA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4226is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4226\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Merkley (for himself, Ms. Warren , Mr. Blumenthal , Mr. Van Hollen , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Commodity Exchange Act to prohibit certain event contracts on prediction markets, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Trading On Predictions and Corrupt Bets Act of 2026 or the STOP Corrupt Bets Act of 2026 .\n#### 2. Prohibition on certain event contracts\nSection 5c(c)(5) of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132(c)(5) ) is amended by adding at the end the following:\n(D) Prohibition on certain event contracts (i) In general Notwithstanding any other provision of this section, no agreement, contract, transaction, or swap involving any matter described in clause (ii) (or any index, measure, value, or data related thereto, or occurrence, extent of an occurrence, or contingency based thereon) may be listed or made available for clearing or trading on or through a registered entity. (ii) Matters described The matters referred to in clause (i) are\u2014 (I) any political election or contest; (II) subject to clause (iii), any action taken by the executive, legislative, or judicial branch of the United States; (III) any sporting event or contest; and (IV) any military action taken by the United States or any foreign country. (iii) Hedging The prohibition under clause (i) with respect to any matter described in clause (ii)(II) shall not apply to an agreement, contract, transaction, or swap that is used for hedging or mitigating commercial risk, as the Commission may determine by rule or regulation. .\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nnotwithstanding the amendment made by section 2, the intent of Congress in the Commodity Exchange Act ( 7 U.S.C. 1 et seq. ) is the prohibition of the conduct prohibited by that amendment;\n**(2)**\nfor the purpose of preventing a Federal regulatory structure that permits gambling, the Commodity Futures Trading Commission should prohibit the availability for clearing or trading on or through any registered entity (as defined in section 1a of that Act ( 7 U.S.C. 1a )) any agreement, contract, transaction, or swap (as defined in that section) that is not used for hedging or mitigating commercial risk; and\n**(3)**\nnothing in this Act or any amendment made by this Act preempts any State law that regulates or prohibits gambling or gaming.\n#### 4. GAO study\nNot later than 60 days after the date of enactment of this Act, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct a study on\u2014\n**(A)**\nprediction markets, including\u2014\n**(i)**\ninsider trading in prediction markets; and\n**(ii)**\nthe impacts on individuals aged 18 to 20 years old of trading in prediction markets;\n**(B)**\nadditional types of prediction markets that are not prohibited by the Commodity Exchange Act ( 7 U.S.C. 1 et seq. ) (as amended by section 2) for the purpose of preventing a Federal regulatory structure that permits gambling, including by examining any agreement, contract, transaction, or swap (as defined in section 1a of that Act ( 7 U.S.C. 1a )) that is not used for hedging or mitigating commercial risk; and\n**(C)**\nmeans Congress can use to address illegal acts occurring in foreign prediction markets and in domestic prediction markets committed by companies with a presence in a foreign country and in the United States to preserve the integrity of prediction markets; and\n**(2)**\nmake publicly available and submit to Congress a report describing the results of the study conducted under paragraph (1), including recommendations to Congress to preserve the integrity of prediction markets.",
      "versionDate": "2026-03-26",
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
        "actionDate": "2026-03-26",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "8123",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STOP Corrupt Bets Act of 2026",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-13T18:30:11Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4226is.xml"
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
      "title": "STOP Corrupt Bets Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP Corrupt Bets Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Trading On Predictions and Corrupt Bets Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Commodity Exchange Act to prohibit certain event contracts on prediction markets, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:35Z"
    }
  ]
}
```
