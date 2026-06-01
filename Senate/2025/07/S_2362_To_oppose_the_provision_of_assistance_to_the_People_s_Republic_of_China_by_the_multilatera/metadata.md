# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2362?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2362
- Title: Ending Lending to China Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2362
- Origin chamber: Senate
- Introduced date: 2025-07-21
- Update date: 2025-10-01T11:03:12Z
- Update date including text: 2025-10-01T11:03:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in Senate
- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Foreign Relations. (text: CR S4506)
- Latest action: 2025-07-21: Introduced in Senate

## Actions

- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Foreign Relations. (text: CR S4506)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2362",
    "number": "2362",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Ending Lending to China Act of 2025",
    "type": "S",
    "updateDate": "2025-10-01T11:03:12Z",
    "updateDateIncludingText": "2025-10-01T11:03:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations. (text: CR S4506)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T21:14:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "IA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "IA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "FL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "WY"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "UT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NE"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MO"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "TX"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "KS"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NE"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "MO"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "WV"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2362is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2362\nIN THE SENATE OF THE UNITED STATES\nJuly 21, 2025 Mr. Barrasso (for himself, Mr. Grassley , Mrs. Blackburn , Mr. Budd , Ms. Ernst , Mr. Scott of Florida , Ms. Lummis , Mr. Lee , Mr. Ricketts , Mr. Hawley , Mr. Cruz , Mr. Tillis , Mr. Marshall , and Mrs. Fischer ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo oppose the provision of assistance to the People's Republic of China by the multilateral development banks.\n#### 1. Short title\nThis Act may be cited as the Ending Lending to China Act of 2025 .\n#### 2. Opposition to provision of assistance to People's Republic of China by multilateral development banks\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe People\u2019s Republic of China is the world\u2019s second largest economy and a major global lender.\n**(2)**\nIn April 2025, the foreign exchange reserves of the People\u2019s Republic of China totaled more than $3,281,000,000,000.\n**(3)**\nThe World Bank classifies the People\u2019s Republic of China as a country with an upper-middle-income economy.\n**(4)**\nOn February 25, 2021, President Xi Jinping announced complete victory over extreme poverty in the People\u2019s Republic of China.\n**(5)**\nThe Government of the People\u2019s Republic of China utilizes state resources to create and promote the Asian Infrastructure Investment Bank, the New Development Bank, and the Belt and Road Initiative.\n**(6)**\nThe People\u2019s Republic of China is the world\u2019s largest official creditor.\n**(7)**\nThrough a multilateral development bank, countries are eligible to borrow until they can manage long-term development and access to capital markets without financial resources from the bank.\n**(8)**\nThe World Bank reviews the graduation of a country from eligibility to borrow from the International Bank for Reconstruction and Development once the country reaches the graduation discussion income, which is equivalent to the gross national income. For fiscal year 2025, the graduation discussion income is a gross national income per capita exceeding $7,895.\n**(9)**\nMany of the other multilateral development banks, such as the Asian Development Bank, use the gross national income per capita benchmark used by the International Bank for Reconstruction and Development to trigger the graduation process.\n**(10)**\nThe People\u2019s Republic of China exceeded the graduation discussion income threshold in 2016.\n**(11)**\nSince fiscal year 2016, the International Bank for Reconstruction and Development has approved project loans totaling $12,938,000,000 to the People\u2019s Republic of China.\n**(12)**\nIn 2024, the Asian Development Bank approved loans and technical assistance to the People\u2019s Republic of China totaling more than $901,000,000. The Bank also approved non-sovereign commitments in the People\u2019s Republic of China totaling more than $483,000,000.\n**(13)**\nThe World Bank calculates the People\u2019s Republic of China\u2019s 2024 gross national income per capita as $13,660.\n##### (b) Statement of policy\nIt is the policy of the United States to oppose any additional lending from the multilateral development banks, including the International Bank for Reconstruction and Development and the Asian Development Bank, to the People\u2019s Republic of China as a result of the People\u2019s Republic of China\u2019s successful graduation from the eligibility requirements for assistance from those banks.\n##### (c) Opposition to lending to People's Republic of China\nThe Secretary of the Treasury shall instruct the United States Executive Director at each multilateral development bank to use the voice, vote, and influence of the United States\u2014\n**(1)**\nto oppose any loan or extension of financial or technical assistance by the bank to the People\u2019s Republic of China; and\n**(2)**\nto end lending and assistance to countries that exceed the graduation discussion income of the bank.\n##### (d) Report required\nNot later than one year after the date of the enactment of this Act, and annually thereafter, the Secretary of the Treasury shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\nan assessment of the status of borrowing by the People\u2019s Republic of China from each multilateral development bank;\n**(2)**\na description of voting power, shares, and representation by the People\u2019s Republic of China at each such bank;\n**(3)**\na list of countries that have exceeded the graduation discussion income at each such bank;\n**(4)**\na list of countries that have graduated from eligibility for assistance from each such bank; and\n**(5)**\na full description of the efforts taken by the United States to graduate countries from such eligibility once they exceed the graduation discussion income at each such bank.\n##### (e) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on Financial Services and the Committee on Foreign Affairs of the House of Representatives.\n**(2) Multilateral development banks**\nThe term multilateral development banks has the meaning given that term in section 1701(c) of the International Financial Institutions Act ( 22 U.S.C. 262r(c) ).",
      "versionDate": "2025-07-21",
      "versionType": "Introduced in Senate"
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
        "name": "International Affairs",
        "updateDate": "2025-09-18T18:21:03Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2362is.xml"
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
      "title": "Ending Lending to China Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T11:03:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ending Lending to China Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to oppose the provision of assistance to the People's Republic of China by the multilateral development banks.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:25Z"
    }
  ]
}
```
