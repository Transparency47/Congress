# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3076?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3076
- Title: Nitazene Control Act
- Congress: 119
- Bill type: S
- Bill number: 3076
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2025-11-25T20:22:32Z
- Update date including text: 2025-11-25T20:22:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3076",
    "number": "3076",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001243",
        "district": "",
        "firstName": "David",
        "fullName": "Sen. McCormick, David [R-PA]",
        "lastName": "McCormick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Nitazene Control Act",
    "type": "S",
    "updateDate": "2025-11-25T20:22:32Z",
    "updateDateIncludingText": "2025-11-25T20:22:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T15:18:05Z",
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "AZ"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "NE"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "NH"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "MO"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "MI"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3076is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3076\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. McCormick (for himself, Mr. Gallego , Mr. Ricketts , Mrs. Shaheen , Mr. Schmitt , Ms. Slotkin , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Controlled Substances Act to permanently schedule the class of 2-benzylbenzimidazole-opioids known as nitazenes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nitazene Control Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\n2-Benzylbenzimidazole opioids are a class of synthetic opioids first synthesized in the 1950s that exhibit significant potency at the mu-opioid receptor, with some substances exceeding the potency of fentanyl.\n**(2)**\nThe Drug Enforcement Administration has temporarily or permanently scheduled multiple 2-benzylbenzimidazole opioids compounds under schedule I of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) due to their high abuse potential and lack of accepted medical use.\n**(3)**\nNitazenes and related compounds have emerged in the illicit drug supply as designer drugs and contribute to overdose and fatal poisonings in the United States.\n**(4)**\nA class-wide permanent scheduling of 2-benzylbenzimidazole opioids is necessary to preemptively address the proliferation of new analogs, streamline enforcement, and protect public health.\n**(5)**\nThe HALT Fentanyl Act ( 28 U.S.C. 801 note; Public Law 119\u201326 ) created pathways for research using schedule I controlled substances that apply to scheduled nitazenes.\n#### 3. Schedule I classification of nitazenes\n##### (a) Amendment\nSchedule I of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) is amended by adding at the end the following:\n(f) (1) Unless specifically exempted or unless listed in another schedule, any material, compound, mixture, or preparation which contains any quantity of a 2-benzylbenzimidazole opioid, or which contains the salts, isomers, and salts of isomers of a 2-benzylbenzimidazole opioid. (2) For purposes of paragraph (1), the term 2-benzylbenzimidazole opioid includes the following: (A) A substance that is structurally related to 2-benzylbenzimidazole with the following modifications: (i) At the 1-position, substitution with an alkyl linker connected to a substituted amine group containing hydrogen, alkyl, alkenyl, or heteroaryl group, such as a morphilino, pyrrolidino, or piperidinyl groups, whether or not further substituted. (ii) At the 2-position\u2014 (I) replacement of the alkyl portion of the benzyl group with a substituted or unsubstituted alkyl, alkoxy, carbamates group, nitrogen, sulfur, or oxygen atom; or (II) replacement of the phenyl portion of the benzyl group with an aryl or heteroaryl group. (iii) Substitution on the phenyl portion of the benzimidazole ring with a hydrogen atom, halogen, nitro, cyano, substituted or unsubstituted amide, amine, alkyl, alkoxy, aryl, or heteroaryl group. (iv) At the 6-position, substitution with hydrogen, nitro, trifluoromethyl, methoxy, trifluoromethoxy, cyano, and halogen groups. (B) A substance that exhibits agonist activity at the mu-opioid receptor. (C) Etonitazene, clonitazene, metonitazene, isotonitazene, protonitazene, butonitazene, etodesnitazene, flunitazene, N-pyrrolidino etonitazene, N-desethyl isotonitazene, and N-piperidinyl etonitazene. .\n##### (b) Removal of temporary status\nAny substance included in the amendment made by subsection (a) that was temporarily scheduled under section 201(h) of the Controlled Substances Act ( 21 U.S.C. 811(h) ) shall be deemed permanently scheduled and subject to the requirements of schedule I of section 202(c) of that Act ( 21 U.S.C. 812(c) ) as of the date of enactment of this Act.\n##### (c) Rule of construction\nNothing in this subsection shall be construed to authorize the initiation of new research using 2-benzylbenzimidazole opioids, as defined in subsection (f) of schedule I of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ), as added by subsection (a) of this section, without proper registration and scheduling compliance.",
      "versionDate": "2025-10-30",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-25T20:22:32Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3076is.xml"
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
      "title": "Nitazene Control Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-06T07:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nitazene Control Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-06T07:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Controlled Substances Act to permanently schedule the class of 2-benzylbenzimidazole-opioids known as nitazenes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-06T07:48:19Z"
    }
  ]
}
```
