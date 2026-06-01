# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2746?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2746
- Title: Produce Epstein Treasury Records Act
- Congress: 119
- Bill type: S
- Bill number: 2746
- Origin chamber: Senate
- Introduced date: 2025-09-09
- Update date: 2025-12-18T12:03:20Z
- Update date including text: 2025-12-18T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in Senate
- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-09: Introduced in Senate

## Actions

- 2025-09-09 - IntroReferral: Introduced in Senate
- 2025-09-09 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2746",
    "number": "2746",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Produce Epstein Treasury Records Act",
    "type": "S",
    "updateDate": "2025-12-18T12:03:20Z",
    "updateDateIncludingText": "2025-12-18T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-09",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T22:04:09Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MN"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MA"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NM"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NV"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NJ"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "RI"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2746is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2746\nIN THE SENATE OF THE UNITED STATES\nSeptember 9, 2025 Mr. Wyden introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the Secretary of the Treasury to produce suspicious activity reports relating to Jeffrey Epstein and his associates, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Produce Epstein Treasury Records Act .\n#### 2. Epstein Treasury records\n##### (a) Production of certain records\nNot later than 30 days after the date of enactment of this Act, the Secretary of the Treasury shall submit to the Chairman and Ranking Member of the Committee on Finance of the Senate and the Committee on Banking, Housing, and Urban Affairs of the Senate physical copies of all records described in subsection (b).\n##### (b) Records described\n**(1) In general**\nThe records described in this subsection are all suspicious activity reports relating to Jeffrey Epstein and his co-conspirators (whether indicted or unindicted) and any third-party individual or entity that transacted with Jeffrey Epstein or any entity he owned or controlled, whether directly or through any representative of Jeffrey Epstein.\n**(2) Individuals and entities**\nThe individuals and entities described in paragraph (1) include the following:\n**(A)**\nJeffrey Epstein.\n**(B)**\nGhislaine Maxwell.\n**(C)**\nDarren K. Indyke.\n**(D)**\nRichard D. Kahn.\n**(E)**\nHarry Beller.\n**(F)**\nErika Kellerhals.\n**(G)**\nSouthern Trust Company, Inc.\n**(H)**\nSouthern Financial LLC.\n**(I)**\nHaze Trust.\n**(J)**\nEnvironmental Solutions Worldwide, Inc.\n**(K)**\nThe 1953 Trust.\n**(L)**\nPlan D, LLC.\n**(M)**\nGreat St. Jim, LLC.\n**(N)**\nNautilus, Inc.\n**(O)**\nHyperion Air, LLC.\n**(P)**\nPoplar, Inc.\n**(Q)**\nJ. Epstein Virgin Islands Foundation Inc.\n**(R)**\nGratitude America Ltd.\n**(S)**\nButterfly Trust.\n**(T)**\nLa Hougue.\n**(U)**\nScott Borgerson.\n**(V)**\nMalcolm Grumbridge.\n**(W)**\nJ.P. Morgan Chase Bank, N.A. (and any subsidiary thereof).\n**(X)**\nDeutsche Bank (and any subsidiary thereof).\n**(Y)**\nBank of America (and any subsidiary thereof).\n**(Z)**\nBank of New York Mellon Corporation (and any subsidiary thereof).\n**(AA)**\nUBS Financial Services.\n**(BB)**\nWells Fargo.\n**(CC)**\nAlfa Bank.\n**(DD)**\nSberbank.\n**(EE)**\nJes Staley.\n**(FF)**\nLeon D. Black.\n**(GG)**\nDebra R. Black.\n**(HH)**\nBlack Family Partners, LP.\n**(II)**\nElysium Trust.\n**(JJ)**\nElysium Management, LLC.\n**(KK)**\nJ Black Trust.\n**(LL)**\nMelanie Spinella.\n**(MM)**\nBV70, LLC.\n**(NN)**\nLes Wexner.\n**(OO)**\nBella Wexner.\n**(PP)**\nAbigail Wexner.\n**(QQ)**\nThe Wexner Foundation.\n**(RR)**\nArts Interests.\n**(SS)**\nHealth and Science Interests.\n**(TT)**\nThe Wexner Children\u2019s Trust II.\n**(UU)**\nInternational Charitable Interests.\n**(VV)**\nL Brands (formerly Limited Brands).\n**(WW)**\nAlan Dershowitz.\n**(XX)**\nGlenn Dubin.\n**(YY)**\nChristie\u2019s.\n**(ZZ)**\nSotheby\u2019s.\n**(AAA)**\nHB Multi-Strategy Holdings, Ltd.\n**(BBB)**\nHighbridge Capital Corporation.\n**(CCC)**\nAP Narrows Holding AP.\n**(DDD)**\nLDB 2011 LLC.\n**(EEE)**\nElizabeth Johnson.\n**(FFF)**\nJohnson & Johnson.\n**(GGG)**\nBarclays.\n**(HHH)**\nPeter Thiel.\n**(III)**\nValar Ventures.\n**(JJJ)**\nKaryna Shuliak.\n**(KKK)**\nAppleby law firm.\n**(LLL)**\nStandard Chartered.\n**(MMM)**\nHSBC.\n**(NNN)**\nJulius Baer.\n**(OOO)**\nBNP Paribas.\n**(PPP)**\nCitibank.\n**(QQQ)**\nSarah Kellen.\n**(RRR)**\nNadia Marcinko (also known as Nada Marcinkova).\n**(SSS)**\nMC2, modeling agency.\n**(TTT)**\nJean-Luc Brunel.\n**(UUU)**\nAny other individual or entity identified by the Secretary of the Treasury, the Attorney General, the Director of the Federal Bureau of Investigation, or the head of any other Federal agency to have transacted with Jeffrey Epstein or Ghislaine Maxwell.\n##### (c) Reports required\n**(1) Financial institutions**\nNot later than 30 days after the date of enactment of this Act, the Secretary of the Treasury shall submit to the Chairman and Ranking Member of the Committee on Finance of the Senate and the Committee on Banking, Housing, and Urban Affairs of the Senate a report containing\u2014\n**(A)**\na list of all financial institutions that filed the records described in subsection (b);\n**(B)**\na list of all individuals and entities flagged in the records described in subsection (b); and\n**(C)**\nthe total dollar value of the transactions in the records described in subsection (b), organized by financial institution.\n**(2) Investigations**\nNot later than 60 days after the date of enactment of this Act, the Secretary of the Treasury shall submit to the Chairman and Ranking Member of the Committee on Finance of the Senate and the Committee on Banking, Housing, and Urban Affairs of the Senate a report detailing all investigations conducted by any component of the Department of the Treasury, including the Financial Crimes Enforcement Network, into any violation of subchapter II of chapter 53 of title 31, United States Code, or any other Federal law, by a financial institution relating to the handling of any account identified in the records described in subsection (b).",
      "versionDate": "2025-09-09",
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
        "updateDate": "2025-09-23T15:51:28Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2746is.xml"
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
      "title": "Produce Epstein Treasury Records Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Produce Epstein Treasury Records Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Treasury to produce suspicious activity reports relating to Jeffrey Epstein and his associates, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:48:32Z"
    }
  ]
}
```
