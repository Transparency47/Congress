# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1356?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1356
- Title: TICKER Act
- Congress: 119
- Bill type: S
- Bill number: 1356
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1356",
    "number": "1356",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TICKER Act",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T21:55:04Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "sponsorshipWithdrawnDate": "2025-04-09",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1356is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1356\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Scott of Florida (for himself and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Securities Exchange Act of 1934 to require national securities exchanges to identify issuers that are consolidated variable interest entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Trading and Investing with Clear Knowledge and Expectations about Risk Act or the TICKER Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nvariable interest entities based in foreign jurisdictions, including the People\u2019s Republic of China, pose a specific and significant risk to investors in the United States, including because investors that purchase shares of those entities\u2014\n**(A)**\nhave no equity or direct ownership interest; and\n**(B)**\nlack legal recourse; and\n**(2)**\ninvestors in the United States should more clearly be made aware of the risk described in paragraph (1) in a transparent, easily accessible, and standardized manner that is recognizable to all persons that have invested, or seek to invest, in entities that are described in that paragraph and are listed on exchanges in the United States, such as through clearly visible warning indicators on ticker symbols and other company symbols used by those exchanges.\n#### 3. Identification of risk with respect to certain entities\n##### (a) Definitions\nIn this section\u2014\n**(1)**\nthe terms broker , dealer , exchange , and security have the meanings given those terms in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) );\n**(2)**\nthe term Commission means the Securities and Exchange Commission;\n**(3)**\nthe term covered entity means a consolidated variable interest entity;\n**(4)**\nthe term national securities exchange means an exchange that is registered as a national securities exchange pursuant to section 6 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f ), as amended by subsection (b) of this section; and\n**(5)**\nthe term variable interest entity has the meaning given the term under generally accepted accounting principles.\n##### (b) Requirements\n**(1) National securities exchanges**\n**(A) In general**\nSection 6(b) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f(b) ) is amended by adding at the end the following:\n(11) (A) In this paragraph, the term covered entity has the meaning given the term in section 3(a) of the Trading and Investing with Clear Knowledge and Expectations about Risk Act . (B) The rules of the exchange require the identification of each covered entity, the securities of which are listed on the exchange, as a covered entity in the symbol for the covered entity used on the exchange. .\n**(B) Effective date; applicability**\nThe amendment made by subparagraph (A) shall\u2014\n**(i)**\ntake effect on the date that is 180 days after the date of enactment of this Act; and\n**(ii)**\napply with respect to a covered entity, the securities of which are listed on a national securities exchange on or after the date that is 180 days after the date of enactment of this Act.\n**(2) Brokers and dealers**\nBeginning not later than 180 days after the date of enactment of this Act, the Commission shall require brokers and dealers to provide warnings to investors investing in covered entities that those investors may lack legal recourse with respect to such an investment.",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-19T14:35:20Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1356is.xml"
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
      "title": "TICKER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-23T02:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TICKER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Trading and Investing with Clear Knowledge and Expectations about Risk Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Securities Exchange Act of 1934 to require national securities exchanges to identify issuers that are consolidated variable interest entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:29Z"
    }
  ]
}
```
