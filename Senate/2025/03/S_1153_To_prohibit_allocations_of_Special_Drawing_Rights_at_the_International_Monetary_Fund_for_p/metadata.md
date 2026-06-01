# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1153
- Title: No Dollars for Dictators Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1153
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-10-09T03:26:21Z
- Update date including text: 2025-10-09T03:26:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1153",
    "number": "1153",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
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
    "title": "No Dollars for Dictators Act of 2025",
    "type": "S",
    "updateDate": "2025-10-09T03:26:21Z",
    "updateDateIncludingText": "2025-10-09T03:26:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T19:29:59Z",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "WY"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "IA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "TN"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "WV"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1153is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1153\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Kennedy (for himself, Mr. Barrasso , Mr. Grassley , Mr. Scott of Florida , Mrs. Blackburn , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit allocations of Special Drawing Rights at the International Monetary Fund for perpetrators of genocide and state sponsors of terrorism without congressional authorization.\n#### 1. Short title\nThis Act may be cited as the No Dollars for Dictators Act of 2025 .\n#### 2. Prohibition on allocations of Special Drawing Rights at International Monetary Fund for perpetrators of genocide and state sponsors of terrorism without congressional authorization\nSection 6 of the Special Drawing Rights Act ( 22 U.S.C. 286q ) is amended by adding at the end the following:\n(c) Unless Congress by law authorizes such action, neither the President nor any person or agency shall on behalf of the United States vote to allocate Special Drawing Rights under article XVIII, sections 2 and 3, of the Articles of Agreement of the Fund to a member country of the Fund, if the government of the member country has\u2014 (1) committed genocide at any time during the 10-year period ending with the date of the vote; or (2) been determined by the Secretary of State, as of the date of the enactment of the No Dollars for Dictators Act of 2025 , to have repeatedly provided support for acts of international terrorism, for purposes of\u2014 (A) section 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) ); (B) section 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 ); (C) section 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) ); or (D) any other provision of law. .",
      "versionDate": "2025-03-26",
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
        "updateDate": "2025-05-14T20:31:33Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1153is.xml"
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
      "title": "No Dollars for Dictators Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Dollars for Dictators Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit allocations of Special Drawing Rights at the International Monetary Fund for perpetrators of genocide and state sponsors of terrorism without congressional authorization.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:18:19Z"
    }
  ]
}
```
