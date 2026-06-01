# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1868?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1868
- Title: Stop Tax Penalties on American Hostages Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1868
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-03-31T18:46:39Z
- Update date including text: 2026-03-31T18:46:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1868",
    "number": "1868",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001072",
        "district": "2",
        "firstName": "J.",
        "fullName": "Rep. Hill, J. French [R-AR-2]",
        "lastName": "Hill",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Stop Tax Penalties on American Hostages Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-31T18:46:39Z",
    "updateDateIncludingText": "2026-03-31T18:46:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "PA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "VA"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "FL"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "GA"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NJ"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "NJ"
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
      "sponsorshipDate": "2026-01-13",
      "state": "FL"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1868ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1868\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Hill of Arkansas (for himself, Ms. Titus , Ms. Tenney , and Mr. Beyer ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to postpone tax deadlines and reimburse paid late fees for United States nationals who are unlawfully or wrongfully detained or held hostage abroad, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Tax Penalties on American Hostages Act of 2025 .\n#### 2. Postponement of tax deadlines for hostages and individuals wrongfully detained abroad\n##### (a) In general\nChapter 77 of the Internal Revenue Code of 1986 is amended by inserting after section 7510 the following new section:\n7511. Time for performing certain acts postponed for hostages and individuals wrongfully detained abroad (a) Time To be disregarded (1) In general The period during which an applicable individual was unlawfully or wrongfully detained abroad, or held hostage abroad, shall be disregarded in determining, under the internal revenue laws, in respect of any tax liability of such individual\u2014 (A) whether any of the acts described in section 7508(a)(1) were performed within the time prescribed thereof (determined without regard to extension under any other provision of this subtitle for periods after the initial date (as determined by the Secretary) on which such individual was unlawfully or wrongfully detained abroad or held hostage abroad), (B) the amount of any interest, penalty, additional amount, or addition to the tax for periods after such date, and (C) the amount of any credit or refund. (2) Application to spouse The provisions of paragraph (1) shall apply to the spouse of any individual entitled to the benefits of such paragraph. (3) Special rule for overpayments The rules of section 7508(b) shall apply for purposes of this section. (b) Applicable individual (1) In general For purposes of this section, the term applicable individual means any individual who is\u2014 (A) a United States national unlawfully or wrongfully detained abroad, as determined under section 302 of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 ), or (B) a United States national taken hostage abroad, as determined pursuant to the findings of the Hostage Recovery Fusion Cell (as described in section 304 of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741b )). (2) Information provided to Treasury For purposes of identifying individuals described in paragraph (1), not later than January 1, 2026, and annually thereafter\u2014 (A) the Secretary of State shall provide the Secretary with a list of the individuals described in paragraph (1)(A), as well as any other information necessary to identify such individuals, and (B) the Attorney General, acting through the Hostage Recovery Fusion Cell, shall provide the Secretary with a list of the individuals described in paragraph (1)(B), as well as any other information necessary to identify such individuals. (c) Modification of Treasury databases and information systems The Secretary shall update, as necessary, any database or information system of the Department of the Treasury in order to ensure that the provisions of subsection (a) are applied with respect to each applicable individual. (d) Refund and abatement of penalties and fines imposed prior to identification as applicable individual In the case of any applicable individual\u2014 (1) for whom any interest, penalty, additional amount, or addition to the tax in respect to any tax liability for any taxable year ending during the period described in subsection (a)(1) was assessed or collected, and (2) who was, subsequent to such assessment or collection, determined to be an individual described in subparagraph (A) or (B) of subsection (b)(1), the Secretary shall abate any such assessment and refund any amount collected to such applicable individual in the same manner as any refund of an overpayment of tax under section 6402. .\n##### (b) Clerical amendment\nThe table of sections for chapter 77 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 7510 the following new item:\nSec. 7511. Time for performing certain acts postponed for hostages and individuals wrongfully detained abroad. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of enactment of this Act.\n#### 3. Refund and abatement of penalties and fines paid by eligible individuals\n##### (a) In general\nSection 7511 of the Internal Revenue Code of 1986, as added by section 2, is amended by adding at the end the following new subsection:\n(d) Refund and abatement of penalties and fines paid by eligible individuals (1) In general (A) Establishment Not later than January 1, 2026, the Secretary (in consultation with the Secretary of State and the Attorney General) shall establish a program to allow any eligible individual (or the spouse or any dependent (as defined in section 152) of such individual) to apply for a refund or an abatement of any amount described in paragraph (2) (including interest) to the extent such amount was attributable to the applicable period. (B) Identification of individuals Not later than January 1, 2026, the Secretary of State and the Attorney General, acting through the Hostage Recovery Fusion Cell (as described in section 304 of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741b )), shall\u2014 (i) compile a list, based on such information as is available, of individuals who were applicable individuals during the applicable period, and (ii) provide the list described in clause (i) to the Secretary. (C) Notice For purposes of carrying out the program described in subparagraph (A), the Secretary (in consultation with the Secretary of State and the Attorney General) shall, with respect to any individual identified under subparagraph (B), provide notice to such individual\u2014 (i) in the case of an individual who has been released on or before the date of enactment of this subsection, not later than 90 days after the date of enactment of this subsection, or (ii) in the case of an individual who is released after the date of enactment of this subsection, not later than 90 days after the date on which such individual is released, that such individual may be eligible for a refund or an abatement of any amount described in paragraph (2) pursuant to the program described in subparagraph (A). (D) Authorization (i) In general Subject to clause (ii), in the case of any refund described in subparagraph (A), the Secretary shall issue such refund to the eligible individual in the same manner as any refund of an overpayment of tax. (ii) Extension of limitation on time for refund With respect to any refund under subparagraph (A)\u2014 (I) the 3-year period of limitation prescribed by section 6511(a) shall be extended until the end of the 1-year period beginning on the date that the notice described in subparagraph (C) is provided to the eligible individual, and (II) any limitation under section 6511(b)(2) shall not apply. (2) Eligible individual For purposes of this subsection, the term eligible individual means any applicable individual who, for any taxable year ending during the applicable period, paid or incurred any interest, penalty, additional amount, or addition to the tax in respect to any tax liability for such year of such individual based on a determination that an act described in section 7508(a)(1) which was not performed by the time prescribed therefor (without regard to any extensions). (3) Applicable period For purposes of this subsection, the term applicable period means the period\u2014 (A) beginning on January 1, 2021, and (B) ending on the date of enactment of this subsection. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years ending on or before the date of enactment of this Act.",
      "versionDate": "2025-03-05",
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
        "actionDate": "2026-02-26",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3931",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TAS Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "655",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Stop Tax Penalties on American Hostages Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-07T20:00:41Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1868ih.xml"
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
      "title": "Stop Tax Penalties on American Hostages Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T10:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Tax Penalties on American Hostages Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to postpone tax deadlines and reimburse paid late fees for United States nationals who are unlawfully or wrongfully detained or held hostage abroad, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T10:48:29Z"
    }
  ]
}
```
