# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7902?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7902
- Title: Safeguarding Women from Chemical Abortion Act
- Congress: 119
- Bill type: HR
- Bill number: 7902
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-05-22T08:08:13Z
- Update date including text: 2026-05-22T08:08:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7902",
    "number": "7902",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Safeguarding Women from Chemical Abortion Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:13Z",
    "updateDateIncludingText": "2026-05-22T08:08:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:32:45Z",
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
          "date": "2026-03-12T13:32:40Z",
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
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "TN"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "FL"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-03-20",
      "state": "MO"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "NJ"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "IL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7902ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7902\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mrs. Harshbarger introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide that the approved application under the Federal Food, Drug, and Cosmetic Act for the drug mifepristone for the purpose of the termination of intrauterine pregnancy is deemed to have been withdrawn, to establish a Federal tort for harm to women caused by chemical abortion drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Women from Chemical Abortion Act .\n#### 2. Withdrawal of approval of the drug mifepristone for termination of pregnancy\nEffective upon the expiration of 14 days after the date of the enactment of this Act:\n**(1)**\nApproval of an application submitted under subsection (b) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ) for the drug mifepristone (marketed as Mifeprex, and also known as RU\u2013486) with an indication for the termination of intrauterine pregnancy, and of any application submitted under subsection (j) of such section for a drug with the same indication and for which mifepristone is the reference drug, is deemed to have been withdrawn under subsection (e) of such section.\n**(2)**\nFor purposes of sections 301(d) and 304 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331(d) ; 334), the introduction or delivery for introduction of a drug, the approval of which has been withdrawn as described in paragraph (1), into interstate commerce shall be considered a violation of section 505 of such Act ( 21 U.S.C. 355 ).\n**(3)**\nThe drug mifepristone shall be considered misbranded for purposes of sections 301 and 304 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331 ; 334) if the drug bears labeling providing that the drug may be used for the termination of intrauterine pregnancy or that the drug may be used in conjunction with another drug for the termination of intrauterine pregnancy.\n#### 3. Federal tort for harm to women caused by chemical abortion drugs\n##### (a) Definitions\nIn this section:\n**(1) Covered entity**\nThe term covered entity means a person that manufactures a covered medication for introduction into interstate commerce.\n**(2) Covered medication**\nThe term covered medication means the drug mifepristone (marketed as Mifeprex, and also known as RU\u2013486), with an indication for the termination of intrauterine pregnancy, approved pursuant to an application submitted under subsection (b) or (j) of section 505 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355 ).\n##### (b) Liability\nA covered entity shall be liable in accordance with this section to any individual who suffers bodily injury or harm to mental health (including any physical, psychological, emotional, or physiological harm) that is attributable, in whole or in part, to the individual\u2019s use of a covered medication manufactured by a covered entity.\n##### (c) Private right of action\nAn individual who suffers bodily injury or harm to mental health that is attributable, in whole or in part, to the individual\u2019s use of a covered medication as described in subsection (b) may bring a civil action against the covered entity in an appropriate district court of the United States or a State court of competent jurisdiction for\u2014\n**(1)**\ncompensatory damages;\n**(2)**\npunitive damages; and\n**(3)**\nattorney\u2019s fees and costs.\n##### (d) Rules of construction\nNothing in this section shall be construed to preempt any State law that makes available any other remedy to an individual described in subsection (b).\n##### (e) Effective date\nThis section shall take effect on the date that is 90 days after the date of enactment of this Act.\n#### 4. Rule of construction\nNothing in this Act shall be construed to affect any provision of section 1461 of title 18, United States Code.",
      "versionDate": "2026-03-12",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4066",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safeguarding Women from Chemical Abortion Act",
      "type": "S"
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
        "name": "Health",
        "updateDate": "2026-04-24T19:52:59Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7902ih.xml"
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
      "title": "Safeguarding Women from Chemical Abortion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Women from Chemical Abortion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T06:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide that the approved application under the Federal Food, Drug, and Cosmetic Act for the drug mifepristone for the purpose of the termination of intrauterine pregnancy is deemed to have been withdrawn, to establish a Federal tort for harm to women caused by chemical abortion drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T06:17:19Z"
    }
  ]
}
```
