# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4115?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4115
- Title: BETS OFF Act
- Congress: 119
- Bill type: S
- Bill number: 4115
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-04-16T11:03:25Z
- Update date including text: 2026-04-23T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4115",
    "number": "4115",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001169",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Murphy, Christopher [D-CT]",
        "lastName": "Murphy",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "BETS OFF Act",
    "type": "S",
    "updateDate": "2026-04-16T11:03:25Z",
    "updateDateIncludingText": "2026-04-23T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T18:53:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CO"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4115is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4115\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Murphy (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo ban certain types of wagers.\n#### 1. Short title\nThis Act may be cited as the Banning Event Trading on Sensitive Operations and Federal Functions Act or the BETS OFF Act .\n#### 2. Definitions\nIn this Act:\n**(1) Specified event**\nThe term specified event means\u2014\n**(A)**\nan act of terrorism;\n**(B)**\nan assassination;\n**(C)**\na war; or\n**(D)**\nany event\u2014\n**(i)**\nthe primary underlying characteristic of which is not financial, commercial, or economic; and\n**(ii)**\n**(I)**\nthat is an action taken by any government, unit of government, intergovernmental organization, or government official;\n**(II)**\nthe outcome of which is under the complete control of any person; or\n**(III)**\nthe outcome of which is known by any person in advance.\n**(2) Wager**\nThe term wager \u2014\n**(A)**\nmeans the staking or risking by any person of something of value upon the outcome of an event, including the outcome of any portion or aspect thereof, upon an agreement or understanding that the person or another person will receive something of value in the event of a certain outcome; and\n**(B)**\ndoes not include insurance for which the insured holds a lawful insurable interest\u2014\n**(i)**\nunder State law, within the meaning of the Act entitled An Act to express the intent of the Congress with reference to the regulation of the business of insurance , approved March 9, 1945 (commonly known as the McCarran-Ferguson Act ; 15 U.S.C. 1011 et seq. );\n**(ii)**\nunder foreign law, with respect\u2014\n**(I)**\nto risks located outside the United States; or\n**(II)**\nthe reinsurance of risks covered under clause (i); or\n**(iii)**\nunder Federal law, including under\u2014\n**(I)**\nthe Terrorism Insurance Program established under the Terrorism Risk Insurance Act of 2002 ( 15 U.S.C. 6701 note; Public Law 107\u2013297 );\n**(II)**\nthe National Flood Insurance Program established under the National Flood Insurance Act of 1968 ( 42 U.S.C. 4001 et seq. ); or\n**(III)**\nthe Federal crop insurance program established under the Federal Crop Insurance Act ( 7 U.S.C. 1501 et seq. ).\n#### 3. Prohibited conduct\n##### (a) Prohibition\nIt shall be unlawful for any person to place, accept, or facilitate the placement or acceptance of a wager regarding a specified event.\n##### (b) Civil action\nThe Attorney General may bring a civil action for injunctive relief in an appropriate district court of the United States against any person who violates subsection (a).\n#### 4. Amendments\n##### (a) Interstate and foreign travel or transportation in aid of racketeering enterprises\nSection 1952(b)(i)(1) of title 18, United States Code, is amended by inserting after gambling the following: (including conduct prohibited by section 3(a) of the BETS OFF Act ) .\n##### (b) Prohibition of illegal gambling businesses\nSection 1955(b) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)(i), by inserting section 3(a) of the BETS OFF Act or after is a violation of ; and\n**(2)**\nin paragraph (4), by inserting conducted prohibited by section 3(a) of the BETS OFF Act , after gambling includes but is not limited to .\n##### (c) Prohibition on funding of unlawful internet gambling\nSection 5362(1) of title 31, United States Code, is amended\u2014\n**(1)**\nin subparagraph (D), by striking and at the end;\n**(2)**\nby redesignating subparagraph (E) as subparagraph (F); and\n**(3)**\nby inserting after subparagraph (D) the following:\n(E) includes conduct prohibited by section 3(a) of the BETS OFF Act , without regard to subparagraph (F) of this paragraph; and .\n##### (d) Common provisions applicable to registered entities\nSection 5c(c)(5) of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132(c)(5) ) is amended\u2014\n**(1)**\nin subparagraph (C)(i)\u2014\n**(A)**\nby striking subclauses (II), (III), and (IV); and\n**(B)**\nby redesignating subclauses (V) and (VI) as subclauses (II) and (III), respectively; and\n**(2)**\nby adding at the end the following:\n(D) Prohibition relating to specified events Notwithstanding any other provision of this section, no agreement, contract, transaction, or swap involving any specified event, as defined in section 2 of the BETS OFF Act (or any index, measure, value, or data related thereto, or occurrence, extent of an occurrence, or contingency based thereon), may be listed or made available for clearing or trading on or through a registered entity. .\n#### 5. Severability\nIf any provision of this Act or amendment made by this Act, or the application of such provision or amendment to any person or circumstance, is held to be unconstitutional, the remainder of this Act and the amendments made by this Act, and the application of the provision or amendment to any other person or circumstance, shall not be affected.\n#### 6. Effective date\nThis Act shall take effect on the date that is 30 days after the date of enactment of this Act.",
      "versionDate": "2026-03-17",
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
        "actionDate": "2026-03-17",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Agriculture, and Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "BETS OFF Act",
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
        "updateDate": "2026-04-01T14:51:21Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4115is.xml"
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
      "title": "BETS OFF Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BETS OFF Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Banning Event Trading on Sensitive Operations and Federal Functions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ban certain types of wagers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:35Z"
    }
  ]
}
```
