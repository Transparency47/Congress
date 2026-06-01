# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7970?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7970
- Title: STOP Nitazenes Act
- Congress: 119
- Bill type: HR
- Bill number: 7970
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-05-14T08:08:06Z
- Update date including text: 2026-05-14T08:08:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-18 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7970",
    "number": "7970",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000566",
        "district": "5",
        "firstName": "Robert",
        "fullName": "Rep. Latta, Robert E. [R-OH-5]",
        "lastName": "Latta",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "STOP Nitazenes Act",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:06Z",
    "updateDateIncludingText": "2026-05-14T08:08:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-18T14:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "VA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "WA"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "KS"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "TX"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "IN"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7970ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7970\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mr. Latta introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Controlled Substances Act to permanently schedule 2-benzylbenzimidazole opioids (commonly referred to as nitazenes) as Schedule 1 controlled substances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Tools to Outlaw Poisonous Nitazenes Act or the STOP Nitazenes Act .\n#### 2. Class I scheduling of nitazenes\n##### (a) In general\nSection 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) is amended by adding at the end of Schedule I the following:\n(f) (1) Unless specifically exempted or unless listed in another schedule, any material, compound, mixture, or preparation that contains\u2014 (A) any quantity of a 2-benzylbenzimidazole opioid; or (B) the salts, isomers, and salts of isomers of a 2-benzylbenzimidazole opioid. (2) For purposes of paragraph (1), the term \u20182-benzylbenzimidazole opioid\u2019 includes the following: (A) A substance that is structurally related to 2-benzylbenzimidazole with the following modifications: (i) At the 1-position, substitution with an alkyl linker connected to a substituted amine group containing hydrogen, alkyl, alkenyl, or a heteroaryl group, such as a morphilino, pyrrolidino, or piperidinyl group, whether or not further substituted. (ii) At the 2-position\u2014 (I) replacement of the alkyl portion of the benzyl group with a substituted or unsubstituted alkyl, alkoxy, carbamates group, nitrogen, sulfur, or oxygen atom; or (II) replacement of the phenyl portion of the benzyl group with an aryl or heteroaryl group. (iii) Substitution on the phenyl portion of the benzimidazole ring with a hydrogen atom, halogen, nitro, cyano, substituted or unsubstituted amide, amine, alkyl, alkoxy, aryl, or heteroaryl group. (iv) At the 6-position, substitution with hydrogen, nitro, trifluoromethyl, methoxy, trifluoromethoxy, cyano, and halogen group. (B) A substance that exhibits agonist activity at the mu-opioid receptor. (C) Etonitazene, clonitazene, metonitazene, isotonitazene, protonitazene, butonitazene, etodesnitazene, flunitazene, N-pyrrolidino etonitazene, N-desethyl isotonitazene, and N-piperidinyl etonitazene. (3) The Attorney General may by order publish in the Federal Register a list of substances that satisfy the definition of the term 2-benzyl benzimidazole opioid in paragraph (2). .\n##### (b) Removal of temporary status\nAny substance included in the amendment made by subsection (a) that was temporarily scheduled under section 201(h) of the Controlled Substances Act ( 21 U.S.C. 811(h) ) shall be deemed permanently scheduled and subject to the requirements of Schedule I of section 202(c) of that Act ( 21 U.S.C. 812(c) ) as of the date of enactment of this Act.\n#### 3. Rulemaking\n##### (a) Interim final rule\nThe Attorney General\u2014\n**(1)**\nshall, not later than 1 year after the date of enactment of this Act, issue rules to implement this Act, including the amendments made by this Act; and\n**(2)**\nmay issue the rules under paragraph (1) as an interim final rule.\n##### (b) Procedure for final rule\n**(1) Effectiveness of interim final rules**\nA rule issued by the Attorney General as an interim final rule under subsection (a) shall become immediately effective as an interim final rule without requiring the Attorney General to demonstrate good cause therefor, notwithstanding subparagraph (B) of section 553(b) of title 5, United States Code.\n**(2) Opportunity for comment and hearing**\nAn interim final rule issued under subsection (a) shall give interested persons the opportunity to comment and to request a hearing.\n**(3) Final rule**\nAfter the conclusion of proceedings under paragraph (2), the Attorney General shall issue a final rule to implement this Act, including the amendments made by this Act, in accordance with section 553 of title 5, United States Code.",
      "versionDate": "2026-03-18",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-03-24T20:01:16Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7970ih.xml"
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
      "title": "STOP Nitazenes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP Nitazenes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Tools to Outlaw Poisonous Nitazenes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Controlled Substances Act to permanently schedule 2-benzylbenzimidazole opioids (commonly referred to as nitazenes) as Schedule 1 controlled substances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:18:18Z"
    }
  ]
}
```
