# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1223?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1223
- Title: Prohibiting Foreign Adversary Interference in Cryptocurrency Markets Act
- Congress: 119
- Bill type: S
- Bill number: 1223
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-05-23T13:19:33Z
- Update date including text: 2025-05-23T13:19:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1223",
    "number": "1223",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Prohibiting Foreign Adversary Interference in Cryptocurrency Markets Act",
    "type": "S",
    "updateDate": "2025-05-23T13:19:33Z",
    "updateDateIncludingText": "2025-05-23T13:19:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T16:40:36Z",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MS"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1223is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1223\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Tuberville (for himself, Mrs. Hyde-Smith , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Commodity Exchange Act to prohibit interference in United States digital commodity markets by entities organized or established in a foreign adversary, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prohibiting Foreign Adversary Interference in Cryptocurrency Markets Act .\n#### 2. Prohibition on registration of foreign adversary-affiliated digital commodity platforms\nSection 4(b) of the Commodity Exchange Act ( 7 U.S.C. 6(b) ) is amended by adding at the end the following:\n(3) Prohibition on registration of foreign adversary-affiliated digital commodity platforms (A) Definitions In this paragraph: (i) Covered entity The term covered entity means\u2014 (I) an entity that is established or organized under the laws of, or the principal place of business of which is located in, a foreign adversary; and (II) any subsidiary owned (in whole or in part) or operated by an entity described in subclause (I). (ii) Digital commodity (I) In general The term digital commodity means a fungible digital form of personal property that can be possessed and transferred person-to-person without necessary reliance on an intermediary. (II) Inclusions The term digital commodity includes property commonly known as cryptocurrency or virtual currency . (III) Exclusions The term digital commodity does not include\u2014 (aa) an interest in a physical commodity; (bb) a security; (cc) a digital form of currency backed by the full faith and credit of the United States; or (dd) any other instrument that the Commission determines not to be a digital commodity. (iii) Digital commodity broker (I) In general The term digital commodity broker means a person that is engaged, as an identifiable business, in\u2014 (aa) soliciting or accepting orders on behalf of another person for a digital commodity trade; (bb) accepting digital commodities from another person for the purpose of entering into digital commodity trades; (cc) arranging digital commodity trades on behalf of another person; or (dd) a similar activity, as determined by the Commission. (II) Exclusion The term digital commodity broker does not include a person solely because that person validates digital commodity transactions. (iv) Digital commodity custodian The term digital commodity custodian means a person that, as an identifiable business, maintains possession, custody, or control over digital commodities on behalf of another person. (v) Digital commodity dealer (I) In general The term digital commodity dealer means a person that\u2014 (aa) has an identifiable business of dealing in a digital commodity as principal for its own account; (bb) makes a market in a digital commodity; (cc) holds itself out as a dealer in a digital commodity; (dd) has as an identifiable business of buying or selling digital commodities for conversion into other digital commodities, currency, or other consideration; (ee) has as an identifiable business of accepting digital commodities from another person (referred to in this item as a depositor ) with an obligation to return to the depositor the digital commodities, consideration linked to the digital commodities, or both; or (ff) engages in a similar activity, as determined by the Commission. (II) Exclusion The term digital commodity dealer does not include a person solely because that person validates digital commodity transactions. (vi) Digital commodity platform The term digital commodity platform means a person that is 1 or more of the following: (I) A digital commodity broker. (II) A digital commodity custodian. (III) A digital commodity dealer. (IV) A digital commodity trading facility. (vii) Digital commodity trade (I) In general The term digital commodity trade means a purchase or sale of a digital commodity in exchange for\u2014 (aa) another digital commodity; or (bb) any other consideration. (II) Inclusions The term digital commodity trade includes\u2014 (aa) an offer to enter into a purchase or sale described in subclause (I); and (bb) a loan of a digital commodity, an offer to enter into a loan of a digital commodity, or a similar activity, as determined by the Commission. (viii) Digital commodity trading facility (I) In general The term digital commodity trading facility means a trading facility that facilitates the execution or trading of digital commodity trades between persons. (II) Exclusion The term digital commodity trading facility does not include a person solely because that person validates digital commodity transactions. (ix) Foreign adversary The term foreign adversary means\u2014 (I) the People\u2019s Republic of China, including the Hong Kong Special Administrative Region and the Macao Special Administrative Region; (II) the Republic of Cuba; (III) the Islamic Republic of Iran; (IV) the Democratic People\u2019s Republic of Korea; (V) the Russian Federation; and (VI) the Bolivarian Republic of Venezuela under the regime of Nicol\u00e1s Maduro Moros. (B) Prohibition on registration The Commission shall not register under this Act a digital commodity platform that is owned (in whole or in part) by a covered entity. (C) Revocation of registration The Commission shall revoke the registration under this Act of a digital commodity platform if a covered entity acquires all or any part of the ownership of the digital commodity platform. .",
      "versionDate": "2025-04-01",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-23T13:19:33Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1223is.xml"
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
      "title": "Prohibiting Foreign Adversary Interference in Cryptocurrency Markets Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prohibiting Foreign Adversary Interference in Cryptocurrency Markets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Commodity Exchange Act to prohibit interference in United States digital commodity markets by entities organized or established in a foreign adversary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:31Z"
    }
  ]
}
```
