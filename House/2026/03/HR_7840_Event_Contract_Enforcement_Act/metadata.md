# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7840?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7840
- Title: Event Contract Enforcement Act
- Congress: 119
- Bill type: HR
- Bill number: 7840
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-05-27T08:06:04Z
- Update date including text: 2026-05-27T08:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-03-18 - IntroReferral: Sponsor introductory remarks on measure. (CR H2588-2589)
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-03-18 - IntroReferral: Sponsor introductory remarks on measure. (CR H2588-2589)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7840",
    "number": "7840",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001213",
        "district": "1",
        "firstName": "Blake",
        "fullName": "Rep. Moore, Blake D. [R-UT-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Event Contract Enforcement Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:04Z",
    "updateDateIncludingText": "2026-05-27T08:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2588-2589)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NM"
    },
    {
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7840ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7840\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Moore of Utah (for himself and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Commodity Exchange Act to prohibit event contracts based on terrorism, assassination, war, gaming, illegal activity, election outcomes, government activities, or other activities determined by the Commodity Futures Trading Commission to be contrary to the public interest, and to allow States to exempt themselves from the prohibition on gaming contracts.\n#### 1. Short title\nThis Act may be cited as the Event Contract Enforcement Act .\n#### 2. Prohibition on event contracts contrary to the public interest\n##### (a) In general\nSection 5c(c)(5)(C) of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132(c)(5)(C) ) is amended\u2014\n**(1)**\nby striking clauses (i) and (ii) and inserting the following:\n(i) Event contracts Subject to clause (ii), it shall be unlawful to list or make available for trading on or through a registered entity an agreement, contract, transaction, or swap in an excluded commodity that is based on an occurrence, the extent of an occurrence, or a contingency (other than a change in the price, rate, value, or level of a commodity described in section 1a(19)(i)) in relation to\u2014 (I) activity that is unlawful under Federal or State law; (II) terrorism; (III) assassination; (IV) war; (V) gaming; (VI) the result of any vote in an election (as defined in section 301 of the Federal Election Campaign Act of 1971) held under Federal, State, or local law, including a ballot initiative or referendum; (VII) conduct by or in any level or branch of the Federal Government or of any State or local government, including by or in any instrumentality or by any personnel of any level or branch of any such government; or (VIII) other similar activity determined by the Commission, by rule or regulation, to be contrary to the public interest. (ii) Exemption Clause (i)(V) shall not apply with respect to conduct in a State if the law of the State expressly exempts conduct in the State from the application of such clause. ; and\n**(2)**\nby adding at the end the following:\n(v) Gaming defined In clause (i), the term gaming means any aspect of a live, simulated, or virtual physical or mental challenge or game of chance. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2026-03-05",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-01T16:08:16Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7840ih.xml"
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
      "title": "Event Contract Enforcement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T04:58:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Event Contract Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T04:58:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Commodity Exchange Act to prohibit event contracts based on terrorism, assassination, war, gaming, illegal activity, election outcomes, government activities, or other activities determined by the Commodity Futures Trading Commission to be contrary to the public interest, and to allow States to exempt themselves from the prohibition on gaming contracts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T04:48:27Z"
    }
  ]
}
```
