# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/680?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/680
- Title: Ending China's Unfair Advantage Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 680
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-05-19T11:03:44Z
- Update date including text: 2026-05-19T11:03:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations. (text: CR S1130-1131)
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Foreign Relations. (text: CR S1130-1131)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/680",
    "number": "680",
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
    "title": "Ending China's Unfair Advantage Act of 2025",
    "type": "S",
    "updateDate": "2026-05-19T11:03:44Z",
    "updateDateIncludingText": "2026-05-19T11:03:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations. (text: CR S1130-1131)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-20",
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
        "item": [
          {
            "date": "2025-02-20T23:38:33Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-20T23:38:33Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "WV"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "ND"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "WV"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "UT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "MS"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "TN"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s680is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 680\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Barrasso (for himself, Mrs. Capito , Mr. Hoeven , Mr. Justice , Mr. Lee , Ms. Lummis , Mr. Wicker , and Mr. Hagerty ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit funding for the Montreal Protocol on Substances that Deplete the Ozone Layer and the United Nations Framework Convention on Climate Change until China is no longer defined a developing country.\n#### 1. Short title\nThis Act may be cited as the Ending China's Unfair Advantage Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Appropriations of the Senate ;\n**(C)**\nthe Committee on Foreign Affairs of the House of Representatives ; and\n**(D)**\nthe Committee on Appropriations of the House of Representatives .\n**(2) Montreal Protocol**\nThe term Montreal Protocol means the Montreal Protocol on Substances that Deplete the Ozone Layer, done at Montreal September 16, 1987.\n**(3) United Nations Framework Convention on Climate Change**\nThe term United Nations Framework Convention on Climate Change means the United Nations Framework Convention on Climate Change, adopted in Rio de Janeiro, Brazil in June 1992.\n#### 3. Prohibition on use of funds for the Montreal Protocol on Substances that Deplete the Ozone Layer until China is no longer defined as a developing country\nNotwithstanding any other provision of law, no Federal funds may be obligated or expended to implement the Montreal Protocol, including its protocols and amendments, or any fund established under the Protocol, until the President certifies to the appropriate congressional committees that the Parties to the Montreal Protocol have amended their Decision I/12E, Clarification of terms and definitions: developing countries, made at the First Meeting of the Parties to remove the People's Republic of China.\n#### 4. Prohibition on use of funds for the United Nations Framework Convention on Climate Change until China is included among the countries listed in Annex I of the Convention\nNotwithstanding any other provision of law, no Federal funds may be obligated or expended to fund the operations and meetings of the United Nations Framework Convention on Climate Change, including it protocols or agreements, or any fund established under the Convention or its agreements, until the President certifies to the appropriate congressional committees that the Parties to the Framework Convention have included the People\u2019s Republic of China in Annex I of the Convention.",
      "versionDate": "2025-02-20",
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
        "actionDate": "2025-03-14",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2115",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ending China\u2019s Unfair Advantage Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-05-08T15:48:25Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s680is.xml"
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
      "title": "Ending China's Unfair Advantage Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T11:03:44Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ending China's Unfair Advantage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit funding for the Montreal Protocol on Substances that Deplete the Ozone Layer and the United Nations Framework Convention on Climate Change until China is no longer defined as a developing country.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:20Z"
    }
  ]
}
```
